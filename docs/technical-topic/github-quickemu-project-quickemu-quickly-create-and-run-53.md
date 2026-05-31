---
id: 53
url: https://github.com/quickemu-project/quickemu
title: 'GitHub - quickemu-project/quickemu: Quickly create and run optimised Windows,
  macOS and Linux virtual machines'
domain: github.com
source_date: '2026-01-02'
tags:
- github-repo
- cli-tool
- devops
summary: Quickemu is a user-friendly wrapper for QEMU that simplifies creating and
  running optimized virtual machines for Windows, macOS, and Linux without requiring
  extensive configuration. The tool automates the setup process by automatically downloading
  OS images and configuring virtual machines with optimal settings for your hardware.
  It supports nearly 1,000 operating system editions and offers advanced features
  like file sharing, USB pass-through, clipboard sharing, and SSH port forwarding
  for both Linux and macOS hosts.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# GitHub - quickemu-project/quickemu: Quickly create and run optimised Windows, macOS and Linux virtual machines

[![Quickemu](/quickemu-project/quickemu/raw/master/.github/logo.png)](/quickemu-project/quickemu/blob/master/.github/logo.png)

Quickemu
========

**Quickly create and run optimised Windows, macOS and Linux virtual machines:**

**Made with 💝 for [![Tux (Linux)](/quickemu-project/quickemu/raw/master/.github/tux.png)](/quickemu-project/quickemu/blob/master/.github/tux.png) & [![Apple (macOS)](/quickemu-project/quickemu/raw/master/.github/apple.png)](/quickemu-project/quickemu/blob/master/.github/apple.png)**

