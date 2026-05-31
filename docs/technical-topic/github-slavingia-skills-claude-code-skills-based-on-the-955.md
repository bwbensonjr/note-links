---
id: 955
url: https://github.com/slavingia/skills
title: 'GitHub - slavingia/skills: Claude Code skills based on The Minimalist Entrepreneur
  by Sahil Lavingia · GitHub'
domain: github.com
source_date: '2026-03-23'
tags:
- github-repo
- cli-tool
- nonfiction-book
summary: This GitHub repository provides Claude Code skills based on Sahil Lavingia's
  "The Minimalist Entrepreneur" book, offering a plugin that guides entrepreneurs
  through building a business sustainably. The plugin includes eight command-based
  skills—from finding community and validating ideas to pricing, marketing, and scaling—that
  follow the book's sequential framework of building a lean, profitable business.
  Users can install the plugin locally and use specific commands at different stages
  of their entrepreneurial journey to receive guidance aligned with minimalist business
  principles.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# GitHub - slavingia/skills: Claude Code skills based on The Minimalist Entrepreneur by Sahil Lavingia · GitHub

The Minimalist Entrepreneur — Claude Code Skills
================================================

Claude Code skills based on [The Minimalist Entrepreneur](https://www.minimalistentrepreneur.com/) by Sahil Lavingia.

Installation
------------

In Claude Code:

```
/plugin marketplace add slavingia/skills
/plugin install minimalist-entrepreneur
```

That's it — Claude Code will fetch the repo and register all 10 skills automatically.

Alternative: install from a local clone

```
git clone https://github.com/slavingia/skills.git ~/.claude/plugins/skills
```

Then in Claude Code:

```
/plugin marketplace add ~/.claude/plugins/skills
/plugin install minimalist-entrepreneur
```

Skills
------

| Skill | Command | When to use |
| --- | --- | --- |
| **Find Community** | `/find-community` | Looking for a business idea, trying to find your community |
| **Validate Idea** | `/validate-idea` | Testing if a business idea is worth pursuing |
| **MVP** | `/mvp` | Ready to build your first product, struggling with scope |
| **Processize** | `/processize` | Have a product idea, want to deliver value by hand before writing code |
| **First Customers** | `/first-customers` | Have a product, need to find your first 100 customers |
| **Pricing** | `/pricing` | Setting prices, considering price changes |
| **Marketing Plan** | `/marketing-plan` | Have product-market fit, ready to scale with content |
| **Grow Sustainably** | `/grow-sustainably` | Making decisions about spending, hiring, or scaling |
| **Company Values** | `/company-values` | Defining culture, preparing to hire |
| **Minimalist Review** | `/minimalist-review` | Gut-checking any business decision |

The Minimalist Entrepreneur Journey
-----------------------------------

The skills follow the book's progression:

1. **Community** — Start by finding your people
2. **Validate** — Make sure the problem is worth solving
3. **Build** — Ship a manual process, then productize it
4. **Processize** — Turn your product idea into a manual process you can deliver today
5. **Sell** — Get to 100 customers one by one
6. **Price** — Charge something from day one
7. **Market** — Build an audience through content
8. **Grow** — Stay profitable, grow sustainably
9. **Culture** — Build the house you want to live in
10. **Review** — Apply minimalist principles to every decision
