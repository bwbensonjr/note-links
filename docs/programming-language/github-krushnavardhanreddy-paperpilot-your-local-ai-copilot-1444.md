---
id: 1444
url: https://github.com/KrushnaVardhanReddy/PaperPilot
title: 'GitHub - KrushnaVardhanReddy/PaperPilot: Your local AI copilot for documents
  · GitHub'
domain: github.com
source_date: '2026-10-26'
tags:
- rust
- github-repo
- cli-tool
- ai
summary: PaperPilot is an open-source, Rust-based PDF and document toolkit that runs
  locally, so files never leave the user's machine. It offers the same engine through
  an MCP server for AI coding agents, a CLI, a browser (WASM) version, a desktop app,
  and a local REST API, with features spanning merging, compression, OCR, text extraction,
  security scanning, and Excel conversion. Its key selling points are privacy, consistent
  behavior across all interfaces, and first-class support for AI agent integration.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-5-5
---

# GitHub - KrushnaVardhanReddy/PaperPilot: Your local AI copilot for documents · GitHub

PaperPilot
==========

**PDF tools for your AI agent — and for you. Pure Rust. Runs locally. Files never leave your machine.**

[![CI](https://github.com/KrushnaVardhanReddy/PaperPilot/actions/workflows/rust.yml/badge.svg)](https://github.com/KrushnaVardhanReddy/PaperPilot/actions)
[![License: Apache 2.0](https://camo.githubusercontent.com/5b60841bea9e11d9d0b0950d690c9bc554e06385634056a7d5d62a15d1a4eabe/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4c6963656e73652d4170616368655f322e302d626c75652e737667)](/KrushnaVardhanReddy/PaperPilot/blob/main/LICENSE)
[![Rust 1.75+](https://camo.githubusercontent.com/eacc1bb9ed9ca0f62e9f291205449010ea03f45f969f7fa7010b2a7442ef60c0/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f727573742d312e37352532422d6f72616e67652e737667)](https://www.rust-lang.org)
[![MCP Compatible](https://camo.githubusercontent.com/c332c857e0683a73d89ebd05aaaba82cb85137fc6cfc7b31bb1eb92049b1b4d7/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4d43502d3130302532355f436f6d70617469626c652d707572706c652e737667)](https://modelcontextprotocol.io)
[![PRs Welcome](https://camo.githubusercontent.com/dd0b24c1e6776719edb2c273548a510d6490d8d25269a043dfabbd38419905da/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f5052732d77656c636f6d652d627269676874677265656e2e737667)](/KrushnaVardhanReddy/PaperPilot/blob/main/CONTRIBUTING.md)

[![PaperPilot demo](/KrushnaVardhanReddy/PaperPilot/raw/main/docs/assets/demo.gif)](/KrushnaVardhanReddy/PaperPilot/blob/main/docs/assets/demo.gif)

[**Try it in your browser →**](https://usepaperpilot.com) · [Download](https://github.com/KrushnaVardhanReddy/PaperPilot/releases) · [Contributing](/KrushnaVardhanReddy/PaperPilot/blob/main/CONTRIBUTING.md) · [Roadmap](/KrushnaVardhanReddy/PaperPilot/blob/main/ROADMAP.md)

PaperPilot is a PDF and document toolkit written in Rust. The same engine runs as:

| Surface | Use it for |
| --- | --- |
| **MCP server** | Give Codex, Claude Code, Kimi Code, Pi, Claude Desktop, Cursor, or any MCP client the ability to merge, split, OCR, and compress PDFs |
| **CLI** | Batch and scripted workflows |
| **Browser (WASM)** | Zero-install tools; files are processed in browser memory, nothing is uploaded |
| **Desktop app** | Tauri + Svelte GUI with viewer, markup, and diff |
| **Local REST API** | Call it from Python, Node, or n8n at `localhost:7823` |

No Chromium, no C++ runtime, no cloud calls.

**Open-WebUI integration (source builds):** use the local gateway as a
PDF-only Tika-compatible extraction server. See the
[Open-WebUI setup guide](/KrushnaVardhanReddy/PaperPilot/blob/main/docs/integrations/open_webui.md).

---

Quick start
-----------

### 1. Use it with your coding agent (MCP)

Codex, Claude Code, Kimi Code, and current Pi releases connect to the same local
stdio server. See the [coding agent setup guide](/KrushnaVardhanReddy/PaperPilot/blob/main/docs/coding-agents.md) for each
client's configuration and verification steps. Builds from this source can also
print ready-to-merge configuration:

```
paperpilot-mcp --client-config codex
# Also: claude-code, kimi-code, pi, claude-desktop, cursor
```

Download `paperpilot-mcp` from [Releases](https://github.com/KrushnaVardhanReddy/PaperPilot/releases), then add it to `claude_desktop_config.json`:

```
{
  "mcpServers": {
    "paperpilot": {
      "command": "/path/to/paperpilot-mcp"
    }
  }
}
```

Restart Claude and try: *"Merge these two PDFs and compress the result."*

### 2. Use the CLI

```
# Merge
paperpilot merge --inputs doc1.pdf doc2.pdf --output merged.pdf

# Compress
paperpilot compress --input in.pdf --quality 75 --output compressed.pdf

# Rotate pages 1, 3–5 by 90°
paperpilot rotate --input in.pdf --pages 1,3-5 --angle 90 --output out.pdf
```

### 3. Use it in the browser

Go to [usepaperpilot.com](https://usepaperpilot.com). Open your browser's Network tab while you work — you'll see no file uploads.

### 4. Build from source

```
git clone https://github.com/KrushnaVardhanReddy/PaperPilot.git
cd PaperPilot
cargo build --release -p paperpilot-cli -p paperpilot-mcp -p paperpilot-gateway
```

Desktop app:

```
cd apps/desktop && pnpm install && pnpm tauri dev
```

Requires Rust 1.75+, Node.js, and pnpm.

---

What it can do today (v0.6)
---------------------------

* **Organize & Layout:** merge, split, rotate, delete pages, reorder pages, extract pages, booklet imposition, N-up grid, multi-sheet poster tile slicing (`pdf_posterize`)
* **Optimize & Compress:** lossy compression, stream deduplication, CMYK safety guards
* **Extract & Ingest:** structured text, detected Markdown tables, native Open-WebUI & Apache Tika ingestion adapter (`/tika/text`, `/tika/json/md`, `/rmeta/text`), pure-Rust OCR (PaddleOCR via `rten`)
* **Security & Analysis:** watermark, validate signatures, remove signatures, PII scan, deep sanitize, malformed fuzzing & panic-free error handling
* **Office Data:** Excel → JSON, Excel → CSV

---

Why another PDF tool?
---------------------

* **Private by default.** Everything runs locally or in your browser tab.
* **Agent-ready.** MCP support is first-class, not an afterthought.
* **One engine, many surfaces.** CLI, MCP, REST, WASM, and desktop share the same Rust core, so behavior is consistent.
* **Small and dependency-light.** Pure Rust, built on [`lopdf`](https://github.com/J-F-Liu/lopdf), [`pdf_oxide`](https://crates.io/crates/pdf_oxide), [`rten`](https://github.com/robertknight/rten), and friends.

Benchmarks
----------

Run `cargo bench --workspace` to reproduce. Methodology and results: [SYSTEM\_BENCHMARK\_REPORT.md](/KrushnaVardhanReddy/PaperPilot/blob/main/SYSTEM_BENCHMARK_REPORT.md).

---

Architecture
------------

```
Desktop (Tauri) · CLI · REST (Axum) · MCP (stdio) · WASM (browser / edge)
                              │
                       Rust core workspace
   paperpilot-core · paperpilot-pdf · paperpilot-nlp · paperpilot-gateway
   paperpilot-mcp · paperpilot-wasm · paperpilot-storage
```

Embed in your own site
----------------------

```
<script src="https://cdn.usepaperpilot.com/embed.js" data-tools="merge,compress,ocr"></script>
<div id="paperpilot-widget"></div>
```

Local REST API & Document Ingestion
-----------------------------------

```
paperpilot serve --port 7823
# Standard PDF Operations (JSON & multipart)
curl -X POST http://localhost:7823/api/v1/pdf/merge \
  -H "Content-Type: application/json" \
  -d '{"inputs": ["a.pdf", "b.pdf"], "output": "out.pdf"}'

# Open-WebUI & Tika In-Memory Ingestion (sub-5ms)
curl -X PUT http://localhost:7823/tika/text \
  -H "Content-Type: application/pdf" \
  --data-binary @sample.pdf
```

Interactive Swagger OpenAPI docs at `http://localhost:7823/swagger-ui`.

---

Contributing & Community
------------------------

Issues and PRs are welcome. Good first contributions: bug reports with a sample PDF, new tool requests, and docs fixes.

Special thanks to all community members and contributors recognized in [CONTRIBUTORS.md](/KrushnaVardhanReddy/PaperPilot/blob/main/CONTRIBUTORS.md).

License
-------

Community Edition (this repo): [Apache 2.0](/KrushnaVardhanReddy/PaperPilot/blob/main/LICENSE). It includes the CLI, MCP server, REST gateway, WASM engine, and desktop app.

An Enterprise Edition (SSO, RBAC, audit logs, DLP) is developed separately.
