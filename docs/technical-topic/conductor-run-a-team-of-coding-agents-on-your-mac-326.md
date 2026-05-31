---
id: 326
url: https://conductor.build/
title: Conductor - Run a team of coding agents on your Mac
domain: conductor.build
source_date: '2025-07-21'
tags:
- ai
- llm
- devops
- web-dev
summary: Conductor is a Mac application that enables users to run multiple AI coding
  agents simultaneously in isolated workspaces, allowing them to work on different
  tasks in parallel. Users can monitor the agents' progress in real-time and easily
  review and merge their code changes. The latest version (0.29.5) leverages Claude
  Code agents to streamline collaborative coding workflows.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# Conductor - Run a team of coding agents on your Mac

[Introducing Conductor Cloud →](/cloud)

[See what's new in 0.61.0](/changelog) 

Run a team of coding agents on your Mac.
========================================

Create parallel Codex + Claude Code agents in isolated workspaces. See at a glance what they're working on, then review and merge their changes.

Download Conductor[Learn how it works](/docs)

🚂

Quickstart1. Start here

Start hereApp.tsxTerminal

Show me how Conductor handles this project.

Conductor is a Mac app for running coding agents in parallel. I’ll use one isolated workspace for this task: its own branch, files, chat, terminal, preview, and reviewable diff.
1. Send the drafted task.
2. Run the app with ⌘R.
3. Review the diff before you keep it.

Read

README.md

Read

conductor.json

Read

src/App.tsx

Add a 10-train milestone animation.

Done. I changed the train app in this workspace, kept the preview running, and ran lint. The code is isolated from main until you review it in the [diff viewer](/docs/reference/diff-viewer).

Update

src/App.tsx

Update

src/App.css

Run

npm run lint

12.4s

GPT-5.5FastHighPlan

Switch demo to light modeReset demo

How it works

1. 1.Add your repo.Conductor clones it and works entirely on your Mac.
2. 2.Deploy agents.Each Claude Code you spin up gets an isolated workspace.
3. 3.Conduct.See who's working, what needs attention, and review code.

Frequently asked questions

Does Conductor use worktrees?
:   └Yes, each Conductor workspace is a new git worktree.

Which coding agents does Conductor support?
:   └Claude Code and Codex. Want to see something else? Email us.

How does Conductor pay for Claude Code?
:   └Conductor uses Claude Code however you're already logged in. If you're logged into Claude Code with an API key, Conductor will use that too. If you're logged in with the Claude Pro or Max plan, Conductor will use that.

We built Conductor using Conductor.
-----------------------------------

We think you'll like it as much as we do.

Download Conductor
