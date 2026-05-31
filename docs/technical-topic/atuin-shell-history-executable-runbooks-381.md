---
id: 381
url: https://atuin.sh/
title: Atuin - Shell History & Executable Runbooks
domain: atuin.sh
source_date: '2025-06-24'
tags:
- cli-tool
- github-repo
- devops
- security
summary: '# Atuin Summary


  Atuin is an open-source tool that enhances shell history management by allowing
  developers to sync, search, and backup their command history across machines with
  end-to-end encryption. The platform has expanded beyond its CLI offering to include
  Atuin Desktop (currently in beta), which enables executable runbooks that combine
  shell commands, database queries, and HTTP requests into shareable, collaborative
  workflows. With over 25,000 GitHub stars and trusted by thousands of developers,
  Atuin aims to eliminate context switching and make documentation more dynamic and
  maintainable.'
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# Atuin - Shell History & Executable Runbooks

$ history | grep deploy

$ kubectl get pods

$ git log --oneline

$ \_

$ atuin search docker

$ ssh prod-server

$ atuin sync

$ tail -f logs/app.log

$ docker ps -a

$ atuin import auto

user@atuin:~$ echo "Making your shell"

Making your shell 
magical█
===========================

Sync, search and backup shell history with Atuin.

Install in seconds:

$ curl --proto '=https' --tlsv1.2 -LsSf https://setup.atuin.sh | sh

[$ get-cli](https://docs.atuin.sh/cli/)
[> get-desktop](https://github.com/atuinsh/desktop/releases/latest)

Available for macOS and Linux
[→ Visit our blog](https://blog.atuin.sh)

### 🚀 Try These Commands

$ atuin search docker

# Search through shell history

$ atuin stats

# Show usage statistics

$ atuin sync

# Sync history (demo mode)

$ git status

# Real git commands work!

$ ls -la ~/.local/share/atuin/

# Explore Atuin's files

[close]

Proudly open source
-------------------

Trusted by thousands of developers worldwide

25K+

GitHub Stars

230+

Contributors

220M+

Synced History

Products

Shells all the way down
-----------------------

We started with an open-source CLI that developers actually wanted to use.
Now we're exploring what happens when that same philosophy meets team workflows.

⚡

### Atuin CLI

The magical shell history tool loved by developers worldwide.
**Sync your commands across machines, search everything instantly, and keep your data
encrypted.**
Open source.

* ✓
  Shell history sync across machines
* ✓
  End-to-end encryption. Your data stays yours
* ✓
  Enhanced search with context

[$ get-cli](https://docs.atuin.sh/cli/)
[View on GitHub](https://github.com/atuinsh/atuin)

New

🚀

### Atuin Desktop

*Runbooks that run*
Atuin Desktop looks like a doc, but runs like your terminal. Kill context switching with executable runbooks
that chain shell commands, database queries and HTTP requests.

* ✓
  Docs that don't rot: execute directly + stay relevant
* ✓
  Local-first, CRDT-powered collaboration
* ✓
  Instant recall: autocomplete from your shell history

[> get-desktop](https://github.com/atuinsh/desktop/releases/latest)
[View on GitHub](https://github.com/atuinsh/desktop)

Atuin CLI

Shell history supercharged
--------------------------

Sync, search, and backup your shell history with end-to-end encryption.
The magical shell tool loved by developers worldwide.

$ curl --proto '=https' --tlsv1.2 -LsSf
https://setup.atuin.sh | sh

Install Atuin CLI in seconds. Works with bash, zsh, fish, and more.

🔄

### Shell history sync

Sync your shell history to all of your machines, wherever they are. Never lose a command again.

🔒

### End-to-end encryption

All data is encrypted client-side and can only be read by you. Your commands stay private.

⚡

### Efficient search

Search decades of shell history and recall it in an instant. Configurable full text or fuzzy search.

💖

### Open source

Atuin is open source with a permissive license and has a growing community of contributors.

📥

### Data import

Bring your existing history with you. Atuin supports importing from a wide variety of formats.

📊

### Store extra context

Atuin stores extra context with your commands: working directory, exit code, duration, and more!

Now in Open Beta!

Atuin Desktop Beta
------------------

Runbooks should run. Built to make workflows repeatable, shareable, and reliable.
See what we're building for teams.

[> get-desktop](https://github.com/atuinsh/desktop/releases/latest)

![Atuin Desktop Preview](desktop-screenshot.png)
![Atuin Desktop Preview 2](desktop-screenshot2.png)

Terminal Block

▶
Run

$ kubectl scale deployment api-server --replicas=5

deployment.apps/api-server scaled

$ kubectl rollout status deployment/api-server

Waiting for deployment "api-server" rollout to finish...

deployment "api-server" successfully rolled out

SQL Query

▶
Execute

SELECT status, count(\*) FROM deployments

WHERE created\_at > '2025-01-01'

GROUP BY status;

STATUS

COUNT

success

247

pending

12

failed

3

E

A

Shared with team

Synced

Production deployment runbook • Last edited 2 hours ago

FAQ

Frequently Asked Questions
--------------------------

Everything you need to know about Atuin

### CLI Atuin CLI

#### Is Atuin CLI really free?

Yes! Atuin CLI is completely open source and free
forever. You can self-host the sync server or use our hosted service.

#### Can I use Atuin with my existing shell?

Absolutely! Atuin works with bash, zsh, fish, and other
popular shells. Installation is simple and doesn't interfere with your existing setup.

#### Does Atuin slow down my shell?

Not at all! Atuin is built in Rust for maximum
performance. Most users don't notice any difference, and many find their shell faster thanks to
enhanced search.

#### How is my CLI data protected?

All your command history is encrypted end-to-end before
leaving your machine. Only you can decrypt and read your data. We never see your commands.

#### Can I self-host Atuin CLI?

Absolutely! Atuin CLI is designed for self-hosting. You
can run your own sync server or use our hosted service. Full control over your infrastructure and
data.

### Desktop Atuin Desktop

#### What makes Desktop different?

Atuin Desktop runbooks actually execute. Instead of
copy-pasting commands from docs, you click and run. Database queries render live results.
Documentation that stays current because it runs.

#### When will Desktop be available?

Atuin Desktop is now available as an open beta. You can
[download the latest release for your platform](https://github.com/atuinsh/desktop/releases/latest).

#### Is Desktop open source?

Yes! Atuin Desktop is open source. You can find the source code at our
[GitHub repository](https://github.com/atuinsh/desktop).

#### How is Desktop data handled?

Atuin Desktop is local-first with CRDT collaboration.
Data is stored locally and synced via Atuin Hub. Unlike CLI, Desktop is not end-to-end encrypted.

#### Can I self-host Desktop?

The desktop backend, Atuin Hub, is not currently open source or available for self-hosting.
However, Atuin Desktop supports offline, file-based workspaces, which you can collaborate on
via Git or another VCS.

Transform your workflow today
-----------------------------

Join 200,000+ developers who have already upgraded their command line workflow.
Start with our open-source CLI, and be first in line for Desktop.

[$ get-cli](https://docs.atuin.sh/cli/)
[> get-desktop](https://github.com/atuinsh/desktop/releases/latest)
