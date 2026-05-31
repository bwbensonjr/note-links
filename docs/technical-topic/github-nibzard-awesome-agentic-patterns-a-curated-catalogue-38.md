---
id: 38
url: https://github.com/nibzard/awesome-agentic-patterns
title: 'GitHub - nibzard/awesome-agentic-patterns: A curated catalogue of awesome
  agentic AI patterns'
domain: github.com
source_date: '2026-01-05'
tags:
- ai
- github-repo
- llm
summary: 'This GitHub repository curates practical, production-ready AI agentic patterns—repeatable
  workflows and architectures that help autonomous AI agents perform real work effectively.
  The collection bridges the gap between toy tutorials and hidden industry practices
  by organizing patterns across nine categories including context management, feedback
  loops, orchestration, reliability, security, tool use, and user collaboration. Contributors
  can submit patterns that meet three criteria: they''re used by multiple teams, improve
  how agents sense/reason/act, and are backed by public references like blog posts
  or papers.'
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# GitHub - nibzard/awesome-agentic-patterns: A curated catalogue of awesome agentic AI patterns

Awesome Agentic Patterns
========================

[![Awesome Agentic Patterns](/nibzard/awesome-agentic-patterns/raw/main/agentic-patterns.jpeg)](/nibzard/awesome-agentic-patterns/blob/main/agentic-patterns.jpeg)

A curated catalogue of **agentic AI patterns** — real‑world tricks, workflows, and mini‑architectures that help autonomous or semi‑autonomous AI agents get useful work done in production.

> **Why?**
> Tutorials show toy demos. Real products hide the messy bits. This list surfaces the repeatable patterns that bridge the gap so we can all ship smarter, faster agents.

---

What counts as a pattern?
-------------------------

* **Repeatable** – more than one team is using it.
* **Agent‑centric** – improves how an AI agent senses, reasons, or acts.
* **Traceable** – backed by a public reference: blog post, talk, repo, or paper.

If your link ticks those boxes, it belongs here.

---

🌐 Explore the Website
---------------------

**Visit:** <https://agentic-patterns.com>

The website offers powerful discovery tools beyond this README:

* **Pattern Explorer**: Browse, filter, and search all patterns by category, status, complexity, and more
* **Compare Tool**: Side-by-side comparison of multiple patterns with shared attributes
* **Decision Explorer**: Interactive guide to find the right pattern for your use case
* **Graph Visualization**: Visual map of pattern relationships and connections
* **Pattern Packs**: Curated collections of patterns for common agent architectures
* **Developer Guides**: In-depth documentation on pattern selection and usage
* **Dark Mode**: Full theme support for comfortable reading in any environment

