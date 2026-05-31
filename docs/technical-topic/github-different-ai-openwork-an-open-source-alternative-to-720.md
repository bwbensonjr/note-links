---
id: 720
url: https://github.com/different-ai/openwork
title: 'GitHub - different-ai/openwork: An open-source alternative to Claude Cowork,
  powered by OpenCode'
domain: github.com
source_date: '2026-01-16'
tags:
- github-repo
- ai
- llm
- web-dev
summary: OpenWork is an open-source desktop application that provides a user-friendly
  alternative to Claude Cowork, designed for knowledge workers to perform complex
  tasks without needing command-line expertise. It runs OpenCode under the hood while
  presenting a guided workflow interface with features like session management, real-time
  progress tracking, permission controls, and reusable templates. The tool is extensible
  through plugins and skills, works both locally and remotely, and is available as
  a native desktop app or web UI.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# GitHub - different-ai/openwork: An open-source alternative to Claude Cowork, powered by OpenCode

OpenWork OpenWork is an extensible, open-source “Claude Work” style system for knowledge workers . It’s a native desktop app that runs OpenCode under the hood, but presents it as a clean, guided workflow: pick a workspace start a run watch progress + plan updates approve permissions when needed reuse what works (templates + skills) The goal: make “agentic work” feel like a product, not a terminal. Quick start Download the dmg here https://github.com/different-ai/openwork/releases (or install from source below) Why Knowledge workers don’t want to learn a CLI, fight config sprawl, or rebuild the same workflows in every repo. OpenWork is designed to be: Extensible : skill and opencode plugins are installable modules. Auditable : show what happened, when, and why. Permissioned : access to privileged flows. Local/Remote : OpenWork works locally as well as can connect to remote servers. What’s Included (v0.1) Host mode : start opencode serve locally in a chosen folder. Client mode : connect to an existing OpenCode server by URL. Sessions : create/select sessions and send prompts. Live streaming : SSE /event subscription for realtime updates. Execution plan : render OpenCode todos as a timeline. Permissions : surface permission requests and reply (allow once / always / deny). Templates : save and re-run common workflows (stored locally). Skills manager : list installed .opencode/skill folders install from OpenPackage ( opkg install ... ) import a local skill folder into .opencode/skill/<skill-name> Skill Manager Works on local computer or servers Quick Start Requirements Node.js + pnpm Rust toolchain (for Tauri): cargo , rustc OpenCode CLI installed and available on PATH: opencode Install pnpm install Run (Desktop) pnpm dev Run (Web UI only) pnpm dev:web Architecture (high-level) In Host mode , OpenWork spawns: opencode serve --hostname 127.0.0.1 --port <free-port> with your selected project folder as the process working directory. The UI uses @opencode-ai/sdk/v2/client to: connect to the server list/create sessions send prompts subscribe to SSE events read todos and permission requests Folder Picker The folder picker uses the Tauri dialog plugin. Capability permissions are defined in: src-tauri/capabilities/default.json OpenPackage Notes If opkg is not installed globally, OpenWork falls back to: pnpm dlx opkg install < package > OpenCode Plugins Plugins are the native way to extend OpenCode. OpenWork now manages them from the Skills tab by reading and writing opencode.json . Project scope : <workspace>/opencode.json Global scope : ~/.config/opencode/opencode.json (or $XDG_CONFIG_HOME/opencode/opencode.json ) You can still edit opencode.json manually; OpenWork uses the same format as the OpenCode CLI: { "$schema" : " https://opencode.ai/config.json " , "plugin" : [ " opencode-wakatime " ] } Useful Commands pnpm typecheck pnpm build:web pnpm test:e2e Security Notes OpenWork hides model reasoning and sensitive tool metadata by default. Host mode binds to 127.0.0.1 by default. License MIT — see LICENSE .
