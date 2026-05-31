---
id: 961
url: https://dobase.co/
title: Dobase — Your workspace, your server
domain: dobase.co
source_date: '2026-03-27'
tags:
- github-repo
- devops
- web-dev
- database
summary: Dobase is an open-source, self-hosted productivity suite that consolidates
  eight tools—including email, kanban boards, documents, chat, tasks, file storage,
  calendar, and video conferencing—into a single unified workspace. It prioritizes
  user privacy and control by running entirely on your own server with no tracking
  or third-party data sharing, while offering features like real-time collaboration,
  keyboard shortcuts, and two-factor authentication. The platform is free to use,
  easy to deploy with Docker, and allows you to install only the tools you need while
  maintaining complete ownership of your data.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# Dobase — Your workspace, your server

One workspace. Your server.
===========================

Open-source app that replaces your scattered SaaS tools with a single self-hosted workspace. Mail, boards, docs, chat, and more — all under your control.

[View on GitHub](https://github.com/smgdkngt/dobase)
[Self-host](https://github.com/smgdkngt/dobase#self-hosting)

![Kanban board with cards, due dates, and assignees](screenshots/board-launch.png)
![Email client with threaded conversations](screenshots/mail.png)
![Real-time team chat with file sharing and replies](screenshots/chat.png)
![Weekly calendar view with events](screenshots/calendar.png)
![Rich text document editor](screenshots/docs-editor-edit.png)
![Add any tool to your workspace](screenshots/add-tool.png)
![Task lists with due dates and assignments](screenshots/todos.png)
![File storage with folders and selection](screenshots/files.png)
![Document cards with content previews](screenshots/docs-index.png)
![Command palette for quick navigation](screenshots/command-palette.png)
![Card detail with description, comments, and attachments](screenshots/board-card-detail.png)
![Mail folders and organization](screenshots/mail-folders.png)
![Invite collaborators to share tools](screenshots/collaborators-4.png)
![File preview with metadata](screenshots/file-preview.png)
![Todo item with comments and attachments](screenshots/todo-detail-comment.png)

Eight tools, one app.
---------------------

Install only what you need. Each tool can be shared with different collaborators, or kept private.

### Mail

IMAP/SMTP email client with rich text compose, contacts, and threaded conversations.

### Board

Kanban boards with drag-and-drop columns, cards, comments, and attachments.

### Docs

Rich text documents you can share and edit together with your team.

### Chat

Real-time messaging with typing indicators, threaded replies, and file sharing.

### Todos

Task lists with due dates, assignments, comments, and file attachments.

### Files

File storage with folders, previews, and sharing via public links.

### Calendar

CalDAV-compatible calendar with recurring events and standalone local mode.

### Room

Video conferencing powered by LiveKit, without leaving your workspace.

### Everything you'd expect, and then some.

#### Command palette

Hit `Cmd+K` to instantly jump to any tool, page, or action without touching the mouse.

#### Keyboard shortcuts

Navigate, compose, and act from the keyboard. Every tool ships with a full shortcut set and a `?` help overlay.

#### Real-time notifications

Activity dots appear on tools with new content since your last visit. Pushed live over ActionCable — no polling.

#### Two-factor auth

TOTP-based 2FA compatible with any authenticator app. Enable per-account for an extra layer of security.

#### Collaborative sharing

Invite people as owners or collaborators per tool. Permissions are explicit and instance-based, never global.

#### Mobile-friendly

Responsive layout that works on any screen size. Add to your home screen as a PWA for native-app feel.

Your data, your rules.
----------------------

Dobase runs on your server. No analytics, no tracking, no third-party data sharing. One Rails app, one SQLite database, one Docker container. That is the entire stack.

* Self-hosted on any VPS
* Fully open source
* Real-time collaboration built in
* Install only the tools you need

License

MIT

Free for any purpose. Use, modify, distribute, sell — no restrictions. No vendor lock-in, no surprise pricing, ever.

[Read the license →](https://github.com/smgdkngt/dobase/blob/main/LICENSE.md)

Self-host anywhere.
-------------------

Install with [ONCE](https://once.com) for the easiest setup — backups, updates, and SSL handled automatically. Or deploy with [Kamal](https://kamal-deploy.org) for zero-downtime deploys with LiveKit video. Works on any VPS, cloud server, or Raspberry Pi.

$ docker run -d -p 80:80 \
-v dobase:/rails/storage \
-e SECRET\_KEY\_BASE=$(openssl rand -hex 64) \
ghcr.io/smgdkngt/dobase
