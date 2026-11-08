---
id: 1468
url: https://github.com/kobaltgit/StatCraft
title: 'GitHub - kobaltgit/StatCraft: High-performance, memory-safe, and open-source
  statistical analysis package in 100% pure Safe Rust · GitHub'
domain: github.com
source_date: '2026-11-08'
tags:
- rust
- github-repo
- statistics
- ai
summary: StatCraft is a free, open-source statistical software package written entirely
  in 100% safe Rust, designed as a clean-room alternative to proprietary suites like
  IBM SPSS Statistics. It offers a graphical interface with an SPSS-style output viewer,
  a syntax-driven analytical engine, and procedures such as descriptive statistics,
  t-tests, and one-way ANOVA. Its key differentiator is a local Model Context Protocol
  bridge that lets AI agents run statistical analyses through natural language while
  the deterministic Rust engine performs the actual calculations.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-5-5
---

# GitHub - kobaltgit/StatCraft: High-performance, memory-safe, and open-source statistical analysis package in 100% pure Safe Rust · GitHub

[![StatCraft Banner](/kobaltgit/StatCraft/raw/main/assets/banner.svg)](/kobaltgit/StatCraft/blob/main/assets/banner.svg)

[**English**](/kobaltgit/StatCraft/blob/main/README.md) |
[Русский](/kobaltgit/StatCraft/blob/main/README.ru.md)

