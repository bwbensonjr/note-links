---
id: 1052
url: https://github.com/sachitrafa/YourMemory
title: 'GitHub - sachitrafa/YourMemory: Agentic AI memory with Ebbinghaus forgetting
  curve decay. +16pp better recall than Mem0 on LoCoMo. · GitHub'
domain: github.com
source_date: '2026-04-26'
tags:
- github-repo
- ai
- llm
- python
summary: YourMemory is an AI memory system that implements human-like memory decay
  using the Ebbinghaus forgetting curve, enabling AI agents to retain persistent context
  across sessions without restarting from zero. It achieves 59% recall on benchmarks—2×
  better than competing solutions like Zep Cloud—through a hybrid approach combining
  vector search, graph-based retrieval, and importance-weighted decay, with easy installation
  and zero infrastructure requirements. The system integrates with popular AI clients
  like Claude and Cline via standard MCP servers, offering simple memory management
  tools (recall, store, update) that automatically integrate into agent workflows.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# GitHub - sachitrafa/YourMemory: Agentic AI memory with Ebbinghaus forgetting curve decay. +16pp better recall than Mem0 on LoCoMo. · GitHub

[![YourMemory](/sachitrafa/YourMemory/raw/main/logo.svg.png)](/sachitrafa/YourMemory/blob/main/logo.svg.png)  

YourMemory
==========

**Persistent memory for AI agents — built on the science of how humans remember.**

