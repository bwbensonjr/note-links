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

> OpenWork is the open source alternative to Claude Cowork/Codex (desktop app).

Core Philosophy
---------------

* Local-first, cloud-ready: OpenWork runs on your machine in one click. Send a message instantly.
* Composable: desktop app, Slack/Telegram connector, or server. Use what fits, no lock-in.
* Ejectable: OpenWork is powered by OpenCode, so everything OpenCode can do works in OpenWork, even without a UI yet.
* Sharing is caring: start solo on localhost, then explicitly opt into remote sharing when you need it.

[![OpenWork demo](/different-ai/openwork/raw/dev/app-demo.gif)](/different-ai/openwork/blob/dev/app-demo.gif)

OpenWork is designed around the idea that you can easily ship your agentic workflows for your team as a repeatable, productized process.

Tip

**Looking for an [Enterprise Plan](https://openworklabs.com/enterprise)?** [Speak with our Sales Team today](https://calendar.app.google/86QpCENvhfEzDFLu5)

Get enhanced capabilities including feature prioritization, SSO, SLA support, LTS versions, and more.

Alternate UIs
-------------

* **OpenWork Orchestrator (CLI host)**: run OpenCode + OpenWork server without the desktop UI.
  + install: `npm install -g openwork-orchestrator`
  + run: `openwork start --workspace /path/to/workspace --approval auto`
  + docs: [apps/orchestrator/README.md](/different-ai/openwork/blob/dev/apps/orchestrator/README.md)

Quick start
-----------

Download the desktop app from [openworklabs.com/download](https://openworklabs.com/download), grab the latest [GitHub release](https://github.com/different-ai/openwork/releases), or install from source below.

* macOS and Linux downloads are available directly.
* Windows access is currently handled through the paid support plan on [openworklabs.com/pricing#windows-support](https://openworklabs.com/pricing#windows-support).
* Hosted OpenWork Cloud workers are launched from the web app after checkout, then connected from the desktop app via `Add a worker` -> `Connect remote`.

Why
---

Current CLI and GUIs for opencode are anchored around developers. That means a focus on file diffs, tool names, and hard to extend capabilities without relying on exposing some form of cli.

OpenWork is designed to be:

* **Extensible**: skill and opencode plugins are installable modules.
* **Auditable**: show what happened, when, and why.
* **Permissioned**: access to privileged flows.
* **Local/Remote**: OpenWork works locally as well as can connect to remote servers.

What’s Included
---------------

* **Host mode**: runs opencode locally on your computer
* **Client mode**: connect to an existing OpenCode server by URL.
* **Sessions**: create/select sessions and send prompts.
* **Live streaming**: SSE `/event` subscription for realtime updates.
* **Execution plan**: render OpenCode todos as a timeline.
* **Permissions**: surface permission requests and reply (allow once / always / deny).
* **Templates**: save and re-run common workflows (stored locally).
* **Debug exports**: copy or export the runtime debug report and developer log stream from Settings -> Debug when you need to file a bug.
* **Skills manager**:
  + list installed `.opencode/skills` folders
  + import a local skill folder into `.opencode/skills/<skill-name>`

Skill Manager
-------------

[![image](https://private-user-images.githubusercontent.com/11430621/535399257-b500c1c6-a218-42ce-8a11-52787f5642b6.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3ODAyNDc0OTAsIm5iZiI6MTc4MDI0NzE5MCwicGF0aCI6Ii8xMTQzMDYyMS81MzUzOTkyNTctYjUwMGMxYzYtYTIxOC00MmNlLThhMTEtNTI3ODdmNTY0MmI2LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNjA1MzElMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjYwNTMxVDE3MDYzMFomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTBhMTUzMzg4YjNmNGI5MWNkZTRlN2I5ZmQ2NzE0NTRkZGI0YWVmMWMwOTBjNzM0MzFiMGRjMzc4NThjOWE1YjMmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JnJlc3BvbnNlLWNvbnRlbnQtdHlwZT1pbWFnZSUyRnBuZyJ9.MJrilxB4RtfzXsUBv0q2532leodtLErM0knu5mR4hmw)](https://private-user-images.githubusercontent.com/11430621/535399257-b500c1c6-a218-42ce-8a11-52787f5642b6.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3ODAyNDc0OTAsIm5iZiI6MTc4MDI0NzE5MCwicGF0aCI6Ii8xMTQzMDYyMS81MzUzOTkyNTctYjUwMGMxYzYtYTIxOC00MmNlLThhMTEtNTI3ODdmNTY0MmI2LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNjA1MzElMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjYwNTMxVDE3MDYzMFomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTBhMTUzMzg4YjNmNGI5MWNkZTRlN2I5ZmQ2NzE0NTRkZGI0YWVmMWMwOTBjNzM0MzFiMGRjMzc4NThjOWE1YjMmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JnJlc3BvbnNlLWNvbnRlbnQtdHlwZT1pbWFnZSUyRnBuZyJ9.MJrilxB4RtfzXsUBv0q2532leodtLErM0knu5mR4hmw)

Works on local computer or servers
----------------------------------

[![Screenshot 2026-01-13 at 7 05 16 PM](https://private-user-images.githubusercontent.com/11430621/535399085-9c864390-de69-48f2-82c1-93b328dd60c3.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3ODAyNDc0OTAsIm5iZiI6MTc4MDI0NzE5MCwicGF0aCI6Ii8xMTQzMDYyMS81MzUzOTkwODUtOWM4NjQzOTAtZGU2OS00OGYyLTgyYzEtOTNiMzI4ZGQ2MGMzLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNjA1MzElMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjYwNTMxVDE3MDYzMFomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTU3NmExMTIwMGQ4YWQ1YzhlNDRlMjc4ZjIxOGY1YTk0MzIyZDMwMWVmZTVjNDBhOTk1MmVmMmE4ZjBkNTIzM2UmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JnJlc3BvbnNlLWNvbnRlbnQtdHlwZT1pbWFnZSUyRnBuZyJ9.BukHD3ikWDbIQo_RP_cMAO36mNoVFgxoc426JovS72Y)](https://private-user-images.githubusercontent.com/11430621/535399085-9c864390-de69-48f2-82c1-93b328dd60c3.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3ODAyNDc0OTAsIm5iZiI6MTc4MDI0NzE5MCwicGF0aCI6Ii8xMTQzMDYyMS81MzUzOTkwODUtOWM4NjQzOTAtZGU2OS00OGYyLTgyYzEtOTNiMzI4ZGQ2MGMzLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNjA1MzElMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjYwNTMxVDE3MDYzMFomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTU3NmExMTIwMGQ4YWQ1YzhlNDRlMjc4ZjIxOGY1YTk0MzIyZDMwMWVmZTVjNDBhOTk1MmVmMmE4ZjBkNTIzM2UmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JnJlc3BvbnNlLWNvbnRlbnQtdHlwZT1pbWFnZSUyRnBuZyJ9.BukHD3ikWDbIQo_RP_cMAO36mNoVFgxoc426JovS72Y)

Quick Start
-----------

### Requirements

* Node.js + `pnpm`
* Rust toolchain (for Tauri): install via `curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh`
* Tauri CLI: `cargo install tauri-cli`
* OpenCode CLI installed and available on PATH: `opencode`

### Local Dev Prerequisites (Desktop)

Before running `pnpm dev`, ensure these are installed and active in your shell:

* Node + pnpm (repo uses `pnpm@10.27.0`)
* **Bun 1.3.9+** (`bun --version`)
* Rust toolchain (for Tauri), with Cargo from current `rustup` stable (supports `Cargo.lock` v4)
* Xcode Command Line Tools (macOS)
* On Linux, WebKitGTK 4.1 development packages so `pkg-config` can resolve `webkit2gtk-4.1` and `javascriptcoregtk-4.1`

### One-minute sanity check

Run from repo root:

```
git checkout dev
git pull --ff-only origin dev
pnpm install --frozen-lockfile

which bun
bun --version
pnpm --filter @openwork/desktop exec tauri --version
```

### Install

```
pnpm install
```

OpenWork now lives in `apps/app` (UI) and `apps/desktop` (desktop shell).

### Run (Desktop)

```
pnpm dev
```

`pnpm dev` now enables `OPENWORK_DEV_MODE=1` automatically, so desktop dev uses an isolated OpenCode state instead of your personal global config/auth/data.

### Run (Web UI only)

```
pnpm dev:ui
```

All repo `dev` entrypoints now opt into the same dev-mode isolation so local testing uses the OpenWork-managed OpenCode state consistently.

### Arch Users:

```
sudo pacman -S --needed webkit2gtk-4.1
curl -fsSL https://opencode.ai/install | bash -s -- --version "$(node -e "const fs=require('fs'); const parsed=JSON.parse(fs.readFileSync('constants.json','utf8')); process.stdout.write(String(parsed.opencodeVersion||'').trim().replace(/^v/,''));")" --no-modify-path
```

Architecture (high-level)
-------------------------

* In **Host mode**, OpenWork runs a local host stack and connects the UI to it.
  + Default runtime: `openwork` (installed from `openwork-orchestrator`), which orchestrates `opencode`, `openwork-server`, and optionally `opencode-router`.
  + Fallback runtime: `direct`, where the desktop app spawns `opencode serve --hostname 127.0.0.1 --port <free-port>` directly.

When you select a project folder, OpenWork runs the host stack locally using that folder and connects the desktop UI.
This lets you run agentic workflows, send prompts, and see progress entirely on your machine without a remote server.

* The UI uses `@opencode-ai/sdk/v2/client` to:
  + connect to the server
  + list/create sessions
  + send prompts
  + subscribe to SSE events(Server-Sent Events are used to stream real-time updates from the server to the UI.)
  + read todos and permission requests

Folder Picker
-------------

The folder picker uses the Tauri dialog plugin.
Capability permissions are defined in:

* `apps/desktop/src-tauri/capabilities/default.json`

OpenCode Plugins
----------------

Plugins are the **native** way to extend OpenCode. OpenWork now manages them from the Skills tab by
reading and writing `opencode.json`.

* **Project scope**: `<workspace>/opencode.json`
* **Global scope**: `~/.config/opencode/opencode.json` (or `$XDG_CONFIG_HOME/opencode/opencode.json`)

You can still edit `opencode.json` manually; OpenWork uses the same format as the OpenCode CLI:

```
{
  "$schema": "https://opencode.ai/config.json",
  "plugin": ["opencode-wakatime"]
}
```

Useful Commands
---------------

```
pnpm dev
pnpm dev:ui
pnpm typecheck
pnpm build
pnpm build:ui
pnpm test:e2e
```

Troubleshooting
---------------

If you need to report a desktop or session bug, open Settings -> Debug and export both the runtime debug report and developer logs before filing an issue.

### Linux / Wayland (Hyprland)

If OpenWork crashes on launch with WebKitGTK errors like `Failed to create GBM buffer`, disable dmabuf or compositing before launch. Try one of the following environment flags.

```
WEBKIT_DISABLE_DMABUF_RENDERER=1 openwork
```

```
WEBKIT_DISABLE_COMPOSITING_MODE=1 openwork
```

Security Notes
--------------

* OpenWork hides model reasoning and sensitive tool metadata by default.
* Host mode binds to `127.0.0.1` by default.

Contributing
------------

* Review `AGENTS.md` plus `VISION.md`, `PRINCIPLES.md`, `PRODUCT.md`, and `ARCHITECTURE.md` to understand the product goals before making changes.
* Ensure Node.js, `pnpm`, the Rust toolchain, and `opencode` are installed before working inside the repo.
* Run `pnpm install` once per checkout, then verify your change with `pnpm typecheck` plus `pnpm test:e2e` (or the targeted subset of scripts) before opening a PR.
* Use `.github/pull_request_template.md` when opening PRs and include exact commands, outcomes, manual verification steps, and evidence.
* If CI fails, classify failures in the PR body as either code-related regressions or external/environment/auth blockers.
* Add new PRDs to `apps/app/pr/<name>.md` following the `.opencode/skills/prd-conventions/SKILL.md` conventions described in `AGENTS.md`.

Community docs:

* `CODE_OF_CONDUCT.md`
* `SECURITY.md`
* `SUPPORT.md`
* `TRIAGE.md`

First contribution checklist:

* Run `pnpm install` and baseline verification commands.
* Confirm your change has a clear issue link and scope.
* Add/update tests for behavioral changes.
* Include commands run and outcomes in your PR.
* Add screenshots/video for user-facing flow changes.

Supported Languages
-------------------

Translated READMEs: [`translated_readmes/`](/different-ai/openwork/blob/dev/translated_readmes/README.md), available in English, 简体中文, 繁體中文, 日本語.

The App is available in the following languages:

* English (`en`)
* French (`fr`)
* Spanish (`es`)
* Catalan (`ca`)
* Brazilian Portuguese (`pt-BR`)
* Japanese (`ja`)
* Simplified Chinese (`zh`)
* Thai (`th`)
* Vietnamese (`vi`)
* Russian (`ru`)

For Teams & Businesses
----------------------

Interested in using OpenWork in your organization? We'd love to hear from you — reach out at [ben@openworklabs.com](mailto:ben@openworklabs.com) to chat about your use case.

License
-------

MIT — see `LICENSE`.
