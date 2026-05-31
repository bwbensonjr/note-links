---
id: 869
url: https://shuru.run/
title: shuru - Local-first microVM sandbox for AI agents
domain: shuru.run
source_date: '2026-02-23'
tags:
- ai
- devops
- security
- cli-tool
summary: Shuru is a local-first microVM sandbox platform for macOS that enables safe,
  isolated execution of AI agent code using Apple's Virtualization framework without
  requiring Docker. Key features include ephemeral VMs that start clean on each run,
  checkpoint/restore functionality for saving and branching environments, and Apple
  Silicon native performance with configurable resources and optional networking.
  It's designed for code execution, tool use, evaluations, and development workflows
  where disposable Linux environments are needed.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# shuru - Local-first microVM sandbox for AI agents

Hero

Local-First Sandboxes
  for AI Agents on macOS & Linux.
=======================================================

Lightweight Linux VMs powered by Apple Virtualization.framework on macOS
and KVM on Linux ARM64. Ephemeral by default. No Docker required.

[GET STARTED](#get-started) [GITHUB](https://github.com/superhq-ai/shuru)

Features

Fast, Ephemeral, Stateful.
  Infrastructure for AI Agents.
----------------------------------------------------------

01

### Ephemeral by Default

Every run starts from a clean rootfs. Install anything, break anything. Nothing persists unless you save it.

![Ephemeral container dissolving](/images/card-ephemeral.svg)

02

### Checkpoints

Save disk state as named snapshots. Restore, branch, and iterate. Like git commits for your environment.

![Git DAG branching checkpoint tree](/images/card-checkpoints.svg)

03

### Apple Silicon Native

Built on Virtualization.framework. No emulation layer, no Docker dependency. Near-native speed on ARM64.

![Apple Silicon chip with lightning bolt](/images/card-native.svg)

grid: 3 cols

CLI

Simple CLI.
  Run, checkpoint, restore.
---------------------------------------

[feature

### Ephemeral runs

Boot a fresh VM with a single command. Changes vanish on exit.](#ephemeral-runs)[### Opt-in networking

Sandboxes are offline by default. Enable networking with one flag.](#networking)[### Configurable resources

Set CPUs, memory, and disk size per run or in a config file.](#resources)[### Directory mounts

Share host directories into the VM. Read-only by default; opt in to host writes with :rw.](#mounts)[### Checkpoint & restore

Save environments as snapshots. Branch and reuse across runs.](#checkpoints)[### Port forwarding

Expose guest ports to the host. Works without network access.](#port-forwarding)

terminal

$ shuru run -- echo "hello from the sandbox"

hello from the sandbox

  

$ shuru run -- cat /etc/os-release | head -1

NAME="Debian GNU/Linux"

  

# VM boots, runs, and tears down — nothing persists.

$ shuru run -- curl https://example.com

curl: (6) Could not resolve host: example.com

  

$ shuru run --allow-net -- curl -s https://example.com | head -1

<!doctype html>

  

# Sandboxes are offline by default. All traffic goes through a proxy.

$ shuru run --cpus 4 --memory 4096 -- free -m | head -2

total used free

Mem: 4096 38 4002

  

$ shuru run --disk-size 2048 -- df -h /

Filesystem Size Used Avail Use% Mounted on

/dev/vda 2.0G 18M 1.9G 1% /

$ shuru run --mount ./src:/workspace -- ls /workspace

main.py utils.py tests/

# Read-only by default — guest writes stay in a tmpfs overlay.

  

$ shuru run --allow-host-writes --mount ./src:/workspace:rw -- touch /workspace/new.py

# With :rw + --allow-host-writes, guest writes land on the host.

$ shuru checkpoint create myenv --allow-net -- sh -c 'apt-get install -y nodejs npm'

shuru: checkpoint 'myenv' saved

  

$ shuru run --from myenv -- node -e 'console.log("ready")'

ready

  

# Restore any checkpoint instantly. Branch and reuse.

$ shuru checkpoint create py --allow-net -- apt-get install -y python3

shuru: checkpoint 'py' saved

  

$ shuru run --from py -p 8080:8000 -- python3 -m http.server 8000

shuru: forwarding 127.0.0.1:8080 -> guest:8000

  

$ curl http://127.0.0.1:8080/

<!DOCTYPE HTML>...

  

# No --allow-net needed. Tunneled over vsock.

Use Cases

Built for Agents.
  Safe execution for any workload.
----------------------------------------------------

01

### Code Execution

Run AI-generated code in isolated VMs with real-time output.

![Terminal with code execution](/images/usecase-code.svg)

02

### Tool Use

Let agents install packages, compile code, and use system tools safely.

![Gears and package installation](/images/usecase-tools.svg)

03

### Evaluations

Spin up parallel sandboxes for reproducible evals across environments.

![Parallel evaluation pipeline](/images/usecase-evals.svg)

04

### Development

Disposable Linux environments for testing, debugging, and prototyping.

![Laptop with floating sandbox](/images/usecase-dev.svg)

Config

Configure per project.
  One file, full control.
------------------------------------------------

Define allowed domains, secrets, and resources in a single shuru.json file.

[config

### Secret injection

API key stays on host. Guest gets a placeholder token.](#secret-injection)[### Domain allowlist

Lock down which domains the agent can reach.](#domain-allowlist)[### Multi-provider

Multiple API keys for different services.](#multi-provider)[### Full config

Resources, mounts, secrets, and network together.](#full-config)

shuru.json

{

"secrets": {

"API\_KEY": {

"from": "OPENAI\_API\_KEY",

"hosts": ["api.openai.com"]

}

},

"network": {

"allow": ["api.openai.com"]

}

}

{

"network": {

"allow": [

"registry.npmjs.org",

"github.com",

"\*.githubusercontent.com"

]

}

}

{

"secrets": {

"OPENAI\_KEY": {

"from": "OPENAI\_API\_KEY",

"hosts": ["api.openai.com"]

},

"ANTHROPIC\_KEY": {

"from": "ANTHROPIC\_API\_KEY",

"hosts": ["api.anthropic.com"]

}

},

"network": {

"allow": ["api.openai.com", "api.anthropic.com"]

}

}

{

"cpus": 4,

"memory": 4096,

"mounts": ["./src:/workspace"],

"secrets": {

"API\_KEY": {

"from": "OPENAI\_API\_KEY",

"hosts": ["api.openai.com"]

}

},

"network": {

"allow": ["api.openai.com"]

}

}

Skill

Works with your agent.
  Install once, sandbox everything.
----------------------------------------------------------

Shuru ships as an [agent skill](https://agentskills.io).
Once installed, AI agents automatically use shuru run whenever they need sandboxed execution — no prompting required.

### Install with one command

Works across Claude Code, Cursor, Copilot, and more.

terminal

$ npx skills add superhq-ai/shuru

Works with Claude Code Cursor GitHub Copilot Gemini CLI OpenAI Codex + more

Install

Get started in seconds.
-----------------------

One command to install. One command to run.

### macOS

Apple Silicon

[Homebrew](#macos-homebrew)  [Script](#macos-script)

# Install

$  brew tap superhq-ai/tap && brew install shuru

  

# Run your first sandbox

$  shuru run

# Install

$  curl -fsSL https://shuru.run/install.sh | sh

  

# Run your first sandbox

$  shuru run

### Linux

ARM64 · KVM

[Script](#linux-script) [Setup guide →](/linux)

# Check KVM access

$  ls /dev/kvm && groups | grep -q kvm

  

# Install

$  curl -fsSL https://shuru.run/install.sh | sh

  

# Run your first sandbox

$  shuru run
