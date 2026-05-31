---
id: 1073
url: https://zed.dev/blog/zed-1-0
title: Zed is 1.0 — Zed's Blog
domain: zed.dev
source_date: '2026-04-29'
tags:
- cli-tool
- ai
- github-repo
summary: Zed has reached version 1.0 after being built from the ground up as a GPU-accelerated
  application rather than a web-based editor, allowing it to achieve superior performance
  and capabilities unavailable to competitors built on borrowed platforms like Electron.
  The 1.0 release represents a tipping point where Zed now supports the full range
  of modern development features across multiple languages and operating systems,
  with AI deeply integrated as a native capability rather than an afterthought. Looking
  forward, the team plans to develop DeltaDB, a synchronization engine that will enable
  seamless collaboration between human developers and AI agents on shared codebases
  in real-time.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# Zed is 1.0 — Zed's Blog

[![Nathan Sobo](https://avatars.githubusercontent.com/u/1789?v=4)

Nathan Sobo](/team#nathan-sobo)

April 29th, 2026

To create a fundamentally better editor, we had to invent a new approach to building desktop software. Our previous editor, [Atom](/blog/we-have-to-start-over), was built as a fork of Chromium, spawning the Electron framework in the process. Electron eventually became the foundation of VS Code (which today seems to be forked into a new AI code editor every other week). Web technology offered an easy path to shipping flexible software, but it also imposed a ceiling. No matter how hard we worked, we couldn't make Atom better than the platform it was built on.

So we started over. Instead of building Zed like a web page, we built it [like a video game](/blog/videogame), organizing the entire application around feeding data to shaders running on the GPU. That meant writing our own UI framework, [GPUI](/blog/gpui-ownership), from scratch in Rust.

Owning every layer of our stack lets us take Zed places that no one building on borrowed foundations can go, but we knew from the beginning that it wasn't going to be an easy path. Thanks to years of hard work by our team and community, Zed is closer than ever to that ideal tool we set out to create. We've added a ton of capabilities while remaining true to our core ethos of craft and performance, and hundreds of thousands of developers now rely on Zed to ship software each day. That's part of what gives us the confidence to declare version 1.0.

Zed is 1.0

[What 1.0 Means](#what-10-means)
--------------------------------

Developers expect a modern editor to support dozens of languages and their ecosystems, endless variations and edge cases across every stack: [Git integration](/git), [SSH remoting](/blog/remote-development), a [Debugger](/debugger), and, yes, [rainbow brackets](/blog/rainbow-brackets). We've spent five years building that surface area across Mac, [Windows](/windows), and [Linux](/linux), exceeding a million lines of code.

Zed is also an AI-native editor. You can run [multiple agents in parallel](/blog/parallel-agents), and [edit predictions](/blog/edit-prediction) suggest your next change at keystroke granularity and with the speed you've come to expect from Zed. The [Agent Client Protocol](/blog/bring-your-own-agent-to-zed) opens Zed up to a growing number of the best agents out there, including Claude Agent, Codex, OpenCode, and more recently Cursor. We built AI into our editor's foundation instead of bolting it on top.

We're also launching Zed for Business. Companies have been asking us for a way to roll out Zed to their engineering teams, and very soon they can, with centralized billing, role-based access controls, and team management.

1.0 doesn't mean "done". It also doesn't mean "perfect". It means we've reached a tipping point where most developers can quickly feel at home in Zed. If you tried Zed a year or two ago and bounced because something was missing, 1.0 is our invitation to try again. Zed is more capable than it's ever been, and still more performant.

[Where We're Going](#where-were-going)
--------------------------------------

Our vision hasn't changed since we started: we're building the most performant and collaborative coding environment. What's changed is what collaboration means while creating software. It used to mean humans working together in real time. Now it means humans and AI agents, working in the same space, on the same code.

Building our own foundations is what got us to 1.0, and it's also what makes the next chapter possible. We're actively developing [DeltaDB](/blog/sequoia-backs-zed), a synchronization engine built on [CRDTs](/blog/crdts) that tracks every change with character-level granularity. DeltaDB lets multiple humans and agents share a single, consistent view of the codebase as it evolves. DeltaDB will allow you to invite teammates into conversations with agents to review and evolve agentic code directly in the context from which it's generated.

This vision depends on deep ownership of our fundamental primitives. It's not an experience we'd be able to ship inside of someone else's browser engine.

[A Milestone, Not a Finish Line](#a-milestone-not-a-finish-line)
----------------------------------------------------------------

![Zed v0.13](/cdn-cgi/image/width=3840,quality=75/img/post/one-point-zero/0-13.webp)

![Zed v0.61](/cdn-cgi/image/width=3840,quality=75/img/post/one-point-zero/0-61.webp)

![Zed v0.104](/cdn-cgi/image/width=3840,quality=75/img/post/one-point-zero/0-104.webp)

![Zed v0.152](/cdn-cgi/image/width=3840,quality=75/img/post/one-point-zero/0-152.webp)

![Zed v1.0](/cdn-cgi/image/width=3840,quality=75/img/post/one-point-zero/1-0.webp)

Zed v0.13

We've shipped over a thousand versions of Zed, but all of them began with zero. Today, that changes.

We'll keep shipping every week, the way we always have. The list of things to build will never end, and that's exactly how we like it. Each release moves the craft forward.

If you want to try Zed, [download now](/download). If you want to help us build it, [join us](/jobs)!

![Zed is now 1.0](/img/post/one-point-zero/sticker.webp)

---

---

### Related Posts

Check out similar blogs from the Zed team.

[The Case for Software Craftsmanship in the Era of Vibes
-------------------------------------------------------

![Nathan Sobo](https://avatars.githubusercontent.com/u/1789?v=4)

---

![Nathan Sobo](https://avatars.githubusercontent.com/u/1789?v=4)

|

Agentic Engineering

|

Jun 12, 2025

---](/blog/software-craftsmanship-in-the-era-of-vibes)[Building a platform that open sources itself
--------------------------------------------

![Nathan Sobo](https://avatars.githubusercontent.com/u/1789?v=4)

---

![Nathan Sobo](https://avatars.githubusercontent.com/u/1789?v=4)

Jun 14, 2023

---](/blog/open-sourcing-zed-on-zed)[We're Not Building AI Features for the Money
--------------------------------------------

![Conrad Irwin](https://avatars.githubusercontent.com/u/94272?v=4)

---

![Conrad Irwin](https://avatars.githubusercontent.com/u/94272?v=4)

|

Featured

|

May 05, 2026

---](/blog/not-building-ai-for-the-money)

---

### Looking for a better editor?

You can try Zed today on macOS, Windows, or Linux. [Download now](/download)!

---

### We are hiring!

If you're passionate about the topics we cover on our blog, please consider [joining our team](/jobs) to help us ship the future of software development.
