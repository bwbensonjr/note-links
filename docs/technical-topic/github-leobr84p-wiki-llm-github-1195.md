---
id: 1195
url: https://github.com/LeoBR84p/wiki_llm
title: GitHub - LeoBR84p/wiki_llm · GitHub
domain: github.com
source_date: '2026-06-22'
tags:
- github-repo
- python
- llm
- cli-tool
summary: wiki_llm is a Python tool that automatically transforms scattered documents
  (PDFs, Word files, Markdown, etc.) into an organized, navigable knowledge base powered
  by large language models. The system uses a fully automated pipeline featuring intelligent
  summarization, automatic taxonomy generation, content deduplication, and built-in
  chat search—eliminating the need for manual documentation work. It leverages semantic
  Markdown processing through markdown-hero to ensure all generated wiki pages are
  structurally valid and ready for integration with tools like Obsidian, MkDocs, or
  Docusaurus.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# GitHub - LeoBR84p/wiki_llm · GitHub

wiki-llm
========

[![CI](https://github.com/your-org/wiki-llm/actions/workflows/ci.yml/badge.svg)](https://github.com/your-org/wiki-llm/actions)
[![Python versions](https://camo.githubusercontent.com/96abf9b704f80578ea56dd10cab0d911c56d46dbec347f431ece9cf60ac175ad/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f707974686f6e2d332e31312532422d626c7565)](https://www.python.org/)
[![License: MIT](https://camo.githubusercontent.com/fdf2982b9f5d7489dcf44570e714e3a15fce6253e0cc6b5aa61a075aac2ff71b/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4c6963656e73652d4d49542d79656c6c6f772e737667)](/LeoBR84p/wiki_llm/blob/main/LICENSE)
[![Powered by markdown-hero](https://camo.githubusercontent.com/9955dcfe745c316c58842bc6235b42c9543335bef169958242c51f4aff7bacd6/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f706f776572656425323062792d6d61726b646f776e2d2d6865726f2d626c756576696f6c6574)](https://github.com/LeoBR84p/markdown_hero)

**Turn any document collection into an intelligent wiki — powered by LLM, no code required.**

Drop your `.docx`, `.pdf`, `.md` files into a folder — manuals, recipes, news articles, procedures, regulations, any textual content. Write a Python config file with your domain rules. Run one command. The wiki is generated, organized, and maintained automatically.

---

Why wiki-llm?
-------------

Organizations, teams, and content creators have **knowledge scattered across documents** — manuals, procedures, articles, recipes, policies — that nobody reads because it's inaccessible. Turning that archive into a navigable knowledge base requires:

* Hours of manual summarization by documentation specialists
* Hand-maintained taxonomies that quickly go stale
* No way to ask "which documents cover topic X?"

**wiki-llm solves this with a fully automated pipeline:**

| Problem | Solution |
| --- | --- |
| Documents in mixed formats | Ingests `.docx`, `.pdf`, `.md`, `.txt`, `.xlsx`, `.pptx` |
| Summaries nobody writes | Writer → Evaluator → Editor: pages generated and self-reviewed |
| Unstable IDs that break when files are renamed | Deterministic UUID derived from content hash |
| Stale taxonomies | Automatic term collection + LLM normalization |
| Broken links and orphan pages | LangGraph repair agent after every run |
| "Where is that manual about X?" | Built-in RAG chat (BM25 + LLM, no vector store) |
| Export for meetings | Word (`.docx`) output via markdown-hero |



---

The role of markdown-hero
-------------------------

> **markdown-hero** is the Markdown processing layer that makes the entire pipeline's intelligence possible.

Without a library that understands the *semantics* of Markdown — not just its syntax — an LLM pipeline produces structural garbage: duplicate sections, malformed frontmatter, broken links, out-of-order headings.

**What markdown-hero does in this project:**

| Function | Where it is used |
| --- | --- |
| `extract_frontmatter()` | Reads YAML metadata from documents in the reader |
| `remove_frontmatter()` | Isolates the body before sending it to the LLM |
| `strip()` | Cleans text before hashing — makes the UUID invariant to superficial formatting differences |
| `extract_chunks(purpose="rag")` | Splits pages into section-aware chunks for the BM25 chat index |
| `markdown_merge(dedupe_headings=True)` | Pre-pass for consolidation: structurally merges duplicate content before LLM semantic deduplication |
| `lint()` | Detects skipped headings, duplicate anchors, and unclosed fences before the repair agent |
| `word_format()` | Exports the entire wiki to professionally styled `.docx` files |

**Result:** every wiki page that leaves the pipeline is structurally valid Markdown with consistent frontmatter, ready to be consumed by Obsidian, MkDocs, Docusaurus, or any GFM renderer.

---

Installation
------------

### uv (recommended)

```
uv add wiki-llm
```

Or directly from the repository:

```
uv pip install git+https://github.com/your-org/wiki-llm.git
```

### pip

```
pip install wiki-llm
```

---

Installation-free agent workflow
--------------------------------

If you want to run this project logic directly from an AI coding assistant without installing this repository as a package, use the instruction files below:

* [AGENTS.md](/LeoBR84p/wiki_llm/blob/main/AGENTS.md): canonical workflow and stage-by-stage pipeline rules (setup, read, generate, topics, groups, index, consolidate, lint, repair).
* [CLAUDE.md](/LeoBR84p/wiki_llm/blob/main/CLAUDE.md): Claude-focused entry point that delegates to `AGENTS.md`.

This mode is useful when you want a lightweight, prompt-driven execution model where the assistant follows the documented pipeline and writes wiki outputs directly in your workspace.

---

Quick start
-----------

**1. Set up your secrets:**

```
cp .env.example .env
# Edit .env: fill in WIKI_BACKEND and the corresponding API keys
```

**2. Drop your documents:**

```
content_new/
  manuals/             <- subfolder name defines the entity_type
    onboarding.docx
    usage-policy.pdf
  procedures/
    customer-support.md
    ticket-opening.txt
```

**3. Create your config** (or use the setup wizard):

```
python -m src setup
```

Or write it manually:

```
# config/my_wiki.py
from pathlib import Path
from src.models.config import WikiConfig, EntityTypeConfig, LLMConfig

config = WikiConfig(
    wiki_name="My Wiki",
    wiki_dir=Path("wiki"),
    log_dir=Path("logs"),
    llm=LLMConfig(backend="openrouter", model_id="mistralai/mistral-7b-instruct:free"),
    entity_types=[
        EntityTypeConfig(
            name="Manual",
            slug="manuals",
            wiki_subdir="Manuals",
            prompt_generate=Path("prompts/summarize.md"),
            prompt_evaluate=Path("prompts/evaluate.md"),
        )
    ],
    prompt_editor=Path("prompts/editor.md"),
    prompt_lint=Path("prompts/lint.md"),
    prompt_consolidate=Path("prompts/consolidate.md"),
    prompt_chat=Path("prompts/chat.md"),
)
```

**4. Run:**

```
# Full pipeline
python -m src --config config/my_wiki.py run-all

# Generate pages only (incremental by default)
python -m src --config config/my_wiki.py generate

# Force regeneration with 8 parallel workers
python -m src --config config/my_wiki.py generate --force --workers 8

# Start the chat interface
python -m src --config config/my_wiki.py chat
```

---

CLI reference
-------------

```
Usage: python -m src [OPTIONS] COMMAND [ARGS]

Global options:
  --config PATH      Python WikiConfig file               [default: config/wiki_config.py]
  --force            Regenerate existing pages
  --workers N        Parallel workers for page generation  [default: 4]
  --verbose          Detailed logging
  --no-interactive   Skip confirmation prompts

Commands:
  setup        Interactive wizard to generate config and .env files
  generate     Read content_new/, generate pages, move files to content_processed/ or content_error/
  topics       Collect terms, normalize via LLM, generate taxonomy pages
  groups       Generate organizational grouping pages
  index        Rebuild index.md
  consolidate  Merge duplicates (markdown-hero + LLM)
  lint         Static + semantic analysis (markdown-hero + LLM)
  repair       lint + LangGraph automatic repair agent
  run-all      All stages in order
  chat         Start RAG chat server (NiceGUI)
```

---

Configuration
-------------

The config file is a Python module that exposes `config: WikiConfig` (or `get_config() -> WikiConfig`).

### Supported LLM backends

| Backend | Environment variable |
| --- | --- |
| `openrouter` | `OPENROUTER_APIKEY` |
| `openai` | `OPENAI_API_KEY` |
| `bedrock` | `AWS_LOGINKEY` + `WIKI_BEDROCK_REGION` |
| `ollama` | *(no authentication)* |

### Generated wiki structure

```
wiki/
  Manuals/                         <- EntityTypeConfig.wiki_subdir
    3f6a1b2c-...-uuid.md           <- content UUID (deterministic)
    7c9e4d1a-...-uuid.md
    raw/                           <- original content converted to Markdown (unstripped)
      3f6a1b2c-...-uuid_raw.md
      7c9e4d1a-...-uuid_raw.md
  Topics/                          <- TaxonomyConfig.wiki_subdir
    quality-management.md
  Groups/                          <- GroupingConfig.wiki_subdir
    finance-team.md
  index.md
  lint_report.md
logs/
  {run_id}_summary.jsonl
  {run_id}_detail.jsonl
```

> **About content UUIDs:** each document receives a UUID derived from the SHA-256 of the stripped text (`md_strip()`). The ID is **deterministic and content-addressable** — the same content always produces the same UUID, regardless of filename, metadata, or superficial formatting. The `raw/` page preserves the original Markdown without cleaning, with `content_sha256` for traceability.

---

Architecture
------------

```
content_new/          wiki/
    |                   ^
    v                   |           content_processed/
FilesystemReader                    (success) ^
                                    content_error/
                                    (failure) ^     write_atomic()
(.docx -> markitdown  -----------------------------------------
 .pdf  -> pluggable)       Pipeline (asyncio.gather)
    |                +----------------------------------+
    v                |  generate   -> Writer->Eval->Editor
 Document[]          |               + raw page (original)
(Pydantic)           |  topics     -> collect -> normalize
 id = UUID(          |  groups     -> metadata grouping
  SHA-256(           |  index      -> rebuild index.md
  md_strip(body)     |  consolidate-> markdown_merge + LLM
 ))                  |  lint       -> markdown_hero.lint()
                     |  repair     -> LangGraph agent
                     +----------------------------------+
                              |
                    LLMLogger (JSONL)
                    + Chat UI (NiceGUI + BM25)
```

**Key components:**

* **Pydantic v2** — typed contracts between all pipeline stages
* **instructor** — structured extraction with automatic retry on any LLM backend
* **markdown-hero** — semantic Markdown processing (chunking, lint, merge, Word export)
* **LangGraph** — repair agent with parallel fan-out
* **rank\_bm25** — chat retrieval without vector store or embeddings
* **Jinja2** — parameterized prompt templates

---

Environment variables
---------------------

See [`.env.example`](/LeoBR84p/wiki_llm/blob/main/.env.example) for the full list. Key variables:

```
WIKI_BACKEND=openrouter          # bedrock | openrouter | openai | ollama
WIKI_MODEL_ID=mistralai/mistral-7b-instruct:free
OPENROUTER_APIKEY=sk-or-...
WIKI_DIR=wiki
CONTENT_DIR=content_new
WIKI_UI_PORT=8080
```

---

Supported input formats
-----------------------

| Extension | Converter |
| --- | --- |
| `.md`, `.txt` | native |
| `.docx`, `.pptx`, `.xlsx` | [markitdown](https://github.com/microsoft/markitdown) |
| `.pdf` | pluggable via `PdfReaderProtocol` (e.g. pymupdf, pytesseract, Azure DI) |



---

Documentation
-------------

* Full configuration example: [`config/exemplo_normas.py`](/LeoBR84p/wiki_llm/blob/main/config/exemplo_normas.py)
* markdown-hero reference: [docs/reference.md](https://github.com/LeoBR84p/markdown_hero/blob/main/docs/reference.md)
* Medium article (more context and background): [Building wiki-llm with agent-driven workflows](https://medium.com/@bernardo.leandro/08b31170999a?sk=03579bb6d5a6f297495025a8d311ea08)

---

Contributing
------------

1. Fork -> branch `feat/my-feature`
2. `uv sync --group dev` — install development dependencies
3. `pytest` — run the test suite
4. Pull Request against `main`

---

License
-------

[MIT](/LeoBR84p/wiki_llm/blob/main/LICENSE) (c) 2026

---

Contact
-------

Questions, suggestions, and bug reports:

* Email: [bernardo.leandro@gmail.com](mailto:bernardo.leandro@gmail.com)
* Website: <https://www.leobr.site>
* Buymeacoffee: <https://buymeacoffee.com/leobr>
* Use the subject prefix `wiki-llm:`
