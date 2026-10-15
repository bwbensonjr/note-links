---
id: 1422
url: https://uji.sh/ito/
title: ito playground · uji
domain: uji.sh
source_date: '2026-10-15'
tags:
- tutorial
- cli-tool
- llm
summary: This page is an interactive workshop for building terminal user interfaces
  (TUIs) in Lua, with a code editor and live preview where edits update the output
  as you type. It walks through examples like input flow, a counter, a daily list,
  preferences, and a small shop, and explains core concepts such as using require("ito")
  to return a view function, ito.state for changing values, and layout and styling
  modifiers like :spacing(), :padding(), and :bold(). A reference guide (ito.md) is
  also provided that can be shared with an LLM.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-5-5
---

# ito playground · uji

ITO / AN INTERACTIVE WORKSHOP

Make something with Lua.
========================

Build your own terminal UI.

Your earlier drafts are still available. Download your previous drafts

Start here

01Input flow02Counter03Daily list04Preferences05Little shop

CodePreview

main.luaito.md

**Something needs a look.**Go to line

Ln 1, Col 1

Reset example

Preview

Getting your workspace ready…

Loading

A few things to try+

The same Lua
------------

Start with `require("ito")` and return a function that builds a view. Use `ito.state(value)` for values that change.

Compose with `VStack`, `HStack`, `Text`, and the controls in `ito.md`.

Views and modifiers
-------------------

Use `:spacing(1)`, `:padding(2)`, `:grow()`, `:bold()`, and `:dim()` to arrange and style your views.

Try your changes
----------------

Your preview updates as you edit. If an edit has an error, the last working preview stays visible.

Try Input flow for keyboard navigation, editing, and cancellation. Use the expand icon for fullscreen. Open `ito.md` for a guide you can give your LLM.
