---
id: 766
url: https://tailscale.com/blog/aperture-private-alpha
title: Aperture by Tailscale, an AI usage and access tool, now in alpha
domain: tailscale.com
source_date: '2026-01-27'
tags:
- ai
- llm
- security
- devops
summary: Tailscale has launched Aperture, an AI gateway in private alpha that provides
  organizations with visibility and control over coding agent usage without restricting
  developer access. Built on Tailscale's identity infrastructure, Aperture eliminates
  the need for API keys, supports all major LLM providers, and enables IT leaders
  to monitor AI adoption, costs, and usage patterns while maintaining security. The
  tool is extensible and designed to eventually support broader agentic AI workloads
  beyond coding agents.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# Aperture by Tailscale, an AI usage and access tool, now in alpha

[Blog](/blog)|productJanuary 27, 2026

A first look at Aperture by Tailscale (private alpha)
=====================================================

![Two screenshots of Aperture, one the Dashboard (in dark mode), floating in front of Logs, against a very light gray background, with blue shapes floating behind each of the screens. A Tailscale logo is in the upper-right corner.](https://cdn.sanity.io/images/w77i7m8x/production/5383452392390bbb0d8b54cbd4fe7c6cdf081957-2400x1260.png?w=3840&q=75&fit=clip&auto=format)

It’s understandable if you missed it, but coding agents are getting good [[^1]](#fn1). Throughout 2025 they went from interesting in limited circumstances, to nearly there, to being able to generate and review code at a surprisingly advanced level. As coding agents have been able to take on more and more complex tasks, it’s no surprise more and more folks want to bring them to work, even if their company’s tooling and policies are far from ready.

With growing interest in coding agents—not only from individual engineers, but also executives looking for force multipliers—security, IT, and engineering management are left with a difficult question: How can they enable secure, visible AI usage, without putting up roadblocks that engineers will work around?

We heard from countless customers that they don’t have a good answer to this. The thing is, neither did we. So we built one.

[Sign up for Aperture →](https://cta-service-cms2.hubspot.com/web-interactives/public/v1/track/redirect?encryptedPayload=AVxigLIi30sl%2F1M0ylNdKs%2Fpg5gaMvgrQgaw8Wy4j3IRR%2B8w%2FmsnnostWEQ4iDt6QMJmWXNBdl%2B0KDYXHuyPLbwfZOtkIa12DWVhRHhVoSWfWMFK2uV2twtd2uuK5Z7Ks9m9fNi8QThG9bvjYuJ7V3Ms3fcea0K4nTnRD9i7QXWXuvnaqbU%3D&webInteractiveContentId=206114498918&portalId=40004831)

[Bringing AI usage into focus with Aperture by Tailscale](#bringing-ai-usage-into-focus-with-aperture-by-tailscale)
-------------------------------------------------------------------------------------------------------------------

[Aperture](https://aperture.tailscale.com), currently in alpha release, is an AI gateway that provides visibility into coding agent usage across your entire organization without getting in the way of developers. It works great with most CLI or VS-Code-based AI coding tools, including Claude Code, Codex, Gemini CLI, and custom agent frameworks. It uses the underlying identity built into every Tailscale connection to eliminate distributing API keys to developer laptops, VMs, containers, CI/CD platforms (e.g. GitHub Actions), and other sandbox environments.

![A diagram with "Tailscale/Aperture" in the center, with four pieces flowing into it: "LLM API A," with a key icon near it; "LLM API O," with another key; "Autonomous Agent," with a "tag:pr-review-bot" icon underneath, and "Coding Agent," with "user:pangolin@" nearby. ](https://cdn.sanity.io/images/w77i7m8x/production/e24ebe3fc8dfe849850e97771044cae3eb0f34d7-1728x792.svg?w=3840&q=75&fit=clip&auto=format)

Any environment that can connect via Tailscale can use Aperture to eliminate keys and improve visibility. From an end-user perspective, setting up Aperture with an agent like Claude Code is as simple as adding the following to `~/.claude/settings.json`, either manually or via MDM:

```
{
  "apiKeyHelper": "echo '-'",
  "env": {
    "ANTHROPIC_BASE_URL": "http://ai"
  }
}
```

[Save time with just one key to rule them all](#save-time-with-just-one-key-to-rule-them-all)
---------------------------------------------------------------------------------------------

Giving developers or agents within your organization access to new models or providers is as simple as adding a single API key and endpoint to Aperture's settings. Once a new provider is added, Aperture associates user and machine identities with API usage, while transparently passing along traffic to the LLM provider.

![A screenshot of Tailscale/Aperture, showing the "Logs" section selected, with select users and metrics shown and tallied for: Requests, Input Tokens, Output Tokens, Cached, Reasoning, Tool Uses, Models, User, and Last Activity.](https://cdn.sanity.io/images/w77i7m8x/production/4bfdb8a0fe7209b0ee5fdde4acb27a5fd3493423-3248x1930.svg?w=3840&q=75&fit=clip&auto=format)

Since Aperture picks up identity information from your Tailscale network (tailnet), there is no need to set up user accounts or keys. Out of the gate, Aperture supports all major LLM providers using their native protocols, as well as most major cloud AI endpoints, self-hosted LLMs, and LLM inference providers that conform to the [OpenAI v1 response or chat completions](https://platform.openai.com/docs/api-reference/introduction) endpoint specifications.

[Make usage visible](#make-usage-visible)
-----------------------------------------

The visibility provided by Aperture can be used in two main ways. The first is to understand AI adoption across an organization. The second is to look for signs of compromised or unapproved usage of agents or tools.

### [Understand AI adoption and cost](#understand-ai-adoption-and-cost)

Models, agents, and AI usage best practices are constantly changing, and sometimes seemingly innocuous changes can have drastic impacts on tokens and, by extension, cost. By collecting usage information into a single place, engineering and IT leaders can get a complete picture into both user and agent token efficiency across the organization and providers.

![A bar chart graph, showing peaks and valleys of usage increasing over time. Users are charted at the bottom, "amelie@tailscale.com" and "pangolin@tailscale.com," with numbers for each: "Cached tokens," "Input tokens," "Output tokens," "Reasoning Tokens," and "Requests."](https://cdn.sanity.io/images/w77i7m8x/production/f3f6e5d22338753240d461141d84ef240a2ed8fe-3248x1930.svg?w=3840&q=75&fit=clip&auto=format)

### [Secure everything with simple access](#secure-everything-with-simple-access)

When users feel security postures are too cumbersome, they’ll work around them and end up out on their own, unmonitored and unprotected. When deployed, Aperture quickly becomes the *lowest-friction* way to access AI at your company, while seamlessly attaching existing machine and user identities to logs, sessions, local tool calls, and local or remote MCP tool calls. All information can be easily viewed, filtered, and sorted inside Aperture, while also exported to S3 for easy SIEM integration.

![A chart showing layered usage across days, with colored bands for tool call breakdowns by type for each session. One highlighted day, Jan 15, shows calls for "Bash," "Read," "Edit," "Grep," "TodoWrite," "Write," "Glob," "Task," "WebFetch," and "WebSearch," and "+6 more tools."](https://cdn.sanity.io/images/w77i7m8x/production/e513b474c05a4380907a1158faecbc06f13e0e36-3248x1930.svg?w=3840&q=75&fit=clip&auto=format)

[A platform on a platform](#a-platform-on-a-platform)
-----------------------------------------------------

While Aperture itself is built on the Tailscale platform to leverage the built-in identity and connectivity, we’re making Aperture extensible as well. As part of making the safe way of providing AI access the easy way, we’ve made Aperture extensible, so that any company can provide detailed AI agent security features on top of Aperture. One of the first companies we'll be partnering with is [Oso](https://www.osohq.com/), to provide additional visibility, controls, alerting, and auditing for AI agents.

![Oso Agent Dashboard, showing event volume over time, tools by risk score, and other statistics.](https://cdn.sanity.io/images/w77i7m8x/production/8ccb3817edab51cd751e96f23160a7bfc2fb998f-4498x2384.png?w=3840&q=75&fit=clip&auto=format)

Oso Agent Dashboard.

[Visibility into coding agents is just the beginning](#visibility-into-coding-agents-is-just-the-beginning)
-----------------------------------------------------------------------------------------------------------

In our initial alpha release of Aperture, we’ve focused mostly on providing security and insights for coding agent usage. But coding agents, we believe, are just the beginning of the proverbial agentic AI iceberg.

So in addition to expanding Aperture to cover more typical chat-UI-based use cases, we’re also planning support for other agentic workloads. Inside organizations there are tons of other processes beyond coding, waiting for their coding agent moment. And, Aperture will be there to provide the right visibility, control, convenience, and ease of use to make it happen.

[How to get started with Aperture](#how-to-get-started-with-aperture)
---------------------------------------------------------------------

Try it out today for free by [signing up here](https://aperture.tailscale.com/). Like the Tailscale Personal plan, Aperture comes with similar usage limits of 3 free users. However, it can be used on any plan type. If you are trying to safely deploy coding agents for 10s, 100s, or 1000s of engineers inside your organization or building internal agents, [sign up for the waitlist](https://aperture.tailscale.com/). We’d be happy to walk through your requirements and set you up with a dedicated instance of Aperture.

*Please keep in mind that this is an early alpha release of an experimental product. It’s still a work in progress, so pieces may be incomplete, features may change, and you may experience bugs. We’re sharing it to learn and gather feedback, so before using it in production, please talk to us.*

---

[1]: Look, they’re certainly not perfect, but if it’s been more than 6 months since you’ve tried Claude Code or Codex, I think you’ll be surprised as to how good they are now. I just recommend you start with a plan and iterate a bit to refine it before you ask it to start building something from scratch. [[Back ⤴︎](#backfrom1)]

Share

Author

![Remy Guercio](https://cdn.sanity.io/images/w77i7m8x/production/ff6a9084239f0cf846ccac30adb605705e852d79-512x512.jpg?w=1080&q=75&fit=clip&auto=format)Remy Guercio

Author

![Remy Guercio](https://cdn.sanity.io/images/w77i7m8x/production/ff6a9084239f0cf846ccac30adb605705e852d79-512x512.jpg?w=1080&q=75&fit=clip&auto=format)Remy Guercio

Share

Loading...
