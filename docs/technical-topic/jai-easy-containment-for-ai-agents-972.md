---
id: 972
url: https://jai.scs.stanford.edu/
title: jai - easy containment for AI agents
domain: jai.scs.stanford.edu
source_date: '2026-03-28'
tags:
- ai
- security
- cli-tool
- devops
summary: jai is a lightweight Linux tool that provides effortless containment for
  AI agents by creating a sandboxed environment with minimal setup, addressing real
  incidents where AI tools have accidentally deleted files and corrupted user systems.
  It works by prefixing commands with "jai" to give agents access only to the working
  directory while protecting the rest of the home directory through copy-on-write
  overlays or complete isolation, depending on the selected mode. The tool fills the
  gap between trusting AI agents with full system access and the overhead of setting
  up containers or VMs, making safe AI agent usage practical for everyday workflows.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# jai - easy containment for AI agents

jai Go hard on agents, not on your filesystem. Use jai for effortless containment of AI agents on Linux. Get Started Security Model This is not hypothetical. ​ People are already reporting lost files, emptied working trees, and wiped home directories after giving AI tools ordinary machine access. 15 years of family photos “It’s not in trash; it was done via terminal.” Nick Davidov on X ↗ Claude Code wiped a home directory “Complete loss of active development projects.” Anthropic GitHub issue #10077 ↗ Cursor emptied a working tree “Everything just gone.” Cursor Community Forum ↗ Antigravity wiped a whole drive “My whole D drive was unintentionally wiped.” Reddit post ↗ Cursor deleted 100GB “decided to delete 100GB from my computer.” Cursor Community Forum ↗ ← → There's a gap between giving an agent your real account and stopping everything to build a container or VM. jai fills that gap. One command, no images, no Dockerfiles — just a light-weight boundary for the workflows you're already running: quick coding help, one-off local tasks, running installer scripts you didn't write. Your files, your rules Use AI agents without handing over your whole account. jai gives your working directory full access and keeps the rest of your home behind a copy-on-write overlay — or hidden entirely. Stop trusting blindly One-line installer scripts, AI-generated shell commands, unfamiliar CLIs — stop running them against your real home directory. Drop jai in front and the worst case gets a lot smaller. Containment shouldn't be hard No images to build, no Dockerfiles to maintain, no 40-flag bwrap invocations. Just jai your-agent . If containment isn't easier than YOLO mode, nobody will bother. How it works ​ One command. No setup required. 1 Prefix your command jai codex , jai claude , or just jai for a shell. 2 CWD stays writable Your working directory keeps full read/write access inside the jail. 3 Home is an overlay Changes to your home directory are captured copy-on-write. Originals are untouched. 4 Rest is locked down /tmp and /var/tmp are private. All other files are read-only. Three modes ​ Pick the level of isolation that fits your workflow. Casual Strict Bare Home directory Copy-on-write overlay Empty private home Empty private home Process runs as Your user Unprivileged jai user Your user Confidentiality Weak — most files readable Strong — separate UID Medium — your UID, but home hidden Integrity Overlay protects originals Full isolation Full isolation NFS home support Yes No Yes Learn more about modes → Free software, not a funnel ​ jai is free software, brought to you by the Stanford Secure Computer Systems research group and the Future of Digital Currency Initiative . The goal is to get people using AI more safely. Versus the alternatives ​ jai is not trying to replace containers. It fills a different niche. Docker Great for reproducible, image-based environments. Heavier to set up for ad-hoc sandboxing of host tools. No overlay-on-home workflow. bubblewrap Powerful namespace sandbox. Requires explicitly assembling the filesystem view — often turns into a long wrapper script, which is the friction jai removes. chroot Not a security mechanism. No mount isolation, no PID namespace, no credential separation. Linux documents it as not intended for sandboxing. Full comparison → jai is not a promise of perfect safety. jai is a casual sandbox — it reduces the blast radius, but does not eliminate all the ways AI agents can harm you or your system. Casual mode does not protect confidentiality. Even strict mode is not equivalent to a hardened container runtime or VM. When you need strong multi-tenant isolation or defense against a determined adversary, use a proper container or virtual machine. Read the full security model →
