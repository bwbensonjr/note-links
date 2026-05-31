---
id: 807
url: https://github.com/stablyai/agent-slack
title: 'GitHub - stablyai/agent-slack: Slack automation CLI for AI agents'
domain: github.com
source_date: '2026-02-09'
tags:
- github-repo
- cli-tool
- typescript
- ai
- llm
summary: agent-slack is a TypeScript-based CLI tool that enables AI agents to automate
  Slack interactions with token-efficient JSON output designed for LLM consumption.
  It provides commands for reading messages and threads, searching content, managing
  reactions, listing users, and fetching Slack canvases as Markdown, with zero-config
  authentication that automatically works with Slack Desktop. The tool is available
  as both a standalone CLI and as an agent skill compatible with Claude, Codex, and
  other AI platforms.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# GitHub - stablyai/agent-slack: Slack automation CLI for AI agents

agent-slack
===========

Slack automation CLI for AI agents (TypeScript + Bun).

Guiding principle:

* **Token-efficient** — (compact JSON, minimal duplication, and empty/null fields pruned) so LLMs can consume results cheaply.
* **Zero-config auth** — Auth just works if you have Slack Desktop (with fallbacks available). No Python dependency.
* **Human-in-the-loop** — When appropriate (not in CI environments), loop humans in. Ex: `message draft`
  [![image](https://private-user-images.githubusercontent.com/4138956/553226935-92ecbb71-18ca-4516-a874-c83c154b0709.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3ODAyNDczOTksIm5iZiI6MTc4MDI0NzA5OSwicGF0aCI6Ii80MTM4OTU2LzU1MzIyNjkzNS05MmVjYmI3MS0xOGNhLTQ1MTYtYTg3NC1jODNjMTU0YjA3MDkucG5nP1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQVZDT0RZTFNBNTNQUUs0WkElMkYyMDI2MDUzMSUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyNjA1MzFUMTcwNDU5WiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9ZTJjMjFmMWUwMDhlNTc3NWE1ODQyZDFkM2E2NmIxMzdkYzJmNjAyYTkxNTVlYTE4ZmFiMWY2MWViZTRhYjZiYiZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QmcmVzcG9uc2UtY29udGVudC10eXBlPWltYWdlJTJGcG5nIn0.EhCrKtRFF4JnInAVDwRT9Q2fhoUGv2x1Sf4IPeJAuso)](https://private-user-images.githubusercontent.com/4138956/553226935-92ecbb71-18ca-4516-a874-c83c154b0709.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3ODAyNDczOTksIm5iZiI6MTc4MDI0NzA5OSwicGF0aCI6Ii80MTM4OTU2LzU1MzIyNjkzNS05MmVjYmI3MS0xOGNhLTQ1MTYtYTg3NC1jODNjMTU0YjA3MDkucG5nP1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQVZDT0RZTFNBNTNQUUs0WkElMkYyMDI2MDUzMSUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyNjA1MzFUMTcwNDU5WiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9ZTJjMjFmMWUwMDhlNTc3NWE1ODQyZDFkM2E2NmIxMzdkYzJmNjAyYTkxNTVlYTE4ZmFiMWY2MWViZTRhYjZiYiZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QmcmVzcG9uc2UtY29udGVudC10eXBlPWltYWdlJTJGcG5nIn0.EhCrKtRFF4JnInAVDwRT9Q2fhoUGv2x1Sf4IPeJAuso)

Getting started
---------------

Install via Bun (recommended):

```
curl -fsSL https://raw.githubusercontent.com/stablyai/agent-slack/main/install.sh | sh
```

OR npm global install (requires Node >= 22.5):

```
npm i -g agent-slack
```

OR run via Nix flake:

```
nix run github:stablyai/agent-slack
```

At a glance
-----------

* **Read**: fetch a message, browse channel history, list full threads
* **Search**: messages + files (with filters)
* **Artifacts**: auto-download snippets/images/files to local paths for agents
* **Write**: send now or schedule delivery, edit/delete messages, add reactions (bullet lists auto-render as native Slack rich text)
* **Channels**: list conversations, create channels, and invite users by id/handle/email
* **Canvas**: fetch Slack canvases as Markdown

Agent skill
-----------

This repo ships an agent skill at `skills/agent-slack/` compatible with Claude Code, Codex, Cursor, etc

**Install via [skills.sh](https://skills.sh)** (recommended):

```
npx skills add stablyai/agent-slack
```

Manual installation

```
bash ./scripts/install-skill.sh
```

Command map (high level)
------------------------

```
agent-slack
├── update                         # self-update (detects npm/bun/binary)
├── auth
│   ├── whoami
│   ├── test
│   ├── import-desktop
│   ├── import-brave
│   ├── import-chrome
│   ├── import-firefox
│   └── parse-curl
├── message
│   ├── get   <target>             # fetch 1 message (+ thread meta )
│   ├── list  <target>             # fetch thread or recent channel messages
│   ├── send  <target> [text]      # send / reply / schedule (supports --attach, --blocks)
│   ├── scheduled
│   │   ├── list                   # list pending scheduled messages
│   │   └── cancel <id>            # cancel a pending scheduled message
│   ├── draft <target> [text]      # open Slack-like editor in browser
│   ├── edit  <target> <text>      # edit a message
│   ├── delete <target>            # delete a message
│   └── react
│       ├── add    <target> <emoji>
│       └── remove <target> <emoji>
├── channel
│   ├── list                        # list conversations (user-scoped or all)
│   ├── new                         # create channel
│   └── invite                      # invite users to channel
├── user
│   ├── list
│   └── get <user>
├── search
│   ├── all      <query>           # messages + files
│   ├── messages <query>
│   └── files    <query>
├── workflow
│   ├── list    <channel>          # workflows bookmarked in a channel
│   ├── preview <trigger-id>       # trigger metadata (no side effects)
│   ├── get     <id>               # workflow definition + form fields
│   └── run     <trigger-id>       # trip a workflow trigger
└── canvas
    └── get <canvas-url-or-id>     # canvas → markdown
```

Notes:

* Output is **always JSON** and aggressively pruned (`null`/empty fields removed).
* Attached files are auto-downloaded and returned as absolute local paths.

Authentication (no fancy setup)
-------------------------------

On macOS and Windows, authentication happens automatically:

* Default: reads Slack Desktop local data (no need to quit Slack)
* Fallbacks: if that fails, tries Chrome/Brave/Firefox extraction (macOS)

You can also run manual imports:

```
agent-slack auth whoami
agent-slack auth import-desktop
agent-slack auth import-brave
agent-slack auth import-chrome
agent-slack auth import-firefox
agent-slack auth test
```

Note

`import-brave` / `import-chrome` read tokens from a logged-in Slack tab via AppleScript. Both browsers ship with **Allow JavaScript from Apple Events** disabled by default — enable it in **View → Developer** before running these commands. macOS will prompt for your password the first time.

Alternatively, set env vars:

```
export SLACK_TOKEN="xoxc-..."      # browser token
export SLACK_COOKIE_D="xoxd-..."   # cookie d
agent-slack auth test
```

Or use a standard Slack token (xoxb/xoxp):

```
export SLACK_TOKEN="xoxb-..."
agent-slack auth test
```

Targets: URL or channel
-----------------------

`message get` / `message list` accept either a Slack message URL or a channel reference:

* URL: `https://workspace.slack.com/archives/<channel>/p<digits>[?thread_ts=...]`
* Channel: `#general` (or bare `general`) or a channel ID like `C0123...`

In practice:

```
# Get a single message by channel + ts
agent-slack message get "#general" --ts "1770165109.628379"

# List a full thread by channel + thread root ts
agent-slack message list "#general" --thread-ts "1770165109.000001"
```

If you have multiple workspaces configured and you use a channel **name** (`#channel` / `channel`), you must pass `--workspace` (or set `SLACK_WORKSPACE_URL`).
`--workspace` accepts a full URL or a unique substring selector:

```
agent-slack message get "#general" --workspace "https://stablygroup.slack.com" --ts "1770165109.628379"
agent-slack message get "#general" --workspace "stablygroup" --ts "1770165109.628379"
```

Examples
--------

Tip

You should probably just use the skill for your agent instead of reading below.

### Read messages / threads

```
# Single message (+ thread summary if threaded)
agent-slack message get "https://workspace.slack.com/archives/C123/p1700000000000000"

# Full thread for a message
agent-slack message list "https://workspace.slack.com/archives/C123/p1700000000000000"

# Recent channel messages (browse channel history)
agent-slack message list "#general" --limit 20

# Recent channel messages that are marked with :eyes:
agent-slack message list "#general" --with-reaction eyes --oldest "1770165109.000000" --limit 20

# Recent channel messages that do not have :dart:
agent-slack message list "#general" --without-reaction dart --oldest "1770165109.000000" --limit 20
```

Optional:

```
# Include reactions + which users reacted
agent-slack message get "https://workspace.slack.com/archives/C123/p1700000000000000" --include-reactions
```

### Draft a message (browser editor)

Opens a Slack-like WYSIWYG editor in your browser for composing messages with full formatting support (bold, italic, strikethrough, links, lists, quotes, code, code blocks).

```
# Open editor for a channel
agent-slack message draft "#general"

# Open editor with initial text
agent-slack message draft "#general" "Here's my update"

# Reply in a thread
agent-slack message draft "https://workspace.slack.com/archives/C123/p1700000000000000"
```

After sending, the editor shows a "View in Slack" link to the posted message.

### Reply, edit, delete, and react

```
agent-slack message send "https://workspace.slack.com/archives/C123/p1700000000000000" "I can take this."
agent-slack message send "#alerts-staging" "here's the report" --attach ./report.md
agent-slack message send "#announcements" "Deploy starts at 6pm." --schedule "<future-iso-with-timezone>"
agent-slack message send "U05BRPTKL6A" "Heads up before standup" --schedule-in "monday 9am"
agent-slack message edit "https://workspace.slack.com/archives/C123/p1700000000000000" "I can take this today."
agent-slack message delete "https://workspace.slack.com/archives/C123/p1700000000000000"
agent-slack message react add "https://workspace.slack.com/archives/C123/p1700000000000000" "eyes"
agent-slack message react remove "https://workspace.slack.com/archives/C123/p1700000000000000" "eyes"
```

Channel mode requires `--ts`:

```
agent-slack message edit "#general" "Updated text" --workspace "myteam" --ts "1770165109.628379"
agent-slack message delete "#general" --workspace "myteam" --ts "1770165109.628379"
```

`message send` and `message edit` convert bullet/numbered lists to Slack native rich text. Inline mentions, broadcasts, emoji shortcodes, and `<#C...>` channel references inside those lists are preserved as Slack elements.

Send options for `message send`:

* `--attach <path>` upload a local file (repeatable; `<text>` is optional when attaching files)
* `--blocks <path>` send raw [Block Kit](https://docs.slack.dev/block-kit/) blocks from a JSON file (or `-` for stdin). Bypasses the automatic markdown-to-rich-text conversion, unlocking header/divider/section/table blocks and other structured layouts. Cannot be combined with `--attach`.
* `--reply-broadcast` when replying in a thread, also post the reply to the parent channel (Slack's "Also send to #channel" checkbox). For channel targets, pair with `--thread-ts`; for URL targets, the thread context is derived from the message. Not supported for DM targets; cannot be combined with `--attach`.
* `--schedule <time>` schedule delivery at an ISO 8601 timestamp with explicit timezone (for example `YYYY-MM-DDTHH:mm:ss-07:00`) or a Unix timestamp. The timestamp must be in the future and within Slack's 120-day scheduled-send limit. Works with `--blocks`, `--thread-ts`, and `--reply-broadcast`; cannot be combined with `--attach`.
* `--schedule-in <duration>` schedule delivery after a duration or simple future phrase (`30m`, `3h`, `2d`, `tomorrow 9am`, `monday 9am`; phrases use your local timezone). Mutually exclusive with `--schedule`; cannot be combined with `--attach`.

Upload files through `message send`:

```
agent-slack message send "#general" "Coverage report" --attach ./report.md
```

Broadcast a thread reply to the parent channel:

```
agent-slack message send "#general" "Decision: shipping v2 today" \
  --thread-ts "1770160000.000001" --reply-broadcast
```

Scheduled sends use Slack's server-side scheduled message queue:

```
# Absolute time with explicit timezone; replace with a future value within 120 days
agent-slack message send "#general" "Reminder: deploy starts soon." \
  --schedule "<future-iso-with-timezone>"

# Relative / natural future time
agent-slack message send "#general" "Monday launch checklist" --schedule-in "monday 9am"

# Scheduled thread reply with a Block Kit payload
agent-slack message send "#general" "fallback text" \
  --thread-ts "1770160000.000001" --blocks /tmp/blocks.json --schedule-in "3h"
```

Manage pending scheduled messages:

```
agent-slack message scheduled list
agent-slack message scheduled list --channel "#general" --limit 25
agent-slack message scheduled cancel "Q1234ABCD" --channel "C12345678"
```

Example — post a message with a native Slack table block:

```
cat > /tmp/blocks.json <<'EOF'
[
  {
    "type": "header",
    "text": { "type": "plain_text", "text": "Weekly digest" }
  },
  {
    "type": "table",
    "rows": [
      [
        { "type": "raw_text", "text": "Name" },
        { "type": "raw_text", "text": "Why" }
      ],
      [
        { "type": "raw_text", "text": "Caveman MCP" },
        { "type": "raw_text", "text": "~80% token cut on nav" }
      ]
    ]
  }
]
EOF
agent-slack message send "#alerts-staging" --blocks /tmp/blocks.json
```

When `--blocks` is used, the positional `<text>` argument (if provided) is still sent as the message's `text` fallback (for notifications and unfurls).

`message send` returns `channel_id` plus the posted `ts` and a `permalink` (for non-attachment sends). `thread_ts` appears only when replying in a thread. Scheduled sends return `scheduled_message_id` and `post_at` instead of `ts`/`permalink`.

### List, create, and invite channels

```
# List conversations for current user (users.conversations)
agent-slack channel list

# List conversations for a specific user
agent-slack channel list --user "@alice" --limit 50

# List all workspace conversations (conversations.list)
agent-slack channel list --all --limit 100

# Create a public channel
agent-slack channel new --name "incident-war-room"

# Create a private channel
agent-slack channel new --name "incident-leads" --private

# Invite users by id, handle, or email
agent-slack channel invite --channel "incident-war-room" --users "U01AAAA,@alice,bob@example.com"

# Invite external Slack Connect users by email (restricted by default)
agent-slack channel invite --channel "incident-war-room" --users "partner@vendor.com" --external

# External invite with permission for invitees to invite others
agent-slack channel invite --channel "incident-war-room" --users "partner@vendor.com" --external --allow-external-user-invites
```

Notes:

* `channel list` returns a single page plus `next_cursor`; use `--cursor` to fetch the next page.
* `channel list --all` and `channel list --user` are mutually exclusive.
* `--external` maps to `conversations.inviteShared` and expects email targets.
* External invites default to restricted mode (`external_limited=true`); add `--allow-external-user-invites` to disable that restriction.
* External invites require Slack Connect permissions/scopes in your workspace.

### Message get vs list

**`message get`** fetches a single message. If the message is in a thread, it also returns thread metadata (reply count, participants) but **not** the full thread contents:

```
{
  "message": { "ts": "...", "text": "...", "user": "U123", ... },
  "thread": { "ts": "...", "length": 6 }
}
```

**`message list`** fetches all replies in a thread, or recent channel messages when no thread is specified. Use this when you need the full conversation:

```
{
  "messages": [
    { "ts": "...", "text": "...", "user": "U123", ... },
    { "ts": "...", "text": "...", "user": "U456", ... }
  ]
}
```

When to use which:

* Use `get` to check a single message or see if there's a thread worth expanding
* Use `list` to read an entire thread conversation
* Use `list` on a channel (without `--thread-ts`) to browse recent channel messages
* Use `list` with `--with-reaction` / `--without-reaction` plus `--oldest` to filter channel history by reaction markers

### Files (snippets/images/attachments)

`message get/list` auto-download attached files to an agent-friendly temp directory and return file metadata in `message.files[]`, including `name` when Slack provides the original filename and `path` for the local download. Failed downloads keep the attachment entry, preserve `message.files[].path` with a local `.download-error.txt` file, and include `message.files[].error`. `search messages` and `search all` use the same attachment shape for message results, while `search files` skips entries whose download fails.

* macOS default: `~/.agent-slack/tmp/downloads/`

Agents can read those paths directly (e.g. snippets as `.txt`, images as `.png`).

### Search (messages + files)

```
# Search both messages and files
agent-slack search all "smoke tests failed" --channel "#alerts" --after 2026-01-01 --before 2026-02-01

# Search messages only
agent-slack search messages "stably ai" --user "@stablyai" --channel general

# Search files only (downloads files and returns local paths)
agent-slack search files "testing" --content-type snippet --limit 10
```

Tips:

* For reliable results, include `--channel ...` (channel-scoped search scans history/files and filters locally).
* Use `--workspace <url-or-unique-substring>` when using `#channel` names across multiple workspaces.

### Users

```
# List users (email requires appropriate Slack scopes; fields are pruned if missing)
agent-slack user list --workspace "https://workspace.slack.com" --limit 200 | jq .

# Get one user by id or handle
agent-slack user get U12345678 --workspace "https://workspace.slack.com" | jq .
agent-slack user get "@alice" --workspace "https://workspace.slack.com" | jq .
```

### Unreads (inbox view)

See all unread messages across channels, DMs, and threads in one place:

```
# Show all unreads with message content
agent-slack unreads

# Show only unread counts (no message content)
agent-slack unreads --counts-only

# Limit messages per channel (default 10)
agent-slack unreads --max-messages 5

# Include system messages (joins, leaves, topic changes)
agent-slack unreads --include-system
```

Output includes channels sorted by mention count, then unread count:

```
{
  "channels": [
    {
      "channel_id": "C123...",
      "channel_name": "general",
      "channel_type": "channel",
      "unread_count": 5,
      "mention_count": 2,
      "messages": [...]
    }
  ],
  "threads": {
    "has_unreads": true,
    "mention_count": 3
  }
}
```

Note: This feature uses the `client.counts` API which may be restricted in some Enterprise Grid workspaces (`team_is_restricted` error).

### Later (saved messages)

Manage your saved-for-later messages (Slack's Later tab):

```
# List saved messages (in-progress by default)
agent-slack later list

# Show only counts per state
agent-slack later list --counts-only

# Filter by state: in_progress, completed, archived, all
agent-slack later list --state completed

# Save a message for later
agent-slack later save "https://workspace.slack.com/archives/C123/p1700000000000000"

# Mark as completed
agent-slack later complete "https://workspace.slack.com/archives/C123/p1700000000000000"

# Archive
agent-slack later archive "https://workspace.slack.com/archives/C123/p1700000000000000"

# Move back to in-progress
agent-slack later reopen "https://workspace.slack.com/archives/C123/p1700000000000000"

# Remove from saved
agent-slack later remove "https://workspace.slack.com/archives/C123/p1700000000000000"

# Set a reminder
agent-slack later remind "https://workspace.slack.com/archives/C123/p1700000000000000" --in 1h
agent-slack later remind "https://workspace.slack.com/archives/C123/p1700000000000000" --in tomorrow
```

### Fetch a Canvas as Markdown

```
agent-slack canvas get "https://workspace.slack.com/docs/T123/F456"
agent-slack canvas get "F456" --workspace "https://workspace.slack.com"
```

Developing / Contributing
-------------------------

See [CONTRIBUTING.md](/stablyai/agent-slack/blob/main/CONTRIBUTING.md).

---

[![Stably](https://camo.githubusercontent.com/bd6d79da2c10c63160b6d93b6be8ddd2e99f03faf9f3ec127d0720e3517291f0/68747470733a2f2f7075626c69632d6172746966616374732e737461626c792e61692f6c6f676f2d77686974652d776974682d62672e706e67)](https://stably.ai)

### [Stably](https://stably.ai)

Code. Ship. ~~Test.~~

[**Documentation**](https://docs.stably.ai/) ·
[**Homepage**](https://stably.ai/)
