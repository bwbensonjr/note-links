---
id: 1134
url: http://www.ableton.com/en/live/extensions/
title: Extensions SDK
domain: www.ableton.com
source_date: '2026-06-04'
tags:
- javascript
- web-dev
- cli-tool
summary: Ableton Extensions is a new JavaScript-based SDK that allows users to build
  custom tools within Ableton Live 12 Suite, enabling them to automate tasks, transform
  MIDI data, analyze song structure, and customize Live's capabilities in ways it
  wasn't originally designed for. Extensions integrate directly into Live's workflow
  through a right-click context menu and can interact with tracks, clips, devices,
  and other Set elements, with a growing community sharing experimental tools on Discord.
  The SDK requires Node.js and is accessible to both developers and non-developers
  using AI coding assistants, offering a more flexible alternative to Max for Live
  focused on Set interaction rather than synthesis and signal processing.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# Extensions SDK

Break what’s expected. Make Live your own.
==========================================

[Start building](https://ableton.github.io/extensions-sdk# "Link will open in a new window/tab")
[Explore Extensions](#browse_extensions)

IntroducingExtensions
---------------------

Build Extensions that take Live Suite places it was never designed to go with a new, open JavaScript SDK.

![](https://beta-ableton.imgix.net/media/q2bhzti0/extensions-thumbnail.png?width=160&height=120&v=1dcf156aec1f320&fit=cropquality=100&format=webp)

screen reader text here

The Extensions SDK gives you the JavaScript API to build them: open, documented, and purpose-built for Live.  
[Get started](https://ableton.github.io/extensions-sdk "Extensions")

Extensions integrate directly into Live’s workflow. They can read your entire Set: tracks, clips, structure – and then rewrite it.

Tools with no rules
-------------------

Browse untested hacks, strange add-ons and experimental integrations – a starting point for your own ideas.

[Share and discover Extensions on Discord](https://discord.gg/ableton?ref=extensions)

[CLICK TO EXPAND]

BBenCut

![BBenCut](https://beta-ableton.imgix.net/media/mzjdexbj/bbencut-final.jpg?height=780&v=1dcf1576afbae00&fit=crop)

Photo MIDI

![Photo MIDI](https://beta-ableton.imgix.net/media/eq4hmem5/photo-midi-thumbnail-mbk-05-28.jpg?height=780&v=1dcf1576ad401c0&fit=crop)

Notation

![Notation](https://beta-ableton.imgix.net/media/hl5brz3x/notation-thumbnail-final.jpg?height=780&v=1dcf1576ab68eb0&fit=crop)

Paulstretch for Live

![Paulstretch for Live](https://beta-ableton.imgix.net/media/3dkmenoo/paulstretch-thumbnail-final.jpg?height=780&v=1dcf1576aa6b030&fit=crop)

Vivarium

![Vivarium](https://beta-ableton.imgix.net/media/qjyb4w04/vivarium-thumbnail-mbk-05-28.jpg?height=780&v=1dcf1576aeae520&fit=crop)

Beat Buddy

![Beat Buddy](https://beta-ableton.imgix.net/media/o5slajkp/beat-buddy-thumbnail-final.jpg?height=780&v=1dcf1576ac4bf80&fit=crop)

Bird Game

![Bird Game](https://beta-ableton.imgix.net/media/jhvjux1u/bird-game-thumbnail-final.jpg?height=780&v=1dcf1576a980a30&fit=crop)

RNMR

![RNMR](https://beta-ableton.imgix.net/media/intfn3fe/rnmr-thumbnail-final.jpg?height=780&v=1dcf1576a88c7f0&fit=crop)

![]()

### Expand, reshape and customize Live. Join the beta, download the SDK and start experimenting.

[Start building](https://ableton.github.io/extensions-sdk# "Link will open in a new window/tab")

### FAQs

[What are Extensions?](#collapse_e1b8cc93-67ff-434a-9c88-82b9d834c99d_1)

Ableton Extensions, introduced in Live 12.4.5, provide a way for users to develop and use their own tools within Ableton Live using the Ableton Extensions SDK.

Extensions can interact with tracks, clips, MIDI, devices, tempo, and other parts of a Live Set to automate tasks, transform musical data, and customize Live’s capabilities.

[In which versions and editions of Live are Extensions available?](#collapse_e1b8cc93-67ff-434a-9c88-82b9d834c99d_2)

Extensions are available in Live 12 Suite Beta, version 12.4.5 or later. Extensions are not available in Live Standard, Intro, or Lite.

[What can I do with Extensions?](#collapse_e1b8cc93-67ff-434a-9c88-82b9d834c99d_3)

Extensions can be programmed to affect tracks, clips, MIDI notes, devices, tempo and more. You can build Extensions to:

* Transform MIDI
* Analyze song and track structure
* Automate repetitive tasks
* Create unusual generative patterns
* Connect to external services
* Even play games in Live!

[How do I use Extensions in Live?](#collapse_e1b8cc93-67ff-434a-9c88-82b9d834c99d_4)

After you install an Extension in Live (via Settings → Extensions), here's how to access it:

* Right-click an item in your Set (e.g. a MIDI clip, track, or other item).
* Look in the context menu that appears.
* If the Extension can be used on that item, it will show up there.
* Click the name to run or edit the Extension.

After choosing it from the menu, a pop-up will appear in which you can alter the parameters of the Extension before running it. Triggering an extension causes it to run once, performing its task which returns a result or applies changes, then stop.

[What is needed to develop Extensions?](#collapse_e1b8cc93-67ff-434a-9c88-82b9d834c99d_5)

Developing with Extensions requires the following to be installed on your computer (macOS or Windows):

* The [Ableton Extensions SDK](https://ableton.github.io/extensions-sdk)
* [Node JS](https://nodejs.org/en/download)v24.16.0 (LTS)

[How do Extensions run inside Live?](#collapse_e1b8cc93-67ff-434a-9c88-82b9d834c99d_6)

Extensions are built on the NodeJS platform, a free, open-source, cross-platform JavaScript runtime environment. Extensions are triggered from the right-click context menu for the relevant item in your Set.

[How are Extensions different from Max for Live?](#collapse_e1b8cc93-67ff-434a-9c88-82b9d834c99d_7)

Max for Live is a deep creative patching environment offering synthesis, custom instruments and complex signal chains. Extensions are JavaScript-based tools that interact with the Set itself, affecting structure, data, and workflow.

[Do I need to be a developer to build an Extension?](#collapse_e1b8cc93-67ff-434a-9c88-82b9d834c99d_8)

The SDK is built on standard web technologies that AI coding assistants handle well. If you can clearly describe your idea for an Extension, you may be able to build a working Extension with AI assistance, without any coding experience.

[Where can I find more information about Extensions?](#collapse_e1b8cc93-67ff-434a-9c88-82b9d834c99d_9)

Check out the documentation in the [Ableton Extensions SDK GitHub repository](https://ableton.github.io/extensions-sdk) for more information.

[Read the docs on GitHub](https://ableton.github.io/extensions-sdk/ "Read the docs on GitHub")[Join the community on Discord](https://discord.com/invite/ableton "Join the community on Discord")

[Download Live 12.4.5 beta to get started](https://www.ableton.com/en/beta/)
