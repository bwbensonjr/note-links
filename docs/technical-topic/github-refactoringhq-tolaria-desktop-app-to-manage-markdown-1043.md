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

💧 Tolaria Tolaria is a desktop app for Mac and Linux for managing markdown knowledge bases . People use it for a variety of use cases: Operate second brains and personal knowledge Organize company docs as context for AI Store OpenClaw/assistants memory and procedures Personally, I use it to run my life (hey 👋 Luca here ). I have a massive workspace of 10,000+ notes, which are the result of my Refactoring work + a ton of personal journaling and second braining . Walkthroughs You can find some Loom walkthroughs below — they are short and to the point: How I Organize My Own Tolaria Workspace My Inbox Workflow How I Save Web Resources to Tolaria Principles 📑 Files-first — Your notes are plain markdown files. They're portable, work with any editor, and require no export step. Your data belongs to you, not to any app. 🔌 Git-first — Every vault is a git repository. You get full version history, the ability to use any git remote, and zero dependency on Tolaria servers. 🛜 Offline-first, zero lock-in — No accounts, no subscriptions, no cloud dependencies. Your vault works completely offline and always will. If you stop using Tolaria, you lose nothing. 🔬 Open source — Tolaria is free and open source. I built this for myself and for sharing it with others. 📋 Standards-based — Notes are markdown files with YAML frontmatter. No proprietary formats, no locked-in data. Everything works with standard tools if you decide to move away from Tolaria. 🔍 Types as lenses, not schemas — Types in Tolaria are navigation aids, not enforcement mechanisms. There's no required fields, no validation, just helpful categories for finding notes. 🪄 AI-first but not AI-only — A vault of files works very well with AI agents, but you are free to use whatever you want. We support Claude Code and Codex CLI (for now), but you can edit the vault with any AI you want. We provide an AGENTS file for your agents to figure out. ⌨️ Keyboard-first — Tolaria is designed for power-users who want to use keyboard as much as possible. A lot of how we designed the Editor and the Command Palette is based on this. 💪 Built from real use — Tolaria was created for manage my personal vault of 10,000+ notes, and I use it every day. Every feature exists because it solved a real problem. Getting started Download the latest release here . When you open Tolaria for the first time you get the chance of cloning the getting started vault — which gives you a walkthrough of the whole app. Open source and local setup Tolaria is open source and built with Tauri, React, and TypeScript. If you want to run or contribute to the app locally, here is how to get started . You can also find the gist below 👇 Prerequisites Node.js 20+ pnpm 8+ Rust stable macOS or Linux for development Linux system dependencies Tauri 2 on Linux requires WebKit2GTK 4.1 and GTK 3: Arch / Manjaro: sudo pacman -S --needed webkit2gtk-4.1 base-devel curl wget file openssl \ appmenu-gtk-module libappindicator-gtk3 librsvg Debian / Ubuntu (22.04+): sudo apt install libwebkit2gtk-4.1-dev build-essential curl wget file \ libxdo-dev libssl-dev libayatana-appindicator3-dev librsvg2-dev \ libsoup-3.0-dev patchelf Fedora 38+: sudo dnf install webkit2gtk4.1-devel openssl-devel curl wget file \ libappindicator-gtk3-devel librsvg2-devel The bundled MCP server still spawns the system node binary at runtime on Linux, so install Node from your distro package manager if you want the external AI tooling flow. Quick start pnpm install pnpm dev Open http://localhost:5173 for the browser-based mock mode, or run the native desktop app with: pnpm tauri dev Tech Docs 📐 ARCHITECTURE.md — System design, tech stack, data flow 🧩 ABSTRACTIONS.md — Core abstractions and models 🚀 GETTING-STARTED.md — How to navigate the codebase 📚 ADRs — Architecture Decision Records Security If you believe you have found a security issue, please report it privately as described in SECURITY.md . License Tolaria is licensed under AGPL-3.0-or-later. The Tolaria name and logo remain covered by the project’s trademark policy.
