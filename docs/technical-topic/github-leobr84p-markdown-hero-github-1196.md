---
id: 1196
url: https://github.com/LeoBR84p/markdown_hero/tree/main
title: GitHub - LeoBR84p/markdown_hero · GitHub
domain: github.com
source_date: '2026-06-22'
tags:
- github-repo
- python
- cli-tool
- tutorial
summary: markdown_hero is a Python library that provides comprehensive tools for processing
  Markdown files, including cleanup, chunking, Word export, file concatenation, splitting,
  and validation with support for GitHub Flavored Markdown. The library offers both
  programmatic functions and command-line interface commands for common tasks like
  normalizing text, extracting document chunks for RAG purposes, converting to .docx
  format, and detecting formatting issues. It's compatible with Python 3.10+ and includes
  features for managing metadata, extracting frontmatter and document elements, and
  intelligently merging multiple Markdown files.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# GitHub - LeoBR84p/markdown_hero · GitHub

markdown\_hero
==============

[![CI](https://github.com/leobr84p/markdown_hero/actions/workflows/ci.yml/badge.svg)](https://github.com/leobr84p/markdown_hero/actions/workflows/ci.yml)
[![PyPI version](https://camo.githubusercontent.com/2aa27018534876e161b82ea87c70791e0cb2d32a6c684e73d1e411181c14952a/68747470733a2f2f696d672e736869656c64732e696f2f707970692f762f6d61726b646f776e5f6865726f2e737667)](https://pypi.org/project/markdown_hero/)
[![Python versions](https://camo.githubusercontent.com/6be4165a60b2f2a7d547d5b1f72213d569050ae003650b794315a4038f9d6a34/68747470733a2f2f696d672e736869656c64732e696f2f707970692f707976657273696f6e732f6d61726b646f776e5f6865726f2e737667)](https://pypi.org/project/markdown_hero/)
[![License: MIT](https://camo.githubusercontent.com/fdf2982b9f5d7489dcf44570e714e3a15fce6253e0cc6b5aa61a075aac2ff71b/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4c6963656e73652d4d49542d79656c6c6f772e737667)](/LeoBR84p/markdown_hero/blob/main/LICENSE)
[![Typed](https://camo.githubusercontent.com/a36d636ac92948968a17b9ec10ef1253a741436531b5a463c02c505d4a8675f1/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f747970696e672d74797065642d627269676874677265656e2e737667)](https://peps.python.org/pep-0561/)

A Python library for processing Markdown — cleanup, chunking, Word
(.docx) export, concatenation, splitting by delimiters, and validation.

Compatible with Python 3.10+. Target dialect: GitHub Flavored Markdown (GFM).

Installation
------------

```
pip install markdown_hero
# with a real tokenizer (tiktoken) for accurate chunking:
pip install "markdown_hero[tokenizers]"
```

Main functions
--------------

| Function | What it does |
| --- | --- |
| `strip(md, ...)` | Reduces Markdown to normalized plain text (no diacritics, no punctuation, lowercase). |
| `extract_chunks(md, purpose=...)` | Splits the document respecting heading hierarchy, with rich metadata. |
| `word_format(md, output)` | Exports to .docx with a fixed set of professional styles. |
| `markdown_append(*paths, output)` | Concatenates files with heading shift and frontmatter merge. |
| `markdown_break(path, delimiter, ...)` | Splits a file into N+1 parts. Accepts string, regex, or list. |
| `markdown_merge(*paths, output)` | Smart append with section dedupe and TOC generation. |
| `extract_*` | Frontmatter, links, images, tables, code blocks, headings, TOC. |
| `lint(md)` | Detects skipped headings, duplicate anchors, unclosed fences. |
| CLI `markdown-hero` | Command-line access. |

See `docs/reference.md` for the full technical reference and
`docs/helpers.md` for the index of internal utilities.

Quick example
-------------

```
from markdown_hero import strip, extract_chunks, word_format

text = "**Hello!** See [docs](https://x). p=2 captures both."
print(strip(text))
# "hello see docs p2 captures both"

chunks = extract_chunks(open("doc.md").read(), purpose="rag", max_tokens=512)
word_format("doc.md", "doc.docx")
```

CLI
---

```
markdown-hero strip doc.md -o doc.txt
markdown-hero chunk doc.md --purpose rag --max-tokens 512 -o chunks.json
markdown-hero word doc.md -o doc.docx
markdown-hero append a.md b.md -o merged.md
markdown-hero break doc.md "---" --output-dir parts/
markdown-hero lint doc.md
```

Documentation
-------------

* Technical reference: [`docs/reference.md`](/LeoBR84p/markdown_hero/blob/main/docs/reference.md)
* Internal helpers index: [`docs/helpers.md`](/LeoBR84p/markdown_hero/blob/main/docs/helpers.md)
* Release history: [`CHANGELOG.md`](/LeoBR84p/markdown_hero/blob/main/CHANGELOG.md)
* How to contribute: [`CONTRIBUTING.md`](/LeoBR84p/markdown_hero/blob/main/CONTRIBUTING.md)
* Security policy: [`SECURITY.md`](/LeoBR84p/markdown_hero/blob/main/SECURITY.md)

Contact
-------

Questions, suggestions, and reports:

* Email: [bernardo.leandro@gmail.com](mailto:bernardo.leandro@gmail.com)
* **Always include the prefix `Markdown Hero:` in the subject line** so
  the message is routed correctly.

For security vulnerabilities follow the instructions in
[`SECURITY.md`](/LeoBR84p/markdown_hero/blob/main/SECURITY.md) (same email, same subject prefix).

License
-------

[MIT](/LeoBR84p/markdown_hero/blob/main/LICENSE) © 2026 Bernardo Leandro.
