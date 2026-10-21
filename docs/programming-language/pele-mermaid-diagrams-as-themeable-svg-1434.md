---
id: 1434
url: https://pele.run/
title: Pele · Mermaid diagrams as themeable SVG
domain: pele.run
source_date: '2026-10-17'
tags:
- javascript
- web-dev
summary: Pele is a lightweight, open source JavaScript library that renders Mermaid
  diagram syntax into SVG, with colors and fonts themed through CSS variables that
  apply without re-rendering. Compared to Mermaid.js, it has a much smaller bundle
  (about 230 kB gzipped versus 1.6 MB), faster render times (0.05–0.3 ms), and zero
  direct dependencies. It is installable via npm, pnpm, yarn, or bun, and you call
  its render() function and insert the returned SVG into your page.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-5-5
---

# Pele · Mermaid diagrams as themeable SVG

![](/pele-home.svg)

Pele is a lightweight [open source](https://github.com/obsidianmd/pele) library that renders [Mermaid](https://mermaid.js.org) diagrams to SVG, [themed with CSS variables](/theming).
======================================================================================================================================================================================

Write Mermaid syntax, Pele renders it to SVG. Try editing the example below.

Mermaid

```
1flowchart TD2  A[Mermaid text] --> B{Flowchart?}3  B -- Yes --> C[Pele]4  B -- No --> D[Mermaid]5  C --> E([SVG])6  D --> E
```

Pele[Open in Playground](/playground#source=flowchart+TD%0A++A%5BMermaid+text%5D+--%3E+B%7BFlowchart%3F%7D%0A++B+--+Yes+--%3E+C%5BPele%5D%0A++B+--+No+--%3E+D%5BMermaid%5D%0A++C+--%3E+E%28%5BSVG%5D%29%0A++D+--%3E+E)

YesNoMermaid textFlowchart?PeleMermaidSVG

Use CSS variables to set colors and fonts. Color changes apply without re-rendering.

CSS

```
1.pele {2  --pele-bg: #fffcf0;3  --pele-fg: #100f0f;4  --pele-muted: #6f6e69;5  --pele-line: #100f0f;6  --pele-surface: #f2f0e5;7  --pele-surface-alt: #e6e4d9;8  --pele-border: #cecdc3;9}
```

Pele

ThemesVariablesLightDark

|  | Pele | Mermaid.js |
| --- | --- | --- |
| Bundle size gzip | 230 kB | 1.6 MB |
| Render time | 0.05–0.3 ms | 6–82 ms |
| Direct dependencies | 0 | 23 |
| Small screens | Adapts the layout | Scales the diagram |
| Theming | CSS variables | Theme configuration |

Add Pele to your app using the [API](/api).

npmpnpmyarnbun

```
1npm install pele
```

```
1pnpm add pele
```

```
1yarn add pele
```

```
1bun add pele
```

Pass Mermaid syntax to `render()` and insert the returned SVG into your page.

```
1import { render } from 'pele';23const { svg } = render(`flowchart LR4  A[Mermaid text] --> B[SVG]`);56document.querySelector('#diagram').innerHTML = svg;
```
