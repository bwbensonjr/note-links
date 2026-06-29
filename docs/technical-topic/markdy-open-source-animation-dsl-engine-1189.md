---
id: 1189
url: https://markdy.com/
title: Markdy — Open-Source Animation DSL Engine
domain: markdy.com
source_date: '2026-06-25'
tags:
- github-repo
- web-dev
- cli-tool
summary: Markdy is an open-source animation DSL (Domain Specific Language) engine
  that allows users to create motion graphics and animations through code, similar
  to how Mermaid works for diagrams. To start an animation project, users must first
  define a canvas scene by specifying properties like width, height, frame rate, background
  color, and optional duration. The tool uses a `.markdy` file format where the scene
  setup serves as the foundational first line for any animation.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# Markdy — Open-Source Animation DSL Engine

1

### Scene Setup

Every animation starts by defining the canvas. This must be the first line in your `.markdy` file.

```
scene width=800 height=400 fps=30 bg=#fafafa
```

| Property | Default | Description |
| --- | --- | --- |
| `width` | `800` | Canvas width in pixels |
| `height` | `400` | Canvas height in pixels |
| `fps` | `30` | Frame rate for the rendering engine |
| `bg` | `white` | Any CSS color value (e.g. `#1a1a2e`) |
| `duration` | *auto* | Override total length in seconds |
