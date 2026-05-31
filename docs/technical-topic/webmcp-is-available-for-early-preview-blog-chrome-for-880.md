---
id: 880
url: https://developer.chrome.com/blog/webmcp-epp
title: WebMCP is available for early preview  |  Blog  |  Chrome for Developers
domain: developer.chrome.com
source_date: '2026-03-01'
tags:
- ai
- web-dev
- javascript
summary: WebMCP is a new standard being introduced by Chrome that enables websites
  to define structured tools and interactions for AI agents, allowing them to perform
  actions on sites more reliably and efficiently. The platform offers two APIs—a Declarative
  API for standard HTML form actions and an Imperative API for complex JavaScript-based
  interactions—making websites "agent-ready" for tasks like customer support, e-commerce
  transactions, and travel bookings. Chrome is now accepting early preview program
  participants to help prototype and test the technology.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# WebMCP is available for early preview  |  Blog  |  Chrome for Developers

* [Chrome for Developers](https://developer.chrome.com/)
* [Blog](https://developer.chrome.com/blog)

WebMCP is available for early preview


Stay organized with collections

Save and categorize content based on your preferences.
===============================================================================================================================



![André Cipriani Bandarra](https://web.dev/images/authors/andreban.jpg)

André Cipriani Bandarra

[X](https://twitter.com/andreban)
[GitHub](https://github.com/andreban)
[Mastodon](https://mastodon.social/@andreban)
[Bluesky](https://bsky.app/profile/bandarra.me)
[Homepage](https://bandarra.me)

Published: February 10, 2026

As the agentic web evolves, we want to help websites play an active role in how AI agents interact with them. WebMCP aims to provide a standard way for exposing structured tools, ensuring AI agents can perform actions on your site with increased speed, reliability, and precision.

By defining these tools, you tell agents how and where to interact with your site, whether it's booking a flight, filing a support ticket, or navigating complex data. This direct communication channel eliminates ambiguity and allows for faster, more robust agent workflows.

Structured interactions for the agentic web
-------------------------------------------

WebMCP proposes two new APIs that allow browser agents to take action on behalf of the user:

* **Declarative API**: Perform standard actions that can be defined directly in HTML forms.
* **Imperative API**: Perform complex, more dynamic interactions that require JavaScript execution.

These APIs serve as a bridge, making your website "agent-ready" and enabling more reliable and performant agent workflows compared to raw DOM actuation.

Use cases
---------

Imagine an agent that can handle complex tasks for your users with confidence and speed.

* **Customer support**: Help users create detailed customer support tickets, by enabling agents to fill in all of the necessary technical details automatically.
* **Ecommerce**: Users can better shop your products when agents can easily find what they're looking for, configure particular shopping options, and navigate checkout flows with precision.
* **Travel**: Users could more easily get the exact flights they want, by allowing the agent to search, filter results, and handle bookings using structured data to ensure accurate results every time.

Join the early preview program
------------------------------

WebMCP is available for prototyping to early preview program participants.

Sign up for the [early preview program](/docs/ai/join-epp) to gain access to the documentation and demos, stay up-to-date with the latest changes, and discover new APIs.
