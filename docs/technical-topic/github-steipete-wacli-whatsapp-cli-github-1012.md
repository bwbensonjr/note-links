---
id: 1012
url: https://github.com/steipete/wacli
title: 'GitHub - steipete/wacli: WhatsApp CLI · GitHub'
domain: github.com
source_date: '2026-04-15'
tags:
- github-repo
- cli-tool
- go
summary: wacli is an unofficial WhatsApp command-line tool built on the WhatsApp Web
  protocol that enables users to sync message history locally, search messages offline,
  send messages, and manage contacts and groups. The tool can be installed via Homebrew
  or built locally with Go, and requires QR code authentication on first use followed
  by continuous syncing capabilities. Key features include best-effort message history
  synchronization, fast offline search, file and text message sending, and optional
  history backfilling from your primary WhatsApp device.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# GitHub - steipete/wacli: WhatsApp CLI · GitHub

🗃️ wacli — WhatsApp CLI: sync, search, send
===========================================

[![wacli banner](/openclaw/wacli/raw/main/docs/assets/readme-banner.jpg)](/openclaw/wacli/blob/main/docs/assets/readme-banner.jpg)

A scriptable WhatsApp client built on [`whatsmeow`](https://github.com/tulir/whatsmeow). Pairs as a linked WhatsApp Web device, mirrors your messages into a local SQLite store, and gives you offline search, sending, and chat/group/contact management from the command line.

> Third-party tool. Uses the WhatsApp Web protocol via `whatsmeow`. Not affiliated with WhatsApp.

Full documentation: **<https://wacli.sh>**

Features
--------

* **Auth + sync** — QR pairing, one-shot or follow-mode sync, optional media downloads, optional signed webhook fan-out.
* **Offline message store** — SQLite with FTS5 search (LIKE fallback), filterable by chat, sender, direction, time, and media type, with status broadcasts stored separately.
* **Sending** — text with mentions/replies/link-previews, files (image/video/audio/document, ≤100 MiB), stickers, voice notes, reactions, and status broadcasts; rapid-send guardrails and retry-receipt grace.
* **History backfill** — best-effort per-chat requests to your primary device for older messages.
* **Contacts / chats / groups / channels / profile** — search, alias, tag, archive, pin, mute, mark-read, rename, prune, manage participants and invite links, send to channels, and manage profile metadata.
* **Diagnostics + safety** — `doctor`, read-only mode, store locks with owner reporting, panic recovery, bounded media queue, owner-only DB perms.
* **Scriptable** — `--json` everywhere, `--events` NDJSON lifecycle stream, deterministic exit codes.

Install
-------

### Homebrew (recommended)

```
brew install openclaw/tap/wacli
```

If a Linux install reports `Binary was compiled with 'CGO_ENABLED=0'`, run `brew update && brew reinstall openclaw/tap/wacli`.

### Build from source

`wacli` uses `go-sqlite3`, so cgo + a C compiler are required.

* macOS: Xcode Command Line Tools.
* Debian/Ubuntu: `sudo apt install build-essential`.

```
CGO_ENABLED=1 CGO_CFLAGS="-Wno-error=missing-braces" \
  go install -tags sqlite_fts5 github.com/openclaw/wacli/cmd/wacli@latest
```

For local development:

```
git clone https://github.com/openclaw/wacli.git
cd wacli
CGO_ENABLED=1 CGO_CFLAGS="-Wno-error=missing-braces" \
  go build -tags sqlite_fts5 -o ./dist/wacli ./cmd/wacli
./dist/wacli --help
```

### Docker

```
docker build -t wacli .
docker run --rm -it -v "$PWD/.wacli:/data" wacli auth
docker run --rm -v "$PWD/.wacli:/data" wacli sync --follow
```

The image keeps WhatsApp auth, SQLite, config, and cache under `/data`; it also includes `ffmpeg` for media helpers.

Quick start
-----------

```
# 1. Pair (shows QR), then bootstrap sync
wacli auth

# 2. Keep syncing in the background (no QR; needs prior auth)
wacli sync --follow

# 3. Search
wacli messages search "meeting"

# 4. Send
wacli send text --to 1234567890 --message "hello"
wacli send file --to mom --file ./pic.jpg --caption "hi"
wacli send status --message "available today" --background-color '#1f7a8c'

# 5. Diagnostics
wacli doctor
```

Recipients accept a JID, phone number (E.164 or formatted), channel JID, or a synced contact/group/chat name. Ambiguous names prompt in a TTY; pass `--pick N` in scripts.

More recipes — replies, mentions, stickers, voice, reactions, statuses, channels, history backfill, chat management — live in the [docs](https://wacli.sh).

Documentation
-------------

| Area | Pages |
| --- | --- |
| **Setup** | [overview](/openclaw/wacli/blob/main/docs/overview.md) · [auth](/openclaw/wacli/blob/main/docs/auth.md) · [accounts](/openclaw/wacli/blob/main/docs/accounts.md) · [sync](/openclaw/wacli/blob/main/docs/sync.md) · [doctor](/openclaw/wacli/blob/main/docs/doctor.md) |
| **Messaging** | [messages](/openclaw/wacli/blob/main/docs/messages.md) · [calls](/openclaw/wacli/blob/main/docs/calls.md) · [send](/openclaw/wacli/blob/main/docs/send.md) · [media](/openclaw/wacli/blob/main/docs/media.md) · [presence](/openclaw/wacli/blob/main/docs/presence.md) |
| **Address book** | [contacts](/openclaw/wacli/blob/main/docs/contacts.md) · [chats](/openclaw/wacli/blob/main/docs/chats.md) · [groups](/openclaw/wacli/blob/main/docs/groups.md) · [channels](/openclaw/wacli/blob/main/docs/channels.md) |
| **History** | [history coverage / fill / backfill](/openclaw/wacli/blob/main/docs/history.md) |
| **Local store** | [store](/openclaw/wacli/blob/main/docs/store.md) · [companion integrations](/openclaw/wacli/blob/main/docs/integrations.md) |
| **Misc** | [profile](/openclaw/wacli/blob/main/docs/profile.md) · [version](/openclaw/wacli/blob/main/docs/version.md) · [completion](/openclaw/wacli/blob/main/docs/completion.md) · [release](/openclaw/wacli/blob/main/docs/release.md) |

Configuration
-------------

Default store: `~/.local/state/wacli` on Linux, `~/.wacli` elsewhere. Existing `~/.wacli` directories on Linux keep working. Use `wacli accounts add NAME` and `--account NAME` for first-class multi-account stores.

**Global flags:** `--store DIR`, `--account NAME`, `--json`, `--events`, `--full`, `--timeout DUR`, `--lock-wait DUR`, `--read-only`.

**Environment overrides:**

| Variable | Effect |
| --- | --- |
| `WACLI_STORE_DIR` | Default store directory. |
| `WACLI_READONLY` | `1`/`true`/`yes`/`on` enables read-only mode. |
| `WACLI_DEVICE_LABEL` | Linked-device label shown in WhatsApp. Defaults to `wacli - <OS> (<host>)`. |
| `WACLI_DEVICE_PLATFORM` | Linked-device platform. Defaults to `DESKTOP`; invalid values fall back to `CHROME`. |
| `WACLI_SYNC_MAX_MESSAGES` | Stop sync once total local messages exceed this count. |
| `WACLI_SYNC_MAX_DB_SIZE` | Stop sync once `wacli.db` + sidecars reach a size like `500MB` or `2GB`. |

Backfilling older history
-------------------------

`wacli sync` only stores what WhatsApp Web sends opportunistically. To fetch *older* messages, `wacli` issues on-demand history requests to your **primary device** (your phone), which must be online.

* Best-effort: WhatsApp may not return full history.
* One request anchors on the **oldest locally stored message** in that chat — run `sync` first.
* Recommended `--count 50` per request (max 500). Max `--requests 100` per run.
* `history coverage` shows which chats are eligible. `history fill --dry-run` plans without connecting.

```
wacli history coverage --include-blocked
wacli history fill --dry-run --kind group --limit 20
wacli history backfill --chat 1234567890@s.whatsapp.net --requests 10 --count 50
```

Loop over every known chat:

```
wacli --json chats list --limit 100000 \
  | jq -r '.data[].JID' \
  | while read -r jid; do
      wacli history backfill --chat "$jid" --requests 3 --count 50
    done
```

Credits
-------

Heavily inspired by [`whatsapp-cli`](https://github.com/vicentereig/whatsapp-cli) by Vicente Reig.

Maintainers
-----------

* Created by [@steipete](https://github.com/steipete)
* Currently maintained by [@dinakars777](https://github.com/dinakars777)

License
-------

See [`LICENSE`](/openclaw/wacli/blob/main/LICENSE).
