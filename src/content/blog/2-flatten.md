---
title: 'Flattening JSON'
description: 'flattening JSON in polars'
pubDate: 'Jul 29 2025'
# heroImage: '../../assets/blog-placeholder-4.jpg'
tags: ["polars", "data"]
---

I recently encountered a super useful pattern for flattening JSON in dataframes. Sometimes, I'm faced with truly chaotic JSON data -- nested data that does not follow any schema whatsoever, or with so many deviations that creating a fully comprehensive schema is impossible. Examples include LLM output and user-generated data dumps.

How can this data be best stored? There's pickle, but it takes quite a long time for python to serialize/deserialize. Parquet does not support python dict (de-)serialization. Most often, JSON is encountered as strings, but then `json.loads(obj)` is needed every time the data is loaded, which takes a noticable amount of time. 

The trick? Transform data into `key` and `value` columns. By flattening, everything can be stored as native types.


## Why not pl.json_normalize()?

Polars provides [json_normalize](https://docs.pola.rs/api/python/stable/reference/api/polars.json_normalize.html), which is quite similar. Why not use that?

First, `json_normalize` requires that the json always follows a consistent schema. This may not be the case when working with truly chaotic JSON data.

Hence, a gigantic `infer_schema_length` is required to capture all variations in the schema. Worse, the more variations there are, the more columns are necessary. At >1000 columns, I had a noticable slowdown. Plus, with many of the columns almost entirely empty, this is almost certainly not the right approach.

Finally, at time of writing, `json_normalize` has limited support for nested lists.


## The approach

As mentioned above: transform data into `key` and `value` columns, completely unnesting everything. Former nesting is described through prefixes in `key`.

Perhaps the approach is best described with an example.

```json
{
  "storeName": "The Reading Nook",
  "location": "123 Main St, Fictionville",
  "inventory": [
    {
      "id": "B001",
      "title": "The Art of Code",
      "author": "Jane Developer",
      "price": 29.99,
      "ratings": {
        "average": 4.5,
        "reviews": 134
      }
    },
    {
      "id": "B002",
      "title": "Mystery at Midnight",
      "author": "Samantha Sleuth",
      "price": 15.5,
      "ratings": {
        "average": 4.0,
        "reviews": 89
      }
    },
  ]
}
```

| key                          | value                     |
|:-----------------------------|:--------------------------|
| storeName                    | The Reading Nook          |
| location                     | 123 Main St, Fictionville |
| inventory[0].id              | B001                      |
| inventory[0].title           | The Art of Code           |
| inventory[0].author          | Jane Developer            |
| inventory[0].price           | 29.99                     |
| inventory[0].ratings.average | 4.5                       |
| inventory[0].ratings.reviews | 134                       |
| inventory[1].id              | B002                      |
| inventory[1].title           | Mystery at Midnight       |
| inventory[1].author          | Samantha Sleuth           |
| inventory[1].price           | 15.5                      |
| inventory[1].ratings.average | 4                         |
| inventory[1].ratings.reviews | 89                        |
<br>

### Wiktionary Example

In this real example, the input data comes from Tatu Ylönen's [wiktextract](https://github.com/tatuylonen/wiktextract), parsed from raw Wiktionary data.

<details>
<summary>
Expand Data
</summary>

|   entry_id | templates|
|-----------:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|          2 | [{"name": "der", "args": {"1": "en", "2": "ar", "3": "\u0623\u064e\u0628\u0652\u0647\u064e\u0644"}, "expansion": "Arabic \u0623\u064e\u0628\u0652\u0647\u064e\u0644 (\u0294abhal)"}] |
|          3 | [{"name": "der", "args": {"1": "en", "2": "fro", "3": "abaissance"}, "expansion": "Old French abaissance"}] |
|          5 | [{"name": "suffix", "args": {"1": "en", "2": "abeyance", "3": "y"}, "expansion": "abeyance + -y"}]  |
|          6 | [{"name": "af", "args": {"1": "en", "2": "averruncate", "3": "-or"}, "expansion": "averruncate + -or"}] |
|          7 | [{"name": "bor", "args": {"1": "en", "2": "LL.", "3": "aberuncare"}, "expansion": "Late Latin aberuncare"}, {"name": "bor", "args": {"1": "en", "2": "la", "3": "averruncare"}, "expansion": "Latin averruncare"}] |

After flattening:

|   entry_id |   template_number | template_name   | key       | value                   |
|-----------:|------------------:|:----------------|:----------|:------------------------|
|          2 |                 0 | der             | args.1    | en                      |
|          2 |                 0 | der             | args.2    | ar                      |
|          2 |                 0 | der             | args.3    | أَبْهَل                 |
|          2 |                 0 | der             | expansion | Arabic أَبْهَل (ʔabhal) |
|          3 |                 0 | der             | args.1    | en                      |
|          3 |                 0 | der             | args.2    | fro                     |
|          3 |                 0 | der             | args.3    | abaissance              |
|          3 |                 0 | der             | expansion | Old French abaissance   |
|          5 |                 0 | suffix          | args.1    | en                      |
|          5 |                 0 | suffix          | args.2    | abeyance                |
|          5 |                 0 | suffix          | args.3    | y                       |
|          5 |                 0 | suffix          | expansion | abeyance + -y           |
|          6 |                 0 | af              | args.1    | en                      |
|          6 |                 0 | af              | args.2    | averruncate             |
|          6 |                 0 | af              | args.3    | -or                     |
|          6 |                 0 | af              | expansion | averruncate + -or       |
|          7 |                 0 | bor             | args.1    | en                      |
|          7 |                 0 | bor             | args.2    | LL.                     |
|          7 |                 0 | bor             | args.3    | aberuncare              |
|          7 |                 0 | bor             | expansion | Late Latin aberuncare   |
|          7 |                 1 | bor             | args.1    | en                      |
|          7 |                 1 | bor             | args.2    | la                      |
|          7 |                 1 | bor             | args.3    | averruncare             |
|          7 |                 1 | bor             | expansion | Latin averruncare       |

</details>
<br>

The data is taller but completely unnested.

## The code

Note that this code converts everything to string. If you wish to retain the original data type, 
you can create multiple columns: `value_str`, `value_float`, `value_int` etc. and assign
the value only to the column of the correct type.

```python
import json
import polars as pl
import os

from tqdm import tqdm

def flat_iter_dict(d, parent_key='', sep='.'):
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            yield from flat_iter_dict(v, new_key, sep=sep)
        elif isinstance(v, list):
            for i, item in enumerate(v):
                if isinstance(item, dict):
                    yield from flat_iter_dict(item, f"{new_key}[{i}]", sep=sep)
                else:
                    yield f"{new_key}[{i}]", item
        else:
            yield new_key, v

def flatten_json_field(df, field_name):
    """
    Flatten a JSON field from a DataFrame and save to parquet.
    
    Args:
        df: polars DataFrame containing the field to flatten
        field_name: name of the column containing JSON data
    """
    collector = []
    series = df[field_name]
    
    for entry_id, json_obj in tqdm(enumerate(series), total=len(series), desc=f"Flattening {field_name}"):
        obj = json.loads(json_obj) if json_obj else []
        for i, item in enumerate(obj):
            for k, v in flat_iter_dict(item):
                collector.append((entry_id, i, k, str(v) or None))
    
    flattened_df = pl.DataFrame(collector, schema=['entry_id', 'item_number', 'key', 'value'], orient='row')
    return flattened_df
```