---
id: 790
url: https://agentskills.io/home
title: Overview - Agent Skills
domain: agentskills.io
source_date: '2026-02-04'
tags:
- ai
- llm
- github-repo
summary: Agent Skills are packages of instructions, scripts, and resources that enable
  AI agents to work more accurately and efficiently by providing them with procedural
  knowledge and contextual information they can access on demand. The platform allows
  skill authors to build capabilities once and deploy them across multiple agent products,
  while enabling teams and enterprises to capture organizational knowledge in portable,
  version-controlled packages that support domain expertise, new capabilities, and
  repeatable workflows. Agent Skills is an open standard originally developed by Anthropic
  that is supported by leading AI development tools and remains open for contributions
  from the broader ecosystem.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# Overview - Agent Skills

> Documentation Index
> -------------------
>
> Fetch the complete documentation index at: <https://agentskills.io/llms.txt>
>
> Use this file to discover all available pages before exploring further.

[​](#what-are-agent-skills) What are Agent Skills?
--------------------------------------------------

Agent Skills are a lightweight, open format for extending AI agent capabilities with specialized knowledge and workflows.
At its core, a skill is a folder containing a `SKILL.md` file. This file includes metadata (`name` and `description`, at minimum) and instructions that tell an agent how to perform a specific task. Skills can also bundle scripts, reference materials, templates, and other resources.

```
my-skill/
├── SKILL.md          # Required: metadata + instructions
├── scripts/          # Optional: executable code
├── references/       # Optional: documentation
├── assets/           # Optional: templates, resources
└── ...               # Any additional files or directories
```

[​](#why-agent-skills) Why Agent Skills?
----------------------------------------

Agents are increasingly capable, but often don’t have the context they need to do real work reliably. Skills solve this by packaging procedural knowledge and company-, team-, and user-specific context into portable, version-controlled folders that agents load on demand. This gives agents:

* **Domain expertise**: Capture specialized knowledge — from legal review processes to data analysis pipelines to presentation formatting — as reusable instructions and resources.
* **Repeatable workflows**: Turn multi-step tasks into consistent, auditable procedures.
* **Cross-product reuse**: Build a skill once and use it across any skills-compatible agent.

[​](#how-do-agent-skills-work) How do Agent Skills work?
--------------------------------------------------------

Agents load skills through **progressive disclosure**, in three stages:

1. **Discovery**: At startup, agents load only the name and description of each available skill, just enough to know when it might be relevant.
2. **Activation**: When a task matches a skill’s description, the agent reads the full `SKILL.md` instructions into context.
3. **Execution**: The agent follows the instructions, optionally executing bundled code or loading referenced files as needed.

Full instructions load only when a task calls for them, so agents can keep many skills on hand with only a small context footprint.

[​](#where-can-i-use-agent-skills) Where can I use Agent Skills?
----------------------------------------------------------------

Agent Skills are supported by a large number of AI tools and agentic clients — see the [Client Showcase](/clients) to explore some of them!


[​](#open-development) Open development
---------------------------------------

The Agent Skills format was originally developed by [Anthropic](https://www.anthropic.com/), released as an open standard, and has been adopted by a growing number of agent products. The standard is open to contributions from the broader ecosystem.
Come join the discussion on [GitHub](https://github.com/agentskills/agentskills) or [Discord](https://discord.gg/MKPE9g8aUy)!

[​](#get-started-with-agent-skills) Get started with Agent Skills
-----------------------------------------------------------------

Quickstart
----------

Create your first Agent Skill and see it in action.

Specification
-------------

The complete format specification for Agent Skills.

[Specification](/specification)

⌘I
