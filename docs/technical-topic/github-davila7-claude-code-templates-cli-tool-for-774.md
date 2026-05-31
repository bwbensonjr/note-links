---
id: 774
url: https://github.com/davila7/claude-code-templates
title: 'GitHub - davila7/claude-code-templates: CLI tool for configuring and monitoring
  Claude Code'
domain: github.com
source_date: '2026-02-01'
tags:
- github-repo
- cli-tool
- llm
- python
summary: Claude Code Templates is a CLI tool that provides ready-to-use configurations
  and components for Anthropic's Claude Code, including AI agents, custom commands,
  MCPs (external integrations), settings, hooks, and project templates to enhance
  development workflows. The tool offers over 100+ pre-built components accessible
  through an interactive web interface or command line, plus additional features like
  analytics, conversation monitoring, and health checks to optimize your AI-powered
  development environment. It's open-source, MIT-licensed, and welcomes community
  contributions from developers looking to expand its template library.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# GitHub - davila7/claude-code-templates: CLI tool for configuring and monitoring Claude Code

[![npm version](https://camo.githubusercontent.com/e97033892406a11c293e7b09a1358796b50f64cd09dd58650343e36c7b677977/68747470733a2f2f696d672e736869656c64732e696f2f6e706d2f762f636c617564652d636f64652d74656d706c617465732e737667)](https://www.npmjs.com/package/claude-code-templates)
[![npm downloads](https://camo.githubusercontent.com/f371d59fb827c858e53a6fe9e835c4393dd12862185c99f37b054d5d7bf526b5/68747470733a2f2f696d672e736869656c64732e696f2f6e706d2f64742f636c617564652d636f64652d74656d706c617465732e737667)](https://www.npmjs.com/package/claude-code-templates)
[![License: MIT](https://camo.githubusercontent.com/fdf2982b9f5d7489dcf44570e714e3a15fce6253e0cc6b5aa61a075aac2ff71b/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4c6963656e73652d4d49542d79656c6c6f772e737667)](https://opensource.org/licenses/MIT)
[![PRs Welcome](https://camo.githubusercontent.com/dd0b24c1e6776719edb2c273548a510d6490d8d25269a043dfabbd38419905da/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f5052732d77656c636f6d652d627269676874677265656e2e737667)](/davila7/claude-code-templates/blob/main/CONTRIBUTING.md)
[![Sponsored by Z.AI](https://camo.githubusercontent.com/fb79c02ab8516cc8c48fbd460b661e02dfe5f7f02611e65e751e0133a84898e2/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f53706f6e736f72656425323062792d5a2e41492d3235363365623f7374796c653d666c6174266c6f676f3d646174613a696d6167652f7376672b786d6c3b6261736536342c50484e325a79423361575230614430694d6a51694947686c6157646f644430694d6a516949485a705a58644362336739496a41674d4341794e4341794e4349675a6d6c7362443069626d39755a53496765473173626e4d39496d6830644841364c79393364336375647a4d7562334a6e4c7a49774d44417663335a6e496a344b50484268644767675a4430695454457949444a4d4d6941794d6b67794d6b77784d694179576949675a6d6c736244306964326870644755694c7a344b5043397a646d632b)](https://z.ai/subscribe?ic=8JVLJQFSKB&utm_source=github&utm_medium=badge&utm_campaign=readme)
[![Claude for Open Source](https://camo.githubusercontent.com/490dbc5c430efb2b733ec7b856fd1ed25a879c948fd1046172a71695e98bcdc8/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f436c617564652d4f70656e253230536f7572636525323050726f6772616d2d4439373735373f7374796c653d666c6174266c6f676f3d646174613a696d6167652f7376672b786d6c3b6261736536342c50484e325a79423361575230614430694d6a51694947686c6157646f644430694d6a516949485a705a58644362336739496a41674d4341794e4341794e4349675a6d6c7362443069626d39755a53496765473173626e4d39496d6830644841364c79393364336375647a4d7562334a6e4c7a49774d44417663335a6e496a343859326c795932786c49474e34505349784d69496759336b39496a4579496942795053497a4969426d6157787350534a3361476c305a534976506a777663335a6e50673d3d)](https://claude.com/contact-sales/claude-for-oss)
[![Neon Open Source Program](https://camo.githubusercontent.com/d5aa098372a702b58359a663b65c2fb3a039801ae258b1d035bb64c3a584954f/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4e656f6e2d4f70656e253230536f7572636525323050726f6772616d2d3030453539393f7374796c653d666c6174)](https://get.neon.com/4eCjZDz)
[![Buy Me A Coffee](https://camo.githubusercontent.com/418c63057144bd4345ef93b2bf86dd622f2b40f0492b818be8d7719cf94bf103/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4275792532304d6525323041253230436f666665652d737570706f72742d79656c6c6f773f7374796c653d666c6174266c6f676f3d6275792d6d652d612d636f66666565)](https://buymeacoffee.com/daniavila)
[![GitHub stars](https://camo.githubusercontent.com/04828f01e4ede731a3da6a95d8876be74627fd99655b7d0e2fa8d39e1e0afa67/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f73746172732f646176696c61372f636c617564652d636f64652d74656d706c617465732e7376673f7374796c653d736f6369616c266c6162656c3d53746172)](https://github.com/davila7/claude-code-templates)

[![davila7%2Fclaude-code-templates | Trendshift](https://camo.githubusercontent.com/1568745f75c4eff96e67b1e8e57855ff877519bdbfc44728de5fd9cd57add4c7/68747470733a2f2f7472656e6473686966742e696f2f6170692f62616467652f7265706f7369746f726965732f3135313133)](https://trendshift.io/repositories/15113)
  
  
[![Vercel OSS Program](https://camo.githubusercontent.com/3c85f1c0ed664075fccfc31b30444162e075143946c28524be13df55df566e34/68747470733a2f2f76657263656c2e636f6d2f6f73732f70726f6772616d2d62616467652e737667)](https://vercel.com/oss)
  
[![Neon Open Source Program](https://camo.githubusercontent.com/e0cbcf922ffa8519c15367c61db209e4c4b73da547f1a377254f1cd26fe2bb0e/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4e656f6e2d4f70656e253230536f7572636525323050726f6772616d2d3030453539393f7374796c653d666f722d7468652d6261646765)](https://get.neon.com/4eCjZDz)
  
[![Claude for Open Source](/davila7/claude-code-templates/raw/main/docs/claude-oss-badge.svg)](https://claude.com/contact-sales/claude-for-oss)

---

> **🧪 NEW: Dashboard** — Explore components, manage collections, and track installations at **[www.aitmpl.com](https://www.aitmpl.com)**. Currently in beta — feedback welcome!

Claude Code Templates ([aitmpl.com](https://aitmpl.com))
========================================================

**Ready-to-use configurations for Anthropic's Claude Code.** A comprehensive collection of AI agents, custom commands, settings, hooks, external integrations (MCPs), and project templates to enhance your development workflow.

Browse & Install Components and Templates
-----------------------------------------

**[Browse All Templates](https://aitmpl.com)** - Interactive web interface to explore and install 100+ agents, commands, settings, hooks, and MCPs.

[![Screenshot 2025-08-19 at 08 09 24](https://private-user-images.githubusercontent.com/6216945/479499740-e3617410-9b1c-4731-87b7-a3858800b737.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3ODAyNDc0MzQsIm5iZiI6MTc4MDI0NzEzNCwicGF0aCI6Ii82MjE2OTQ1LzQ3OTQ5OTc0MC1lMzYxNzQxMC05YjFjLTQ3MzEtODdiNy1hMzg1ODgwMGI3MzcucG5nP1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQVZDT0RZTFNBNTNQUUs0WkElMkYyMDI2MDUzMSUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyNjA1MzFUMTcwNTM0WiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9YTY2YzkwZjZlNWY2ZGVkYTg0OWZhNjc5Y2JlODU1ZGZjODU1ZTdlMWYxNDRiZWRmODEzNjBiZWI3ODcyY2I4NSZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QmcmVzcG9uc2UtY29udGVudC10eXBlPWltYWdlJTJGcG5nIn0.aykukqJFNKPAY-UQ2XUb262FexNX_E42eCoKPiLkdd4)](https://private-user-images.githubusercontent.com/6216945/479499740-e3617410-9b1c-4731-87b7-a3858800b737.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3ODAyNDc0MzQsIm5iZiI6MTc4MDI0NzEzNCwicGF0aCI6Ii82MjE2OTQ1LzQ3OTQ5OTc0MC1lMzYxNzQxMC05YjFjLTQ3MzEtODdiNy1hMzg1ODgwMGI3MzcucG5nP1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQVZDT0RZTFNBNTNQUUs0WkElMkYyMDI2MDUzMSUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyNjA1MzFUMTcwNTM0WiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9YTY2YzkwZjZlNWY2ZGVkYTg0OWZhNjc5Y2JlODU1ZGZjODU1ZTdlMWYxNDRiZWRmODEzNjBiZWI3ODcyY2I4NSZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QmcmVzcG9uc2UtY29udGVudC10eXBlPWltYWdlJTJGcG5nIn0.aykukqJFNKPAY-UQ2XUb262FexNX_E42eCoKPiLkdd4)

🚀 Quick Installation
--------------------

```
# Install a complete development stack
npx claude-code-templates@latest --agent development-team/frontend-developer --command testing/generate-tests --mcp development/github-integration --yes

# Browse and install interactively
npx claude-code-templates@latest

# Install specific components
npx claude-code-templates@latest --agent development-tools/code-reviewer --yes
npx claude-code-templates@latest --command performance/optimize-bundle --yes
npx claude-code-templates@latest --setting performance/mcp-timeouts --yes
npx claude-code-templates@latest --hook git/pre-commit-validation --yes
npx claude-code-templates@latest --mcp database/postgresql-integration --yes
```

What You Get
------------

| Component | Description | Examples |
| --- | --- | --- |
| **🤖 Agents** | AI specialists for specific domains | Security auditor, React performance optimizer, database architect |
| **⚡ Commands** | Custom slash commands | `/generate-tests`, `/optimize-bundle`, `/check-security` |
| **🔌 MCPs** | External service integrations | GitHub, PostgreSQL, Stripe, AWS, OpenAI |
| **⚙️ Settings** | Claude Code configurations | Timeouts, memory settings, output styles |
| **🪝 Hooks** | Automation triggers | Pre-commit validation, post-completion actions |
| **🎨 Skills** | Reusable capabilities with progressive disclosure | PDF processing, Excel automation, custom workflows |

🛠️ Additional Tools
-------------------

Beyond the template catalog, Claude Code Templates includes powerful development tools:

### 📊 Claude Code Analytics

Monitor your AI-powered development sessions in real-time with live state detection and performance metrics.

```
npx claude-code-templates@latest --analytics
```

### 💬 Conversation Monitor

Mobile-optimized interface to view Claude responses in real-time with secure remote access.

```
# Local access
npx claude-code-templates@latest --chats

# Secure remote access via Cloudflare Tunnel
npx claude-code-templates@latest --chats --tunnel
```

### 🔍 Health Check

Comprehensive diagnostics to ensure your Claude Code installation is optimized.

```
npx claude-code-templates@latest --health-check
```

### 🔌 Plugin Dashboard

View marketplaces, installed plugins, and manage permissions from a unified interface.

```
npx claude-code-templates@latest --plugins
```

📖 Documentation
---------------

**[📚 docs.aitmpl.com](https://docs.aitmpl.com/)** - Complete guides, examples, and API reference for all components and tools.

Contributing
------------

We welcome contributions! **[Browse existing templates](https://aitmpl.com)** to see what's available, then check our [contributing guidelines](/davila7/claude-code-templates/blob/main/CONTRIBUTING.md) to add your own agents, commands, MCPs, settings, or hooks.

**Please read our [Code of Conduct](/davila7/claude-code-templates/blob/main/CODE_OF_CONDUCT.md) before contributing.**

Attribution
-----------

This collection includes components from multiple sources:

**Scientific Skills:**

* **[K-Dense-AI/claude-scientific-skills](https://github.com/K-Dense-AI/claude-scientific-skills)** by K-Dense Inc. - MIT License (139 scientific skills for biology, chemistry, medicine, and computational research)

**Official Anthropic:**

* **[anthropics/skills](https://github.com/anthropics/skills)** - Official Anthropic skills (21 skills)
* **[anthropics/claude-code](https://github.com/anthropics/claude-code)** - Development guides and examples (10 skills)

**Community Skills & Agents:**

* **[obra/superpowers](https://github.com/obra/superpowers)** by Jesse Obra - MIT License (14 workflow skills)
* **[alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills)** by Alireza Rezvani - MIT License (36 professional role skills)
* **[wshobson/agents](https://github.com/wshobson/agents)** by wshobson - MIT License (48 agents)
* **NerdyChefsAI Skills** - Community contribution - MIT License (specialized enterprise skills)

**Commands & Tools:**

* **[awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code)** by hesreallyhim - CC0 1.0 Universal (21 commands)
* **[awesome-claude-skills](https://github.com/mehdi-lamrani/awesome-claude-skills)** - Apache 2.0 (community skills)
* **move-code-quality-skill** - MIT License
* **cocoindex-claude** - Apache 2.0

Each of these resources retains its **original license and attribution**, as defined by their respective authors.
We respect and credit all original creators for their work and contributions to the Claude ecosystem.

📄 License
---------

This project is licensed under the MIT License - see the [LICENSE](/davila7/claude-code-templates/blob/main/LICENSE) file for details.

🔗 Links
-------

* **🌐 Browse Templates**: [aitmpl.com](https://aitmpl.com)
* **📚 Documentation**: [docs.aitmpl.com](https://docs.aitmpl.com)
* **💬 Community**: [GitHub Discussions](https://github.com/davila7/claude-code-templates/discussions)
* **🐛 Issues**: [GitHub Issues](https://github.com/davila7/claude-code-templates/issues)

Stargazers over time
--------------------

[![Stargazers over time](https://camo.githubusercontent.com/609b03e457a058c0e78213f583f658ea58afcb789f42d3a13920ff94fcd2650d/68747470733a2f2f7374617263686172742e63632f646176696c61372f636c617564652d636f64652d74656d706c617465732e7376673f76617269616e743d6164617074697665)](https://starchart.cc/davila7/claude-code-templates)

---

**⭐ Found this useful? Give us a star to support the project!**

[![Buy Me A Coffee](https://camo.githubusercontent.com/0fc0705004ac0b674c90f8ef4b20b0d671f6950ec3f6a40c689a6f79f3d2878a/68747470733a2f2f696d672e6275796d6561636f666665652e636f6d2f627574746f6e2d6170692f3f746578743d4275792532306d6525323061253230636f6666656526736c75673d64616e696176696c6126627574746f6e5f636f6c6f75723d46464444303026666f6e745f636f6c6f75723d30303030303026666f6e745f66616d696c793d436f6f6b6965266f75746c696e655f636f6c6f75723d30303030303026636f666665655f636f6c6f75723d666666666666)](https://buymeacoffee.com/daniavila)
