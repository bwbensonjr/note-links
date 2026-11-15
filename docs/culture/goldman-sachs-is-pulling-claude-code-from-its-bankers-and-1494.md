---
id: 1494
url: https://www.thestateofai.com/news/goldman-sachs-claude-code-traders-bankers
title: Goldman Sachs Is Pulling Claude Code From Its Bankers and Traders | State of
  AI
domain: www.thestateofai.com
source_date: '2026-11-09'
tags:
- news
- ai
- llm
- security
summary: Goldman Sachs has restricted tools like Anthropic's Claude Code and Microsoft's
  GitHub Copilot to its engineers, cutting off traders and bankers who used them to
  track client flows and build market models. The change, made through an October
  guidance update, follows a review of productivity and risk concerns, particularly
  around unreviewed code running on trading desks and information barrier rules. The
  article argues the restriction was justified but poorly handled, since it withdrew
  tools that non-engineers had been relying on without offering a replacement.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-5-5
---

# Goldman Sachs Is Pulling Claude Code From Its Bankers and Traders | State of AI

*Goldman Sachs has restricted Anthropic's Claude Code and Microsoft's GitHub to its engineers, cutting off traders and bankers who used the tools to track client flows and build market models. The bank barred its Hong Kong bankers from Claude in April and is now a lead underwriter on Anthropic's IPO.*

Most traders and bankers at Goldman Sachs can no longer use AI coding tools at work. Internal guidance updated in October restricts Anthropic's Claude Code and Microsoft's GitHub to the bank's engineers, [Bloomberg News reported](https://www.fa-mag.com/news/goldman-restricts-traders-and-bankers-from-using-some-ai-tools-89026.html), following a review of productivity and risk concerns.

Strats, who work across trading, quantitative research and software engineering, still have access, according to a second person familiar with the matter.

The change has frustrated some traders, a person familiar with the matter told Bloomberg. They had been using the tools to monitor client trading flows, model market moves and positions, and put together written and graphic material. Goldman spokesperson Nick Carcaterra said the bank makes certain AI tools available to staff "to determine the best use cases" across the firm.

Argenti was praising trader-built tools in July
-----------------------------------------------

As recently as July, chief information officer Marco Argenti was talking up "vibe coding" by Goldman's non-technical employees. He told Bloomberg that traders and bankers had built tools with AI and passed them to the firm's engineers, of whom there are about 12,000, to be improved.

That arrangement let the people closest to a problem build a first version without waiting for engineering time. It also meant thousands of employees without engineering training were running software that writes and executes code, on the same machines they use to handle client information.

