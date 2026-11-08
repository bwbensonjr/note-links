---
id: 1470
url: https://meccanicos.com/
title: MeccanicOS
domain: meccanicos.com
source_date: '2026-11-07'
tags:
- nix
- security
- ai
- cli-tool
summary: MeccanicOS is a NixOS-based Linux distribution that runs from USB or installs
  to disk, with an included tool that downloads the latest ISO and makes a bootable
  USB drive on Windows, macOS, or Linux. Its key features include a keyboard-first
  command bar (Super+Space), full offline operation with a broad set of bundled drivers,
  encrypted storage and vaults, atomic upgrades with rollback, and optional local
  or cloud AI chat.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-5-5
---

# MeccanicOS

Make a USB drive
----------------

One small program does it all: it downloads the latest MeccanicOS, checks it,
and makes a USB drive (16 GB or larger) bootable with [Ventoy](https://www.ventoy.net), with MeccanicOS on it.
(On macOS, where Ventoy does not run, it writes MeccanicOS directly to the drive.)

### Windows

[Download mos-usb-windows.exe](https://github.com/unofficialtools/meccanicos/releases/download/latest/mos-usb-windows.exe)

Double-click it and allow it to make changes. If Windows warns about an unknown publisher: *More info* → *Run anyway*.

### macOS

In Terminal (Apple silicon; on an Intel Mac use `mos-usb-macos-x86_64`):

```
curl -fLO https://github.com/unofficialtools/meccanicos/releases/download/latest/mos-usb-macos-arm64
chmod +x mos-usb-macos-arm64
./mos-usb-macos-arm64
```

### Linux

In a terminal (on ARM use `mos-usb-linux-arm64`):

```
curl -fLO https://github.com/unofficialtools/meccanicos/releases/download/latest/mos-usb-linux-x86_64
chmod +x mos-usb-linux-x86_64
./mos-usb-linux-x86_64
```

Prefer to do it by hand? [Download the ISO](https://github.com/unofficialtools/meccanicos/releases/tag/latest) and follow
[Write it to a USB stick](https://github.com/unofficialtools/meccanicos#2-write-it-to-a-usb-stick).
Every MeccanicOS USB drive has a **MeccanicOS-README.pdf** on it: how to start the computer from the drive, and the BIOS settings if it does not.

Stuck, or have a question? Ask in the [MeccanicOS group](https://groups.google.com/g/meccanicos).

Principles
----------

Built on NixOS, but designed as one coherent system instead of a collection of unrelated Linux tools.

### Keyboard first

No start menu. Super+Space opens one command bar for apps, commands, websites, folders and questions.

### Works offline

The desktop, the included apps and the drivers are on the stick, and installing needs no network. More apps and local AI models are downloaded once, when you ask for them.

### Secure, with stated trade-offs

Installed: the whole disk encrypted (LUKS2). Live: the session stays in memory, and your vaults and persistent home are encrypted. A hardened kernel, a firewall, login alerts. For convenience `sudo` asks no password, and an installed system has an SSH server (keys only) that is off until you turn it on.

### Coherent

One way to open any file, one look for every tool, apps named by what they do: "Web Browser (Brave)".

### Reproducible

The whole system is one Nix flake. Upgrades are atomic: a failed one changes nothing, and you can roll back.

### Hardware first

MeccanicOS comes with a large collection of drivers and firmware (all of it freely redistributable): Mesa and Vulkan, video acceleration, PipeWire, Bluetooth, printers and scanners, NVIDIA's driver picked by itself. Hardening never gets in a driver's way.

### Free to share

Only freely redistributable software, so you may share any ISO you build.

Features
--------

What you get on the stick.

### Command bar

Type part of an app name, a website, a command, a path (`~/Documents` opens it in yazi) or `!command` to run it in a new shell. `?question` asks the AI.

### Live, persistent or installed

Run from USB with nothing kept, keep your home encrypted on the stick, or install to the disk from one page. [What survives a restart](https://github.com/unofficialtools/meccanicos#what-survives-a-restart).

### Encrypted vaults

LUKS2 vaults in the stick's free space, and on Ventoy sticks as files next to the ISO.

### Open anything

`open FILE` works like on a Mac, and the same rules apply in the shell, yazi, mc, fzf and on a double-click.

### Apps on demand

With a network: search nixpkgs' 120,000 packages, try an app without installing it, or give one folder its own tools with direnv.

### AI chat, your choice

Local AI after a one-time model download (Qwen3 through Ollama, ~2.5 GB; then offline, and nothing leaves the computer), or Claude, ChatGPT or Grok with your API key (your questions go to that company).

### Read aloud

Copy any text and an offline voice (Piper) reads it, sentence by sentence.

### Login alerts

An alert on an SSH login from somewhere new or an SSH attack, never more than a few an hour. One key disconnects everything.

### Backups like Time Machine

Encrypted, every night or when you plug in the disk, or to the cloud. Get back any earlier version of a file from a right-click.

### Settings and a doctor

Common settings in one place, exported to another computer in one file; a doctor that finds problems and offers a fix.

### Scales to the screen

Text grows with large and sharp screens by itself; icons keep their size.

### A terminal that helps

VictorMono Nerd Font, Atuin history, fzf, zoxide, yazi with image previews and drag and drop.

### Fleets (experimental)

Run all of an organization's computers on MeccanicOS from one MeccanicOS server, with git, SSH and SQLite: one repository says what each computer runs and who logs in where; disk unlocking with Tang, the TPM or a security key.

[Admin guide →](https://github.com/unofficialtools/meccanicos/blob/main/docs/fleet/ADMIN-GUIDE.md)

### A guided tour, and Help

A tutorial video with subtitles on every desktop, filmed in a VM from the same system; the manual is on the stick too (Help in the command bar).

MeccanicOS tools
----------------

You meet them by name in the command bar (Super+Space); in a terminal, every `mos-*` command answers `--help` and `mos` lists them all. The full-screen ones look and work the same way: a teal title bar, the keys at the bottom, and whatever Enter acts on in orange. Click a screenshot to enlarge it.

Pre-installed packages
----------------------

All on the stick, all working offline. More with `apps install NAME`.