[![Discord](https://camo.githubusercontent.com/4e8ee487a047ed8cee9c5544665adb7bee716baf1ba167e191b3c43efc77cad7/68747470733a2f2f696d672e736869656c64732e696f2f646973636f72642f3731323835303637323232333132353536353f7374796c653d666f722d7468652d6261646765266c6f676f3d646973636f7264266c6f676f436f6c6f723d253233666666666666266c6162656c3d446973636f7264266c6162656c436f6c6f723d25323334323533653826636f6c6f723d253233653465326532)](https://wimpysworld.io/discord) 
 [![Mastodon](https://camo.githubusercontent.com/570703e4da282f75e11929e34c9e06076790bddf4fe24e91861f4cc6433ce6ab/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4d6173746f646f6e2d3634363866613f7374796c653d666f722d7468652d6261646765266c6f676f3d6d6173746f646f6e266c6f676f436f6c6f723d253233666666666666)](https://fosstodon.org/@wimpy) 
 [![Twitter](https://camo.githubusercontent.com/606cd4dc4abd0e19d79703850c7d3b656dd8abb856d2aff203deaee271b2810d/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f547769747465722d3330333033303f7374796c653d666f722d7468652d6261646765266c6f676f3d78266c6f676f436f6c6f723d253233666666666666)](https://twitter.com/m_wimpress) 
 [![LinkedIn](https://camo.githubusercontent.com/32e353d0bc4fdd89385fb23e3ee65d9631d2b0cab07089b3ace38d7c5a1e7c47/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4c696e6b6564496e2d3136363762653f7374796c653d666f722d7468652d6261646765266c6f676f3d6c696e6b6564696e266c6f676f436f6c6f723d253233666666666666)](https://linkedin.com/in/martinwimpress)

Introduction
============

**Quickemu** is a wrapper for the excellent [QEMU](https://www.qemu.org/) that
automatically *"does the right thing"* when creating virtual machines. No
requirement for exhaustive configuration options. You decide what operating
system you want to run and Quickemu takes care of the rest 🤖

* `quickget` **automatically downloads the upstream OS** and creates the configuration 📀
* `quickemu` enumerates your hardware and launches the virtual machine with the **optimum configuration best suited to your computer** ⚡️

The original objective of the project was to [enable quick testing of Linux
distributions](https://github.com/quickemu-project/quickemu/wiki/02-Create-Linux-virtual-machines)
where the virtual machines and their configuration can be stored anywhere (such
as external USB storage or your home directory) and no elevated permissions are
required to run the virtual machines.

**Today, Quickemu includes comprehensive support for [macOS](https://github.com/quickemu-project/quickemu/wiki/03-Create-macOS-virtual-machines),
[Windows](https://github.com/quickemu-project/quickemu/wiki/04-Create-Windows-virtual-machines)**, most of the BSDs, novel non-Linux operating systems such as FreeDOS, Haiku, KolibriOS, OpenIndiana, ReactOS, and more.

Features
========

* Host support for **Linux and macOS**
* **macOS** Sequoia, Sonoma, Ventura, Monterey, Big Sur, Catalina & Mojave
* **Windows** 10 and 11 including TPM 2.0
* **Windows Server** 2022 2019 2016
* **ARM64 guest support** for running aarch64 VMs (native on ARM hosts, emulated on x86\_64)
* [Ubuntu](https://ubuntu.com/desktop) and all the **[official Ubuntu
  flavours](https://ubuntu.com/download/flavours)**
* **Nearly 1000 operating system editions are supported!**
* Full SPICE support including host/guest clipboard sharing
* VirtIO-webdavd file sharing for Linux and Windows guests
* VirtIO-9p file sharing for Linux and macOS guests
* [QEMU Guest Agent
  support](https://wiki.qemu.org/Features/GuestAgent); provides access
  to a system-level agent via standard QMP commands
* Samba file sharing for Linux, macOS and Windows guests (*if `smbd`
  is installed on the host*)
* VirGL acceleration
* USB device pass-through
* Smartcard pass-through
* Automatic SSH port forwarding to guests
* Network port forwarding
* Full duplex audio
* Braille support
* EFI (with or without SecureBoot) and Legacy BIOS boot

As featured on [Linux Matters](https://linuxmatters.sh) podcast!
----------------------------------------------------------------

The presenters of Linux Matters 🐧🎙️ are the creators of each of the principal Quickemu projects. We discussed Quickemu's 2024 reboot in [Episode 30 - Quickemu Rising From the Bashes](https://linuxmatters.sh/30).

[![Linux Matters Podcast](https://github.com/wimpysworld/nix-config/raw/main/.github/screenshots/linuxmatters.png)](https://linuxmatters.sh)
  
*Linux Matters Podcast*

Quick start
===========

[Once Quickemu is installed](https://github.com/quickemu-project/quickemu/wiki/01-Installation), there are two simple steps to create and run a virtual machine:

* `quickget` automatically downloads the ISO image for the operating system you want to run and creates a configuration file for the virtual machine.

```
quickget nixos unstable minimal
```

* `quickemu` starts the virtual machine using the configuration file created by `quickget`.

```
quickemu --vm nixos-unstable-minimal.conf
```

Execute `quickget` (with no arguments) to see a list of all the supported operating systems.

Demo
----

[![](https://camo.githubusercontent.com/0f486e084d20398a948361b2871b434f534ec4a4766e4b49848add85f9b2a006/68747470733a2f2f61736369696e656d612e6f72672f612f3635383134382e737667)](https://asciinema.org/a/658148?autoplay=1)

Documentation
=============

The wiki describes how to get up and running with Quickemu and also covers more advanced configuration and usage.

* [**Installation**](https://github.com/quickemu-project/quickemu/wiki/01-Installation) 💾
* [**Create Linux virtual machines**](https://github.com/quickemu-project/quickemu/wiki/02-Create-Linux-virtual-machines) 🐧
* [**Create macOS virtual machines**](https://github.com/quickemu-project/quickemu/wiki/03-Create-macOS-virtual-machines) 🍏
* [**Create Windows virtual machines**](https://github.com/quickemu-project/quickemu/wiki/04-Create-Windows-virtual-machines) 🪟
* [**Advanced quickemu configuration**](https://github.com/quickemu-project/quickemu/wiki/05-Advanced-quickemu-configuration) 🔧
* [**Advanced quickget features**](https://github.com/quickemu-project/quickemu/wiki/06-Advanced-quickget-features) 🤓
* [**Alternative frontends**](https://github.com/quickemu-project/quickemu/wiki/07-Alternative-frontends) 🧑‍💻
* [**References**](https://github.com/quickemu-project/quickemu/wiki/08-References) 📚️
