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

Docs by LangChain home page LangChain + LangGraph Search... ⌘ K Search... Navigation LangChain overview LangChain LangGraph Deep Agents Integrations Learn Reference Contribute Python Overview Get started Install Quickstart Changelog Philosophy Core components Agents Models Messages Tools Short-term memory Streaming Structured output Middleware Overview Built-in middleware Custom middleware Advanced usage Guardrails Runtime Context engineering Model Context Protocol (MCP) Human-in-the-loop Multi-agent Retrieval Long-term memory Agent development LangSmith Studio Test Agent Chat UI Deploy with LangSmith Deployment Observability On this page Create an agent core benefits LangChain is the easiest way to start building agents and applications powered by LLMs. With under 10 lines of code, you can connect to OpenAI, Anthropic, Google, and more . LangChain provides a pre-built agent architecture and model integrations to help you get started quickly and seamlessly incorporate LLMs into your agents and applications. We recommend you use LangChain if you want to quickly build agents and autonomous applications. Use LangGraph , our low-level agent orchestration framework and runtime, when you have more advanced needs that require a combination of deterministic and agentic workflows, heavy customization, and carefully controlled latency. LangChain agents are built on top of LangGraph in order to provide durable execution, streaming, human-in-the-loop, persistence, and more. You do not need to know LangGraph for basic LangChain agent usage. ​ Create an agent Copy # pip install -qU langchain "langchain[anthropic]" from langchain.agents import create_agent def get_weather ( city : str ) -> str : """Get weather for a given city.""" return f "It's always sunny in { city } !" agent = create_agent( model = "claude-sonnet-4-5-20250929" , tools = [get_weather], system_prompt = "You are a helpful assistant" , ) # Run the agent agent.invoke( { "messages" : [{ "role" : "user" , "content" : "what is the weather in sf" }]} ) See the Installation instructions and Quickstart guide to get started building your own agents and applications with LangChain. ​ core benefits Standard model interface Different providers have unique APIs for interacting with models, including the format of responses. LangChain standardizes how you interact with models so that you can seamlessly swap providers and avoid lock-in. Learn more Easy to use, highly flexible agent LangChain’s agent abstraction is designed to be easy to get started with, letting you build a simple agent in under 10 lines of code. But it also provides enough flexibility to allow you to do all the context engineering your heart desires. Learn more Built on top of LangGraph LangChain’s agents are built on top of LangGraph. This allows us to take advantage of LangGraph’s durable execution, human-in-the-loop support, persistence, and more. Learn more Debug with LangSmith Gain deep visibility into complex agent behavior with visualization tools that trace execution paths, capture state transitions, and provide detailed runtime metrics. Learn more Edit this page on GitHub or file an issue . Connect these docs to Claude, VSCode, and more via MCP for real-time answers. Was this page helpful? Yes No Install LangChain Next ⌘ I