[![Rust 1.80+](https://camo.githubusercontent.com/5afad1d84522c535870499f2c34acb10163fc3704c0906bb3e8f2a077c72560f/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f527573742d312e38302532422d6f72616e67653f6c6f676f3d72757374)](https://www.rust-lang.org/)
[![License: MIT OR Apache-2.0](https://camo.githubusercontent.com/f39131127545ad7907bcecba201dabc10b0b32199c4a45b16a35959a3eb21da4/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4c6963656e73652d4d49542532304f522532304170616368652d2d322e302d626c75652e737667)](/kobaltgit/StatCraft/blob/main/LICENSE-MIT)
[![Platform: Windows | Linux | macOS](https://camo.githubusercontent.com/db2400e631ed4ed2b89963c527d3ccc20f40e469ea17769c09c41c2b3e7147fe/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f506c6174666f726d2d57696e646f77732532302537432532304c696e75782532302537432532306d61634f532d6c69676874677265792e737667)](https://camo.githubusercontent.com/db2400e631ed4ed2b89963c527d3ccc20f40e469ea17769c09c41c2b3e7147fe/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f506c6174666f726d2d57696e646f77732532302537432532304c696e75782532302537432532306d61634f532d6c69676874677265792e737667)
[![100% Safe Rust](https://camo.githubusercontent.com/3d898384195b18a1b81a018079ba14687d0a20bfe0145b84f2b2e5cbaf5c8f1c/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4172636869746563747572652d31303025323525323053616665253230527573742d627269676874677265656e2e737667)](https://camo.githubusercontent.com/3d898384195b18a1b81a018079ba14687d0a20bfe0145b84f2b2e5cbaf5c8f1c/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4172636869746563747572652d31303025323525323053616665253230527573742d627269676874677265656e2e737667)
[![Tests: 90+ Passing](https://camo.githubusercontent.com/59ef5550078600cc486fef8c2e370bac8e19f6c13053b19b676da7b4a4e95c87/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f54657374732d50617373696e67253230283930253242292d737563636573732e737667)](https://camo.githubusercontent.com/59ef5550078600cc486fef8c2e370bac8e19f6c13053b19b676da7b4a4e95c87/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f54657374732d50617373696e67253230283930253242292d737563636573732e737667)
[![i18n: EN | RU](https://camo.githubusercontent.com/6877c2aee5162d2d6e505d56e490204ea8027c55e932a16b5ccbfbf4b49ca878/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6931386e2d454e25323025374325323052552d696e666f726d6174696f6e616c2e737667)](https://camo.githubusercontent.com/6877c2aee5162d2d6e505d56e490204ea8027c55e932a16b5ccbfbf4b49ca878/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6931386e2d454e25323025374325323052552d696e666f726d6174696f6e616c2e737667)
[![MCP: Live GUI Bridge & Code Mode](https://camo.githubusercontent.com/add1d9306235e68169155a2864f795fc8faf3e5d0e891cf5f6cb4909ff99da4f/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4d43502d4c697665253230475549253230427269646765253230253236253230436f64652532304d6f64652d3633363646313f6c6f676f3d616e7468726f706963266c6f676f436f6c6f723d7768697465)](#4-statcraft-bridge--ai-agents-model-context-protocol--code-mode)
[![Sponsor: Lava.top](https://camo.githubusercontent.com/4461eab75476594902a2e4a1a017a307c7ba779b197fb0ca66067379bd903869/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f53706f6e736f722d4c6176612e746f702d4646354333353f6c6f676f3d67697468756273706f6e736f7273266c6f676f436f6c6f723d7768697465)](https://app.lava.top/kobaltgit)

---

Overview
--------

**StatCraft** is a free, modern, open-source statistical software package built entirely in **100% pure Safe Rust**. Designed as an uncompromising, clean-room alternative to proprietary statistical suites such as IBM SPSS Statistics, StatCraft combines academic precision, instantaneous launch times, and guaranteed crash immunity.

Whether you are conducting psychological research, analyzing clinical trials, teaching university statistics, or manipulating enterprise datasets, StatCraft provides an intuitive graphical interface alongside a deterministic, syntax-driven analytical engine.

[![StatCraft Graphical Interface](/kobaltgit/StatCraft/raw/main/assets/screenshot.png)](/kobaltgit/StatCraft/blob/main/assets/screenshot.png)
  
*Interactive workspace: Variable View metadata dictionary, syntax execution log, and canonical SPSS-style Output Viewer with structured pivot tables.*

---

Core Pillars & Design Principles
--------------------------------

* **100% Safe Rust & Never Crash Guarantee:** Zero `unsafe` blocks, zero panics (`panic!`, `unwrap()`, `expect()`). Malformed datasets, empty samples, or division by zero yield explicit, typed `Result<T, E>` errors rather than application crashes.
* **Commands, Not Handlers:** Every analytical procedure and user interaction is an atomic engine command (`EngineCommand`). All commands support non-destructive Undo/Redo, serialize to standard SPSS syntax (`.sps`), and can be scripted headlessly.
* **Agent-Ready & MCP Bridge (Code Mode):** Built-in local IPC socket (port 18493) and Model Context Protocol (MCP) server (`--mcp` flag). Enables external autonomous AI agents (Antigravity, Claude, ChatGPT, Ollama) to inspect metadata, execute batch syntax, perform mathematical computations, and stream live results into the Output Viewer.
* **SPSS-Style Canonical Output Viewer:** Hierarchical navigation outline tree paired with authentic multi-level pivot tables. Results can be copied to the clipboard with one click as structured TSV data that pastes cleanly into Microsoft Excel without distorted columns or unwanted date conversions.
* **Vector-First UI:** Rendered with native `egui` via `ui.painter()` and vector SVG icons. Strict zero-emoji and zero-unsupported Unicode symbol policy eliminates tofu squares (`□`) across all platforms.
* **Zero-Hardcode i18n:** 100% of user-facing strings are decoupled into Project Fluent catalogs (`locales/en.ftl`, `locales/ru.ftl`) with real-time runtime language switching.
* **Resource Guard:** Thread-limited builds (`-j 1`, `codegen-units = 1`) protect development workstations from memory exhaustion.

---

Key Features
------------

Tip

📖 **Comprehensive Feature Guide:** An exhaustive reference of all available analytical procedures, data manipulations, transformation algorithms, and keyboard shortcuts is available in **[FEATURES.md](/kobaltgit/StatCraft/blob/main/docs/FEATURES.md)** (English) and **[FEATURES\_RU.md](/kobaltgit/StatCraft/blob/main/docs/FEATURES_RU.md)** (Русский).

### 1. Dual-View Data Management

* **Data View:** High-performance, virtualized tabular grid displaying cases and variables. Supports instant toggling between raw numeric values and human-readable value labels (`1/A`).
* **Variable View:** Comprehensive metadata dictionary managing:
  + **Name:** Normalized variable identifiers.
  + **Type:** 9 canonical SPSS types (Numeric, Comma, Dot, Scientific, Date, Dollar, Custom Currency, String, Restricted Numeric).
  + **Width & Decimals:** Visual width and precision control with custom vector spinners.
  + **Labels:** Descriptive variable titles displayed in dialogs and tables.
  + **Values:** Discrete and range value labels with dedicated modal editors.
  + **Missing Values:** Configurable discrete missing values and continuous missing ranges.
  + **Columns & Align:** Table layout and alignment (Left, Center, Right).
  + **Measure:** Measurement level classification (Scale, Ordinal, Nominal) with custom vector scale icons.

### 2. Parametric & Descriptive Statistical Procedures

* **Descriptive Statistics:** Mean, Std. Error Mean, Standard Deviation, Variance, Minimum, Maximum, Range, Sum, Skewness (with SE), Kurtosis (with SE), and Valid N (listwise).
* **Frequencies:** Frequency counts, percentages, valid percentages, cumulative percentages, discrete missing value breakdown, percentiles, and quartiles.
* **One-Sample T-Test:** Student's $t$-test against customizable test values, degrees of freedom, two-tailed significance, mean differences, confidence intervals ($95%$ default or user-defined), and dual-table SPSS output.
* **Independent-Samples T-Test:** Two-group comparison with automatic Levene's Test for Equality of Variances ($F$, $p$), Student's $t$-test (Equal Variances Assumed), Welch's $t$-test (Equal Variances Not Assumed), and full Group Statistics table.
* **Paired-Samples T-Test:** Dependent group comparison providing Paired Samples Statistics, Pearson Correlation coefficients ($r$, $p$), and Paired Differences test tables.
* **One-Way ANOVA:** One-Way Analysis of Variance with Fisher's $F$-test, between-groups and within-groups sums of squares, Levene's Test of Homogeneity of Variances, and descriptive statistics.

### 3. Canonical Output Viewer

* **Outline Tree Navigation:** Interactive document tree on the left panel to jump directly to any procedure, log, or table.
* **Pivot Tables:** Multi-tier nested tables with authentic SPSS headers, alternating row striping, and right-aligned numeric formatting.
* **TSV Clipboard Export:** One-click `[ Copy Table (TSV) ]` button with instant visual feedback and right-click context menus. Exports tables with clean headers and row separators specifically structured for Excel import.
* **Execution Protocols:** Monospace log blocks documenting executed SPSS syntax (`GET DATA`, `DESCRIPTIVES`, `T-TEST`, `ONEWAY`).

### 4. StatCraft Bridge & AI Agents (Model Context Protocol / Code Mode)

StatCraft is the world's first statistical software package natively equipped with the **Model Context Protocol (MCP)** and direct two-way control via autonomous AI agents (Antigravity, Claude, ChatGPT, Ollama, and local LLMs).

**🔍 Why StatCraft Bridge? Zero SPSS Experience Required (Click to expand)**

#### You No Longer Need to Learn SPSS: Statistical Analysis in Natural Language

Historically, performing rigorous statistical analysis required mastering legacy statistical GUI suites (SPSS, SAS, Stata) or writing complex code in R and Python. Researchers had to memorize arcane syntax commands (`DESCRIPTIVES VARIABLES=...`), navigate dozens of nested dialog boxes, or write data wrangling scripts from scratch.

**With StatCraft Bridge, that barrier is completely gone:** Connect your favorite AI assistant to StatCraft and describe what you want in plain human language:

> *"Inspect the loaded survey dataset. Compare the mean salary between males and females using an independent-samples t-test, check Levene's test for equality of variances, and explain in simple terms whether the difference is statistically significant."*

The AI agent will autonomously:

1. Query dataset metadata and variable dictionaries via the bridge;
2. Generate and execute commands through StatCraft's core;
3. Retrieve verified mathematical output tables;
4. Present a plain-language summary with effect sizes and $p$-value interpretations.

#### Why Use StatCraft Bridge Instead of Plain LLM Chat?

1. **Absolute Mathematical Exactness vs. LLM Hallucinations:**
   Large Language Models frequently hallucinate when processing thousands of numbers, calculating means, or estimating non-linear test statistics. StatCraft serves as the **deterministic calculation oracle**: the LLM guides the inquiry, while native Rust handles the math with $\le 10^{-6}$ precision verified against SciPy and SPSS algorithms.
2. **Real-Time Visual Synchronization on Your Screen:**
   As the agent executes procedures, the StatCraft desktop GUI updates live in front of you. Authentic Pivot Tables appear in the Output Viewer, syntax logs record the audit trail, and all results can be copied into Excel with a single click.
3. **100% Local & Privacy-Preserving:**
   The socket bridge runs locally (`127.0.0.1:18493`). Your medical, corporate, or private research data never leaves your workstation.
4. **Autonomous Code Mode:**
   Agents can run arbitrary SPSS syntax scripts (`.sps`), sort cases, filter subsets, recode scales, handle missing values, and trigger any of StatCraft's statistical modeling procedures.

#### How to Connect Your AI Agent

* **Desktop GUI:** Open `Extensions -> MCP Bridge / Copilot` in StatCraft. The dialog provides live server status, activity logs, and one-click configuration snippets for Antigravity, Claude Desktop, and Cursor.
* **Headless CLI (stdio MCP):** Configure `statcraft.exe --mcp` inside your MCP client settings.


---

Layered Architecture (L0 – L6)
------------------------------

StatCraft is engineered in strict compliance with the **ArtCraft Layering Law**. Dependencies flow strictly downwards:

```
L6: statcraft_app        Desktop GUI (egui / eframe / DialogKit / Output Viewer)
 └── L5: statcraft_syntax CommandBus, SPS syntax parser, engine transactions
      ├── L4: statcraft_reporting Pivot table models, TSV / HTML / Text export
      └── L2: statcraft_algo      Pure statistical math (Golden Oracle vs SciPy)
           └── L1: statcraft_core In-memory dataset, RawTable, VariableDictionary
                └── L0: statcraft_io  Data codecs (CSV/TSV streaming, Excel .xlsx/.xls/.ods, SPSS .sav/.zsav)

Cross-cutting utility crates:
* statcraft_bridge Local IPC socket (18493) and Model Context Protocol (MCP) server
* statcraft_i18n   Fluent localization engine with zero hardcoded strings
* xtask            Developer tools: file-guard, layers, design-guard, parity, test-corpus
```

---

Getting Started
---------------

### Prerequisites

* [Rust toolchain](https://rustup.rs/) (version 1.80 or newer recommended).

### Building and Running

Clone the repository and launch the desktop application:

```
git clone https://github.com/kobaltgit/StatCraft.git
cd StatCraft

# Run StatCraft in release mode (strictly single-threaded compiler guard)
cargo run --package statcraft_app --release -j 1
```

### Running Tests and Quality Guards

StatCraft enforces a strict **Definition of Done (DoD)**. All tests and architectural linters must pass with zero warnings:

```
# Run all workspace unit, integration, and golden oracle tests
cargo test --workspace -j 1

# Check file size limits across all crates (anti-monolith guard)
cargo run -p xtask -j 1 -- file-guard

# Check architectural layering rules (L0 - L6 strict downwards dependencies)
cargo run -p xtask -j 1 -- layers

# Check dialog UI design system compliance (DialogKit guard)
cargo run -p xtask -j 1 -- design-guard

# Verify SPSS feature parity status
cargo run -p xtask -j 1 -- parity
```

---

Project Structure
-----------------

| Crate / Path | Responsibility |
| --- | --- |
| [`crates/statcraft_app`](/kobaltgit/StatCraft/blob/main/crates/statcraft_app) | Desktop user interface, docking windows, DialogKit, data grid, output viewer |
| [`crates/statcraft_syntax`](/kobaltgit/StatCraft/blob/main/crates/statcraft_syntax) | Engine command bus, transactions, undo/redo, SPSS syntax serializer |
| [`crates/statcraft_algo`](/kobaltgit/StatCraft/blob/main/crates/statcraft_algo) | Pure mathematical algorithms (t-tests, ANOVA, regression, correlations, factor PCA, nonparametrics, frequencies) |
| [`crates/statcraft_core`](/kobaltgit/StatCraft/blob/main/crates/statcraft_core) | In-memory `DataSet`, `RawTable`, `VariableDictionary`, measurement scales, metadata |
| [`crates/statcraft_io`](/kobaltgit/StatCraft/blob/main/crates/statcraft_io) | Data codecs: streaming CSV/TSV, Excel workbooks (.xlsx/.xls/.ods), and SPSS files (.sav/.zsav) |
| [`crates/statcraft_i18n`](/kobaltgit/StatCraft/blob/main/crates/statcraft_i18n) | Localization engine powered by Project Fluent (`locales/*.ftl`) |
| [`xtask`](/kobaltgit/StatCraft/blob/main/xtask) | CI/CD automation: `file-guard`, `layers`, `design-guard`, `parity` |
| [`docs/`](/kobaltgit/StatCraft/blob/main/docs) | Architecture guides, design specs, roadmaps, and development chronicle |



---

Documentation
-------------

* **[Comprehensive Feature Guide (FEATURES.md)](/kobaltgit/StatCraft/blob/main/docs/FEATURES.md)** / **[Справочник возможностей (RU)](/kobaltgit/StatCraft/blob/main/docs/FEATURES_RU.md)** — Exhaustive catalog of all implemented statistical procedures, data transformations, formulas, and UI tools.
* [Contributor Guide (CONTRIBUTING.md)](/kobaltgit/StatCraft/blob/main/CONTRIBUTING.md) — Comprehensive development regulations, Resource Guard (-j 1), architecture rules, and Definition of Done.
* [SPSS Feature Parity Checklist](/kobaltgit/StatCraft/blob/main/docs/parity-checklist.md) — Comprehensive tracking of implemented SPSS commands and menus.
* [SPSS Algorithms Mathematical Audit](/kobaltgit/StatCraft/blob/main/docs/SPSS_ALGORITHMS_AUDIT.md) — Rigorous Clean-Room verification against IBM SPSS 24 Algorithms guide via [Craft Anything](https://github.com/storytold/craft-anything).
* [Strategic Roadmap](/kobaltgit/StatCraft/blob/main/docs/ROADMAP.md) — Long-term technical phases and module milestones.
* [Canonical Design Guide](/kobaltgit/StatCraft/blob/main/docs/DESIGN_GUIDE.md) — Standard layout specifications for all modal dialogs (`DialogKit`).
* [Development Chronicle (EN)](/kobaltgit/StatCraft/blob/main/docs/CHRONICLE.en.md) / [Хроника разработки (RU)](/kobaltgit/StatCraft/blob/main/docs/CHRONICLE.md) — Detailed historical devlog of every architectural milestone.

---

💖 Support & Sponsorship
-----------------------

**StatCraft** is an ambitious, mathematically rigorous, clean-room statistical suite built in **100% pure Safe Rust** with zero legacy C/Fortran code. Developing clean-room analytical algorithms (parametric & non-parametric tests, ANOVA, Levene, regression, syntax pipelines, and canonical pivot tables) requires immense research and mathematical verification.

If **StatCraft** helps your academic research, university coursework, or statistical workflows, and you would like to support its ongoing development:

[![Support on Lava.top](https://camo.githubusercontent.com/4e3d35036726000fb5ac038994a5efc12a90787b26f8b075f959b54adf28c6f1/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f537570706f72745f50726f6a6563742d4c6176612e746f702d4646354333353f7374796c653d666f722d7468652d6261646765266c6f676f3d6865617274266c6f676f436f6c6f723d7768697465)](https://app.lava.top/kobaltgit)

**👉 <https://app.lava.top/kobaltgit>**

*(Accepts Russian cards, CIS, and international payment options)*

---

License
-------

This project is dual-licensed under:

* **MIT License** ([LICENSE-MIT](/kobaltgit/StatCraft/blob/main/LICENSE-MIT))
* **Apache License, Version 2.0** ([LICENSE-APACHE](/kobaltgit/StatCraft/blob/main/LICENSE-APACHE))

You may choose either license at your option.

All brand assets and logos in `assets/` are property of the **StatCraft** project (kobaltGIT).
