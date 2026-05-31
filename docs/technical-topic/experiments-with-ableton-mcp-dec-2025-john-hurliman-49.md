---
id: 49
url: https://jhurliman.org/post/804323197731373056/experiments-with-ableton-mcp-dec-2025
title: Experiments with ableton-mcp (Dec 2025) - John Hurliman
domain: jhurliman.org
source_date: '2026-01-03'
tags:
- ai
- llm
- python
- tutorial
summary: John Hurliman experimented with ableton-mcp, an MCP server that enables Claude
  AI to control Ableton Live through tool-calling, extending its capabilities with
  70+ custom automation tools including vocal-to-MIDI conversion and audio analysis.
  He equipped the AI with "ears" by integrating a Max4Live audio recorder and music
  analysis endpoints, then successfully created a mashup of "Octo" by Deft & Lewis
  James with GloRilla's "Yeah Glo!" using a combination of automated and manual workflows.
  The experiment demonstrates how modern LLMs can effectively learn DAW workflows
  and serve as collaborative pair programmers for music production, significantly
  accelerating the learning and creation process.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# Experiments with ableton-mcp (Dec 2025) - John Hurliman

* [sphere](/sphere)
* [Ask me anything](/ask)
* [About](#footer)
* [Archive](/archive)
* [RSS](https://jhurliman.org/rss)

[John Hurliman](/)
==================

Experiments with ableton-mcp (Dec 2025)
---------------------------------------

*I started tinkering with Ableton and MCPs over the holiday break and ended up creating 70+ automation tool calls and a mashup track.*

[soundcloud.com/jhurliman/octo-glo](https://soundcloud.com/jhurliman/octo-glo)

![image](https://64.media.tumblr.com/18725cc767aab262e62859b1cbc43003/b106372ea8b9929c-ad/s500x750/5ec60d9e54a4ab1a02fd028d459674f71200d93f.jpg)

![image](https://64.media.tumblr.com/985a8d9a6ac74fa3b07999d1a9d99a38/b106372ea8b9929c-c9/s500x750/02c89b93c20792dba88615294aca5f32ac75f055.jpg)

Finding ableton-mcp
-------------------

While looking into automation options for Ableton, I stumbled on [ahujasid/ableton-mcp](https://github.com/ahujasid/ableton-mcp). It’s an MCP server that bridges tool-calling LLMs to Ableton Live via a community-documented Python API. I downloaded Claude Code, switched to Opus 4.5, asked it to install AbletonMCP, and then fired up Ableton.

Out of the box, the tool set was enough for basic creation and editing in Session view. But it didn’t cover Arrangement view, devices and device chains, mixing, and a bunch of other “real DAW” workflows.

Extending ableton-mcp
---------------------

The fun part: modern LLMs are capable enough to look up docs, add new MCP tools, test them, and iterate in a mostly closed loop. For Ableton features that *weren*’*t* exposed by the Python API, Opus 4.5 managed to reverse engineer enough of the .als file format to inject tempo/volume automation and warp markers.

Once the low-level plumbing was in place, I tried building higher-level tools. One example was vocal\_to\_midi(): it analyzes the audio of a vocal track, categorizes onsets into rough phoneme classes, and maps those phoneme categories onto standard Drum Rack MIDI notes. The goal wasn’t to “make drums from vocals” so much as to get a structured representation that helps with tiny phase and timing adjustments when aligning vocals to a drum groove (manually or with automation).

Giving the LLM ears
-------------------

Even with better tools, most attempts were still one-shot, or they required a human tightly in the loop. The core limitation was obvious: the model couldn’t hear what it was doing.

To address that, I created a Max4Live patch that provided a simple WAV file recorder that could be toggled on and off. This seemed to be the only programmatic way to get audio out of Ableton. Next I deployed two Replicate endpoints:

* [jhurliman/allinone-targetbpm](https://replicate.com/jhurliman/allinone-targetbpm): a fork of [mir-aidj/all-in-one](https://github.com/mir-aidj/all-in-one) that returns a structural analysis of a track. My fork exposes min\_bpm and max\_bpm, since I like using [91, 181] so slower tracks get counted at 2x.
* [jhurliman/music-flamingo](https://replicate.com/jhurliman/music-flamingo): an endpoint that takes audio + prompt and returns text output, based on a model fine-tuned with music theory knowledge.

I haven’t gone deep testing closed loop agentic iteration with these, but they’ve proven to be helpful building blocks so far.

Making an actual mashup
-----------------------

With a pile of tools glued together, I tried making something more complex than “edit a clip” or “tweak an EQ.” I started with one of my favorite instrumental bass tracks: [**Deft & Lewis James – Octo**](https://deftldn.bandcamp.com/track/octo). After determining the tempo (which is incorrectly documented in a bunch of places online) and the key, I asked for a playlist of candidate vocal matches and listened through about a dozen options.

[**GloRilla – Yeah Glo!**](https://www.youtube.com/watch?v=QiCpOvRS_1c) sounded like an interesting pairing immediately. After two days of automated and manual work, and a lot of LLM-guided “here’s how to do X in Ableton” tutorials, I had something I felt comfortable uploading[1].

Takeaways
---------

I’ve barely scratched the surface of Ableton, mashup creation, and DAWs in general. But I learned more about Ableton in a few days with AbletonMCP than I have in weeks of blogs and YouTube. The confidence boost from having a pair programmer for the DAW and the ability to go from blank slate to a finished artifact was genuinely useful, at least at this stage of learning.

All of the code generated during this experiment, and documentation of the rough workflow I used for the mashup creation, is available at [jhurliman/ableton-mcp/pull/1](https://github.com/jhurliman/ableton-mcp/pull/1).

—

[1] Immediately after uploading, I noticed several quirks that I went back and fixed. After that upload I decided the final compressor and track volume needed to be remastered. Third upload’s a charm.

* Tags:
  + [ableton](https://jhurliman.org/tagged/ableton)
  + [mcp](https://jhurliman.org/tagged/mcp)
* ### [December 29, 2025, 6:39pm](https://jhurliman.org/post/804323197731373056/experiments-with-ableton-mcp-dec-2025)
* [Permalink](https://jhurliman.org/post/804323197731373056/experiments-with-ableton-mcp-dec-2025)

[← Previous post](https://jhurliman.org/post/700578795268308992)

### About

### Blogroll

### Search

### Colophon

This tumblelog is powered by [Tumblr](http://tumblr.com/) and was designed by [Bill Israel](http://cubicle17.com/).
