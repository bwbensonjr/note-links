---
id: 1240
url: https://github.com/humanlayer/12-factor-agents
title: 'GitHub - humanlayer/12-factor-agents: What are the principles we can use to
  build LLM-powered software that is actually good enough to put in the hands of production
  customers? · GitHub'
domain: github.com
source_date: '2026-07-24'
tags:
- github-repo
- llm
- ai
- devops
summary: This GitHub project presents "12-Factor Agents," a set of principles for
  building reliable, production-ready LLM-powered applications inspired by the 12-factor
  app methodology. The author argues that most AI agent frameworks fail to reach production
  quality because they rely too heavily on the "prompt + tools + loop" pattern, and
  instead advocates for incorporating small, modular agent-building concepts into
  existing products rather than adopting monolithic frameworks. The 12 factors provide
  practical engineering techniques to make LLM software more reliable, scalable, and
  maintainable—ranging from owning prompts and context windows to implementing human
  contact mechanisms and stateless reducer patterns.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# GitHub - humanlayer/12-factor-agents: What are the principles we can use to build LLM-powered software that is actually good enough to put in the hands of production customers? · GitHub

12-Factor Agents - Principles for building reliable LLM applications
====================================================================

[![Code License: Apache 2.0](https://camo.githubusercontent.com/ca34f9d4db9ab9f34416e899ff805504820e1b798ea511881859e82eabc2488d/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f436f64652d417061636865253230322e302d626c75652e737667)](https://www.apache.org/licenses/LICENSE-2.0)
[![Content License: CC BY-SA 4.0](https://camo.githubusercontent.com/e96ba20d4ad3391c17fd32a72efa44a1c9b55ea9daf65f3991e4edc1a194d504/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f436f6e74656e742d434325323042592d2d5341253230342e302d6c69676874677265792e737667)](https://creativecommons.org/licenses/by-sa/4.0/)
[![Discord Server](https://camo.githubusercontent.com/e9cd644682259047523514c2968835aca35c9529c76a3f36eb85e7cb57d8d624/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f636861742d646973636f72642d353836354632)](https://humanlayer.dev/discord)
[![YouTube
Deep Dive](https://camo.githubusercontent.com/6c112d2088c809e72887f779f27623a10f1b8647cfaa848c9184d9889278c07b/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6169646f74656e67696e6565722d636f6e665f74616c6b5f2831376d292d7768697465)](https://www.youtube.com/watch?v=8kMaTybvDUw)
[![YouTube
Deep Dive](https://camo.githubusercontent.com/1774ff77c6a8df66b41e1bed843fb53a3d8d1e23fb495895d44945c8d88434ed/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f796f75747562652d646565705f646976652d6372696d736f6e)](https://www.youtube.com/watch?v=yxJDyQ8v6P0)

*In the spirit of [12 Factor Apps](https://12factor.net/)*. *The source for this project is public at <https://github.com/humanlayer/12-factor-agents>, and I welcome your feedback and contributions. Let's figure this out together!*

Tip

Missed the AI Engineer World's Fair? [Catch the talk here](https://www.youtube.com/watch?v=8kMaTybvDUw)

Looking for Context Engineering? [Jump straight to factor 3](https://github.com/humanlayer/12-factor-agents/blob/main/content/factor-03-own-your-context-window.md)

Want to contribute to `npx/uvx create-12-factor-agent` - check out [the discussion thread](https://github.com/humanlayer/12-factor-agents/discussions/61)

[![](https://camo.githubusercontent.com/118510b0c1b6853f572787d983136d3858b1afd41bae236a59d5ba1c56b4c5f3/68747470733a2f2f7374617469632e73636172662e73682f612e706e673f782d707869643d32616361643939612d633264392d343864662d383666352d396361383036316237626639)](https://camo.githubusercontent.com/118510b0c1b6853f572787d983136d3858b1afd41bae236a59d5ba1c56b4c5f3/68747470733a2f2f7374617469632e73636172662e73682f612e706e673f782d707869643d32616361643939612d633264392d343864662d383666352d396361383036316237626639)

[![Screenshot 2025-04-03 at 2 49 07 PM](https://private-user-images.githubusercontent.com/3730605/430151074-23286ad8-7bef-4902-b371-88ff6a22e998.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3ODUzNDY4NDAsIm5iZiI6MTc4NTM0NjU0MCwicGF0aCI6Ii8zNzMwNjA1LzQzMDE1MTA3NC0yMzI4NmFkOC03YmVmLTQ5MDItYjM3MS04OGZmNmEyMmU5OTgucG5nP1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQVZDT0RZTFNBNTNQUUs0WkElMkYyMDI2MDcyOSUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyNjA3MjlUMTczNTQwWiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9MTc3M2RmMDQyMmIyZTZiOTIzY2VlNDZjZWY3NTdiYzljNTVlYTlhZThiM2U5M2IzZWI0M2E0YmI4YmExOWM0YiZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QmcmVzcG9uc2UtY29udGVudC10eXBlPWltYWdlJTJGcG5nIn0.ojepbeFgi9mMZdxjv93GEfa6INbqWjb7kqXmSVyHWos)](#visual-nav)

Hi, I'm Dex. I've been [hacking](https://youtu.be/8bIHcttkOTE) on [AI agents](https://theouterloop.substack.com) for [a while](https://humanlayer.dev).

**I've tried every agent framework out there**, from the plug-and-play crew/langchains to the "minimalist" smolagents of the world to the "production grade" langraph, griptape, etc.

**I've talked to a lot of really strong founders**, in and out of YC, who are all building really impressive things with AI. Most of them are rolling the stack themselves. I don't see a lot of frameworks in production customer-facing agents.

**I've been surprised to find** that most of the products out there billing themselves as "AI Agents" are not all that agentic. A lot of them are mostly deterministic code, with LLM steps sprinkled in at just the right points to make the experience truly magical.

Agents, at least the good ones, don't follow the ["here's your prompt, here's a bag of tools, loop until you hit the goal"](https://www.anthropic.com/engineering/building-effective-agents#agents) pattern. Rather, they are comprised of mostly just software.

So, I set out to answer:

> ### **What are the principles we can use to build LLM-powered software that is actually good enough to put in the hands of production customers?**

Welcome to 12-factor agents. As every Chicago mayor since Daley has consistently plastered all over the city's major airports, we're glad you're here.

*Special thanks to [@iantbutler01](https://github.com/iantbutler01), [@tnm](https://github.com/tnm), [@hellovai](https://www.github.com/hellovai), [@stantonk](https://www.github.com/stantonk), [@balanceiskey](https://www.github.com/balanceiskey), [@AdjectiveAllison](https://www.github.com/AdjectiveAllison), [@pfbyjy](https://www.github.com/pfbyjy), [@a-churchill](https://www.github.com/a-churchill), and the SF MLOps community for early feedback on this guide.*

The Short Version: The 12 Factors
---------------------------------

Even if LLMs [continue to get exponentially more powerful](https://github.com/humanlayer/12-factor-agents/blob/main/content/factor-10-small-focused-agents.md#what-if-llms-get-smarter), there will be core engineering techniques that make LLM-powered software more reliable, more scalable, and easier to maintain.

* [How We Got Here: A Brief History of Software](https://github.com/humanlayer/12-factor-agents/blob/main/content/brief-history-of-software.md)
* [Factor 1: Natural Language to Tool Calls](https://github.com/humanlayer/12-factor-agents/blob/main/content/factor-01-natural-language-to-tool-calls.md)
* [Factor 2: Own your prompts](https://github.com/humanlayer/12-factor-agents/blob/main/content/factor-02-own-your-prompts.md)
* [Factor 3: Own your context window](https://github.com/humanlayer/12-factor-agents/blob/main/content/factor-03-own-your-context-window.md)
* [Factor 4: Tools are just structured outputs](https://github.com/humanlayer/12-factor-agents/blob/main/content/factor-04-tools-are-structured-outputs.md)
* [Factor 5: Unify execution state and business state](https://github.com/humanlayer/12-factor-agents/blob/main/content/factor-05-unify-execution-state.md)
* [Factor 6: Launch/Pause/Resume with simple APIs](https://github.com/humanlayer/12-factor-agents/blob/main/content/factor-06-launch-pause-resume.md)
* [Factor 7: Contact humans with tool calls](https://github.com/humanlayer/12-factor-agents/blob/main/content/factor-07-contact-humans-with-tools.md)
* [Factor 8: Own your control flow](https://github.com/humanlayer/12-factor-agents/blob/main/content/factor-08-own-your-control-flow.md)
* [Factor 9: Compact Errors into Context Window](https://github.com/humanlayer/12-factor-agents/blob/main/content/factor-09-compact-errors.md)
* [Factor 10: Small, Focused Agents](https://github.com/humanlayer/12-factor-agents/blob/main/content/factor-10-small-focused-agents.md)
* [Factor 11: Trigger from anywhere, meet users where they are](https://github.com/humanlayer/12-factor-agents/blob/main/content/factor-11-trigger-from-anywhere.md)
* [Factor 12: Make your agent a stateless reducer](https://github.com/humanlayer/12-factor-agents/blob/main/content/factor-12-stateless-reducer.md)

### Visual Nav

|  |  |  |
| --- | --- | --- |
| [factor 1](https://github.com/humanlayer/12-factor-agents/blob/main/content/factor-01-natural-language-to-tool-calls.md) | [factor 2](https://github.com/humanlayer/12-factor-agents/blob/main/content/factor-02-own-your-prompts.md) | [factor 3](https://github.com/humanlayer/12-factor-agents/blob/main/content/factor-03-own-your-context-window.md) |
| [factor 4](https://github.com/humanlayer/12-factor-agents/blob/main/content/factor-04-tools-are-structured-outputs.md) | [factor 5](https://github.com/humanlayer/12-factor-agents/blob/main/content/factor-05-unify-execution-state.md) | [factor 6](https://github.com/humanlayer/12-factor-agents/blob/main/content/factor-06-launch-pause-resume.md) |
| [factor 7](https://github.com/humanlayer/12-factor-agents/blob/main/content/factor-07-contact-humans-with-tools.md) | [factor 8](https://github.com/humanlayer/12-factor-agents/blob/main/content/factor-08-own-your-control-flow.md) | [factor 9](https://github.com/humanlayer/12-factor-agents/blob/main/content/factor-09-compact-errors.md) |
| [factor 10](https://github.com/humanlayer/12-factor-agents/blob/main/content/factor-10-small-focused-agents.md) | [factor 11](https://github.com/humanlayer/12-factor-agents/blob/main/content/factor-11-trigger-from-anywhere.md) | [factor 12](https://github.com/humanlayer/12-factor-agents/blob/main/content/factor-12-stateless-reducer.md) |

How we got here
---------------

For a deeper dive on my agent journey and what led us here, check out [A Brief History of Software](https://github.com/humanlayer/12-factor-agents/blob/main/content/brief-history-of-software.md) - a quick summary here:

### The promise of agents

We're gonna talk a lot about Directed Graphs (DGs) and their Acyclic friends, DAGs. I'll start by pointing out that...well...software is a directed graph. There's a reason we used to represent programs as flow charts.

[![010-software-dag](https://github.com/humanlayer/12-factor-agents/raw/main/img/010-software-dag.png)](https://github.com/humanlayer/12-factor-agents/blob/main/img/010-software-dag.png)

### From code to DAGs

Around 20 years ago, we started to see DAG orchestrators become popular. We're talking classics like [Airflow](https://airflow.apache.org/), [Prefect](https://www.prefect.io/), some predecessors, and some newer ones like ([dagster](https://dagster.io/), [inggest](https://www.inngest.com/), [windmill](https://www.windmill.dev/)). These followed the same graph pattern, with the added benefit of observability, modularity, retries, administration, etc.

[![015-dag-orchestrators](https://github.com/humanlayer/12-factor-agents/raw/main/img/015-dag-orchestrators.png)](https://github.com/humanlayer/12-factor-agents/blob/main/img/015-dag-orchestrators.png)

### The promise of agents

I'm not the first [person to say this](https://youtu.be/Dc99-zTMyMg?si=bcT0hIwWij2mR-40&t=73), but my biggest takeaway when I started learning about agents, was that you get to throw the DAG away. Instead of software engineers coding each step and edge case, you can give the agent a goal and a set of transitions:

[![025-agent-dag](https://github.com/humanlayer/12-factor-agents/raw/main/img/025-agent-dag.png)](https://github.com/humanlayer/12-factor-agents/blob/main/img/025-agent-dag.png)

And let the LLM make decisions in real time to figure out the path

[![026-agent-dag-lines](https://github.com/humanlayer/12-factor-agents/raw/main/img/026-agent-dag-lines.png)](https://github.com/humanlayer/12-factor-agents/blob/main/img/026-agent-dag-lines.png)

The promise here is that you write less software, you just give the LLM the "edges" of the graph and let it figure out the nodes. You can recover from errors, you can write less code, and you may find that LLMs find novel solutions to problems.

### Agents as loops

As we'll see later, it turns out this doesn't quite work.

Let's dive one step deeper - with agents you've got this loop consisting of 3 steps:

1. LLM determines the next step in the workflow, outputting structured json ("tool calling")
2. Deterministic code executes the tool call
3. The result is appended to the context window
4. Repeat until the next step is determined to be "done"

```
initial_event = {"message": "..."}
context = [initial_event]
while True:
  next_step = await llm.determine_next_step(context)
  context.append(next_step)

  if (next_step.intent === "done"):
    return next_step.final_answer

  result = await execute_step(next_step)
  context.append(result)
```

Our initial context is just the starting event (maybe a user message, maybe a cron fired, maybe a webhook, etc), and we ask the llm to choose the next step (tool) or to determine that we're done.

Here's a multi-step example:

027-agent-loop-animation.mp4

[
](https://private-user-images.githubusercontent.com/3730605/428690858-3beb0966-fdb1-4c12-a47f-ed4e8240f8fd.mp4?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3ODUzNDY4NDAsIm5iZiI6MTc4NTM0NjU0MCwicGF0aCI6Ii8zNzMwNjA1LzQyODY5MDg1OC0zYmViMDk2Ni1mZGIxLTRjMTItYTQ3Zi1lZDRlODI0MGY4ZmQubXA0P1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQVZDT0RZTFNBNTNQUUs0WkElMkYyMDI2MDcyOSUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyNjA3MjlUMTczNTQwWiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9OTlkNWMzOWZhNjEwMTkzYWJlZjE3MGViNTA1ZmRmNTRhNTc2Y2Y0N2UxZGU1NzJmNzI0MGMyYmYzN2NmNmRjMSZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QmcmVzcG9uc2UtY29udGVudC10eXBlPXZpZGVvJTJGbXA0In0.fJAdKenJSN00WpOco5hb2jhPCI3MYmhsdL3qKptMVCQ)

[GIF Version](https://github.com/humanlayer/12-factor-agents/blob/main/img/027-agent-loop-animation.gif)

[![027-agent-loop-animation](https://github.com/humanlayer/12-factor-agents/raw/main/img/027-agent-loop-animation.gif)](https://github.com/humanlayer/12-factor-agents/blob/main/img/027-agent-loop-animation.gif)

Why 12-factor agents?
---------------------

At the end of the day, this approach just doesn't work as well as we want it to.

In building HumanLayer, I've talked to at least 100 SaaS builders (mostly technical founders) looking to make their existing product more agentic. The journey usually goes something like:

1. Decide you want to build an agent
2. Product design, UX mapping, what problems to solve
3. Want to move fast, so grab $FRAMEWORK and *get to building*
4. Get to 70-80% quality bar
5. Realize that 80% isn't good enough for most customer-facing features
6. Realize that getting past 80% requires reverse-engineering the framework, prompts, flow, etc.
7. Start over from scratch

Random Disclaimers

**DISCLAIMER**: I'm not sure the exact right place to say this, but here seems as good as any: **this in BY NO MEANS meant to be a dig on either the many frameworks out there, or the pretty dang smart people who work on them**. They enable incredible things and have accelerated the AI ecosystem.

I hope that one outcome of this post is that agent framework builders can learn from the journeys of myself and others, and make frameworks even better.

Especially for builders who want to move fast but need deep control.

**DISCLAIMER 2**: I'm not going to talk about MCP. I'm sure you can see where it fits in.

**DISCLAIMER 3**: I'm using mostly typescript, for [reasons](https://www.linkedin.com/posts/dexterihorthy_llms-typescript-aiagents-activity-7290858296679313408-Lh9e?utm_source=share&utm_medium=member_desktop&rcm=ACoAAA4oHTkByAiD-wZjnGsMBUL_JT6nyyhOh30) but all this stuff works in python or any other language you prefer.

Anyways back to the thing...

### Design Patterns for great LLM applications

After digging through hundreds of AI libriaries and working with dozens of founders, my instinct is this:

1. There are some core things that make agents great
2. Going all in on a framework and building what is essentially a greenfield rewrite may be counter-productive
3. There are some core principles that make agents great, and you will get most/all of them if you pull in a framework
4. BUT, the fastest way I've seen for builders to get high-quality AI software in the hands of customers is to take small, modular concepts from agent building, and incorporate them into their existing product
5. These modular concepts from agents can be defined and applied by most skilled software engineers, even if they don't have an AI background

> #### The fastest way I've seen for builders to get good AI software in the hands of customers is to take small, modular concepts from agent building, and incorporate them into their existing product

The 12 Factors (again)
----------------------

* [How We Got Here: A Brief History of Software](https://github.com/humanlayer/12-factor-agents/blob/main/content/brief-history-of-software.md)
* [Factor 1: Natural Language to Tool Calls](https://github.com/humanlayer/12-factor-agents/blob/main/content/factor-01-natural-language-to-tool-calls.md)
* [Factor 2: Own your prompts](https://github.com/humanlayer/12-factor-agents/blob/main/content/factor-02-own-your-prompts.md)
* [Factor 3: Own your context window](https://github.com/humanlayer/12-factor-agents/blob/main/content/factor-03-own-your-context-window.md)
* [Factor 4: Tools are just structured outputs](https://github.com/humanlayer/12-factor-agents/blob/main/content/factor-04-tools-are-structured-outputs.md)
* [Factor 5: Unify execution state and business state](https://github.com/humanlayer/12-factor-agents/blob/main/content/factor-05-unify-execution-state.md)
* [Factor 6: Launch/Pause/Resume with simple APIs](https://github.com/humanlayer/12-factor-agents/blob/main/content/factor-06-launch-pause-resume.md)
* [Factor 7: Contact humans with tool calls](https://github.com/humanlayer/12-factor-agents/blob/main/content/factor-07-contact-humans-with-tools.md)
* [Factor 8: Own your control flow](https://github.com/humanlayer/12-factor-agents/blob/main/content/factor-08-own-your-control-flow.md)
* [Factor 9: Compact Errors into Context Window](https://github.com/humanlayer/12-factor-agents/blob/main/content/factor-09-compact-errors.md)
* [Factor 10: Small, Focused Agents](https://github.com/humanlayer/12-factor-agents/blob/main/content/factor-10-small-focused-agents.md)
* [Factor 11: Trigger from anywhere, meet users where they are](https://github.com/humanlayer/12-factor-agents/blob/main/content/factor-11-trigger-from-anywhere.md)
* [Factor 12: Make your agent a stateless reducer](https://github.com/humanlayer/12-factor-agents/blob/main/content/factor-12-stateless-reducer.md)

Honorable Mentions / other advice
---------------------------------

* [Factor 13: Pre-fetch all the context you might need](https://github.com/humanlayer/12-factor-agents/blob/main/content/appendix-13-pre-fetch.md)

Related Resources
-----------------

* Contribute to this guide [here](https://github.com/humanlayer/12-factor-agents)
* [I talked about a lot of this on an episode of the Tool Use podcast](https://youtu.be/8bIHcttkOTE) in March 2025
* I write about some of this stuff at [The Outer Loop](https://theouterloop.substack.com)
* I do [webinars about Maximizing LLM Performance](https://github.com/hellovai/ai-that-works/tree/main) with [@hellovai](https://github.com/hellovai)
* We build OSS agents with this methodology under [got-agents/agents](https://github.com/got-agents/agents)
* We ignored all our own advice and built a [framework for running distributed agents in kubernetes](https://github.com/humanlayer/kubechain)
* Other links from this guide:
  + [12 Factor Apps](https://12factor.net)
  + [Building Effective Agents (Anthropic)](https://www.anthropic.com/engineering/building-effective-agents#agents)
  + [Prompts are Functions](https://thedataexchange.media/baml-revolution-in-ai-engineering/)
  + [Library patterns: Why frameworks are evil](https://tomasp.net/blog/2015/library-frameworks/)
  + [The Wrong Abstraction](https://sandimetz.com/blog/2016/1/20/the-wrong-abstraction)
  + [Mailcrew Agent](https://github.com/dexhorthy/mailcrew)
  + [Mailcrew Demo Video](https://www.youtube.com/watch?v=f_cKnoPC_Oo)
  + [Chainlit Demo](https://x.com/chainlit_io/status/1858613325921480922)
  + [TypeScript for LLMs](https://www.linkedin.com/posts/dexterihorthy_llms-typescript-aiagents-activity-7290858296679313408-Lh9e)
  + [Schema Aligned Parsing](https://www.boundaryml.com/blog/schema-aligned-parsing)
  + [Function Calling vs Structured Outputs vs JSON Mode](https://www.vellum.ai/blog/when-should-i-use-function-calling-structured-outputs-or-json-mode)
  + [BAML on GitHub](https://github.com/boundaryml/baml)
  + [OpenAI JSON vs Function Calling](https://docs.llamaindex.ai/en/stable/examples/llm/openai_json_vs_function_calling/)
  + [Outer Loop Agents](https://theouterloop.substack.com/p/openais-realtime-api-is-a-step-towards)
  + [Airflow](https://airflow.apache.org/)
  + [Prefect](https://www.prefect.io/)
  + [Dagster](https://dagster.io/)
  + [Inngest](https://www.inngest.com/)
  + [Windmill](https://www.windmill.dev/)
  + [The AI Agent Index (MIT)](https://aiagentindex.mit.edu/)
  + [NotebookLM on Finding Model Capability Boundaries](https://open.substack.com/pub/swyx/p/notebooklm?selection=08e1187c-cfee-4c63-93c9-71216640a5f8)

Contributors
------------

Thanks to everyone who has contributed to 12-factor agents!

[![dexhorthy](https://avatars.githubusercontent.com/u/3730605?v=4&s=80)](https://github.com/dexhorthy) [![Sypherd](https://avatars.githubusercontent.com/u/50557586?v=4&s=80)](https://github.com/Sypherd) [![tofaramususa](https://avatars.githubusercontent.com/u/66259401?v=4&s=80)](https://github.com/tofaramususa) [![a-churchill](https://avatars.githubusercontent.com/u/18105223?v=4&s=80)](https://github.com/a-churchill) [![Elijas](https://avatars.githubusercontent.com/u/4084885?v=4&s=80)](https://github.com/Elijas) [![hugolmn](https://avatars.githubusercontent.com/u/39267118?v=4&s=80)](https://github.com/hugolmn) [![jeremypeters](https://avatars.githubusercontent.com/u/1882972?v=4&s=80)](https://github.com/jeremypeters)

[![kndl](https://avatars.githubusercontent.com/u/380402?v=4&s=80)](https://github.com/kndl) [![maciejkos](https://avatars.githubusercontent.com/u/16674643?v=4&s=80)](https://github.com/maciejkos) [![pfbyjy](https://avatars.githubusercontent.com/u/85041180?v=4&s=80)](https://github.com/pfbyjy) [![0xRaduan](https://avatars.githubusercontent.com/u/36044389?v=4&s=80)](https://github.com/0xRaduan) [![zyuanlim](https://avatars.githubusercontent.com/u/7169731?v=4&s=80)](https://github.com/zyuanlim) [![lombardo-chcg](https://avatars.githubusercontent.com/u/15862501?v=4&s=80)](https://github.com/lombardo-chcg) [![sahanatvessel](https://avatars.githubusercontent.com/u/160066852?v=4&s=80)](https://github.com/sahanatvessel)

License
-------

All content and images are licensed under a [CC BY-SA 4.0 License](https://creativecommons.org/licenses/by-sa/4.0/)

Code is licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