At a conference in Turin last month, Argenti [described Goldman's AI adoption in waves](https://thenextweb.com/news/marco-argenti-goldman-sachs-ai-third-wave-growth-wave-by-vento) and said developers, more than 12,000 of the bank's roughly 47,000 staff, had made up the first. The October guidance limits the coding agents to that group.

Goldman restricted Claude in Hong Kong in April
-----------------------------------------------

In April, Goldman removed Claude from its internal AI platform for bankers in Hong Kong. The Financial Times reported that the bank had [read its contract with Anthropic strictly](https://whbl.com/2026/04/28/goldman-sachs-bars-hong-kong-bankers-from-anthropic-ai-use-ft-reports/), and an Anthropic spokesperson said Claude had never been officially supported in Hong Kong. ChatGPT and Gemini remained available there. JPMorgan [removed Claude from its Hong Kong approved list](https://thenextweb.com/news/jpmorgan-cuts-off-anthropic-access-for-hong-kong-staff) in June.

The Hong Kong restriction was based on location and contract terms, and the new one is based on role. Goldman's in-house AI assistant, which uses models from several companies, is still available across the firm. The restriction applies to third-party agents that can write and run code by themselves.

Goldman is still working closely with Anthropic
-----------------------------------------------

Earlier this year, Goldman said Anthropic engineers had spent six months at the bank helping build [Claude-based agents for trade accounting and client onboarding](https://www.webpronews.com/goldman-sachs-bets-big-on-anthropics-claude-to-reshape-wall-streets-back-office/). Those agents sit in the back office and are run by Goldman's engineering teams.

Goldman and Morgan Stanley are also the [lead underwriters on Anthropic's IPO](https://www.iposcoop.com/the-ipo-buzz-anthropic-ant-proposed-files-its-s-1/), according to the S-1 filed October 26. Anthropic is expected to list on Nasdaq under the ticker ANT before the end of November, as we [reported last week](https://www.thestateofai.com/news/anthropic-junk-rating-blackstone-ipo). Over the next few weeks, Goldman's bankers will be marketing shares in a company whose coding agent most of them are no longer allowed to use.

Why a coding agent is riskier on a trading desk
-----------------------------------------------

Claude Code reads files, writes programs and runs them, typically with the same access as the person using it. Code an engineer writes with it usually goes through review, testing and deployment controls before it reaches anything important. A script a trader builds to watch client flows can end up in daily use without going through any of those.

Banks are also required to keep information barriers between groups, for example between bankers working on deals and traders who could profit from knowing about them. Goldman built its internal AI platform around controls like these. A tool a trader puts together with an agent wasn't designed with them in mind, and engineers can only check it if someone sends it their way.

There is also the matter of whether anyone understands the code. Last month a Meta engineer [said he now ships code he can't fully account for](https://www.thestateofai.com/news/meta-engineer-shipping-code-he-doesnt-understand), and writing software is his job. A trader using an agent to model positions is less likely to know how that code handles unusual cases, which on a trading desk can mean losses.

Cost may also have played a part. Agent usage is billed by the token, and several companies that gave agents to everyone have seen spending climb. Amazon [shut down an internal leaderboard](https://www.thestateofai.com/news/amazon-tokenmaxxing-memo-ai-metrics) after employees ran agents on pointless tasks to move up it, and Accenture [now funds $29 a month of Claude per employee](https://www.thestateofai.com/news/accenture-caps-claude-spending-29-dollars). Bloomberg's sources said productivity was part of Goldman's review.

Barclays is moving in the other direction
-----------------------------------------

Barclays said in October that it expects half its developers to be using Claude Code by the end of the year, and three weeks later [named developers among 5,000 job cuts](https://www.thestateofai.com/news/barclays-cuts-developers-coding-agents). Like Goldman, it is giving coding agents to engineers. Unlike Goldman, it is also using them to reduce how many engineers it employs.

Banks have tightened agent access in other places this fall. JPMorgan and Schwab are [blocking outside agents from customer accounts](https://www.thestateofai.com/news/delta-jpmorgan-schwab-yelp-amazon-block-ai-agents), and Goldman has now set limits on which of its own employees can use them.

Our take
--------

At State of AI, we think Goldman was right to restrict the tools and wrong in how it went about it.

A trading floor is a bad place for unreviewed code written by people who can't read it, and the information barrier problem would be reason enough on its own. Requiring that agent-written code come from people trained to review it is a sensible rule for a regulated business.

Goldman's own CIO was promoting traders' AI-built tools in July, though. Withdrawing access through a guideline update, with no replacement mentioned in Bloomberg's reporting, tells the traders who found good uses that they were the risk. Their complaints point to work the engineering team could take on, and Goldman would get more out of collecting them than out of waiting for them to fade.

Leaders at other companies should settle who owns agent-built code before handing agents out. When someone outside engineering builds a tool with Claude Code or Copilot, a named engineer should take responsibility for it before it touches production data.

Existing controls should cover code an agent writes. Information barriers, data entitlements and software approval rules still apply when the code came from a prompt.

And when a tool is taken away, it's worth recording what people were using it for. Goldman's traders were watching client flows and modeling positions, and they will still need to do both.

Recent News
-----------

[![Story image](https://www.thestateofai.com/media/uploads/b8c82e38a2c68b7e1b705a058497b758b50663db625c399ab7beebe18fc39ce0.png)

AI & TECHNOLOGY

### Feds Are Now Looking at Whether the FAA's New AI Tool Caused Today's Nationwide Ground Stop

Nov 13, 2026](/news/faa-ground-stop-smart-ai-rollout)[![Story image](https://www.thestateofai.com/media/uploads/a70c8e535b36ef68702fbad76a3fd2f372bab09712da9da53752daa01c884938.png)

AI & TECHNOLOGY

### As Nvidia Faces Scrutiny Over China, a Researcher Says Banned Blackwell Chips Trained China's Top AI Models

Nov 12, 2026](/news/will-depue-blackwell-fingerprint-chinese-ai-models)[![Story image](https://www.thestateofai.com/media/uploads/56ec3ca8f61d2d3cb9fcbce724741d8d2999c9645bd29097289daf3f0c3e4736.png)

AI & TECHNOLOGY

### Anthropic Just Put Claude in Your Meetings. AI Notetakers Should Be Paying Attention.

Nov 12, 2026](/news/anthropic-claude-meetings-ai-notetakers)[![Story image](https://www.thestateofai.com/media/uploads/5676542cb8d7cf4c25110e30ab9f66206386a5bc7e178ba251b114233e6f0499.webp)

AI & TECHNOLOGY

### AI Is Taking Over The First Three Years Of The Job. Year Four Has To Be Rebuilt On Purpose.

Nov 12, 2026](/news/ted-rusch-ai-and-expertise-development-batson-cook-construction)
