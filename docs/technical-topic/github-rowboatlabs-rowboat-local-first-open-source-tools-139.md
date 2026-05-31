---
id: 139
url: https://github.com/rowboatlabs/rowboat
title: 'GitHub - rowboatlabs/rowboat: Local-first, open-source tools for automating
  everyday work.'
domain: github.com
source_date: '2025-11-19'
tags:
- github-repo
- cli-tool
- ai
- python
summary: RowboatX is a local-first, open-source CLI tool that enables users to create
  and manage background AI agents with shell access for automating everyday tasks
  like meeting research, podcast summarization, and Slack message triage. The tool
  supports integration with multiple AI models (OpenAI, Anthropic, Google, Ollama,
  etc.) and Model Context Protocol (MCP) servers to extend agent capabilities. Users
  can build, schedule, monitor, and run agents through simple commands, with an optional
  web UI (Rowboat Studio) available for those preferring a graphical interface.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# GitHub - rowboatlabs/rowboat: Local-first, open-source tools for automating everyday work.

[![rowboat-github-2](https://private-user-images.githubusercontent.com/6592213/547591215-fc463b99-01b3-401c-b4a4-044dad480901.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3ODAyNDc3MzMsIm5iZiI6MTc4MDI0NzQzMywicGF0aCI6Ii82NTkyMjEzLzU0NzU5MTIxNS1mYzQ2M2I5OS0wMWIzLTQwMWMtYjRhNC0wNDRkYWQ0ODA5MDEucG5nP1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQVZDT0RZTFNBNTNQUUs0WkElMkYyMDI2MDUzMSUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyNjA1MzFUMTcxMDMzWiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9OTQxYjhlMjkyNWQyM2YyNDg5NDhkYjQ3MTEyMjY2ZGI2ZjFlMzBkMGViMDQ0OTYyNDdhOGM5OGZiNjM2NWFjMyZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QmcmVzcG9uc2UtY29udGVudC10eXBlPWltYWdlJTJGcG5nIn0.Yee68Caqk_ImhfOeTSe4CROTXApl4yt70p0sRmqcVd0)](https://www.youtube.com/watch?v=5AWoGo-L16I)

##### [rowboatlabs/rowboat | Trendshift](https://trendshift.io/repositories/13609) [Website](https://www.rowboatlabs.com/) [Discord](https://discord.gg/wajrgmJQ6b) [Twitter](https://x.com/intent/user?screen_name=rowboatlabshq) [Y Combinator](https://www.ycombinator.com)

Rowboat
=======

**Open-source AI coworker that turns work into a knowledge graph and acts on it**

Rowboat connects to your email and meeting notes, builds a long-lived knowledge graph, and uses that context to help you get work done - privately, on your machine.

You can do things like:

* `Build me a deck about our next quarter roadmap` → generates a PDF using context from your knowledge graph
* `Prep me for my meeting with Alex` → pulls past decisions, open questions, and relevant threads into a crisp brief (or a voice note)
* Track a person, company or topic through live notes
* Visualize, edit, and update your knowledge graph anytime (it’s just Markdown)
* Record voice memos that automatically capture and update key takeaways in the graph

Download latest for Mac/Windows/Linux: [Download](https://www.rowboatlabs.com/downloads)

⭐ If you find Rowboat useful, please star the repo. It helps more people find it.

Demo
----

[![Demo](https://private-user-images.githubusercontent.com/6592213/575088204-8b9a859b-d4f1-47ca-9d1d-9d26d982e15d.gif?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3ODAyNDc3MzMsIm5iZiI6MTc4MDI0NzQzMywicGF0aCI6Ii82NTkyMjEzLzU3NTA4ODIwNC04YjlhODU5Yi1kNGYxLTQ3Y2EtOWQxZC05ZDI2ZDk4MmUxNWQuZ2lmP1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQVZDT0RZTFNBNTNQUUs0WkElMkYyMDI2MDUzMSUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyNjA1MzFUMTcxMDMzWiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9NjAwYjM3MDViNWFlMWMxNTVmMjVkMGVlMDZmYTA5YjI3ZmNhM2UyMDY5NTgyZjVmOTJkOGMzOTFjYjUzZjkxNCZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QmcmVzcG9uc2UtY29udGVudC10eXBlPWltYWdlJTJGZ2lmIn0.qf2BxCWIHKrbZg2am97vJrsYatId6H7OEQ68mueoWFY)](https://www.youtube.com/watch?v=7xTpciZCfpw)

[Watch the full video](https://www.youtube.com/watch?v=7xTpciZCfpw)

---

Installation
------------

**Download latest for Mac/Windows/Linux:** [Download](https://www.rowboatlabs.com/downloads)

**All release files:** <https://github.com/rowboatlabs/rowboat/releases/latest>

### Google setup

To connect Google services (Gmail, Calendar, and Drive), follow [Google setup](https://github.com/rowboatlabs/rowboat/blob/main/google-setup.md).

### Voice input

To enable voice input and voice notes (optional), add a Deepgram API key in `~/.rowboat/config/deepgram.json`

### Voice output

To enable voice output (optional), add an ElevenLabs API key in `~/.rowboat/config/elevenlabs.json`

### Web search

To use Exa research search (optional), add the Exa API key in `~/.rowboat/config/exa-search.json`

### External tools

To enable external tools (optional), you can add any MCP server or use Composio tools by adding an API key in `~/.rowboat/config/composio.json`

All API key files use the same format:

```
{
  "apiKey": "<key>"
}
```

What it does
------------

Rowboat is a **local-first AI coworker** that can:

* **Remember** the important context you don’t want to re-explain (people, projects, decisions, commitments)
* **Understand** what’s relevant right now (before a meeting, while replying to an email, when writing a doc)
* **Help you act** by drafting, summarizing, planning, and producing real artifacts (briefs, emails, docs, PDF slides)

Under the hood, Rowboat maintains an **Obsidian-compatible vault** of plain Markdown notes with backlinks — a transparent “working memory” you can inspect and edit.

Integrations
------------

Rowboat builds memory from the work you already do, including:

* **Gmail** (email)
* **Google Calendar**
* **Rowboat meeting notes** or **Fireflies**

It also contains a library of product integrations through Composio.dev

How it’s different
------------------

Most AI tools reconstruct context on demand by searching transcripts or documents.

Rowboat maintains **long-lived knowledge** instead:

* context accumulates over time
* relationships are explicit and inspectable
* notes are editable by you, not hidden inside a model
* everything lives on your machine as plain Markdown

The result is memory that compounds, rather than retrieval that starts cold every time.

What you can do with it
-----------------------

* **Meeting prep** from prior decisions, threads, and open questions
* **Email drafting** grounded in history and commitments
* **Docs & decks** generated from your ongoing context (including PDF slides)
* **Follow-ups**: capture decisions, action items, and owners so nothing gets dropped
* **On-your-machine help**: create files, summarize into notes, and run workflows using local tools (with explicit, reviewable actions)

Live notes
----------

Live notes are notes that stay updated automatically. You can create one by typing '@rowboat' on a note.

* Track a competitor or market topic across X, Reddit, and the news
* Monitor a person, project, or deal across web or your communications
* Keep a running summary of any subject you care about

Everything is written back into your local Markdown vault. You control what runs and when.

Bring your own model
--------------------

Rowboat works with the model setup you prefer:

* **Local models** via Ollama or LM Studio
* **Hosted models** (bring your own API key/provider)
* Swap models anytime — your data stays in your local Markdown vault

Extend Rowboat with tools (MCP)
-------------------------------

Rowboat can connect to external tools and services via **Model Context Protocol (MCP)**.
That means you can plug in (for example) search, databases, CRMs, support tools, and automations - or your own internal tools.

Examples: Exa (web search), Twitter/X, ElevenLabs (voice), Slack, Linear/Jira, GitHub, and more.

Local-first by design
---------------------

* All data is stored locally as plain Markdown
* No proprietary formats or hosted lock-in
* You can inspect, edit, back up, or delete everything at any time

---

[Discord](https://discord.gg/wajrgmJQ6b) · [Twitter](https://x.com/intent/user?screen_name=rowboatlabshq)
