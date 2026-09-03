---
id: 1330
url: https://www.darlinghq.org/
title: Darling |  macOS translation layer for Linux
domain: www.darlinghq.org
source_date: '2026-08-31'
tags:
- emulator
- devops
- c
summary: Darling is a free, open-source translation layer that enables users to run
  macOS software natively on Linux without hardware emulation, similar to how Wine
  works for Windows applications. It implements a complete Darwin environment and
  aims to integrate macOS apps seamlessly into the Linux desktop experience, though
  GUI support is still experimental. The project is based on Darwin source code released
  by Apple and welcomes contributions from developers interested in expanding its
  capabilities.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# Darling |  macOS translation layer for Linux

```
~ $ uname
Linux
~ $ darling shell
Darling [~]$ uname
Darwin
```

Darling
=======

Darling is a translation layer that lets you run macOS software on Linux

* Fast

  Darling runs macOS software directly without using a hardware emulator.
* Free

  Like Linux, Darling is free and open-source software.   
   It is developed openly on GitHub and distributed under the GNU GPL license version 3.
* Compatible

  Darling implements a complete Darwin environment. Mach, dyld, launchd — everything you'd expect.
* Easy to use

  Darling does most of the setup for you. Sit back and enjoy using your favorite software.
* Native

  We aim to fully integrate apps running under Darling into the Linux desktop experience by making them look, feel and behave just like native Linux apps.

* That sounds a lot like [Wine](https://www.winehq.org/)

  And it is! Wine lets you run Windows software on Linux, and Darling does the same for macOS software.
* Does it support GUI apps?

  Almost! This took us a lot of time and effort, but we finally have basic experimental support for running *simple* graphical applications.
* Does it violate Apple's EULA?

  No! We only directly use those parts of Darwin that are released as fully free software.
* Does the name Darling mean anything?

  The name Darling is a combination of “Darwin” and “Linux”. Darwin is the core operating system macOS and iOS are based on.
* Can I run Darling on Windows using WSL?

  With WSL 2, yes! See [the documentation](https://docs.darlinghq.org/wsl-build.html) for more details.
* Do you know about [opensource.apple.com](https://opensource.apple.com/), GNUstep, The Cocotron and other projects?

  We do, and in fact, Darling is largely based on the original Darwin source code published by Apple. We use The Cocotron as a basis for our Cocoa implementation, along with the [Apportable Foundation](https://github.com/apportable/Foundation) and various bits of GNUstep.
* Do you have plans for supporting iOS apps?

  Yes, in the long run, we'd like to be able to run iOS apps on ARM devices (like most Android phones). A significant challenge here would be to write our own implementation of UIKit. Come talk to us if you're interested in working on this!
* How do I contribute?

  Start by reading the [documentation](https://docs.darlinghq.org) and [our blog](http://blog.darlinghq.org) to get familiar with Darling internals. Then, come and join us [on GitHub](https://github.com/darlinghq/darling). It's great if you have experience in developing for macOS or iOS, but it's absolutely not required to start contributing.
