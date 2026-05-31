---
id: 148
url: https://www.claude.com/blog/structured-outputs-on-the-claude-developer-platform
title: Structured outputs on the Claude Developer Platform | Claude
domain: www.claude.com
source_date: '2025-11-14'
tags:
- llm
- web-dev
- cli-tool
summary: Anthropic has launched structured outputs for the Claude Developer Platform,
  now available in public beta for Claude Sonnet 4.5 and Opus 4.1. This feature guarantees
  that API responses match specified JSON schemas or tool definitions, eliminating
  parsing errors and failed tool calls while improving reliability for production
  applications. The capability is particularly valuable for data extraction, multi-agent
  architectures, and complex workflows where consistent, error-free formatting is
  critical.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# Structured outputs on the Claude Developer Platform | Claude

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d223de65e7dcca8267d8_ea364001be6bf6d2e86b58109ead6a779d5771a7-1000x1000.svg)

Structured outputs on the Claude Developer Platform
===================================================

Guarantee responses match your JSON schemas and tool definitions with structured outputs.

* Category

  [Product announcements](https://claude.com/blog/category/announcements)
* Product

  Claude Platform
* Date

  November 14, 2025
* Reading time

  5

  min
* Share

  [Copy link](#)

  https://claude.com/blog/structured-outputs-on-the-claude-developer-platform

***Update:*** *Now generally available (GA) natively on the Claude Developer Platform and in Amazon Bedrock for Claude Sonnet 4.5, Opus 4.5, and Haiku 4.5. GA adds support for more complex schemas. (Feb 4, 2026)*

***Update:*** *Now available on Claude Haiku 4.5—supported on the Claude Developer Platform, natively and in Microsoft Foundry. (Dec 4, 2025)*

The Claude Developer Platform now supports structured outputs for Claude Sonnet 4.5 and Opus 4.1. Available in public beta, this feature ensures API responses always match your specified JSON schemas or tool definitions.

With structured outputs, developers can eliminate schema-related parsing errors and failed tool calls by ensuring that Claude's responses conform to a defined schema—whether you're extracting data from images, orchestrating agents, or integrating with external APIs.

### Building reliable applications

For developers building applications and agents in production, a single error in data formatting can cause cascading failures. Structured outputs solves this by guaranteeing your response matches the exact structure you define, without any impact to model performance. This makes Claude dependable for applications and agents where accuracy is critical, including:

* **Data extraction** when downstream systems rely on error-free, consistent formats.
* **Multi-agent architectures** where consistent communication between agents is critical for a performant, stable experience.
* **Complex search tools** where multiple search fields must be filled in accurately and conform to specific patterns.

Structured outputs can be used two ways: with JSON or tools. When used with JSON, you provide your schema definition in the API request. For tools, you define your tool specifications, and Claude's output conforms to those tool definitions automatically.

The end result is a reliable output, reduced retries, and a simplified codebase that no longer needs failover logic or complex error handling.

### Customer Spotlight: OpenRouter

OpenRouter provides 4M+ developers access to all major AI models through a single, unified interface.

"Structured outputs have become a really valuable part of the agentic AI stack. Agents constantly ingest and produce structured data, so Anthropic’s structured outputs close a real gap for developers. Agent workflows run reliably, every time, and teams can focus on their customers rather than debugging tool calls,” said Chris Clark, COO, OpenRouter.

### Getting started

Structured outputs is now available in public beta for Sonnet 4.5 and Opus 4.1 on the Claude Developer Platform, with support for Haiku 4.5 coming soon. Explore our [documentation](https://docs.claude.com/en/docs/build-with-claude/structured-outputs) for supported JSON schema types, implementation examples, and best practices.

No items found.

[Prev](#)Prev

0/5

[Next](#)Next

eBook

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

FAQ

No items found.

Related posts
-------------

Explore more product news and best practices for teams building with Claude.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d223de65e7dcca8267d8_ea364001be6bf6d2e86b58109ead6a779d5771a7-1000x1000.svg)

May 28, 2026

### Introducing dynamic workflows in Claude Code

Product announcements

[Introducing dynamic workflows in Claude Code](#)Introducing dynamic workflows in Claude Code

[Introducing dynamic workflows in Claude Code](/blog/introducing-dynamic-workflows-in-claude-code)Introducing dynamic workflows in Claude Code

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/690937bee860a953417a8eee_Object-CodeBrowserGlobe.svg)

May 26, 2026

### Code w/ Claude London 2026: Rethinking how we build

Product announcements

[Code w/ Claude London 2026: Rethinking how we build](#)Code w/ Claude London 2026: Rethinking how we build

[Code w/ Claude London 2026: Rethinking how we build](/blog/code-w-claude-london-2026-rethinking-how-we-build)Code w/ Claude London 2026: Rethinking how we build

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22bed4b18b6703cd710_e750c875fbd7f08ffb6495efa180a8ed60de3611-1000x1000.svg)

May 19, 2026

### New in Claude Managed Agents: self-hosted sandboxes and MCP tunnels

Product announcements

[New in Claude Managed Agents: self-hosted sandboxes and MCP tunnels](#)New in Claude Managed Agents: self-hosted sandboxes and MCP tunnels

[New in Claude Managed Agents: self-hosted sandboxes and MCP tunnels](/blog/claude-managed-agents-updates)New in Claude Managed Agents: self-hosted sandboxes and MCP tunnels

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22e13864f88ea55c2d8_b5c98d26c46edc43193e7f7e28a00633a538bb9c-1000x1000.svg)

May 12, 2026

### Code w/ Claude SF 2026 recap: Building on the AI exponential

Product announcements

[Code w/ Claude SF 2026 recap: Building on the AI exponential](#) Code w/ Claude SF 2026 recap: Building on the AI exponential

[Code w/ Claude SF 2026 recap: Building on the AI exponential](/blog/code-w-claude-sf-2026-sf) Code w/ Claude SF 2026 recap: Building on the AI exponential

Transform how your organization operates with Claude
----------------------------------------------------

See pricing

[See pricing](https://claude.com/pricing#api)See pricing

Contact sales

[Contact sales](https://claude.com/contact-sales)Contact sales

Get the developer newsletter

Product updates, how-tos, community spotlights, and more. Delivered monthly to your inbox.

Thank you! You’re subscribed.

Sorry, there was a problem with your submission, please try again later.
