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

Ever wanted to control Ableton with just your voice? Me too! I made this MCP server so I could just ask Codex to do anything in Ableton Live for me, while I was nap-trapped by my baby. Unlike other Ableton MCPs I tried, this one can do pretty much anything that is possible via Ableton's Object model; the agent can just eval arbitrary python that runs inside Ableton. It also has some tools defined for common tasks so those work faster and more reliably. I had Codex CLI optimize this for hours with the new /goal command to prioritize low end-to-end latency, high reliability, low token usage, while maintaining full flexibility. How to setup Just tell your AI agent (Codex, Claude Code, Cursor, Copilot, Gemini, etc.) to Set up the https://github.com/bschoepke/ableton-live-mcp MCP server for me . It should work on Mac and Windows with recent Ableton versions, but I have only tested it on Ableton Live Suite 12.3.8 on macOS Tahoe. Back up your Live Set before using this. The MCP can edit your set directly and could corrupt it. Demo https://www.youtube.com/watch?v=8dRRrIY7NI0 The chat messages I sent to Codex to make this: in ableton, make a self reflective song, with audio vocals (via macos say) and chip tunes and 80's drum machines. should be a real edm banger i want midi for everything but vocals please, with ableton devices. not prerendered audio for instruments needs some fills and should hit way harder after "3-2-1 i become the sound" the vocals are squished too much (read too quickly), give them a little more length add some dynamics, the song is basically one volume. and some pumping side chain improve dynamics of the clap, seems a bit flat and indistinguished, want it harder after the 3-2-1 drop introduce a new element on a new track after the 3-2-1 drop, that comes in but then recedes before the final exit doesn't seem like the new thing has any notes the element is a bit muddy/indistinct. perhaps it needs simplification and more space, different instrument choice, i dunno Ideas Control your external synthesizers and hardware with the MCP You can tell it use third party plugins (VSTs, audio units) like Serum and Keyscape. Tell your agent to incorporate your existing vocal samples, including asking it to trim silence and transcribe your audio samples before creatively incorporating them into your live set Ask your agent to set up crazy user controlled DJ effects Experiment with VJ plugins like Videosync to make music videos driven by your live set
