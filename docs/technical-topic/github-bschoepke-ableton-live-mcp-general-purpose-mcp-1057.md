---
id: 1057
url: https://github.com/bschoepke/ableton-live-mcp
title: 'GitHub - bschoepke/ableton-live-mcp: General-purpose MCP bridge for Ableton
  Live · GitHub'
domain: github.com
source_date: '2026-05-04'
tags:
- github-repo
- python
- llm
- cli-tool
summary: This GitHub project is an MCP (Model Context Protocol) server that enables
  voice control of Ableton Live through AI agents like Claude or Copilot by allowing
  arbitrary Python execution within Ableton's object model. It offers both general-purpose
  scripting capabilities and pre-built tools for common tasks, optimized for low latency
  and token efficiency, with the ability to control synthesizers, process audio samples,
  and create complex music production workflows. The creator demonstrated its capabilities
  by using voice commands to build a complete EDM track with vocals, drum machines,
  and dynamic effects adjustments in real-time.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# GitHub - bschoepke/ableton-live-mcp: General-purpose MCP bridge for Ableton Live · GitHub

Ever wanted to control Ableton with just your voice? Me too! I made this MCP server so I could just ask Codex to do anything in Ableton Live for me, while I was nap-trapped by my baby.

Unlike other Ableton MCPs I tried, this one can do pretty much anything that is possible via Ableton's Object model; the agent can just eval arbitrary python that runs inside Ableton. It also has some tools defined for common tasks so those work faster and more reliably. I had Codex CLI optimize this for hours with the new `/goal` command to prioritize low end-to-end latency, high reliability, low token usage, while maintaining full flexibility.

Things you can use it for: create MIDI clips, insert audio files, general Ableton questions (with this, your agent can see your whole live set), add tracks with different devices and effects, analyze harmony, analyze audio signals at any point in the signal chain, generate spectrograms, clip automation, setting up mastering or vocal processing chains, insert MIDI the agent finds from the web... it's very general purpose, I'm not sure what the limits are.

How to setup
------------

Just tell your AI agent (Codex, Claude Code, Cursor, Copilot, Gemini, etc.) to:

`Set up the https://github.com/bschoepke/ableton-live-mcp MCP server for me`

It should work on Mac and Windows with recent Ableton versions, but I have only tested it on Ableton Live Suite 12.3.8 on macOS Tahoe.

Back up your Live Set before using this. The MCP can edit your set directly and could corrupt it.

How to update
-------------

`git pull` this repo or ask your agent to:

`Update the https://github.com/bschoepke/ableton-live-mcp MCP server for me`

Demos
-----

Here are a couple examples of live sets made from scratch with Codex in just a few minutes, along with their prompts. After it makes something, you can ask for follow up changes.

