---
id: 1043
url: https://github.com/refactoringhq/tolaria
title: 'GitHub - refactoringhq/tolaria: Desktop app to manage markdown knowledge bases
  · GitHub'
domain: github.com
source_date: '2026-04-24'
tags:
- github-repo
- web-dev
- ai
- devops
summary: Tolaria is a free, open-source desktop application for Mac and Linux that
  enables users to manage markdown-based knowledge bases with a focus on portability,
  offline functionality, and integration with AI tools. Built on principles like files-first
  storage, git-based version control, and keyboard-first design, it allows users to
  organize personal notes, company documentation, and AI assistant memory without
  relying on cloud services or proprietary formats. The app is designed for power
  users managing large note collections and includes features like type-based organization,
  AI agent support, and full version history through git integration.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# GitHub - refactoringhq/tolaria: Desktop app to manage markdown knowledge bases · GitHub

[![Latest stable](https://camo.githubusercontent.com/63b9d2627c5149087f485729c7e8dc6f5d1887f64ebcfd3fdf0bb3533db1a191/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f762f72656c656173652f7265666163746f72696e6768712f746f6c617269613f646973706c61795f6e616d653d746167)](https://camo.githubusercontent.com/63b9d2627c5149087f485729c7e8dc6f5d1887f64ebcfd3fdf0bb3533db1a191/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f762f72656c656173652f7265666163746f72696e6768712f746f6c617269613f646973706c61795f6e616d653d746167) [![CI](https://github.com/refactoringhq/tolaria/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/refactoringhq/tolaria/actions/workflows/ci.yml) [![Codecov](https://camo.githubusercontent.com/8fd51d3ec4e16efc165908f94283072efa08033f89b241ca93bfe9b7f01831fa/68747470733a2f2f636f6465636f762e696f2f67682f7265666163746f72696e6768712f746f6c617269612f67726170682f62616467652e7376673f6272616e63683d6d61696e)](https://codecov.io/gh/refactoringhq/tolaria) [![CodeScene Hotspot Code Health](https://camo.githubusercontent.com/ab81929ff57bce9e380153db1f1020f0c2549ba6bdfbc41649b753990718a6b5/68747470733a2f2f636f64657363656e652e696f2f70726f6a656374732f37363836352f7374617475732d6261646765732f686f7473706f742d636f64652d6865616c7468)](https://codescene.io/projects/76865)

💧 Tolaria
=========

Tolaria is a desktop app for macOS, Windows, and Linux for managing **markdown knowledge bases**. People use it for a variety of use cases:

* Operate second brains and personal knowledge
* Organize company docs as context for AI
* Store OpenClaw/assistants memory and procedures

Personally, I use it to **run my life** (hey 👋 [Luca here](http://x.com/lucaronin)). I have a massive workspace of 10,000+ notes, which are the result of my [Refactoring](https://refactoring.fm/) work + a ton of personal journaling and *second braining*.

[![1776506856823-CleanShot_2026-04-18_at_12 06 57_2x](https://private-user-images.githubusercontent.com/695274/580447132-8aeafb0a-b236-43c2-a083-ec111f903c38.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3ODAyNDcxMTIsIm5iZiI6MTc4MDI0NjgxMiwicGF0aCI6Ii82OTUyNzQvNTgwNDQ3MTMyLThhZWFmYjBhLWIyMzYtNDNjMi1hMDgzLWVjMTExZjkwM2MzOC5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjYwNTMxJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI2MDUzMVQxNzAwMTJaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT01ZGM3NjUyNTY3ZDM1MjRiMjFjZjcwNzA2ZDBlMzRjNWJhOWFhODlkNTlmNjFiN2U5MWUyMmE5MjhlNDYwMTNjJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZyZXNwb25zZS1jb250ZW50LXR5cGU9aW1hZ2UlMkZwbmcifQ.ostmMMtVjDVoUBS5Af9J573D3tedFTZ0bNg33lJ6H6I)](https://private-user-images.githubusercontent.com/695274/580447132-8aeafb0a-b236-43c2-a083-ec111f903c38.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3ODAyNDcxMTIsIm5iZiI6MTc4MDI0NjgxMiwicGF0aCI6Ii82OTUyNzQvNTgwNDQ3MTMyLThhZWFmYjBhLWIyMzYtNDNjMi1hMDgzLWVjMTExZjkwM2MzOC5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjYwNTMxJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI2MDUzMVQxNzAwMTJaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT01ZGM3NjUyNTY3ZDM1MjRiMjFjZjcwNzA2ZDBlMzRjNWJhOWFhODlkNTlmNjFiN2U5MWUyMmE5MjhlNDYwMTNjJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZyZXNwb25zZS1jb250ZW50LXR5cGU9aW1hZ2UlMkZwbmcifQ.ostmMMtVjDVoUBS5Af9J573D3tedFTZ0bNg33lJ6H6I)

Walkthroughs
------------

You can find some Loom walkthroughs below — they are short and to the point:

* [How I Organize My Own Tolaria Workspace](https://www.loom.com/share/bb3aaffa238b4be0bd62e4464bca2528)
* [My Inbox Workflow](https://www.loom.com/share/dffda263317b4fa8b47b59cdf9330571)
* [How I Save Web Resources to Tolaria](https://www.loom.com/share/8a3c1776f801402ebbf4d7b0f31e9882)

Principles
----------

* 📑 **Files-first** — Your notes are plain markdown files. They're portable, work with any editor, and require no export step. Your data belongs to you, not to any app.
* 🔌 **Git-first** — Every vault is a git repository. You get full version history, the ability to use any git remote, and zero dependency on Tolaria servers.
* 🛜 **Offline-first, zero lock-in** — No accounts, no subscriptions, no cloud dependencies. Your vault works completely offline and always will. If you stop using Tolaria, you lose nothing.
* 🔬 **Open source** — Tolaria is free and open source. I built this for [myself](https://x.com/lucaronin) and for sharing it with others.
* 📋 **Standards-based** — Notes are markdown files with YAML frontmatter. No proprietary formats, no locked-in data. Everything works with standard tools if you decide to move away from Tolaria.
* 🔍 **Types as lenses, not schemas** — Types in Tolaria are navigation aids, not enforcement mechanisms. There's no required fields, no validation, just helpful categories for finding notes.
* 🪄**AI-first but not AI-only** — A vault of files works very well with AI agents, but you are free to use whatever you want. We support Claude Code, Codex CLI, and Gemini CLI setup paths, but you can edit the vault with any AI you want. We provide an AGENTS file for your agents to figure out.
* ⌨️ **Keyboard-first** — Tolaria is designed for power-users who want to use keyboard as much as possible. A lot of how we designed the Editor and the Command Palette is based on this.
* 💪 **Built from real use** — Tolaria was created for manage my personal vault of 10,000+ notes, and I use it every day. Every feature exists because it solved a real problem.

Installation
------------

### Homebrew

Install via Homebrew on macOS:

```
brew install --cask tolaria
```

### Download from releases

Download the [latest release here](https://refactoringhq.github.io/tolaria/download/) for macOS, Windows, or Linux. Windows installers are Authenticode-signed; company-managed devices may still require IT approval of the Tolaria publisher before first install.

Getting started
---------------

When you open Tolaria for the first time you get the chance of cloning the [getting started vault](https://github.com/refactoringhq/tolaria-getting-started) — which gives you a walkthrough of the whole app.

The public user docs live in [`site/`](/refactoringhq/tolaria/blob/main/site) and are published to GitHub Pages. Start with [Install Tolaria](/refactoringhq/tolaria/blob/main/site/start/install.md), then [First Launch](/refactoringhq/tolaria/blob/main/site/start/first-launch.md).

Open source and local setup
---------------------------

Tolaria is open source and built with Tauri, React, and TypeScript. If you want to run or contribute to the app locally, here is [how to get started](https://github.com/refactoringhq/tolaria/blob/main/docs/GETTING-STARTED.md). You can also find the gist below 👇

### Prerequisites

* Node.js 20+
* pnpm 8+
* Rust stable
* macOS or Linux for development

#### Linux system dependencies

Tauri 2 on Linux requires WebKit2GTK 4.1 and GTK 3:

* Arch / Manjaro:

  ```
  sudo pacman -S --needed webkit2gtk-4.1 base-devel curl wget file openssl \
    appmenu-gtk-module libappindicator-gtk3 librsvg
  ```
* Debian / Ubuntu (22.04+):

  ```
  sudo apt install libwebkit2gtk-4.1-dev build-essential curl wget file \
    libxdo-dev libssl-dev libayatana-appindicator3-dev librsvg2-dev \
    libsoup-3.0-dev patchelf
  ```
* Fedora 38+:

  ```
  sudo dnf install webkit2gtk4.1-devel openssl-devel curl wget file \
    libappindicator-gtk3-devel librsvg2-devel
  ```

The bundled MCP server still spawns the system `node` binary at runtime on Linux, so install Node from your distro package manager if you want the external AI tooling flow.

### Quick start

```
pnpm install
pnpm dev
```

Open `http://localhost:5173` for the browser-based mock mode, or run the native desktop app with:

```
pnpm tauri dev
```

Tech Docs
---------

* 📐 [ARCHITECTURE.md](/refactoringhq/tolaria/blob/main/docs/ARCHITECTURE.md) — System design, tech stack, data flow
* 🧩 [ABSTRACTIONS.md](/refactoringhq/tolaria/blob/main/docs/ABSTRACTIONS.md) — Core abstractions and models
* 🚀 [GETTING-STARTED.md](/refactoringhq/tolaria/blob/main/docs/GETTING-STARTED.md) — How to navigate the codebase
* 📚 [ADRs](/refactoringhq/tolaria/blob/main/docs/adr) — Architecture Decision Records

Security
--------

If you believe you have found a security issue, please report it privately as described in [SECURITY.md](/refactoringhq/tolaria/blob/main/SECURITY.md).

License
-------

Tolaria is licensed under AGPL-3.0-or-later. The Tolaria name and logo remain covered by the project’s trademark policy.
