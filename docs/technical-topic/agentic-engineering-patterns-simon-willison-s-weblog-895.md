---
id: 895
url: https://simonwillison.net/guides/agentic-engineering-patterns/
title: Agentic Engineering Patterns - Simon Willison's Weblog
domain: simonwillison.net
source_date: '2026-03-04'
tags:
- ai
- llm
- tutorial
summary: Simon Willison's guide on agentic engineering patterns provides best practices
  for working effectively with AI coding agents like Claude Code and OpenAI Codex.
  The guide emphasizes key principles including treating code as inexpensive to generate,
  documenting known solutions, implementing rigorous testing with TDD approaches,
  and using clear explanations and annotated prompts to achieve better results. It
  offers practical patterns for understanding, testing, and iterating on agent-generated
  code through interactive and linear walkthroughs.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# Agentic Engineering Patterns - Simon Willison's Weblog

[Simon Willison’s Weblog](/)
============================

[Subscribe](/about/#subscribe)

**Sponsored by:** The AI App and Agent Factory — Microsoft Foundry is the enterprise Al platform where intelligence and trust ship with every agent. [Try Foundry](https://fandf.co/3Py9DbX)

Agentic Engineering Patterns
----------------------------

Patterns for getting the best results out of coding agents like Claude Code and OpenAI Codex. See [my introduction](https://simonwillison.net/2026/Feb/23/agentic-engineering-patterns/) for more on this project.

1. **Principles**
   1. [What is agentic engineering?](/guides/agentic-engineering-patterns/what-is-agentic-engineering/)
      * [Agentic engineering](/guides/agentic-engineering-patterns/what-is-agentic-engineering/#agentic-engineering)
      * [Isn't this just vibe coding?](/guides/agentic-engineering-patterns/what-is-agentic-engineering/#isnt-this-just-vibe-coding)
      * [About this guide](/guides/agentic-engineering-patterns/what-is-agentic-engineering/#about-this-guide)
   2. [Writing code is cheap now](/guides/agentic-engineering-patterns/code-is-cheap/)
      * [Good code still has a cost](/guides/agentic-engineering-patterns/code-is-cheap/#good-code)
      * [We need to build new habits](/guides/agentic-engineering-patterns/code-is-cheap/#we-need-to-build-new-habits)
   3. [Hoard things you know how to do](/guides/agentic-engineering-patterns/hoard-things-you-know-how-to-do/)
      * [Recombining things from your hoard](/guides/agentic-engineering-patterns/hoard-things-you-know-how-to-do/#recombining-things-from-your-hoard)
      * [Coding agents make this even more powerful](/guides/agentic-engineering-patterns/hoard-things-you-know-how-to-do/#coding-agents-make-this-even-more-powerful)
   4. [AI should help us produce better code](/guides/agentic-engineering-patterns/better-code/)
      * [Avoiding taking on technical debt](/guides/agentic-engineering-patterns/better-code/#avoiding-taking-on-technical-debt)
      * [Coding agents can handle these for us](/guides/agentic-engineering-patterns/better-code/#coding-agents-can-handle-these-for-us)
      * [AI tools let us consider more options](/guides/agentic-engineering-patterns/better-code/#ai-tools-let-us-consider-more-options)
      * [Embrace the compound engineering loop](/guides/agentic-engineering-patterns/better-code/#embrace-the-compound-engineering-loop)
   5. [Anti-patterns: things to avoid](/guides/agentic-engineering-patterns/anti-patterns/)
      * [Inflicting unreviewed code on collaborators](/guides/agentic-engineering-patterns/anti-patterns/#inflicting-unreviewed-code-on-collaborators)
2. **Working with coding agents**
   1. [How coding agents work](/guides/agentic-engineering-patterns/how-coding-agents-work/)
      * [Large Language Models](/guides/agentic-engineering-patterns/how-coding-agents-work/#large-language-models)
      * [Chat templated prompts](/guides/agentic-engineering-patterns/how-coding-agents-work/#chat-templated-prompts)
      * [Token caching](/guides/agentic-engineering-patterns/how-coding-agents-work/#token-caching)
      * [Calling tools](/guides/agentic-engineering-patterns/how-coding-agents-work/#calling-tools)
      * [The system prompt](/guides/agentic-engineering-patterns/how-coding-agents-work/#the-system-prompt)
      * [Reasoning](/guides/agentic-engineering-patterns/how-coding-agents-work/#reasoning)
      * [LLM + system prompt + tools in a loop](/guides/agentic-engineering-patterns/how-coding-agents-work/#llm-system-prompt-tools-in-a-loop)
   2. [Using Git with coding agents](/guides/agentic-engineering-patterns/using-git-with-coding-agents/)
      * [Git essentials](/guides/agentic-engineering-patterns/using-git-with-coding-agents/#git-essentials)
      * [Core concepts and prompts](/guides/agentic-engineering-patterns/using-git-with-coding-agents/#core-concepts-and-prompts)
      * [Rewriting history](/guides/agentic-engineering-patterns/using-git-with-coding-agents/#rewriting-history)
   3. [Subagents](/guides/agentic-engineering-patterns/subagents/)
      * [Claude Code’s Explore subagent](/guides/agentic-engineering-patterns/subagents/#claude-codes-explore-subagent)
      * [Parallel subagents](/guides/agentic-engineering-patterns/subagents/#parallel-subagents)
      * [Specialist subagents](/guides/agentic-engineering-patterns/subagents/#specialist-subagents)
      * [Official documentation](/guides/agentic-engineering-patterns/subagents/#official-documentation)
3. **Testing and QA**
   1. [Red/green TDD](/guides/agentic-engineering-patterns/red-green-tdd/)
   2. [First run the tests](/guides/agentic-engineering-patterns/first-run-the-tests/)
   3. [Agentic manual testing](/guides/agentic-engineering-patterns/agentic-manual-testing/)
      * [Mechanisms for agentic manual testing](/guides/agentic-engineering-patterns/agentic-manual-testing/#mechanisms-for-agentic-manual-testing)
      * [Using browser automation for web UIs](/guides/agentic-engineering-patterns/agentic-manual-testing/#using-browser-automation-for-web-uis)
      * [Have them take notes with Showboat](/guides/agentic-engineering-patterns/agentic-manual-testing/#have-them-take-notes-with-showboat)
4. **Understanding code**
   1. [Linear walkthroughs](/guides/agentic-engineering-patterns/linear-walkthroughs/)
      * [An example using Showboat and Present](/guides/agentic-engineering-patterns/linear-walkthroughs/#an-example-using-showboat-and-present)
   2. [Interactive explanations](/guides/agentic-engineering-patterns/interactive-explanations/)
      * [Understanding word clouds](/guides/agentic-engineering-patterns/interactive-explanations/#understanding-word-clouds)
5. **Annotated prompts**
   1. [GIF optimization tool using WebAssembly and Gifsicle](/guides/agentic-engineering-patterns/gif-optimization/)
      * [The follow-up prompts](/guides/agentic-engineering-patterns/gif-optimization/#the-follow-up-prompts)
   2. [Adding a new content type to my blog-to-newsletter tool](/guides/agentic-engineering-patterns/adding-a-new-content-type/)
6. **Appendix**
   1. [Prompts I use](/guides/agentic-engineering-patterns/prompts/)
      * [Artifacts](/guides/agentic-engineering-patterns/prompts/#artifacts)
      * [Proofreader](/guides/agentic-engineering-patterns/prompts/#proofreader)
      * [Alt text](/guides/agentic-engineering-patterns/prompts/#alt-text)
      * [Podcast highlights](/guides/agentic-engineering-patterns/prompts/#podcast-highlights)

* [Disclosures](/about/#disclosures)
* [Colophon](/about/#about-site)
* ©
* [2002](/2002/)
* [2003](/2003/)
* [2004](/2004/)
* [2005](/2005/)
* [2006](/2006/)
* [2007](/2007/)
* [2008](/2008/)
* [2009](/2009/)
* [2010](/2010/)
* [2011](/2011/)
* [2012](/2012/)
* [2013](/2013/)
* [2014](/2014/)
* [2015](/2015/)
* [2016](/2016/)
* [2017](/2017/)
* [2018](/2018/)
* [2019](/2019/)
* [2020](/2020/)
* [2021](/2021/)
* [2022](/2022/)
* [2023](/2023/)
* [2024](/2024/)
* [2025](/2025/)
* [2026](/2026/)
