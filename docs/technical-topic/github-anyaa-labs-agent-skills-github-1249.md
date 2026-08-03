---
id: 1249
url: https://github.com/anyaa-labs/agent-skills
title: GitHub - anyaa-labs/agent-skills · GitHub
domain: github.com
source_date: '2026-08-01'
tags:
- github-repo
- ai
- llm
- distributed-systems
summary: 'Agent-skills is a GitHub repository providing Claude Code and Codex skills
  for evaluating and designing multi-agent AI systems. The primary tool, agent-architect,
  offers three modes: AUDIT (comprehensive 11-dimension evaluation of existing systems),
  REVIEW (focused analysis of specific prompts or tools), and DESIGN (architecting
  new agent systems from scratch), with capabilities covering production-level concerns
  like API contracts, tool governance, and multimodal surfaces. The skills can be
  installed locally and invoked through Claude Code or Codex, with the framework designed
  to be extensible through new skill modules.'
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# GitHub - anyaa-labs/agent-skills · GitHub

agent-skills
============

Claude Code and Codex skills for evaluating and designing multi-agent systems.

Skills
------

### `/agent-architect`

Senior architect review for agent systems, prompt engineering, and harness design.

**Three modes:**

* **AUDIT** — Full 11-dimension evaluation of an existing agent system. Scores prompt architecture, tool design, context management, multi-agent orchestration, eval infrastructure, production readiness, model awareness, agent security, memory architecture, harness architecture, and multimodal architecture. Produces a maturity score with prioritized recommendations.
* **REVIEW** — Focused teardown of a specific prompt, skill file, or tool definition. Line-by-line findings with confidence scores.
* **DESIGN** — Architect a new agent system from scratch. Produces system prompt drafts, tool specs, failure mode maps, eval plans, and implementation checklists.

The current agent-architect version is built for production AI systems, not just prompt review. It evaluates runtime API contracts, tool harness boundaries, MCP/tool governance, background task execution, trace-based evaluation, and voice/image/video surfaces when those modalities are present.

Install
-------

`./setup` installs each skill into both `~/.claude/skills` and `~/.agents/skills`.

```
git clone git@github.com:YOUR_ORG/agent-skills.git ~/.claude/skills/agent-skills
cd ~/.claude/skills/agent-skills
./setup
```

Or install from any location:

```
git clone git@github.com:YOUR_ORG/agent-skills.git ~/path/to/agent-skills
cd ~/path/to/agent-skills
./setup
```

Usage
-----

In Claude Code:

```
/agent-architect
```

In Codex, once installed under `~/.agents/skills`, reference `agent-architect` by name in your request.

The skill auto-detects your codebase and selects the appropriate mode. You can also be explicit:

```
/agent-architect audit this system
/agent-architect review this prompt: path/to/prompt.md
/agent-architect design a new agent for customer support
```

Adding New Skills
-----------------

Create a new directory with a `SKILL.md` file:

```
agent-skills/
├── agent-architect/SKILL.md    # existing
├── my-new-skill/SKILL.md       # new skill
└── setup                       # auto-discovers all */SKILL.md
```

Run `./setup` to register the new skill.
