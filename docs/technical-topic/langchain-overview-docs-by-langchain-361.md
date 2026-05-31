---
id: 361
url: https://python.langchain.com/docs/how_to/graph_constructing/
title: LangChain overview - Docs by LangChain
domain: python.langchain.com
source_date: '2025-07-08'
tags:
- llm
- python
- ai
- tutorial
summary: LangChain is a framework that simplifies building LLM-powered agents and
  applications with minimal code (under 10 lines), offering standardized interfaces
  across multiple AI providers like OpenAI, Anthropic, and Google. Its core benefits
  include a standard model interface for provider flexibility, easy-to-use yet highly
  customizable agent abstractions, integration with LangGraph for advanced orchestration,
  and debugging capabilities through LangSmith. For basic agent development, LangChain
  provides quick setup; for more complex needs requiring deterministic workflows and
  heavy customization, the framework recommends using LangGraph directly.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# LangChain overview - Docs by LangChain

> Documentation Index
> -------------------
>
> Fetch the complete documentation index at: <https://docs.langchain.com/llms.txt>
>
> Use this file to discover all available pages before exploring further.

**Agent = Model + Harness.** LangChain provides `create_agent`: a minimal, highly configurable harness. The harness is everything around the model loop: the prompt, the tools, and any middleware that shapes behavior. Start with the primitives and compose exactly what your use case needs. Supports [OpenAI, Anthropic, Google, and more](/oss/python/integrations/providers/overview).

**LangChain vs. LangGraph vs. Deep Agents**Start with [Deep Agents](/oss/python/deepagents/overview) for a “batteries-included” agent with features like automatic context compression, a virtual filesystem, and subagent-spawning. Deep Agents are built on LangChain [agents](/oss/python/langchain/agents) which you can also use directly.Use [LangChain](/oss/python/langchain/agents) (`create_agent`) for a highly customizable harness, easily tailored to your use case and data.Use [LangGraph](/oss/python/langgraph/overview), our low-level orchestration framework, for advanced needs combining deterministic and agentic workflows.Use [LangSmith](/langsmith/home) to trace, debug, and evaluate agents built with any of these frameworks. Follow the [tracing quickstart](/langsmith/trace-with-langchain) to get set up. We recommend you also set up [LangSmith Engine](/langsmith/engine) which monitors your traces, detects issues, and proposes fixes.

[​](#create-an-agent)  Create an agent
--------------------------------------

This example demonstrates how to create a simple LangChain agent with a custom tool:

OpenAI

Google Gemini

Claude (Anthropic)

OpenRouter

Fireworks

Baseten

Ollama

Azure

AWS Bedrock

HuggingFace

```
# pip install -qU langchain "langchain[openai]"
from langchain.agents import create_agent

def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"

agent = create_agent(
    model="openai:gpt-5.4",
    tools=[get_weather],
    system_prompt="You are a helpful assistant",
)

result = agent.invoke(
    {"messages": [{"role": "user", "content": "What's the weather in San Francisco?"}]}
)
print(result["messages"][-1].content_blocks)
```

See the [Installation instructions](/oss/python/langchain/install) and [Quickstart guide](/oss/python/langchain/quickstart) to get started building your own agents and applications with LangChain.

Use [LangSmith](/langsmith/home) to trace requests, debug agent behavior, and evaluate outputs. Set `LANGSMITH_TRACING=true` and your API key to get started.

[​](#core-benefits)  Core benefits
----------------------------------

Standard model interface
------------------------

Different providers have unique APIs for interacting with models, including the format of responses. LangChain standardizes how you interact with models so that you can seamlessly swap providers and avoid lock-in.

Learn more

Highly configurable harness
---------------------------

`create_agent` is a minimal harness: model, tools, prompt, loop. Extend it with middleware: each piece handles one concern and composes freely. Build exactly the agent your use case needs, nothing more.

Learn more

![https://mintcdn.com/langchain-5e9cc07a/nQm-sjd_MByLhgeW/images/brand/langgraph-icon.png?fit=max&auto=format&n=nQm-sjd_MByLhgeW&q=85&s=b997e1a7487d507a36556eedbfd99f81](https://mintcdn.com/langchain-5e9cc07a/nQm-sjd_MByLhgeW/images/brand/langgraph-icon.png?fit=max&auto=format&n=nQm-sjd_MByLhgeW&q=85&s=b997e1a7487d507a36556eedbfd99f81)

Built on top of LangGraph
-------------------------

LangChain’s agents are built on top of LangGraph. This allows us to take advantage of LangGraph’s durable execution, human-in-the-loop support, persistence, and more.

Learn more

![https://mintcdn.com/langchain-5e9cc07a/nQm-sjd_MByLhgeW/images/brand/observability-icon-dark.png?fit=max&auto=format&n=nQm-sjd_MByLhgeW&q=85&s=ccbc183bca2a5e4ca78d30149e3836cc](https://mintcdn.com/langchain-5e9cc07a/nQm-sjd_MByLhgeW/images/brand/observability-icon-dark.png?fit=max&auto=format&n=nQm-sjd_MByLhgeW&q=85&s=ccbc183bca2a5e4ca78d30149e3836cc)

Debug with LangSmith
--------------------

Gain deep visibility into complex agent behavior with visualization tools that trace execution paths, capture state transitions, and provide detailed runtime metrics.

Learn more

---

[Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.

[Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langchain/overview.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).

Was this page helpful?

YesNo

[Install LangChain

Next](/oss/python/langchain/install)

⌘I
