---
id: 1024
url: https://clojure.org/about/documentary
title: Clojure - Documentary
domain: clojure.org
source_date: '2026-04-17'
tags:
- clojure
- video
- academic-paper
summary: A full-length documentary traces Clojure's origins from Rich Hickey's sabbatical
  project to its current role powering major fintech infrastructure, featuring key
  creators and exploring the language's values-driven community and philosophical
  approach to software design. The page provides comprehensive resources including
  foundational research papers, influential books, talks by Rich Hickey on topics
  like simplicity and immutable values, and information about Clojure's various implementations
  (ClojureScript, ClojureCLR, Babashka) and modern applications in data science and
  AI. It also offers getting started guides, a glossary of key terms, and details
  about the vibrant Clojure ecosystem and community.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# Clojure - Documentary

Documentary





Documentary
===========

From a two-year sabbatical and a stubborn idea to powering the engineering stack of one of the world’s largest fintech companies — this is the story of Clojure.

Featuring Rich Hickey, Alex Miller, Stuart Halloway, and many more, this full-length documentary traces Clojure’s unconventional origins, its values-driven community, and the language’s quiet but profound impact on how we think about software.

Documentary made possible with the support of [Nubank](https://building.nubank.com/engineering/)!

Clojure: The Documentary

Show Notes
----------

### Foundational Research Papers

* [Out of the Tarpit](https://curtclifton.net/papers/MoseleyMarks06a.pdf) — Ben Moseley & Peter Marks (2006). Identifies mutable state as the primary source of accidental complexity in software.
* [Ideal Hash Trees](https://infoscience.epfl.ch/record/64398/files/idealhashtrees.pdf) — Phil Bagwell. Research on Hash Array Mapped Tries (HAMTs), the direct inspiration for Clojure’s persistent data structures.
* [Composable Memory Transactions](https://dl.acm.org/doi/10.1145/1065944.1065952) — Tim Harris, Simon Marlow, Simon Peyton-Jones & Maurice Herlihy (2005). Software Transactional Memory; a key influence behind Clojure’s STM concurrency model.
* [Paper Bibliography](https://docs.google.com/spreadsheets/d/1P3z4Nh02l6zIeGypgQ5wKGUe6Lq0lUCR-R35b0MF7mU/edit?gid=1078381722#gid=1078381722) - a full list of papers used by Rich while developing Clojure, compiled by Michael Fogus

### Influential Books

* [On Lisp](https://paulgraham.com/onlisp.html) — Paul Graham. Widely referenced book on advanced Lisp techniques. Free online.
* [Programming Clojure (4th ed.)](https://pragprog.com/titles/shcloj4/programming-clojure-fourth-edition/) — Alex Miller, Stuart Halloway & Aaron Bedra. The first edition by Stuart Halloway launched alongside Clojure 1.0.
* [The Joy of Clojure](https://www.manning.com/books/the-joy-of-clojure-second-edition) — Michael Fogus & Chris Houser.

### Talks by Rich Hickey

* [Simple Made Easy (2011)](https://www.youtube.com/watch?v=LKtk3HCgTa8) — Rich’s famous talk from Strange Loop 2011. Defines the distinction between "simple" and "easy."
* [Clojure at LispNYC (2007)](https://www.youtube.com/watch?v=m1tZEn_NAqg) - the first public talk about Clojure.
* [Sierra’s Blog on LispNYC Presentation](https://stuartsierra.com/2007/11/15/clojure-a-lisp-worth-talking-about/) — 2007. An early public introduction to Clojure.
* [Are We There Yet? (2009)](https://www.youtube.com/watch?v=E4RarTAZ2AY) - The Clojure state model and a dissection of time in programming.
* [Hammock Driven Development (2010)](https://www.youtube.com/watch?v=f84n5oFoZBc) — On thinking deeply about problems before writing code.
* [Strange Loop Language Panel (2011)](https://www.youtube.com/watch?v=zhZMaF8vq5Y) - A fun panel of language designers including Rich Hickey and Gerald Sussman.
* [The Value of Values (2012)](https://www.youtube.com/watch?v=-6BsiVyC1kM) — The case for immutable values over mutable objects.
* [Writing Datomic in Clojure (2012)](https://www.infoq.com/presentations/Datomic/) - An overview of Datomic and how Clojure was the perfect language to write it in.
* [Expert to Expert: Rich Hickey and Brian Beckman - Inside Clojure (2013)](https://www.youtube.com/watch?v=wASCH_gPnDw) - a long-form interview with Rich about Clojure.
* [Effective Programs - 10 Years of Clojure (2017)](https://www.youtube.com/watch?v=2V1FtfBDsLU) - Rich reflects on the first 10 years of Clojure and the prioritization of Clojure’s features for solving real-world problems.
* [Talk Transcripts](https://github.com/matthiasn/talk-transcripts) — Community-maintained transcripts of Clojure talks by Rich Hickey and others.
* [Rich Hickey Talks](https://www.youtube.com/playlist?list=PLZdCLR02grLrEwKaZv-5QbUzK0zGKOOcr) - A video playlist of many of Rich’s talks.

### Paul Graham’s Essays

* [Beating the Averages](https://paulgraham.com/avg.html)
* [Revenge of the Nerds](https://paulgraham.com/icad.html)
* [other essays](https://paulgraham.com/articles.html)

### Important Companies and Projects

* [Cognitect Blog](https://www.cognitect.com/blog/) — The consultancy that stewarded Clojure for many years.
* [Nubank](https://nubank.com.br/en/) — World’s largest independent digital bank, running core infrastructure on Clojure and Datomic. Acquired Cognitect in 2020 and currently stewards Clojure’s development.
* [Datomic](https://www.datomic.com/) — Distributed database built on immutable facts, designed by Rich Hickey and Cognitect.

### Community & Archival Resources

* [Java.next Blog Series](https://www.cognitect.com/blog/2008/9/24/java-next-overview) — Stuart Halloway’s 2008 series on emerging JVM languages.
* [Clojure IRC Log Archive](https://chouser.us/clojure-log/) — Preserved archive of the original Clojure IRC channel.
* [Clojure Etiquette](https://clojure.org/community/etiquette) - derived from Rich’s original post to the mailing list.

Clojure Dialects & Runtimes
---------------------------

### Core

* [Clojure](https://clojure.org/) — Runs on the JVM. Follow the [official getting started guide](https://clojure.org/guides/getting_started) or pick up [Brave Clojure](https://www.braveclojure.com/) for a free, beginner-friendly introduction.
* [ClojureScript](https://clojurescript.org/) — Compiles to JavaScript. Powers frontend development with libraries like [Reagent](https://reagent-project.github.io/) and [Re-frame](https://day8.github.io/re-frame/).
* [ClojureCLR](https://github.com/clojure/clojure-clr) — Clojure on the .NET CLR.

### Beyond the Core

* [Babashka](https://babashka.org/) — Fast scripting without JVM startup time.
* [Jank](https://jank-lang.org/) — Targets LLVM for native compilation.
* [ClojureDart](https://github.com/Tensegritics/ClojureDart) — Flutter mobile apps.
* [Squint](https://github.com/squint-cljs/squint) / [Cherry](https://github.com/squint-cljs/cherry) — Compile to ES modules.
* [Other Clojure-like projects](https://github.com/ilevd/clojure-like)

### Data Science

* [libpython-clj](https://github.com/clj-python/libpython-clj) — Call Python libraries (NumPy, pandas, scikit-learn) directly from Clojure.
* [Noj](https://scicloj.github.io/noj/) — Clojure-native data science toolkit from [SciCloj](https://scicloj.github.io/), combining dataframes, visualization, and machine learning.
* [Tablecloth](https://github.com/scicloj/tablecloth) — Combine Python interop with Clojure’s dataframe library.

### Clojure & AI

* [ECA](https://github.com/editor-code-assistant/eca) - Editor Code Assistant
* [Backseat Driver](https://github.com/BetterThanTomorrow/calva-backseat-driver) - Clojure Tools for Copilot
* [ClojureMCP](https://github.com/bhauman/clojure-mcp) — MCP server connecting AI assistants (Claude, Codex, Gemini) to your Clojure REPL with structure-aware editing.
* [MCP-nREPL](https://github.com/ctford/mcp-nrepl) — Minimal Babashka MCP server giving coding agents direct nREPL access.
* [clojure-mcp-light](https://github.com/bhauman/clojure-mcp-light) — Lightweight CLI tools for delimiter repair and REPL eval with any LLM coding assistant.
* [#ai-assisted-coding on Clojurians Slack](https://clojurians.slack.com/archives/C068E9L5M2Q) — Active community channel for AI + Clojure development.

Getting Started
---------------

1. **Full experience** — Follow the [official getting started guide](https://clojure.org/guides/getting_started) with step-by-step installation videos for [macOS](https://www.youtube.com/watch?v=huGyv5yLIM8), [Linux](https://www.youtube.com/watch?v=544xOAIg3y0), [Windows WSL](https://www.youtube.com/watch?v=TQgzA3QLz-k), and [Windows](https://www.youtube.com/watch?v=NFDAChdzThg). The videos use [Calva](https://calva.io/) in VS Code.
2. **Quickest path** — Install [Babashka](https://babashka.org/) and start scripting immediately. No JVM setup needed.
3. **Web / frontend** — Try [ClojureScript with Shadow CLJS](https://shadow-cljs.github.io/docs/UsersGuide.html).
4. **Mobile apps** — Try [ClojureDart](https://github.com/Tensegritics/ClojureDart) for Flutter.
5. **Already a Python user** — Use [libpython-clj](https://github.com/clj-python/libpython-clj) to call your favorite Python libraries directly from Clojure.
6. **Editor** — [Calva](https://calva.io/) provides Clojure development in VS Code with interactive REPL, structural editing, and AI integration via [Backseat Driver](https://marketplace.visualstudio.com/items?itemName=betterthantomorrow.calva-backseat-driver). See the [editors guide](https://clojure.org/guides/editors) for more options.

Glossary
--------

Watched the documentary and want to dig in? Here are a few terms you’ll encounter.

| Term | Definition |
| --- | --- |
| **Lisp** | A family of programming languages that represent code as nested lists enclosed in parentheses. Clojure is a Lisp dialect. |
| **REPL** | Read-Eval-Print Loop. An interactive session that reads an expression, evaluates it, prints the result, and repeats. Clojure developers use the REPL to build and test programs while they run. |
| **Functional programming** | A programming style built around functions that take values and return values, minimizing mutable state and side effects. |
| **Value** | A piece of data that does not change after creation: a number, a string, or a persistent collection. Clojure defaults to values; you opt in to mutable state explicitly when you need it. |
| **Persistent data structure** | A collection that preserves its previous version when you modify it. Adding an element returns a new collection; the original remains unchanged. "Persistent" here means version-preserving, not stored to disk. |
| **Accidental complexity** | Difficulty in software caused by your tools and design choices, not by the problem itself. Contrasted with *essential (or incidental) complexity*, which is inherent to the problem domain. |
| **STM** | Software Transactional Memory. A concurrency model that coordinates shared-state changes through transactions instead of locks. |
| **Hosted language** | A language designed to run on an existing platform rather than its own runtime. Clojure runs on the JVM, ClojureScript compiles to JavaScript, and ClojureCLR targets the .NET CLR. |

Follow Clojure
--------------

[YouTube](https://www.youtube.com/@ClojureTV) · [Reddit](https://www.reddit.com/r/Clojure/) · [Slack](http://clojurians.net/?utm_source=clojure.org&utm_medium=show_notes&utm_campaign=clojure_documentary&utm_content=clojurians_slack) · [LinkedIn](https://www.linkedin.com/feed/hashtag/clojure/)

Join us at the [Clojure/Conj Conference 2026](https://2026.clojure-conj.org/?utm_source=clojure.org&utm_medium=show_notes&utm_campaign=clojure_documentary&utm_content=clojure_conj_2026) — September 30 – October 2, Charlotte, NC · [LinkedIn](https://www.linkedin.com/company/clojure-conj/)

[ History](history)
[Dynamic Development ](dynamic)