[![Ableton Live MCP demo](https://camo.githubusercontent.com/20bed53183c0dfd52386e4d4a01b4c4abcba6fc0e73127c0ff2c02de13e422a3/68747470733a2f2f696d672e796f75747562652e636f6d2f76692f38645252724959374e49302f6d617872657364656661756c742e6a7067)](https://youtu.be/8dRRrIY7NI0)

<https://www.youtube.com/watch?v=8dRRrIY7NI0>

The chat messages I sent to Codex to make this:

*in ableton, make a self reflective song, with audio vocals (via macos say) and chip tunes and 80's drum machines. should be a real edm banger*

Follow up prompts:

*i want midi for everything but vocals please, with ableton devices. not prerendered audio for instruments*

*needs some fills*

*and should hit way harder after "3-2-1 i become the sound"*

*the vocals are squished too much (read too quickly), give them a little more length*

*add some dynamics, the song is basically one volume. and some pumping side chain*

*improve dynamics of the clap, seems a bit flat and indistinguished, want it harder after the 3-2-1 drop*

*introduce a new element on a new track after the 3-2-1 drop, that comes in but then recedes before the final exit*

*doesn't seem like the new thing has any notes*

*the element is a bit muddy/indistinct. perhaps it needs simplification and more space, different instrument choice, i dunno*

[![Ableton Live MCP piano demo](https://camo.githubusercontent.com/75a945b89418a89372cc0faabe09d17d1305588813d30e59a6de804cf2624902/68747470733a2f2f696d672e796f75747562652e636f6d2f76692f634c43484556316a57516f2f6d617872657364656661756c742e6a7067)](https://youtu.be/cLCHEV1jWQo)
<https://youtu.be/cLCHEV1jWQo>

Prompt used to make this:

*In Ableton, make a piano duet that tells the story of people debating the positive and negative merits of AI. The composition should be both beautiful and dynamic but surprising and fresh. Use Keyscape devices.*

Built in Agent Audio Tap Max for Live device
--------------------------------------------

The MCP includes an "Agent Audio Tap" Max for Live device that enables the agent to capture audio signals at any part of the signal processing chain. This gives the agent a full feedback loop for mixing and mastering tasks: it can capture audio signals for further processing with custom python, then tweak your Ableton devices, and then repeat.

Example usage where I asked Codex to generate a spectrogram of two piano tracks I had:
[![piano_tracks_first10_spectrograms](https://private-user-images.githubusercontent.com/6391254/587169004-6d2b6d9f-9a2c-4552-aa6c-91153de9df44.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3ODAyNDcwNzAsIm5iZiI6MTc4MDI0Njc3MCwicGF0aCI6Ii82MzkxMjU0LzU4NzE2OTAwNC02ZDJiNmQ5Zi05YTJjLTQ1NTItYWE2Yy05MTE1M2RlOWRmNDQucG5nP1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQVZDT0RZTFNBNTNQUUs0WkElMkYyMDI2MDUzMSUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyNjA1MzFUMTY1OTMwWiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9MmU3YThlZDIyODc3MDcxMmU0ZTAwOWZkYWY1MTIzZTJjNDVkOWEzZjA2NWQ2NTU0ZmZmMGNjNTRiMWFlMWIzYSZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QmcmVzcG9uc2UtY29udGVudC10eXBlPWltYWdlJTJGcG5nIn0.HhzlRUAsdn2G4T4Fk1nP-_wHEmU5vRSI2F7qjfXNTNw)](https://private-user-images.githubusercontent.com/6391254/587169004-6d2b6d9f-9a2c-4552-aa6c-91153de9df44.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3ODAyNDcwNzAsIm5iZiI6MTc4MDI0Njc3MCwicGF0aCI6Ii82MzkxMjU0LzU4NzE2OTAwNC02ZDJiNmQ5Zi05YTJjLTQ1NTItYWE2Yy05MTE1M2RlOWRmNDQucG5nP1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQVZDT0RZTFNBNTNQUUs0WkElMkYyMDI2MDUzMSUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyNjA1MzFUMTY1OTMwWiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9MmU3YThlZDIyODc3MDcxMmU0ZTAwOWZkYWY1MTIzZTJjNDVkOWEzZjA2NWQ2NTU0ZmZmMGNjNTRiMWFlMWIzYSZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QmcmVzcG9uc2UtY29udGVudC10eXBlPWltYWdlJTJGcG5nIn0.HhzlRUAsdn2G4T4Fk1nP-_wHEmU5vRSI2F7qjfXNTNw)

Ideas
-----

* Control your external synthesizers and other hardware with the MCP
* Ask it questions like "why does my mix sound muddy?" or "how do I sidechain my bass track?"
* Ask it to do things like "add a chord track that fits with my melody" or "give me a basic backing track for me to noodle on my guitar with"
* You can tell it use third party plugins (VSTs, audio units) like Serum and Keyscape
* Tell your agent to incorporate your existing vocal samples, including asking it to trim silence and transcribe your audio samples before creatively incorporating them into your live set
* Ask your agent to set up crazy user controlled DJ effects
* Experiment with VJ plugins like Videosync to make music videos driven by your live set
