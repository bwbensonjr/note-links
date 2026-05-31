---
id: 151
url: https://deepwiki.com/langchain-ai/local-deep-researcher/3.2-search-api-integration
title: Search API Integration | langchain-ai/local-deep-researcher | DeepWiki
domain: deepwiki.com
source_date: '2025-11-11'
tags:
- github-repo
- ai
- llm
- python
- web-dev
summary: The Local Deep Researcher system provides a unified, pluggable search API
  integration layer that supports multiple web search services (DuckDuckGo, Tavily,
  Perplexity, and SearXNG) through a common interface. All search providers return
  results in a standardized format that enables consistent downstream processing,
  with configurable parameters for result limits, content fetching, and token management.
  The system allows runtime selection of search APIs through configuration while maintaining
  consistent data flow and processing pipelines regardless of which provider is chosen.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# Search API Integration | langchain-ai/local-deep-researcher | DeepWiki

Loading...

Index your code with Devin

[DeepWiki](/)

[DeepWiki](/)

[langchain-ai/local-deep-researcher](https://github.com/langchain-ai/local-deep-researcher "Open repository")

Index your code with

Devin

Edit WikiShare

Loading...

Last indexed: 21 August 2025 ([8a5e22](https://github.com/langchain-ai/local-deep-researcher/commits/8a5e220e))

* [Overview](/langchain-ai/local-deep-researcher/1-overview)
* [Project Structure](/langchain-ai/local-deep-researcher/1.1-project-structure)
* [System Architecture](/langchain-ai/local-deep-researcher/2-system-architecture)
* [Research Workflow](/langchain-ai/local-deep-researcher/2.1-research-workflow)
* [State Management](/langchain-ai/local-deep-researcher/2.2-state-management)
* [Core Components](/langchain-ai/local-deep-researcher/3-core-components)
* [LLM Integration](/langchain-ai/local-deep-researcher/3.1-llm-integration)
* [Search API Integration](/langchain-ai/local-deep-researcher/3.2-search-api-integration)
* [Prompt Engineering](/langchain-ai/local-deep-researcher/3.3-prompt-engineering)
* [Configuration](/langchain-ai/local-deep-researcher/4-configuration)
* [Environment Variables](/langchain-ai/local-deep-researcher/4.1-environment-variables)
* [LangGraph Configuration](/langchain-ai/local-deep-researcher/4.2-langgraph-configuration)
* [Deployment](/langchain-ai/local-deep-researcher/5-deployment)
* [Docker Deployment](/langchain-ai/local-deep-researcher/5.1-docker-deployment)
* [CI/CD Pipeline](/langchain-ai/local-deep-researcher/5.2-cicd-pipeline)
* [Development Workflows](/langchain-ai/local-deep-researcher/5.3-development-workflows)
* [Usage Guide](/langchain-ai/local-deep-researcher/6-usage-guide)
* [Quick Start](/langchain-ai/local-deep-researcher/6.1-quick-start)
* [Advanced Configuration](/langchain-ai/local-deep-researcher/6.2-advanced-configuration)
* [License](/langchain-ai/local-deep-researcher/7-license)

Menu

Search API Integration
======================

Relevant source files

* [src/ollama\_deep\_researcher/graph.py](https://github.com/langchain-ai/local-deep-researcher/blob/8a5e220e/src/ollama_deep_researcher/graph.py)
* [src/ollama\_deep\_researcher/utils.py](https://github.com/langchain-ai/local-deep-researcher/blob/8a5e220e/src/ollama_deep_researcher/utils.py)

Purpose and Scope
-----------------

This document covers the search API integration layer of the Local Deep Researcher system, which provides a unified abstraction for querying multiple web search services. The system supports DuckDuckGo, Tavily, Perplexity, and SearXNG APIs through a common interface that standardizes search results and content processing.

For information about how search results are processed within the research workflow, see [Research Workflow](/langchain-ai/local-deep-researcher/2.1-research-workflow). For configuration of search API credentials and settings, see [Environment Variables](/langchain-ai/local-deep-researcher/4.1-environment-variables).

Search API Architecture
-----------------------

The search integration layer implements a pluggable architecture where different search providers can be selected at runtime through configuration. All search APIs return results in a standardized format that enables consistent processing downstream.

**Sources:** [src/ollama\_deep\_researcher/graph.py192-262](https://github.com/langchain-ai/local-deep-researcher/blob/8a5e220e/src/ollama_deep_researcher/graph.py#L192-L262) [src/ollama\_deep\_researcher/utils.py17-33](https://github.com/langchain-ai/local-deep-researcher/blob/8a5e220e/src/ollama_deep_researcher/utils.py#L17-L33)

Search API Implementations
--------------------------

### Tavily Search

The `tavily_search()` function provides integration with the Tavily API, which specializes in AI-optimized web search with built-in content extraction capabilities.

| Feature | Implementation | Configuration |
| --- | --- | --- |
| API Client | `TavilyClient` | Requires `TAVILY_API_KEY` environment variable |
| Content Extraction | Built-in raw content support | `include_raw_content` parameter |
| Result Limit | Configurable via `max_results` | Default: 3 results |
| Timeout | Handled by Tavily client | N/A |

**Sources:** [src/ollama\_deep\_researcher/utils.py277-306](https://github.com/langchain-ai/local-deep-researcher/blob/8a5e220e/src/ollama_deep_researcher/utils.py#L277-L306)

### DuckDuckGo Search

The `duckduckgo_search()` function uses the `DDGS` library to perform privacy-focused web searches without requiring API keys.

| Feature | Implementation | Configuration |
| --- | --- | --- |
| API Client | `DDGS` from `duckduckgo-search` | No API key required |
| Content Extraction | Manual via `fetch_raw_content()` | Optional full page fetching |
| Result Limit | Configurable via `max_results` | Default: 3 results |
| Timeout | 10 seconds via `httpx.Client` | Hardcoded in `fetch_raw_content()` |

**Sources:** [src/ollama\_deep\_researcher/utils.py165-220](https://github.com/langchain-ai/local-deep-researcher/blob/8a5e220e/src/ollama_deep_researcher/utils.py#L165-L220) [src/ollama\_deep\_researcher/utils.py141-163](https://github.com/langchain-ai/local-deep-researcher/blob/8a5e220e/src/ollama_deep_researcher/utils.py#L141-L163)

### Perplexity Search

The `perplexity_search()` function integrates with Perplexity's `sonar-pro` model for AI-enhanced search with automatic summarization.

| Feature | Implementation | Configuration |
| --- | --- | --- |
| API Client | Direct HTTP requests via `requests` | Requires `PERPLEXITY_API_KEY` environment variable |
| Content Format | AI-generated summary with citations | Fixed system prompt |
| Result Structure | Single content with multiple citations | Loop count tracking for source labeling |
| Error Handling | `response.raise_for_status()` | HTTP error exceptions |

**Sources:** [src/ollama\_deep\_researcher/utils.py309-387](https://github.com/langchain-ai/local-deep-researcher/blob/8a5e220e/src/ollama_deep_researcher/utils.py#L309-L387)

### SearXNG Search

The `searxng_search()` function connects to self-hosted SearXNG instances for privacy-focused metasearch capabilities.

| Feature | Implementation | Configuration |
| --- | --- | --- |
| API Client | `SearxSearchWrapper` from LangChain | `SEARXNG_URL` environment variable |
| Default Host | `http://localhost:8888` | Configurable via environment |
| Content Extraction | Manual via `fetch_raw_content()` | Optional full page fetching |
| Result Processing | Similar to DuckDuckGo pattern | Standard result format |

**Sources:** [src/ollama\_deep\_researcher/utils.py222-274](https://github.com/langchain-ai/local-deep-researcher/blob/8a5e220e/src/ollama_deep_researcher/utils.py#L222-L274)

Unified Data Flow
-----------------

The search integration layer provides a consistent data flow regardless of which search API is selected. All search functions return results in the same standardized format.

**Sources:** [src/ollama\_deep\_researcher/graph.py206-262](https://github.com/langchain-ai/local-deep-researcher/blob/8a5e220e/src/ollama_deep_researcher/graph.py#L206-L262)

Standardized Result Format
--------------------------

All search APIs return results conforming to a common data structure that enables consistent downstream processing.

### Standard Result Schema

### Content Processing Pipeline

The `deduplicate_and_format_sources()` function processes search results through several stages:

| Stage | Function | Purpose |
| --- | --- | --- |
| Input Normalization | Type checking and conversion | Handle both single dict and list inputs |
| Deduplication | URL-based uniqueness | Remove duplicate sources across searches |
| Content Limiting | Token-based truncation | Limit content to `max_tokens_per_source` |
| Formatting | Structured output | Create consistent text format for LLM processing |

**Sources:** [src/ollama\_deep\_researcher/utils.py55-121](https://github.com/langchain-ai/local-deep-researcher/blob/8a5e220e/src/ollama_deep_researcher/utils.py#L55-L121)

Configuration and API Selection
-------------------------------

The search API selection is controlled through the configuration system, with runtime routing handled by the `web_research()` node in the LangGraph workflow.

### API Selection Logic

### Configuration Parameters

| Parameter | Type | Default | Purpose |
| --- | --- | --- | --- |
| `search_api` | `SearchAPI` enum | Set via configuration | Selects which search provider to use |
| `fetch_full_page` | `bool` | `False` | Controls whether to fetch complete page content |
| `max_results` | `int` | Varies by API | Limits number of search results returned |

**Sources:** [src/ollama\_deep\_researcher/graph.py206-256](https://github.com/langchain-ai/local-deep-researcher/blob/8a5e220e/src/ollama_deep_researcher/graph.py#L206-L256) [src/ollama\_deep\_researcher/utils.py17-33](https://github.com/langchain-ai/local-deep-researcher/blob/8a5e220e/src/ollama_deep_researcher/utils.py#L17-L33)

Content Fetching and Processing
-------------------------------

The system provides optional full-page content fetching for enhanced research depth, implemented through the `fetch_raw_content()` function.

### Content Fetching Features

* **Timeout Management**: 10-second timeout prevents hanging on slow sites
* **Markdown Conversion**: HTML content converted via `markdownify` library
* **Error Handling**: Graceful degradation when content fetching fails
* **Token Limiting**: Content truncated based on `max_tokens_per_source` configuration

### Content Processing Flow

**Sources:** [src/ollama\_deep\_researcher/utils.py141-163](https://github.com/langchain-ai/local-deep-researcher/blob/8a5e220e/src/ollama_deep_researcher/utils.py#L141-L163)

Dismiss

Refresh this wiki

Enter email to refresh

### On this page

* [Search API Integration](#search-api-integration)
* [Purpose and Scope](#purpose-and-scope)
* [Search API Architecture](#search-api-architecture)
* [Search API Implementations](#search-api-implementations)
* [Tavily Search](#tavily-search)
* [DuckDuckGo Search](#duckduckgo-search)
* [Perplexity Search](#perplexity-search)
* [SearXNG Search](#searxng-search)
* [Unified Data Flow](#unified-data-flow)
* [Standardized Result Format](#standardized-result-format)
* [Standard Result Schema](#standard-result-schema)
* [Content Processing Pipeline](#content-processing-pipeline)
* [Configuration and API Selection](#configuration-and-api-selection)
* [API Selection Logic](#api-selection-logic)
* [Configuration Parameters](#configuration-parameters)
* [Content Fetching and Processing](#content-fetching-and-processing)
* [Content Fetching Features](#content-fetching-features)
* [Content Processing Flow](#content-processing-flow)
