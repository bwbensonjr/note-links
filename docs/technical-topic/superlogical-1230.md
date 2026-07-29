---
id: 1230
url: https://www.superlogical.com/
title: Superlogical
domain: www.superlogical.com
source_date: '2026-07-29'
tags:
- cli-tool
- devops
- distributed-systems
- github-repo
summary: Superlogical, Mitchell Hashimoto's new company, is building a universal multiplexer
  designed to unify fragmented work environments by consolidating local development,
  remote access, coding agents, production applications, and human-machine collaboration
  into a single cohesive system. The team is starting with a modern terminal multiplexer
  that features web and native app access, built-in session sharing, and improved
  usability, with plans to eventually expand into a comprehensive platform that bridges
  interactive work, automated processes, and production systems. The company is backed
  by notable investors and aims to address the growing complexity created by AI and
  the historical separation of development, operations, and infrastructure tools.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# Superlogical

We are building the multiplexer for all work.all work.local development.remote access.coding agents.background jobs.production applications.live debuggingsandboxes.shared terminals.incident response.humans and machines.operational history.multiplayer work.all work.
=========================================================================================================================================================================================================================================================================

Building and operating software today spans local machines, remote hosts, sandboxes, services,
and production systems. It has many modes of operation: interactively with a human developer,
automatically through CI and background processes, and increasingly through agents working in
parallel.

This work is all related, yet today's tools divide it into separate systems. Interactive tools
assume a person at an interface. Automatic work disappears into jobs and logs. And as the work
moves to production it lives behind separate systems and controls.

AI makes this fragmentation more visible and costly, but it did not create it. System
administration, continuous integration, remote development and collaboration have strained the
same boundaries for decades.

We believe the missing layer is a durable session around the work itself: one that can span
applications and environments, provide relevant context by default, expose structured data and
actions, preserve history, and be driven by software while remaining visible and controllable
by people.

What we're building

This is our plan to build a multiplexer for all work:

1. 1 Build an incredible multiplexer.
2. 2 Make everything in it composable.
3. 3 Make it safe and operable in production.

A multiplexer brings multiple independent streams together through a common interface. For us,
that means interactive work, automatic work, and production work would share one well-crafted
underlying system instead of living in separate tools.

We'll begin with a terminal multiplexer. It keeps multiple terminal blocks organized inside a
long-lived session, so you can close the application, reconnect from another device, and pick
up exactly where you left off.

If you're already familiar with terminal multiplexers, you'll feel right at home, but we're
bringing a more modern touch. Sessions can be accessed through the web and native macOS/iOS
applications, and sharing a live session with other people is built in from the start. We're
also addressing the most common papercuts of existing tools, such as making scrollback,
selection, and scrolling all work natively.

A terminal multiplexer may sound like a narrow place to start a company. Our vision is much
larger, but terminals connect developers, agents, tools, and infrastructure so it is the right
foundation for everything that follows. We will build a high-quality terminal multiplexer that
remains excellent at that job, even as it grows to support the second and third parts of the
plan. We'll have more to say about those later.

Who we are

We're a team that has spent our entire careers building some of the most widely used developer
tooling, infrastructure software, and AI systems. We care deeply about well-crafted software
that is beautiful to use, reliable in practice, and designed for others to build on.

* ![](/headshots/mitchell-hashimoto.webp?v=1785240917834)

  ### [Mitchell Hashimoto](https://mitchellh.com)

  Creator of Ghostty. Co-founded HashiCorp and created Vagrant, Terraform, Vault, and more. Spent more than a decade as CEO and CTO from its earliest days through its IPO.
* ![](/headshots/jack-pearkes.webp?v=1785259397211)

  ### [Jack Pearkes](https://www.jackpearkes.com)

  VP of Engineering and VP of R&D at HashiCorp, and its very first employee. Helped to create HashiCorp's first products and hired and led the original engineering team.
* ![](/headshots/alasdair-monk.webp?v=1785242648177)

  ### [Alasdair Monk](https://www.alasdairmonk.com)

  Head of Experience at Poolside, VP of Design at Vercel, and a senior design leader at HashiCorp and Heroku. Two decades spent designing and building interfaces for developers.
* ![](/headshots/hector-simpson.webp?v=1785240917834)

  ### [Hector Simpson](https://hector.me)

  Designed apps, services, and agentic experiences at Poolside. An interface designer and builder who has shipped developer-first products at Heroku, HashiCorp, Clearbit, and Vercel.

Superlogical is funded by:

* [Notable Capital](https://www.notablecap.com)
* [Amplify Partners](https://amplifypartners.com)
* [Aaron Levie](https://x.com/levie)
* [Armon Dadgar](https://x.com/armon)
* [Dax Raad](https://x.com/thdxr)
* [Greg Foster](https://x.com/gregfoster996)
* [Guillermo Rauch](https://x.com/rauchg)
* [Jacob Thornton](https://x.com/fat)
* [Mario Zechner](https://x.com/badlogicgames)
* [Merrill Lutsky](https://x.com/merrilllutsky)
* [Patrick Collison](https://x.com/patrickc)
* [Stephen Haney](https://x.com/stephenhaney)
* [Steve Ruiz](https://x.com/steveruizok)
* [Tobias Lütke](https://x.com/tobi)
* [Tomas Reimers](https://x.com/tomasreimers)

Get on the list for our first release

We'll let you know when our beta for the terminal multiplexer is available, and any
OSS releases along the way.
