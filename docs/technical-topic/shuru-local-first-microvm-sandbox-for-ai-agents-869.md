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

Hero Local-First Sandboxes for AI Agents on macOS. Lightweight Linux VMs powered by Apple Virtualization.framework. Ephemeral by default. No Docker required. GET STARTED GITHUB Features Fast, Ephemeral, Stateful. Infrastructure for AI Agents. 01 Ephemeral by Default Every run starts from a clean rootfs. Install anything, break anything. Nothing persists unless you save it. 02 Checkpoints Save disk state as named snapshots. Restore, branch, and iterate. Like git commits for your environment. 03 Apple Silicon Native Built on Virtualization.framework. No emulation layer, no Docker dependency. Near-native speed on ARM64. grid: 3 cols CLI Simple CLI. Run, checkpoint, restore. feature Ephemeral runs Boot a fresh VM with a single command. Changes vanish on exit. Opt-in networking Sandboxes are offline by default. Enable NAT with one flag. Configurable resources Set CPUs, memory, and disk size per run or in a config file. Checkpoint & restore Save environments as snapshots. Branch and reuse across runs. Port forwarding Expose guest ports to the host. Works without network access. terminal $ shuru run -- echo "hello from the sandbox" hello from the sandbox $ shuru run -- cat /etc/os-release | head -1 NAME="Alpine Linux" # VM boots, runs, and tears down — nothing persists. $ shuru run -- ping -c1 8.8.8.8 ping: sendto: Operation not permitted $ shuru run --allow-net -- apk add python3 fetch https://dl-cdn.alpinelinux.org/... OK: 45 MiB in 28 packages $ shuru run --cpus 4 --memory 4096 -- free -m | head -2 total used free Mem: 4096 38 4002 $ shuru run --disk-size 2048 -- df -h / Filesystem Size Used Avail Use% Mounted on /dev/vda 2.0G 18M 1.9G 1% / $ shuru checkpoint create myenv --allow-net -- sh -c 'apk add nodejs npm' shuru: checkpoint 'myenv' saved $ shuru run --from myenv -- node -e 'console.log("ready")' ready # Restore any checkpoint instantly. Branch and reuse. $ shuru checkpoint create py --allow-net -- apk add python3 shuru: checkpoint 'py' saved $ shuru run --from py -p 8080:8000 -- python3 -m http.server 8000 shuru: forwarding 127.0.0.1:8080 -> guest:8000 $ curl http://127.0.0.1:8080/ <!DOCTYPE HTML>... # No --allow-net needed. Tunneled over vsock. Use Cases Built for Agents. Safe execution for any workload. 01 Code Execution Run AI-generated code in isolated VMs with real-time output. 02 Tool Use Let agents install packages, compile code, and use system tools safely. 03 Evaluations Spin up parallel sandboxes for reproducible evals across environments. 04 Development Disposable Linux environments for testing, debugging, and prototyping. Install Get started in seconds. One command to install. One command to run. terminal # Install $ curl -fsSL https://shuru.run/install.sh | sh # Run your first sandbox $ shuru run
