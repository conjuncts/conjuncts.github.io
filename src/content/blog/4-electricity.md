---
title: 'Height/Width Analogy of Electricity'
pubDate: 'Apr 7 2026'
revDate: 'Sep 12 2026'
description: "Height/Width Analogy of Electricity"
author: conjuncts
tags: ["conceptual"]
reading_time: "1 min"
---

The water analogy for electricity is widespread, but I propose an even simpler analogy: height/width. 

# Definition

1. **Voltage** is **height**.
2. **Current** is **width**.

That "voltage = height" is easy to justify. Consider terminology such as voltage **drop**, **high** and **low** voltage, and **ground**. It has firm theoretical basis, as electric potential is analogous to gravitational potential.

That "current = width" is harder to justify. Current represents a flow rate (charge over time). There is precedent to thinking of flow as width: [Sankey diagrams](https://en.wikipedia.org/wiki/Sankey_diagram) and highway lanes.

Imagine the width of a river. Neglecting the river's depth, a river's width should be proportional to how much current (how much water) passes through. 


The height/width analogy is rooted in the water analogy. But the appeal is that instead of worrying about pressure, depth, or flow rates, "width" is simpler.

# Series and parallel

The analogy models series and parallel resistors nicely.

## Series

Imagine a resistor as a waterfall with a certain height and width. If the resistors are placed in series, then each waterfall feeds into the other. For the system to make physical sense, the overall difference from beginning to end must be the sum of the heights of each waterfall. 

(That is, overall voltage drop equals the sum of voltage drops per resistor.)

Also, the width of each waterfall must be the same, since there is nowhere for the water to go (so the river can never become wider or narrower). 

(That is, the current is the same for each resistor.)

![Resistors in series](../../assets/resistor_series.png)

## Parallel

Given 3 resistors in parallel, imagine a river diverging into 3 separate streams. Because the water needs somewhere to go, it's reasonable to expect that "width is preserved". That is, the width of the main river equals the sum of the widths of the streams. 

(That is, the overall current equals the sum of current through each resistor.)

Because the tops of each waterfall are connected (and hence level), and the bottoms of each waterfall are connected (and hence level), it's reasonable to expect the difference in height to be the exact same among each waterfall. 

(That is, the voltage drop is the same for each resistor.)


# Kirchhoff's Circuit Laws

In the more general case we turn to Kirchhoff's circuit laws. Yet that is where the height/width analogy works the best!

## Kirchhoff's Voltage Law

If thinking of voltage as height: of course you have to get back to the height you started if walking around a loop!

When thinking of height, we have a natural intuition of what is physical and unphysical.

It is not like an M. C. Escher painting, where you can constantly climb in height yet return back to where you started:

![M. C. Escher](https://upload.wikimedia.org/wikipedia/en/6/66/Ascending_and_Descending.jpg)

We would expect that when walking in a loop, the net gain in elevation must be zero. That intuition translates nicely to Kirchhoff's Voltage Law.

## Kirchhoff's Current Law

When thinking about how rivers split, one reasonable assumption is that if a river splits into two child branches, the width of the original river is split among the children. 

That is the essence of Kirchhoff's Current Law: that current should be "balanced" where the current coming in equals the current coming out.

When thinking about width, that is quite reasonable: [Sankey diagrams](https://en.wikipedia.org/wiki/Sankey_diagram) and highway lanes are two other instances where when things split off, overall "width" is preserved.

# Further thoughts

Warning: uncharacterized

<details>
<summary>Resistance</summary>


Ohm's law states that for many materials, the relationship between voltage drop and current through the material is proportional:

$$
V = IR
$$

This means that resistance is the ratio between voltage and current. In other words, two resistors with the same resistance can be visualized as **similar rectangles**.

High resistance means a very tall but skinny rectangle. This means that for a given voltage drop (induced by a battery - say, 5V) that since the rectangle is very narrow, then very little current can pass if it is used in the circuit.

Conversely, low resistance means a very wide and short rectangle. For that same voltage drop, a lot of current passes.

Actually, if thinking about similar rectangles, the series resistors makes a lot of sense. Combined with the series, If you make width constant (set it to 1), then the effective height is the sum of the individual heights. So effective resistance is the sum of individual resistance.

Resistors in parallel - because now height is conserved, it has to be set to 1. And width can be obtained by taking 1/resistance. And so the width , so the sum of widths is (1/R1 + 1/R2 + ... + 1/Rn) which gives effective width. And then taking the reciprocal to go back from width back to overall resistance yields 1/(1/R1 + 1/R2 + ... + 1/Rn).

</details>


<details>
<summary>Wire loss</summary>


The wire is just a resistor, but with a wire you can think of the voltage drop per distance. Then it becomes a ramp. (Resistors in generals can also be thought of as ramps - just over very short distances.)
In analogy with ohm's law, The ramp does get steeper the more current goes through. 

So in the case of a short circuit, you have a certain voltage drop and nothing but wire. In order for that wire to meet the voltage drop (and KVL), it needs to be a really steep ramp - so that means that tons of current goes through.

</details>

<details>
<summary>Capacitance</summary>


Capacitors dictate the voltage drop across it is proportional to the amount of charge stored; that is,

$$
C = \frac{q}{V}
$$

When thinking about the evolution of a simple battery-capacitor system over time, at first (to preserve KVL) the voltage offset must be provided by the wires, resulting in high initial current draw. But as charge is brought to the capacitor, so at the end, the capacitor contributes most of the voltage drop and the wires almost none (no current at steady state).

</details>
