---
id: 734
url: https://cua.ai/docs/lume/guide/getting-started/introduction
title: What is Lume? | Cua
domain: cua.ai
source_date: '2026-01-19'
tags:
- cli-tool
- devops
- tutorial
summary: Lume is an open-source macOS VM runtime built on Apple's Virtualization Framework
  that enables users to create and run macOS and Linux virtual machines at near-native
  speed on Apple Silicon. It can be used via CLI or HTTP API for various purposes
  including testing across macOS versions, automating tasks, running CI/CD pipelines,
  sandboxing risky operations, and powering AI agents. The tool requires Apple Silicon
  and offers features like efficient storage, Rosetta 2 support, and automated VM
  configuration.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# What is Lume? | Cua

GuideGetting Started

What is Lume?
=============

Introduction to Lume - the macOS VM CLI and framework

Lume is a VM runtime for building AI agents, running CI/CD pipelines, and automating macOS. It uses Apple's native Virtualization Framework to run macOS and Linux VMs at near-native speed on Apple Silicon.

MIT License

Lume is open-source and MIT licensed. If you find it useful, we'd appreciate a [star on
GitHub](https://github.com/trycua/cua)!

Cloud macOS Sandboxes

We're piloting a managed service for customers who want to run cloud macOS sandboxes for CI/CD and
agent workloads. [Book a demo](https://cal.com/cua/cua-demo?overlayCalendar=true) if you're
interested.

```
lume create test-vm --os macos --ipsw latest
lume run test-vm
```

A single binary with an HTTP API. Create a VM, run it headlessly, control it programmatically.

[Architecture](#architecture)
-----------------------------

![Lume Architecture](/docs/_next/image?url=%2Fdocs%2F_next%2Fstatic%2Fmedia%2Flume-architecture.f28fc4a4.png&w=3840&q=75)

You can use Lume directly via CLI, or run `lume serve` to expose an HTTP API for programmatic access. The [Computer SDK](/docs/cua/reference/computer-sdk) uses this API to automate macOS interactions.

[How it works](#how-it-works)
-----------------------------

Lume is a thin layer over Apple's [Virtualization Framework](https://developer.apple.com/documentation/virtualization), which provides hardware-accelerated virtualization on Apple Silicon. This gives you:

* **Native speed** — CPU instructions execute directly via hardware virtualization
* **Paravirtualized graphics** — Basic GPU support via Apple's virtualization layer (limited to GPU Family 5)
* **Efficient storage** — Sparse disk files only consume actual usage, not allocated size
* **Rosetta 2 support** — Run x86 Linux binaries in ARM Linux VMs
* **Automated golden images** — Go from IPSW to fully configured macOS VM without manual intervention
* **Registry support** — Pull and push VM images from GHCR or GCS registries

[When to use Lume](#when-to-use-lume)
-------------------------------------

**Testing across macOS versions** — Spin up a VM with a specific macOS version, test your software, tear it down. No need to maintain multiple physical machines.

**Automating macOS tasks** — Combine Lume with [Unattended Setup](/docs/lume/guide/fundamentals/unattended-setup) to create pre-configured VMs. The setup automation uses VNC and OCR to click through the Setup Assistant without manual intervention.

**Running CI/CD locally** — Test your macOS builds in isolated VMs before pushing to remote CI. The `--no-display` flag runs VMs headlessly.

**Sandboxing risky operations** — Need to test untrusted software or destructive scripts? Run them in a VM, then delete it. Clone a known-good VM to reset to a clean state instantly.

**Building AI agents** — Lume powers the [Cua Computer SDK](/docs/cua/reference/computer-sdk), providing VMs that AI models can interact with through screenshots and input simulation.

Used by Anthropic

Apple's Virtualization Framework—the same technology Lume is built on—powers [Claude
Cowork](https://support.claude.com/en/articles/13345190-getting-started-with-cowork), Anthropic's
sandboxed environment for Claude Code. It downloads a Linux root filesystem and boots it in an
isolated VM where Claude can safely execute commands without access to your broader system.

[What Lume doesn't do](#what-lume-doesnt-do)
--------------------------------------------

Lume requires Apple Silicon—it won't work on Intel Macs or other platforms.

[Get started](#get-started)
---------------------------

Ready to try it? [Install Lume](/docs/lume/guide/getting-started/installation) and create your first VM in the [Quickstart](/docs/lume/guide/getting-started/quickstart).

Was this page helpful?

YesNo