[![PyPI](https://camo.githubusercontent.com/ba1926a3917a53641753a5f7112fe29d3a33f8a8f3e02b98ce758dfd2cece22f/68747470733a2f2f696d672e736869656c64732e696f2f707970692f762f796f75726d656d6f72793f636f6c6f723d626c7565266c6f676f3d70797069266c6f676f436f6c6f723d7768697465)](https://pypi.org/project/yourmemory/)
[![PyPI Downloads](https://camo.githubusercontent.com/dc2a2b1a6d5ec1e0d430c8d1ee6fde1713fa1c855dee2aecf1ef5bc1cd4d488d/68747470733a2f2f696d672e736869656c64732e696f2f707970692f646d2f796f75726d656d6f72793f636f6c6f723d627269676874677265656e)](https://pypi.org/project/yourmemory/)
[![Python](https://camo.githubusercontent.com/7e8d4ec100f8e46e35045d8230e4bee59830cd57798f577d019213fc347d9bf4/68747470733a2f2f696d672e736869656c64732e696f2f707970692f707976657273696f6e732f796f75726d656d6f7279)](https://pypi.org/project/yourmemory/)
[![License: CC BY-NC 4.0](https://camo.githubusercontent.com/da3491dfbd04b0fa38fae54fadfaba684d2d69444b262277ec354e5c7b18a432/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6c6963656e73652d434325323042592d2d4e43253230342e302d6c6967687467726579)](https://creativecommons.org/licenses/by-nc/4.0/)
[![GitHub Stars](https://camo.githubusercontent.com/0377c9634e5663b9e40c638cdbe1da41581b10970cab7c5677939d74a7545fc0/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f73746172732f736163686974726166612f596f75724d656d6f72793f7374796c653d736f6369616c)](https://github.com/sachitrafa/YourMemory)
[![GitHub Issues](https://camo.githubusercontent.com/bb23e00c33fe9c8ce5cf7ae06ac2d77fc0c3f9b0631fe60af28fb18b1cc47fb5/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6973737565732f736163686974726166612f596f75724d656d6f7279)](https://github.com/sachitrafa/YourMemory/issues)
[![Last Commit](https://camo.githubusercontent.com/27c23d2c420f18e55e4f4b8a446f7c06c46fa671c5b9cef84dbdce8ff7c260a0/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6c6173742d636f6d6d69742f736163686974726166612f596f75724d656d6f7279)](https://github.com/sachitrafa/YourMemory/commits/main)
[![Docker Build](https://camo.githubusercontent.com/4658920a408dd85196295157527cc38469f99614f783a450217ca12f51278d50/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f616374696f6e732f776f726b666c6f772f7374617475732f736163686974726166612f596f75724d656d6f72792f646f636b65722d7075626c6973682e796d6c3f6272616e63683d6d61696e266c6162656c3d646f636b6572266c6f676f3d646f636b6572)](https://github.com/sachitrafa/YourMemory/actions/workflows/docker-publish.yml)

[![LoCoMo Recall@5](https://camo.githubusercontent.com/0cc0aeb5b478fd62923edd0b9c8b30237d4c6f0860cd50edfee789c8f0fc5d96/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4c6f436f4d6f253230526563616c6c253430352d35392532352d627269676874677265656e)](/sachitrafa/YourMemory/blob/main/BENCHMARKS.md)
[![LongMemEval Recall@5](https://camo.githubusercontent.com/c1bd64c57f49228cf32a1977f07e223bd4785161ab2793ded817586185c0f008/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4c6f6e674d656d4576616c253230526563616c6c253430352d38392532352d627269676874677265656e)](/sachitrafa/YourMemory/blob/main/BENCHMARKS.md)
[![HotpotQA BOTH@5](https://camo.githubusercontent.com/b6711f51b872ff936ca49b17a357550fc476365a320de9dd8f1746d3f9419659/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f486f74706f745141253230424f5448253430352d37312e352532352d627269676874677265656e)](/sachitrafa/YourMemory/blob/main/BENCHMARKS.md)
[![oosmetrics](https://camo.githubusercontent.com/76892a61f8082828eb544ebc31ac63c7eda5b0a5a257354418cdeaabfab797bc/68747470733a2f2f6170692e6f6f736d6574726963732e636f6d2f6170692f76312f62616467652f616368696576656d656e742f39313036646530322d336461652d343166662d626332382d3130396461393366653837642e737667)](https://oosmetrics.com/repo/sachitrafa/YourMemory)

---

What Is YourMemory?
-------------------

Every session, your AI assistant starts from zero. It asks the same questions, forgets your preferences, re-learns your stack. **There is no memory between conversations.**

YourMemory fixes that with a one-command install that plugs into Claude, Cursor, Cline, Windsurf, or any MCP client. It gives your AI a persistent memory layer modelled on human cognition:

* **Things that matter stick** — importance score controls how quickly a memory decays
* **Outdated facts get replaced** — subject-aware deduplication merges or supersedes memories automatically
* **Related context surfaces together** — entity graph links memories that share people, places, or concepts
* **Old memories fade naturally** — Ebbinghaus forgetting curve prunes stale context every 24 hours

Zero infrastructure required. SQLite by default, Postgres for teams.

---

Table of Contents
-----------------

* [Benchmarks](#benchmarks)
* [Quick Start](#quick-start)
* [Memory Dashboard](#memory-dashboard)
* [Ask Without an LLM Call](#ask-without-calling-the-api)
* [MCP Tools](#mcp-tools)
* [How It Works](#how-it-works)
* [Multi-Agent Memory](#multi-agent-memory)
* [Stack](#stack)
* [Architecture](#architecture)
* [Contributing](#contributing)

---

Benchmarks
----------

Three external datasets, all scripts open source and reproducible. Full methodology in [BENCHMARKS.md](/sachitrafa/YourMemory/blob/main/BENCHMARKS.md).

### LongMemEval-S — 500 questions, ~53 distractor sessions each

The hardest standard benchmark for long-term memory systems. Each question is backed by ~53 conversation sessions; the model must retrieve the right one(s) from the haystack.

| Metric | Score |
| --- | --- |
| **Recall@5** (any gold session in top-5) | **89.4%** |
| Recall-all@5 (all gold sessions in top-5) | 84.8% |
| nDCG@5 (ranking quality) | 87.4% |

**By question type (Recall@5):**

| Question Type | Recall@5 | n |
| --- | --- | --- |
| single-session-assistant | 98.2% | 56 |
| knowledge-update | 96.2% | 78 |
| multi-session | 95.5% | 133 |
| single-session-preference | 90.0% | 30 |
| temporal-reasoning | 84.2% | 133 |
| single-session-user | 72.9% | 70 |

### LoCoMo-10 — 1,534 QA pairs across 10 multi-session conversations

Conversations spanning weeks to months. Every system ingests the same session summaries in the same order.

| System | Recall@5 | 95% CI |
| --- | --- | --- |
| **YourMemory** (BM25 + vector + graph + decay) | **59%** | 56–61% |
| Zep Cloud | 28% | 26–30% |
| Supermemory | 31%\* | 28–33% |
| Mem0 | 18%\* | 16–20% |

> **2× better recall than Zep Cloud across all 10 samples.** \* Supermemory and Mem0 exhausted free-tier quotas mid-benchmark; scores computed over full 1,534 pairs using 0 for unfinished samples.

### HotpotQA — 200 multi-hop questions requiring two facts from different articles

| System | BOTH\_FOUND@5 |
| --- | --- |
| **YourMemory** (vector + BM25 + entity graph) | **71.5%** |
| YourMemory (no entity edges) | 59.5% |

Entity graph edges add **+12 pp** — they traverse from Fact 1 to Fact 2 even when Fact 2 has low embedding similarity to the query.

*Writeup: [I built memory decay for AI agents using the Ebbinghaus forgetting curve](https://dev.to/sachit_mishra_686a94d1bb5/i-built-memory-decay-for-ai-agents-using-the-ebbinghaus-forgetting-curve-1b0e)*

---

Quick Start
-----------

**Supports Python 3.11–3.14. No Docker, no database setup, no external services.**

### 1 — Install

```
pip install yourmemory
yourmemory-setup
```

`yourmemory-setup` auto-detects your AI client (Claude Code, Claude Desktop, Cursor, Cline, Windsurf, OpenCode), writes the MCP config, and initialises your database. **That's it for most users.**

### 2 — Wire into your AI client manually (if needed)

**Claude Code**

Add to `~/.claude/settings.json`:

```
{
  "mcpServers": {
    "yourmemory": {
      "command": "yourmemory"
    }
  }
}
```

Reload (`Cmd+Shift+P` → `Developer: Reload Window`).


**Claude Desktop**

Add to `~/Library/Application Support/Claude/claude_desktop_config.json` (macOS) or `%APPDATA%\Claude\claude_desktop_config.json` (Windows):

```
{
  "mcpServers": {
    "yourmemory": {
      "command": "yourmemory"
    }
  }
}
```

Restart Claude Desktop.


**Cline (VS Code)**

VS Code doesn't inherit your shell PATH. Run `yourmemory-path` first to get the full executable path.

In Cline → **MCP Servers** → **Edit MCP Settings**:

```
{
  "mcpServers": {
    "yourmemory": {
      "command": "/full/path/to/yourmemory",
      "args": [],
      "env": { "YOURMEMORY_USER": "your_name" }
    }
  }
}
```

Restart Cline after saving.


**Cursor**

Add to `~/.cursor/mcp.json`:

```
{
  "mcpServers": {
    "yourmemory": {
      "command": "/full/path/to/yourmemory",
      "args": [],
      "env": { "YOURMEMORY_USER": "your_name" }
    }
  }
}
```


**Windsurf / OpenCode / any MCP client**

YourMemory is a standard stdio MCP server. Use the full path from `yourmemory-path` if the client doesn't inherit shell PATH.

```
{
  "mcpServers": {
    "yourmemory": {
      "command": "/full/path/to/yourmemory",
      "env": { "YOURMEMORY_USER": "your_name" }
    }
  }
}
```

> **First start is automatic.** On the first run, YourMemory initialises your database at `~/.yourmemory/memories.duckdb`, downloads the spaCy language model in the background, and injects memory workflow rules into your AI client config. Nothing to configure manually.

---

Memory Dashboard
----------------

Two built-in browser UIs — no extra setup, start automatically with the MCP server.

### Memory Browser — `http://localhost:3033/ui`

A full read/write view of everything stored in memory.

| What you see | Details |
| --- | --- |
| **Stats bar** | Total · Strong ≥50% · Fading 5–50% · Near prune <10% |
| **Agent tabs** | All / User / per-agent views |
| **Memory cards** | Content · strength bar · category · recall count · last accessed |
| **Filters** | Category (fact / strategy / assumption / failure) · Sort by strength, recency, recall |

Pass `?user=<id>` to pre-load a specific user: `http://localhost:3033/ui?user=sachit`

### Graph Visualiser — `http://localhost:3033/graph`

An interactive force-directed map of how memories connect.

```
http://localhost:3033/graph?memoryId=42&userId=sachit&depth=2
```

* Root memory as a larger cyan node; neighbours color-coded by category
* Edge thickness = connection strength
* Click any node for full content; drag, zoom, reposition freely

---

Ask Without Calling the API
---------------------------

The only memory system that can answer questions **without making any LLM API call.**

```
yourmemory ask "what database does this project use"
# → YourMemory uses DuckDB locally and Postgres in production.

yourmemory ask "what port does the dashboard run on"
# → 3033

yourmemory ask "how do I fix a kubernetes deployment"
# → Not enough memory context to answer without Claude.
```

When memory is strong enough, it answers instantly — zero tokens, zero cloud cost, zero latency. When it isn't, it declines cleanly rather than hallucinating.

| Query | Mem0 / Zep / LangMem | YourMemory |
| --- | --- | --- |
| "What port does the server run on?" | Full LLM API call | Instant, $0 |
| "What database does this project use?" | Full LLM API call | Instant, $0 |
| "How do I fix a k8s deployment?" | Full LLM API call | Declines → Claude |
| Privacy | Query sent to cloud | Never leaves your machine |



---

MCP Tools
---------

Three tools, called by your AI automatically.

| Tool | When your AI calls it | What it does |
| --- | --- | --- |
| `recall_memory(query, current_path?)` | Start of every task | Surfaces memories ranked by similarity × decay strength; spatial boost for path-matched memories |
| `store_memory(content, importance, category?, context_paths?)` | After learning something new | Embeds, deduplicates, stores with decay; tags optional file/dir paths |
| `update_memory(id, new_content, importance)` | When a stored fact is outdated | Re-embeds and replaces; logs old content to audit trail |

```
# Store with spatial context
store_memory(
    "Sachit prefers tabs over spaces in Python",
    importance=0.9,
    category="fact",
    context_paths=["/projects/backend"]
)

# Next session — spatial boost fires when working in that directory
recall_memory("Python formatting", current_path="/projects/backend")
# → {"content": "Sachit prefers tabs over spaces in Python", "strength": 0.87}
```

### Memory categories control decay rate

| Category | Half-life | Best for |
| --- | --- | --- |
| `strategy` | ~38 days | Patterns that worked, architectural decisions |
| `fact` | ~24 days | Preferences, identity, stable knowledge |
| `assumption` | ~19 days | Inferred context, uncertain beliefs |
| `failure` | ~11 days | Errors, wrong approaches, environment-specific issues |



---

How It Works
------------

### Ebbinghaus Forgetting Curve

Memory strength decays exponentially. Importance and recall frequency slow that decay:

```
effective_λ  = base_λ × (1 − importance × 0.8)
strength     = clamp(importance × e^(−effective_λ × active_days) × (1 + recall_count × 0.2), 0, 1)
hybrid_score = 0.4 × bm25_norm + 0.6 × cosine_similarity
```

`active_days` counts only days the user was active — vacations don't cause memory loss. Memories below strength `0.05` are pruned automatically every 24 hours.

**Session wrap-up:** recalled memory IDs are tracked per session. When a session goes idle (30 min default), those memories get a `recall_count` boost. Set `YOURMEMORY_SESSION_IDLE` to change the window.

**Recall throttling:** identical (user, query) pairs are cached within a configurable window. Set `YOURMEMORY_RECALL_COOLDOWN` (seconds, default 0 = off).

### Hybrid Retrieval: Vector + BM25 + Entity Graph

Retrieval runs in two rounds:

**Round 1 — Hybrid search:** cosine similarity + BM25 keyword scoring, returns top-k candidates above threshold.

**Round 2 — Graph expansion:** BFS traversal from Round 1 seeds surfaces memories that share context but not vocabulary — connected via semantic or entity edges.

```
recall("Python backend")
  Round 1 → [1] Python/MongoDB    (sim=0.61)
             [2] DuckDB/spaCy     (sim=0.19)
  Round 2 → [5] Docker/Kubernetes (sim=0.29 — below cut-off, surfaced via shared entity "backend")
```

**Chain-aware pruning:** a decayed memory is kept alive if any graph neighbour is above the prune threshold. Related memories age together.

### Subject-Aware Deduplication

Before storing, YourMemory checks whether the new memory is about the same entity as the nearest existing one:

```
"Sachit uses DuckDB"      vs  "YourMemory uses DuckDB"
 subject: Sachit               subject: YourMemory
 → different entities → stored separately ✓

"YourMemory uses DuckDB"  vs  "YourMemory stores data in DuckDB"
 subject: YourMemory           subject: YourMemory
 → same entity → merged ✓
```

Subject comparison embeds the first two tokens of each sentence — no hardcoded word lists, generalises to any language.

---

Multi-Agent Memory
------------------

Multiple agents can share one YourMemory instance — each with isolated private memories and controlled access to shared context.

```
from src.services.api_keys import register_agent

result = register_agent(
    agent_id="coding-agent",
    user_id="sachit",
    can_read=["shared", "private"],
    can_write=["shared", "private"],
)
# → result["api_key"]  — ym_xxxx (shown once only)
```

```
# Agent stores a private failure memory
store_memory(
    "Staging uses self-signed cert — skip SSL verify",
    importance=0.7, category="failure",
    api_key="ym_xxxx", visibility="private"
)

# Recalls shared + its own private memories; other agents see shared only
recall_memory("staging SSL", api_key="ym_xxxx")
```

---

Stack
-----

| Component | Role |
| --- | --- |
| **DuckDB** | Default vector DB — zero setup, native cosine similarity |
| **NetworkX** | Default graph backend — persists at `~/.yourmemory/graph.pkl` |
| **sentence-transformers** | Local embeddings (`multi-qa-mpnet-base-dot-v1`, 768 dims) |
| **spaCy** | Local NLP for deduplication and entity extraction |
| **APScheduler** | Automatic 24h decay and pruning job |
| **PostgreSQL + pgvector** | Optional — for teams or large datasets |
| **Neo4j** | Optional graph backend — `pip install 'yourmemory[neo4j]'` |


**PostgreSQL setup (optional)**

```
pip install yourmemory[postgres]
```

Create a `.env` file:

```
DATABASE_URL=postgresql://YOUR_USER@localhost:5432/yourmemory
```

**macOS**

```
brew install postgresql@16 pgvector && brew services start postgresql@16
createdb yourmemory
```

**Ubuntu / Debian**

```
sudo apt install postgresql postgresql-contrib postgresql-16-pgvector
createdb yourmemory
```



---

Architecture
------------

```
Claude / Cline / Cursor / Any MCP client
    │
    ├── recall_memory(query, current_path?, api_key?)
    │       └── throttle check → embed → hybrid search (Round 1)
    │               → graph BFS expansion (Round 2)
    │               → score = sim × strength
    │               → spatial boost (+0.08) if current_path matches context_paths
    │               → temporal boost (+0.25) if query has time window expression
    │               → session tracking → recall_count bump on session end
    │
    ├── store_memory(content, importance, category?, context_paths?, api_key?)
    │       └── question? → reject
    │               subject-aware dedup → same entity? merge/reinforce : new
    │               embed() → INSERT → index_memory() → graph node + edges
    │               record_activity(user_id) → active days log
    │
    └── update_memory(id, new_content, importance)
            └── log old content → memory_history (audit trail)
                    embed(new_content) → UPDATE → refresh graph node

  Vector DB (Round 1)              Graph DB (Round 2)
  DuckDB (default)                 NetworkX (default)
    memories.duckdb                  graph.pkl
    ├── embedding FLOAT[768]         ├── nodes: memory_id, strength
    ├── importance FLOAT             └── edges: sim × verb_weight ≥ 0.4
    ├── recall_count INTEGER
    ├── context_paths JSON         Neo4j (opt-in)
    ├── created_at TIMESTAMP         └── bolt://localhost:7687
    ├── visibility VARCHAR
    ├── agent_id VARCHAR
    user_activity  (active days log)
    memory_history (supersession audit)
```

---

Contributing
------------

PRs are welcome. See [CONTRIBUTORS.md](/sachitrafa/YourMemory/blob/main/CONTRIBUTORS.md) for contributors who have already improved YourMemory.

---

Dataset References
------------------

* [LoCoMo](https://github.com/snap-research/locomo) — Maharana et al. (2024). *LoCoMo: Long Context Multimodal Benchmark for Dialogue.* Snap Research.
* [LongMemEval](https://github.com/xiaowu0162/LongMemEval) — Wu et al. (2024). *LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory.*
* [HotpotQA](https://hotpotqa.github.io/) — Yang et al. (2018). *HotpotQA: A Dataset for Diverse, Explainable Multi-hop Question Answering.*

---

License
-------

Copyright 2026 **Sachit Misra** — Licensed under [CC-BY-NC-4.0](/sachitrafa/YourMemory/blob/main/LICENSE).

**Free for:** personal use, education, academic research, open-source projects.
**Not permitted:** commercial use without a separate written agreement.

Commercial licensing: [mishrasachit1@gmail.com](mailto:mishrasachit1@gmail.com)
