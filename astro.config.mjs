// @ts-check

import mdx from '@astrojs/mdx';
import sitemap from '@astrojs/sitemap';
import { defineConfig } from 'astro/config';

// https://astro.build/config
export default defineConfig({
	site: 'https://conjuncts.github.io',
	integrations: [mdx(), sitemap()],
	markdown: {
        remarkPlugins: [
            'remark-math',
        ],
        rehypePlugins: [
            ['rehype-katex', {
                macros: {
                    "\\pdc": "\\left(\\frac{\\partial #1}{\\partial #2}\\right)_{#3}",
                    "\\dd": "\\frac{d#1}{d#2}",
                    "\\pd": "\\frac{\\partial #1}{\\partial #2}"
                }
            }]
        ]
    }
});
