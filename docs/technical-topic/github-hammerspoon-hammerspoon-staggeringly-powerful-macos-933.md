---
id: 933
url: https://github.com/Hammerspoon/hammerspoon?tab=readme-ov-file
title: 'GitHub - Hammerspoon/hammerspoon: Staggeringly powerful macOS desktop automation
  with Lua · GitHub'
domain: github.com
source_date: '2026-03-14'
tags:
- github-repo
- cli-tool
- devops
summary: Hammerspoon is a macOS desktop automation tool that bridges the operating
  system with a Lua scripting engine, allowing users to control various aspects of
  their OS X environment through custom scripts. The tool is installed either manually
  or via Homebrew and requires users to create and configure a Lua initialization
  file to enable automation functionality. The project aims to provide broader system
  API coverage, better extension integration, and an improved user experience for
  desktop automation tasks.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# GitHub - Hammerspoon/hammerspoon: Staggeringly powerful macOS desktop automation with Lua · GitHub

Hammerspoon
===========

[![CI](https://github.com/Hammerspoon/hammerspoon/workflows/CI/badge.svg)](https://github.com/Hammerspoon/hammerspoon/actions?query=workflow%3ACI)
[![codecov.io](https://camo.githubusercontent.com/2d089bb159213bf737ae6f182dbe7ac39f0e1396ed49c5ee9a453d5a3e91c6e6/68747470733a2f2f636f6465636f762e696f2f6769746875622f48616d6d657273706f6f6e2f68616d6d657273706f6f6e2f636f7665726167652e7376673f6272616e63683d6d6173746572)](https://codecov.io/github/Hammerspoon/hammerspoon?branch=master)
[![Downloads current release](https://camo.githubusercontent.com/6ddd625999826b9436ba8dfda7872697cbe33a93b42668563d8fec75630e0469/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f646f776e6c6f6164732f48616d6d657273706f6f6e2f68616d6d657273706f6f6e2f6c61746573742f746f74616c2e737667)](https://github.com/Hammerspoon/hammerspoon/releases)
[![Downloads all releases](https://camo.githubusercontent.com/d96d206320ee016a13854acb8f606b0276f7886ff24e9336f7e1bbbead6a80e2/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f646f776e6c6f6164732f48616d6d657273706f6f6e2f68616d6d657273706f6f6e2f746f74616c2e7376673f6d61784167653d32353932303030)](https://github.com/Hammerspoon/hammerspoon/releases)
[![Latest tag](https://camo.githubusercontent.com/4db7cd41adf93b9876fc868bdb13be57054bffc7a3b7f66fd324569e4022fac7/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f7461672f48616d6d657273706f6f6e2f68616d6d657273706f6f6e2e737667)](https://github.com/Hammerspoon/hammerspoon/tags)
[![Latest release](https://camo.githubusercontent.com/92956660a29d5f072a573d93e9087ca517c1711e02baf6b5db8cd920f5d9d666/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f72656c656173652f48616d6d657273706f6f6e2f68616d6d657273706f6f6e2e737667)](https://github.com/Hammerspoon/hammerspoon/releases/latest)

Discord: [Click to join](https://discord.gg/vxchqkRbkR)

What is Hammerspoon?
--------------------

This is a tool for powerful automation of OS X. At its core, Hammerspoon is just a bridge between the operating system and a Lua scripting engine.

What gives Hammerspoon its power is a set of extensions that expose specific pieces of system functionality, to the user. With these, you can write Lua scripts to control many aspects of your OS X environment.

How do I install it?
--------------------

### Manually

* Download the [latest release](https://github.com/Hammerspoon/hammerspoon/releases/latest)
* Drag `Hammerspoon.app` from your `Downloads` folder to `Applications`

### Homebrew

* `brew install hammerspoon --cask`

What next?
----------

Out of the box, Hammerspoon does nothing - you will need to create `~/.hammerspoon/init.lua` and fill it with useful code. There are several resources which can help you:

* [Getting Started Guide](https://www.hammerspoon.org/go/)
* [API docs](https://www.hammerspoon.org/docs/)
* [FAQ](https://www.hammerspoon.org/faq/)
* [Sample Configurations](https://github.com/Hammerspoon/hammerspoon/wiki/Sample-Configurations) supplied by various users
* [Contribution Guide](https://github.com/Hammerspoon/hammerspoon/blob/master/CONTRIBUTING.md) for developers looking to get involved
* An IRC channel for general chat/support/development (#hammerspoon on Libera)
* [Google Group](https://groups.google.com/forum/#!forum/hammerspoon/) for support

What is the history of the project?
-----------------------------------

Hammerspoon is a fork of [Mjolnir](https://github.com/mjolnirapp/mjolnir). Mjolnir aims to be a very minimal application, with its extensions hosted externally and managed using a Lua package manager. We wanted to provide a more integrated experience.

What is the future of the project?
----------------------------------

Our intentions for Hammerspoon broadly fall into these categories:

* Ever wider coverage of system APIs in Extensions
* Tighter integration between extensions
* Smoother user experience