Built with [Astro](https://astro.build), deployed on [Vercel](https://vercel.com), source code in [`apps/web/`](/nibzard/awesome-agentic-patterns/blob/main/apps/web).

---

Quick Tour of Categories
------------------------

| Category | What you'll find |
| --- | --- |
| [**Context & Memory**](#context-memory) | Sliding-window curation, vector cache, episodic memory |
| [**Feedback Loops**](#feedback-loops) | Compilers, CI, human review, self-healing retries |
| [**Learning & Adaptation**](#learning-adaptation) | Agent RFT, skill libraries, variance-based RL |
| [**Orchestration & Control**](#orchestration-control) | Task decomposition, sub-agent spawning, tool routing |
| [**Reliability & Eval**](#reliability-eval) | Guardrails, eval harnesses, logging, reproducibility |
| [**Security & Safety**](#security-safety) | Isolated VMs, PII tokenization, security scanning |
| [**Tool Use & Environment**](#tool-use-environment) | Shell, browser, DB, Playwright, sandbox tricks |
| [**UX & Collaboration**](#ux-collaboration) | Prompt hand-offs, staged commits, async background agents |

*Categories are fluid — open a PR if you see a better slice!*
The tables below are auto‑generated from the `patterns/` folder.

---

### Context & Memory

* [Agent-Powered Codebase Q&A / Onboarding](/nibzard/awesome-agentic-patterns/blob/main/patterns/agent-powered-codebase-qa-onboarding.md)
* [Context Window Anxiety Management](/nibzard/awesome-agentic-patterns/blob/main/patterns/context-window-anxiety-management.md)
* [Context Window Auto-Compaction](/nibzard/awesome-agentic-patterns/blob/main/patterns/context-window-auto-compaction.md)
* [Context-Minimization Pattern](/nibzard/awesome-agentic-patterns/blob/main/patterns/context-minimization-pattern.md)
* [Curated Code Context Window](/nibzard/awesome-agentic-patterns/blob/main/patterns/curated-code-context-window.md)
* [Curated File Context Window](/nibzard/awesome-agentic-patterns/blob/main/patterns/curated-file-context-window.md)
* [Dynamic Context Injection](/nibzard/awesome-agentic-patterns/blob/main/patterns/dynamic-context-injection.md)
* [Episodic Memory Retrieval & Injection](/nibzard/awesome-agentic-patterns/blob/main/patterns/episodic-memory-retrieval-injection.md)
* [Filesystem-Based Agent State](/nibzard/awesome-agentic-patterns/blob/main/patterns/filesystem-based-agent-state.md)
* [Layered Configuration Context](/nibzard/awesome-agentic-patterns/blob/main/patterns/layered-configuration-context.md)
* [Memory Synthesis from Execution Logs](/nibzard/awesome-agentic-patterns/blob/main/patterns/memory-synthesis-from-execution-logs.md)
* [Proactive Agent State Externalization](/nibzard/awesome-agentic-patterns/blob/main/patterns/proactive-agent-state-externalization.md)
* [Progressive Disclosure for Large Files](/nibzard/awesome-agentic-patterns/blob/main/patterns/progressive-disclosure-large-files.md)
* [Prompt Caching via Exact Prefix Preservation](/nibzard/awesome-agentic-patterns/blob/main/patterns/prompt-caching-via-exact-prefix-preservation.md)
* [Schema-Guided Graph Retrieval for Multi-Hop Reasoning](/nibzard/awesome-agentic-patterns/blob/main/patterns/schema-guided-graph-retrieval.md)
* [Self-Identity Accumulation](/nibzard/awesome-agentic-patterns/blob/main/patterns/self-identity-accumulation.md)
* [Semantic Context Filtering Pattern](/nibzard/awesome-agentic-patterns/blob/main/patterns/semantic-context-filtering.md)
* [Session-Scoped Context Runtime for Agent Tools](/nibzard/awesome-agentic-patterns/blob/main/patterns/session-scoped-context-runtime-for-agent-tools.md)
* [Tool Search Lazy Loading](/nibzard/awesome-agentic-patterns/blob/main/patterns/tool-search-lazy-loading.md)
* [Working Memory via TodoWrite](/nibzard/awesome-agentic-patterns/blob/main/patterns/working-memory-via-todos.md)

### Feedback Loops

* [AI-Assisted Code Review / Verification](/nibzard/awesome-agentic-patterns/blob/main/patterns/ai-assisted-code-review-verification.md)
* [Background Agent with CI Feedback](/nibzard/awesome-agentic-patterns/blob/main/patterns/background-agent-ci.md)
* [Coding Agent CI Feedback Loop](/nibzard/awesome-agentic-patterns/blob/main/patterns/coding-agent-ci-feedback-loop.md)
* [Dogfooding with Rapid Iteration for Agent Improvement](/nibzard/awesome-agentic-patterns/blob/main/patterns/dogfooding-with-rapid-iteration-for-agent-improvement.md)
* [Graph of Thoughts (GoT)](/nibzard/awesome-agentic-patterns/blob/main/patterns/graph-of-thoughts.md)
* [Incident-to-Eval Synthesis](/nibzard/awesome-agentic-patterns/blob/main/patterns/incident-to-eval-synthesis.md)
* [Inference-Healed Code Review Reward](/nibzard/awesome-agentic-patterns/blob/main/patterns/inference-healed-code-review-reward.md)
* [Iterative Prompt & Skill Refinement](/nibzard/awesome-agentic-patterns/blob/main/patterns/iterative-prompt-skill-refinement.md)
* [Reflection Loop](/nibzard/awesome-agentic-patterns/blob/main/patterns/reflection.md)
* [Rich Feedback Loops > Perfect Prompts](/nibzard/awesome-agentic-patterns/blob/main/patterns/rich-feedback-loops.md)
* [Self-Critique Evaluator Loop](/nibzard/awesome-agentic-patterns/blob/main/patterns/self-critique-evaluator-loop.md)
* [Self-Discover: LLM Self-Composed Reasoning Structures](/nibzard/awesome-agentic-patterns/blob/main/patterns/self-discover-reasoning-structures.md)
* [Spec-As-Test Feedback Loop](/nibzard/awesome-agentic-patterns/blob/main/patterns/spec-as-test-feedback-loop.md)
* [Tool Use Incentivization via Reward Shaping](/nibzard/awesome-agentic-patterns/blob/main/patterns/tool-use-incentivization-via-reward-shaping.md)

### Learning & Adaptation

* [Agent Reinforcement Fine-Tuning (Agent RFT)](/nibzard/awesome-agentic-patterns/blob/main/patterns/agent-reinforcement-fine-tuning.md)
* [Compounding Engineering Pattern](/nibzard/awesome-agentic-patterns/blob/main/patterns/compounding-engineering-pattern.md)
* [Frontier-Focused Development](/nibzard/awesome-agentic-patterns/blob/main/patterns/frontier-focused-development.md)
* [Memory Reinforcement Learning (MemRL)](/nibzard/awesome-agentic-patterns/blob/main/patterns/memory-reinforcement-learning-memrl.md)
* [Shipping as Research](/nibzard/awesome-agentic-patterns/blob/main/patterns/shipping-as-research.md)
* [Skill Library Evolution](/nibzard/awesome-agentic-patterns/blob/main/patterns/skill-library-evolution.md)
* [Variance-Based RL Sample Selection](/nibzard/awesome-agentic-patterns/blob/main/patterns/variance-based-rl-sample-selection.md)

### Orchestration & Control

* [Action-Selector Pattern](/nibzard/awesome-agentic-patterns/blob/main/patterns/action-selector-pattern.md)
* [Agent Modes by Model Personality](/nibzard/awesome-agentic-patterns/blob/main/patterns/agent-modes-by-model-personality.md)
* [Agent-Driven Research](/nibzard/awesome-agentic-patterns/blob/main/patterns/agent-driven-research.md)
* [Artifact-Driven Analysis Pipeline Orchestration](/nibzard/awesome-agentic-patterns/blob/main/patterns/multi-step-analysis-pipeline-orchestration.md)
* [Autonomous Workflow Agent Architecture](/nibzard/awesome-agentic-patterns/blob/main/patterns/autonomous-workflow-agent-architecture.md)
* [Budget-Aware Model Routing with Hard Cost Caps](/nibzard/awesome-agentic-patterns/blob/main/patterns/budget-aware-model-routing-with-hard-cost-caps.md)
* [Burn the Boats](/nibzard/awesome-agentic-patterns/blob/main/patterns/burn-the-boats.md)
* [Capability-Escrow-Receipt](/nibzard/awesome-agentic-patterns/blob/main/patterns/capability-escrow-receipt.md)
* [Conditional Parallel Tool Execution](/nibzard/awesome-agentic-patterns/blob/main/patterns/parallel-tool-execution.md)
* [Continuous Autonomous Task Loop Pattern](/nibzard/awesome-agentic-patterns/blob/main/patterns/continuous-autonomous-task-loop-pattern.md)
* [Cross-Cycle Consensus Relay](/nibzard/awesome-agentic-patterns/blob/main/patterns/cross-cycle-consensus-relay.md)
* [Custom Sandboxed Background Agent](/nibzard/awesome-agentic-patterns/blob/main/patterns/custom-sandboxed-background-agent.md)
* [Declarative Multi-Agent Topology Definition](/nibzard/awesome-agentic-patterns/blob/main/patterns/declarative-multi-agent-topology-definition.md)
* [Deterministic Zero-LLM Orchestration](/nibzard/awesome-agentic-patterns/blob/main/patterns/deterministic-zero-llm-orchestration.md)
* [Discrete Phase Separation](/nibzard/awesome-agentic-patterns/blob/main/patterns/discrete-phase-separation.md)
* [Disposable Scaffolding Over Durable Features](/nibzard/awesome-agentic-patterns/blob/main/patterns/disposable-scaffolding-over-durable-features.md)
* [Distributed Execution with Cloud Workers](/nibzard/awesome-agentic-patterns/blob/main/patterns/distributed-execution-cloud-workers.md)
* [Dual LLM Pattern](/nibzard/awesome-agentic-patterns/blob/main/patterns/dual-llm-pattern.md)
* [Economic Value Signaling in Multi-Agent Networks](/nibzard/awesome-agentic-patterns/blob/main/patterns/economic-value-signaling-multi-agent.md)
* [Explicit Posterior-Sampling Planner](/nibzard/awesome-agentic-patterns/blob/main/patterns/explicit-posterior-sampling-planner.md)
* [Factory over Assistant](/nibzard/awesome-agentic-patterns/blob/main/patterns/factory-over-assistant.md)
* [Feature List as Immutable Contract](/nibzard/awesome-agentic-patterns/blob/main/patterns/feature-list-as-immutable-contract.md)
* [Hybrid LLM/Code Workflow Coordinator](/nibzard/awesome-agentic-patterns/blob/main/patterns/hybrid-llm-code-workflow-coordinator.md)
* [Inference-Time Scaling](/nibzard/awesome-agentic-patterns/blob/main/patterns/inference-time-scaling.md)
* [Initializer-Maintainer Dual Agent Architecture](/nibzard/awesome-agentic-patterns/blob/main/patterns/initializer-maintainer-dual-agent.md)
* [Inversion of Control](/nibzard/awesome-agentic-patterns/blob/main/patterns/inversion-of-control.md)
* [Iterative Multi-Agent Brainstorming](/nibzard/awesome-agentic-patterns/blob/main/patterns/iterative-multi-agent-brainstorming.md)
* [Lane-Based Execution Queueing](/nibzard/awesome-agentic-patterns/blob/main/patterns/lane-based-execution-queueing.md)
* [Language Agent Tree Search (LATS)](/nibzard/awesome-agentic-patterns/blob/main/patterns/language-agent-tree-search-lats.md)
* [LLM Map-Reduce Pattern](/nibzard/awesome-agentic-patterns/blob/main/patterns/llm-map-reduce-pattern.md)
* [Multi-Model Orchestration for Complex Edits](/nibzard/awesome-agentic-patterns/blob/main/patterns/multi-model-orchestration-for-complex-edits.md)
* [Opponent Processor / Multi-Agent Debate Pattern](/nibzard/awesome-agentic-patterns/blob/main/patterns/opponent-processor-multi-agent-debate.md)
* [Oracle and Worker Multi-Model Approach](/nibzard/awesome-agentic-patterns/blob/main/patterns/oracle-and-worker-multi-model.md)
* [Parallel Tool Call Learning](/nibzard/awesome-agentic-patterns/blob/main/patterns/parallel-tool-call-learning.md)
* [Plan-Then-Execute Pattern](/nibzard/awesome-agentic-patterns/blob/main/patterns/plan-then-execute-pattern.md)
* [Planner-Worker Separation for Long-Running Agents](/nibzard/awesome-agentic-patterns/blob/main/patterns/planner-worker-separation-for-long-running-agents.md)
* [Progressive Autonomy with Model Evolution](/nibzard/awesome-agentic-patterns/blob/main/patterns/progressive-autonomy-with-model-evolution.md)
* [Progressive Complexity Escalation](/nibzard/awesome-agentic-patterns/blob/main/patterns/progressive-complexity-escalation.md)
* [Recursive Best-of-N Delegation](/nibzard/awesome-agentic-patterns/blob/main/patterns/recursive-best-of-n-delegation.md)
* [Self-Rewriting Meta-Prompt Loop](/nibzard/awesome-agentic-patterns/blob/main/patterns/self-rewriting-meta-prompt-loop.md)
* [Signal-Driven Agent Activation](/nibzard/awesome-agentic-patterns/blob/main/patterns/signal-driven-agent-activation.md)
* [Specification-Driven Agent Development](/nibzard/awesome-agentic-patterns/blob/main/patterns/specification-driven-agent-development.md)
* [Stop Hook Auto-Continue Pattern](/nibzard/awesome-agentic-patterns/blob/main/patterns/stop-hook-auto-continue-pattern.md)
* [Sub-Agent Spawning](/nibzard/awesome-agentic-patterns/blob/main/patterns/sub-agent-spawning.md)
* [Subject Hygiene for Task Delegation](/nibzard/awesome-agentic-patterns/blob/main/patterns/subject-hygiene.md)
* [Swarm Migration Pattern](/nibzard/awesome-agentic-patterns/blob/main/patterns/swarm-migration-pattern.md)
* [Three-Stage Perception Architecture](/nibzard/awesome-agentic-patterns/blob/main/patterns/three-stage-perception-architecture.md)
* [Tool Capability Compartmentalization](/nibzard/awesome-agentic-patterns/blob/main/patterns/tool-capability-compartmentalization.md)
* [Tool Selection Guide](/nibzard/awesome-agentic-patterns/blob/main/patterns/tool-selection-guide.md)
* [Tree-of-Thought Reasoning](/nibzard/awesome-agentic-patterns/blob/main/patterns/tree-of-thought-reasoning.md)
* [Workspace-Native Multi-Agent Orchestration](/nibzard/awesome-agentic-patterns/blob/main/patterns/workspace-native-multi-agent-orchestration.md)

### Reliability & Eval

* [Action Caching & Replay Pattern](/nibzard/awesome-agentic-patterns/blob/main/patterns/action-caching-replay.md)
* [Adaptive Sandbox Fan-Out Controller](/nibzard/awesome-agentic-patterns/blob/main/patterns/adaptive-sandbox-fanout-controller.md)
* [Agent Circuit Breaker](/nibzard/awesome-agentic-patterns/blob/main/patterns/agent-circuit-breaker.md)
* [Anti-Reward-Hacking Grader Design](/nibzard/awesome-agentic-patterns/blob/main/patterns/anti-reward-hacking-grader-design.md)
* [Asynchronous Coding Agent Pipeline](/nibzard/awesome-agentic-patterns/blob/main/patterns/asynchronous-coding-agent-pipeline.md)
* [Canary Rollout and Automatic Rollback for Agent Policy Changes](/nibzard/awesome-agentic-patterns/blob/main/patterns/canary-rollout-and-automatic-rollback-for-agent-policy-changes.md)
* [CriticGPT-Style Code Review](/nibzard/awesome-agentic-patterns/blob/main/patterns/criticgpt-style-evaluation.md)
* [Extended Coherence Work Sessions](/nibzard/awesome-agentic-patterns/blob/main/patterns/extended-coherence-work-sessions.md)
* [Failover-Aware Model Fallback](/nibzard/awesome-agentic-patterns/blob/main/patterns/failover-aware-model-fallback.md)
* [Lethal Trifecta Threat Model](/nibzard/awesome-agentic-patterns/blob/main/patterns/lethal-trifecta-threat-model.md)
* [LLM Observability](/nibzard/awesome-agentic-patterns/blob/main/patterns/llm-observability.md)
* [Merged Code + Language Skill Model](/nibzard/awesome-agentic-patterns/blob/main/patterns/merged-code-language-skill-model.md)
* [No-Token-Limit Magic](/nibzard/awesome-agentic-patterns/blob/main/patterns/no-token-limit-magic.md)
* [Output Verification Loop](/nibzard/awesome-agentic-patterns/blob/main/patterns/output-verification-loop.md)
* [Reliability Problem Map Checklist for RAG and Agents](/nibzard/awesome-agentic-patterns/blob/main/patterns/wfgy-reliability-problem-map.md)
* [RLAIF (Reinforcement Learning from AI Feedback)](/nibzard/awesome-agentic-patterns/blob/main/patterns/rlaif-reinforcement-learning-from-ai-feedback.md)
* [Schema Validation Retry with Cross-Step Learning](/nibzard/awesome-agentic-patterns/blob/main/patterns/schema-validation-retry-cross-step-learning.md)
* [Structured Output Specification](/nibzard/awesome-agentic-patterns/blob/main/patterns/structured-output-specification.md)
* [Subagent Compilation Checker](/nibzard/awesome-agentic-patterns/blob/main/patterns/subagent-compilation-checker.md)
* [Versioned Constitution Governance](/nibzard/awesome-agentic-patterns/blob/main/patterns/versioned-constitution-governance.md)
* [Workflow Evals with Mocked Tools](/nibzard/awesome-agentic-patterns/blob/main/patterns/workflow-evals-with-mocked-tools.md)

### Security & Safety

* [Black-Box Skill Invocation](/nibzard/awesome-agentic-patterns/blob/main/patterns/black-box-skill-invocation.md)
* [Cryptographic Governance Audit Trail](/nibzard/awesome-agentic-patterns/blob/main/patterns/cryptographic-governance-audit-trail.md)
* [Denial Tracking & Permission Escalation](/nibzard/awesome-agentic-patterns/blob/main/patterns/denial-tracking-permission-escalation.md)
* [Deterministic Security Scanning Build Loop](/nibzard/awesome-agentic-patterns/blob/main/patterns/deterministic-security-scanning-build-loop.md)
* [Deterministic Threat Rule Scanning](/nibzard/awesome-agentic-patterns/blob/main/patterns/deterministic-threat-rule-scanning.md)
* [External Credential Sync](/nibzard/awesome-agentic-patterns/blob/main/patterns/external-credential-sync.md)
* [Hook-Based Safety Guard Rails for Autonomous Code Agents](/nibzard/awesome-agentic-patterns/blob/main/patterns/hook-based-safety-guard-rails.md)
* [Isolated VM per RL Rollout](/nibzard/awesome-agentic-patterns/blob/main/patterns/isolated-vm-per-rl-rollout.md)
* [Non-Custodial Spending Controls](/nibzard/awesome-agentic-patterns/blob/main/patterns/non-custodial-spending-controls.md)
* [PII Tokenization](/nibzard/awesome-agentic-patterns/blob/main/patterns/pii-tokenization.md)
* [Policy-Gated Tool Proxy](/nibzard/awesome-agentic-patterns/blob/main/patterns/policy-gated-tool-proxy.md)
* [Sandboxed Tool Authorization](/nibzard/awesome-agentic-patterns/blob/main/patterns/sandboxed-tool-authorization.md)
* [Soulbound Identity Verification](/nibzard/awesome-agentic-patterns/blob/main/patterns/soulbound-identity-verification.md)
* [Transitive Vouch-Chain Trust](/nibzard/awesome-agentic-patterns/blob/main/patterns/transitive-vouch-chain-trust.md)
* [Zero-Trust Agent Mesh](/nibzard/awesome-agentic-patterns/blob/main/patterns/zero-trust-agent-mesh.md)

### Tool Use & Environment

* [Agent SDK for Programmatic Control](/nibzard/awesome-agentic-patterns/blob/main/patterns/agent-sdk-for-programmatic-control.md)
* [Agent-First Tool Discovery](/nibzard/awesome-agentic-patterns/blob/main/patterns/agent-first-tool-discovery.md)
* [Agent-First Tooling and Logging](/nibzard/awesome-agentic-patterns/blob/main/patterns/agent-first-tooling-and-logging.md)
* [Agentic Search Over Vector Embeddings](/nibzard/awesome-agentic-patterns/blob/main/patterns/agentic-search-over-vector-embeddings.md)
* [AI Web Search Agent Loop](/nibzard/awesome-agentic-patterns/blob/main/patterns/ai-web-search-agent-loop.md)
* [CLI-First Skill Design](/nibzard/awesome-agentic-patterns/blob/main/patterns/cli-first-skill-design.md)
* [CLI-Native Agent Orchestration](/nibzard/awesome-agentic-patterns/blob/main/patterns/cli-native-agent-orchestration.md)
* [Code Mode MCP Tool Interface Improvement Pattern](/nibzard/awesome-agentic-patterns/blob/main/patterns/code-first-tool-interface-pattern.md)
* [Code-Over-API Pattern](/nibzard/awesome-agentic-patterns/blob/main/patterns/code-over-api-pattern.md)
* [Code-Then-Execute Pattern](/nibzard/awesome-agentic-patterns/blob/main/patterns/code-then-execute-pattern.md)
* [Cross-Protocol Agent Discovery](/nibzard/awesome-agentic-patterns/blob/main/patterns/cross-protocol-agent-discovery.md)
* [Dual-Use Tool Design](/nibzard/awesome-agentic-patterns/blob/main/patterns/dual-use-tool-design.md)
* [Dynamic Code Injection (On-Demand File Fetch)](/nibzard/awesome-agentic-patterns/blob/main/patterns/dynamic-code-injection-on-demand-file-fetch.md)
* [Egress Lockdown (No-Exfiltration Channel)](/nibzard/awesome-agentic-patterns/blob/main/patterns/egress-lockdown-no-exfiltration-channel.md)
* [Intelligent Bash Tool Execution](/nibzard/awesome-agentic-patterns/blob/main/patterns/intelligent-bash-tool-execution.md)
* [LLM-Friendly API Design](/nibzard/awesome-agentic-patterns/blob/main/patterns/llm-friendly-api-design.md)
* [MCP Pattern Injection](/nibzard/awesome-agentic-patterns/blob/main/patterns/mcp-pattern-injection.md)
* [Multi-Platform Communication Aggregation](/nibzard/awesome-agentic-patterns/blob/main/patterns/multi-platform-communication-aggregation.md)
* [Multi-Platform Webhook Triggers](/nibzard/awesome-agentic-patterns/blob/main/patterns/multi-platform-webhook-triggers.md)
* [Patch Steering via Prompted Tool Selection](/nibzard/awesome-agentic-patterns/blob/main/patterns/patch-steering-via-prompted-tool-selection.md)
* [Progressive Tool Discovery](/nibzard/awesome-agentic-patterns/blob/main/patterns/progressive-tool-discovery.md)
* [Shell Command Contextualization](/nibzard/awesome-agentic-patterns/blob/main/patterns/shell-command-contextualization.md)
* [Static Service Manifest for Agents](/nibzard/awesome-agentic-patterns/blob/main/patterns/static-service-manifest-for-agents.md)
* [Tool Use Steering via Prompting](/nibzard/awesome-agentic-patterns/blob/main/patterns/tool-use-steering-via-prompting.md)
* [Unified Tool Gateway](/nibzard/awesome-agentic-patterns/blob/main/patterns/unified-tool-gateway.md)
* [Virtual Machine Operator Agent](/nibzard/awesome-agentic-patterns/blob/main/patterns/virtual-machine-operator-agent.md)
* [Visual AI Multimodal Integration](/nibzard/awesome-agentic-patterns/blob/main/patterns/visual-ai-multimodal-integration.md)

### UX & Collaboration

* [Abstracted Code Representation for Review](/nibzard/awesome-agentic-patterns/blob/main/patterns/abstracted-code-representation-for-review.md)
* [Agent-Assisted Scaffolding](/nibzard/awesome-agentic-patterns/blob/main/patterns/agent-assisted-scaffolding.md)
* [Agent-Friendly Workflow Design](/nibzard/awesome-agentic-patterns/blob/main/patterns/agent-friendly-workflow-design.md)
* [AI-Accelerated Learning and Skill Development](/nibzard/awesome-agentic-patterns/blob/main/patterns/ai-accelerated-learning-and-skill-development.md)
* [Chain-of-Thought Monitoring & Interruption](/nibzard/awesome-agentic-patterns/blob/main/patterns/chain-of-thought-monitoring-interruption.md)
* [Codebase Optimization for Agents](/nibzard/awesome-agentic-patterns/blob/main/patterns/codebase-optimization-for-agents.md)
* [Democratization of Tooling via Agents](/nibzard/awesome-agentic-patterns/blob/main/patterns/democratization-of-tooling-via-agents.md)
* [Dev Tooling Assumptions Reset](/nibzard/awesome-agentic-patterns/blob/main/patterns/dev-tooling-assumptions-reset.md)
* [Human-in-the-Loop Approval Framework](/nibzard/awesome-agentic-patterns/blob/main/patterns/human-in-loop-approval-framework.md)
* [Latent Demand Product Discovery](/nibzard/awesome-agentic-patterns/blob/main/patterns/latent-demand-product-discovery.md)
* [Milestone Escrow for Agent Resource Funding](/nibzard/awesome-agentic-patterns/blob/main/patterns/agentfund-crowdfunding.md)
* [Proactive Trigger Vocabulary](/nibzard/awesome-agentic-patterns/blob/main/patterns/proactive-trigger-vocabulary.md)
* [Seamless Background-to-Foreground Handoff](/nibzard/awesome-agentic-patterns/blob/main/patterns/seamless-background-to-foreground-handoff.md)
* [Spectrum of Control / Blended Initiative](/nibzard/awesome-agentic-patterns/blob/main/patterns/spectrum-of-control-blended-initiative.md)
* [Team-Shared Agent Configuration as Code](/nibzard/awesome-agentic-patterns/blob/main/patterns/team-shared-agent-configuration.md)
* [Verbose Reasoning Transparency](/nibzard/awesome-agentic-patterns/blob/main/patterns/verbose-reasoning-transparency.md)

---

For AI Assistants (llms.txt)
----------------------------

This project includes [`llms.txt`](https://agentic-patterns.com/llms.txt), a machine-readable documentation file designed to help AI assistants and LLMs understand and recommend appropriate patterns.

**What's included:**

* Pattern categories and their purposes
* Key patterns with concise descriptions
* Usage guidelines for AI assistants
* Pattern selection strategies based on use case requirements

**For developers building AI assistants:**
The `llms.txt` file can be provided to LLMs as context to improve pattern recommendations. It's optimized for:

* RAG systems indexing this catalogue
* AI coding assistants suggesting patterns
* LLM-powered tools that recommend agentic patterns

**Access:** <https://agentic-patterns.com/llms.txt> (also available in [`apps/web/public/llms.txt`](/nibzard/awesome-agentic-patterns/blob/main/apps/web/public/llms.txt))

---

Contributing in 3 steps
-----------------------

1. **Fork & branch** → `git checkout -b add-my-pattern`
2. **Add a pattern file** under `patterns/` using the template above.
3. **Run** `bun run build:data` to refresh the generated README sections and site data.
4. **Open a PR** titled `Add: my-pattern-name`.
5. This repository is pattern-first: proposals that are primarily product announcements or promotions will be rejected, even if technically valid.

See [`CONTRIBUTING.md`](https://github.com/nibzard/awesome-agentic-patterns/blob/main/CONTRIBUTING.md) for the fine print.

---

Inspiration
-----------

This project started after the write‑up [**"What Sourcegraph learned building AI coding agents"**](https://www.nibzard.com/ampcode) (28 May 2025) and the ongoing *Raising an Agent* video diary. Many first patterns come straight from those lessons — thanks to everyone sharing their journey in the open!

---

License
-------

Apache‑2.0. See [`LICENSE`](https://github.com/nibzard/awesome-agentic-patterns/blob/main/LICENSE).

---

Star History
------------

[![Star History Chart](https://camo.githubusercontent.com/3a190810f8f58aba47b04a84cca2ec29c85148a24d01544cb9784bb5ecf5798e/68747470733a2f2f6170692e737461722d686973746f72792e636f6d2f7376673f7265706f733d6e69627a6172642f617765736f6d652d6167656e7469632d7061747465726e7326747970653d64617465266c6567656e643d746f702d6c656674)](https://www.star-history.com/#nibzard/awesome-agentic-patterns&type=date&legend=top-left)
