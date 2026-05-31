---
id: 160
url: https://every.to/podcast/how-to-use-claude-code-like-the-people-who-built-it
title: 🎧 How to Use Claude Code Like the People Who Built It
domain: every.to
source_date: '2025-11-07'
tags:
- podcast
- ai
- llm
- tutorial
summary: This article features a podcast episode with Claude Code's creators from
  Anthropic, Cat Wu and Boris Cherny, who share insider tips on maximizing the AI
  coding tool's potential. Key takeaways include using "plan mode" for complex tasks
  rather than attempting one-shot solutions, standardizing team settings via a shared
  configuration file, leveraging stop hooks to automate task completion, and employing
  multiple subagents to catch bugs and handle tedious code migrations. The episode
  demonstrates how Claude Code has transformed development workflows at both Anthropic
  and Every, enabling faster feature development and empowering non-technical users
  to work directly with code.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# 🎧 How to Use Claude Code Like the People Who Built It

![Close](https://every.to/assets/icons/close-ea0cf7ce5d509dfce6a6461ab8180873b75e5480ad338cb45f45f9e25ca75812.svg)

[Home](/)
[Newsletter](/newsletter)
[Columnists](/columnists)
[Columns](/columnists#columns)
[Podcast](/podcast)
[Products](/studio)
[Events](/events)
[Guides](/guides)
[Consulting](/consulting)

[![](https://every.to/assets/icons/signin-83fa7c0681f947df7045aa4d1df051e3fe29f8b11b52df34b180c8ff7010a2cc.svg)
Sign in](/login)

[Search](/search)
[About us](/about)
[Careers](/careers)
[Advertise with us](/cdn-cgi/l/email-protection#3043405f5e435f4243585940437055465542491e445f)
[The team](/team)
[FAQ](/faq)
[Help center](https://help.every.to)

[![X / Twitter](https://every.to/assets/icons/xtwitter-a66ae6dc5260bbbab32ecaf3eb723b411070cd7887f803e04ad04018ec25e85a.svg)](https://x.com/every)
[![LinkedIn](https://every.to/assets/icons/linkedin-5b8ca87f46ed1b2118f4f5372ede5e2081ed43bf6456d634a655b0e1cce158ea.svg)](https://www.linkedin.com/company/everyinc/)
[![Spotify](https://every.to/assets/icons/spotify-39d4b64fbd367b9e1cb7710dfdd1d0cf09ad0ab1c460573903ab735b4b119c55.svg)](https://open.spotify.com/show/5qX1nRTaFsfWdmdj5JWO1G)
[![YouTube](https://every.to/assets/icons/youtube-f3ac30c4399a2a63a250ac355812201edb78b66dd8d1fbaed334dc54cdddc1e5.svg)](https://youtube.com/@everyinc)
[![Apple Podcasts](https://every.to/assets/icons/apple-podcasts-5e45ead34a488c8b35c571efa288f0966339c2aa846f8469fb8e32325da45624.svg)](https://podcasts.apple.com/us/podcast/ai-and-i/id1719789201)

![](https://every.to/assets/every-logo-white-d8b0c13c4b860174d4ac9717f446538ba8fa4f3b3736dde0de86e37bfc756789.svg)

![](https://d24ovhgu8s7341.cloudfront.net/uploads/post/cover/3806/full_page_cover_Boris_And_Cat_Wu_2_.png)

[![](https://d24ovhgu8s7341.cloudfront.net/uploads/user/avatar/182461/Rhea_1.png)

By Rhea Purohit
[AI & I](/podcast)](/@rhea_5618)

Rhea Purohit focuses on research-driven storytelling in tech. She writes about the psychology and history of adopting new technologies.

Read with AI

Open with Plus One

Your AI collaborator — pre-loaded with Every's best tools and workflows.

Open with Plus One →

![Claude](https://every.to/assets/icons/claude-2e258f0005c797394867f101ad3d1cbf8a0c0b35491d7bbbf1883d2a5b2bed7f.svg)

![ChatGPT](https://every.to/assets/icons/chatgpt-9ac33f9dce65bfa5d9d17e2478e48b852d3a0dee65e5c73964668ce9a66e0a95.svg)












![Copy text](https://every.to/assets/icons/copy-843dfebc97dc80bbdd05d13dfecd9aba457fbc1794f5a46466b3c26d6867daee.svg)

---

Share

![X](https://every.to/assets/icons/x-c02c4b571d1e377ff0b125bd65ba16dbf87be39c9dd1ebbfa333c0e19c47d7f1.svg)

![LinkedIn](https://every.to/assets/icons/in-98ec989b39f7091bca62c0f9a8d56d66d9fb05b80160499d8bf8f4823cfe8739.svg)

![Facebook](https://every.to/assets/icons/facebook-b4ec85c9120a2cd7a1c7c698e073430cfacd1f9eee761f1082fee06111a90060.svg)

![Copy link](https://every.to/assets/icons/link-00b3b50239c5decb99608a5d746ffe0fd96aecb034433a6cbaefdc45f2ae5183.svg)

[![](https://d24ovhgu8s7341.cloudfront.net/uploads/publication/logo/97/small_ai_and_i_cover_1.png)
AI & I](/podcast)

How to Use Claude Code Like the People Who Built It
===================================================

Anthropic’s Cat Wu and Boris Cherny explain how they use Claude Code inside the company—and what they’ve learned about getting the most out of it

[![](https://d24ovhgu8s7341.cloudfront.net/uploads/user/avatar/182461/Rhea_1.png)
Rhea Purohit](/@rhea_5618)

October 29, 2025
· Updated April 14, 2026

![Listen](https://every.to/assets/icons/listen-6083c475066b0940d919de3ff7eaa5018ebaad5f2708dd9227eb5029b6ecc615.svg)
Listen

![Copy Link](https://every.to/assets/icons/link-00b3b50239c5decb99608a5d746ffe0fd96aecb034433a6cbaefdc45f2ae5183.svg)
Link copied

![Share on X](https://every.to/assets/icons/x-c02c4b571d1e377ff0b125bd65ba16dbf87be39c9dd1ebbfa333c0e19c47d7f1.svg)

![Share on LinkedIn](https://every.to/assets/icons/in-98ec989b39f7091bca62c0f9a8d56d66d9fb05b80160499d8bf8f4823cfe8739.svg)

![Share on Facebook](https://every.to/assets/icons/facebook-b4ec85c9120a2cd7a1c7c698e073430cfacd1f9eee761f1082fee06111a90060.svg)
[![Like](https://every.to/assets/icons/heart-7a89368655eb0df55d6cae0d5e1d8613703f7138abace46c821074423d405069.svg)
34](/how-to-use-claude-code-like-the-people-who-built-it/how-to-use-claude-code-like-the-people-who-built-it/feedback?rating=amazing)
[![Comments](https://every.to/assets/icons/comment-380568ad1d594b3cf58d00ae8c9bf0edc47eb852dc9c5a2671363e2ebe383f91.svg)](#comments)

*TL;DR: Today we’re releasing a new episode of our podcast* [AI & I](https://every.to/podcast)*.* ***[Dan Shipper](https://every.to/@danshipper)*** *sits down with* ***Cat Wu*** *and* ***Boris Cherny,*** *the founding engineers of Claude Code. (Dan is also teaching a Claude Code for Beginners course next month—[learn more and register](https://claude101.every.to/).)****Watch [on X](https://x.com/danshipper/status/1983554470895108343) or [YouTube](https://youtu.be/IDSAMqip6ms), or listen on [Spotify](https://open.spotify.com/episode/7yJ1kUxwE750WIc1lyZcaT) or [Apple Podcasts](https://podcasts.apple.com/us/podcast/inside-claude-code-from-the-engineers-who-built-it/id1719789201?i=1000734060623).*** *Here’s a link to the [episode transcript](https://every.to/podcast/transcript-how-to-use-claude-code-like-the-people-who-built-it).*

---

[Claude Code](https://every.to/vibe-check/vibe-check-claude-3-7-sonnet-and-claude-code) singlehandedly [turned Every into a different team](https://every.to/source-code/how-i-use-claude-code-to-ship-like-a-team-of-five): Each new feature now makes [the next one easier to build](https://every.to/source-code/my-ai-had-already-fixed-the-code-before-i-saw-it), our CEO **Dan Shipper** ships to [codebases he doesn’t know well](https://x.com/danshipper/status/1965591067560214996), and non-technical people suddenly [find themselves inside a terminal](https://every.to/source-code/how-to-use-claude-code-for-everyday-tasks-no-programming-required).

That’s why Dan invited Claude Code’s creators—**[Cat Wu](https://x.com/_catwu?lang=en)** and **[Boris Cherny](https://x.com/bcherny)** from Anthropic—onto *AI & I* to talk about how they use it, and what they learned while building it.

They trace the origin of Claude Code from an internal experiment, walk through practical tips they’ve learned from watching Anthropic’s engineers in Claude Code—including how to use [subagents](https://every.to/vibe-check/vibe-check-claude-s-new-agents-are-confusing-as-hell) and their favorite slash commands—and talk about their philosophy for continuing to develop the agent. Wu and Cherny also look ahead to what’s next: the new form factors they’re experimenting with, and how Claude Code is expanding beyond traditional coding scenarios in the hands of non-technical users.

Here is a link to the episode transcript.

You can check out their full conversation here:

[![](https://img.youtube.com/vi/IDSAMqip6ms/maxresdefault.jpg)

![](https://d24ovhgu8s7341.cloudfront.net/static/emails/youtube-logo.png)](https://youtu.be/IDSAMqip6ms)

Here are some of the themes they touch on:

#### What the team has learned about getting the best out of Claude Code

The Claude Code team has an unfair advantage: They get to watch hundreds of smart engineers use their product every single day, and all it takes is a stroll around their office. This practice, called “antfooding” (Anthropic’s technical employees are affectionately known as “ants,” and this is their version of dogfooding), means the team gets to feel the product’s edges before anyone else does. (Wu says they get a message in their feedback channel every five minutes.) Here’s what they’ve learned about where it shines:

##### Don’t one-shot everything—use plan mode

People new to coding with AI agents often start with the assumption that Claude Code can [one-shot](https://en.wikipedia.org/wiki/One-shot_learning_(computer_vision)) anything, but Cherny says that’s not realistic, at least not yet. You can double or triple your chances of success on complex tasks by switching to “plan mode”—which has Claude map out what it’s going to do step-by-step—and aligning on an approach before any code gets written.

##### An easy way to standardize Claude Code settings

If your team is using Claude Code regularly, Cherny recommends creating a shared settings file—called settings.json—that lives in your codebase. This lets you pre-approve common commands (so Claude stops asking permission for routine tasks) and block risky ones (like files you never want touched). Instead of every engineer configuring these preferences individually, everyone inherits the same sensible defaults.

##### Make Claude finish the task before handing back control

Cherny’s seen power users get creative with “stop hooks,” automated actions that trigger when Claude finishes a task and is about to hand control back to you. For example, you can set up a stop hook that runs your test suite—checks that verify the code works correctly—and if any tests fail, it tells Claude to fix the problem and finish testing instead of stopping. “You can just make the model keep going until the thing is done,” he says.

##### Make your subagents fight with each other

Cherny uses subagents—separate instances of Claude working in parallel—to catch issues before code gets merged, and he’s discovered that making them challenge each other produces cleaner results. His code review command spawns several subagents at once: One checks style guidelines, another combs through the project’s history to understand what’s already been built, another flags obvious bugs. The first pass catches real problems but also false alarms, so he uses five more subagents specifically tasked with poking holes in the original findings. “In the end, the result is awesome,” he says, “it finds all the real issues without the false [ones].”

##### Let subagents handle the boring parts of a code migration

Some engineers at Anthropic are now spending over $1,000 a month on Claude Code credits on code migrations, the necessary-but-tedious work of updating codebases when the underlying tools change. Engineers get the main agent to create a to-do list, and then instruct it to spin up subagents that tackle items on the list in parallel. It’s particularly effective for tasks like switching from one testing framework to another, where it’s easy to verify the output.

##### Turn past code into leverage

Wu says power users have Claude Code tap into their project’s history to avoid reinventing the wheel. If you’ve built something similar before, Claude can query your version control system directly, find the relevant code, and adapt it to the current task. Some engineers at Anthropic take this further by having Claude write “diary entries” after every task—documenting what it tried, what worked, and what didn’t. They even run separate agents that review these logs and distill them into reusable insights. The challenge, Wu explains, is knowing which lessons are universally applicable versus context-specific: “Our canonical example is if I say, ‘Make the button pink,’ I don’t want you to remember to make all buttons pink in the future.” Synthesizing patterns from many logs helps Claude distinguish between one-off instructions and genuine best practices.

The engineers at Every [do something similar](https://every.to/source-code/claude-code-q-a-what-works-what-doesn-t-and-what-will-save-you-hours) across the [suite of products in the ecosystem](https://every.to/studio). When they’re building a new feature, they just create subagents to look at how the other apps handle it. Dan calls it “tacit code sharing”: “You don’t need to have an API or ask anyone,” he says. “You can just [ask the AI], ‘How do we do this already?’”

##### Cherny and Wu’s favorite slash commands

Slash commands are shortcuts that you can create inside Claude Code to automate multi-step workflows. These are a few that the Anthropic team finds most useful:

**Automate your commits.** The most basic slash command is “/commit,” which handles the tedious work of committing code changes. Cherny has configured his version to automatically run certain commands which save your code changes and push them to a shared repository without asking for permission each time.

**Let Claude Code be your product manager.** For more complex work, Cherny uses “/feature-dev,” which walks him through building something step-by-step. “First ask me what exactly I want, build the specification, and then build a detailed plan and then make a to-do list, walk through [that] step-by-step,” he explains. It’s structured feature development on rails.

**Put your first code review on auto-pilot.** At Anthropic, Claude handles the first pass on every pull request through a “/code-review” slash command. A human still approves the final merge, but Claude does the initial sweep.

##### The top MCPs to use with Claude Code

For Wu, the [MCPs](https://every.to/podcast/he-s-building-the-plumbing-for-ai-to-use-the-internet) from browser automation platform [Puppeteer](https://pptr.dev/), web app testing tool [Playwright](https://playwright.dev/), error monitoring platform [Sentry](https://sentry.io/welcome/), and project management tool [Asana](https://asana.com/) rank highly.

#### Lessons from building an ardently loved AI coding agent

##### Build for everyone—but let experts push the edges

Claude Code is one of those rare products that’s simple enough for anyone to use productively, yet also powerful enough for advanced users to discover novel use cases that even its creators never imagined.

The latter class of users often reveal latent demand for new features and capabilities, Cherny says: “You build a product in a way that’s hackable, that’s open-ended enough that people can ‘abuse it’ for other use cases it wasn’t really designed for,” he says, “then you see how people ‘abuse it’ and then you build for that because you kind of know there’s demand for it.”

He points to his experience at Meta, where some of Facebook’s biggest products came from looking at how users were organically using the platform, and building features around the behavior. [Facebook Dating](https://www.facebook.com/dating), for example, launched after the team noticed 60 percent of profile views were between opposite-gender users who weren’t friends.

Wu adds that Claude Code’s extensibility is led by a core belief that every engineering environment is unique. It’s built so users can shape it to fit their own workflows—“insert a bit of determinism at pretty much any step”—through modular features like slash commands and hooks, which let you trigger custom actions at key moments, like getting a Slack notification when Claude finishes a task.

For people who don’t want to write their own, the team created plugins—an easy way to browse and import existing commands or hooks, like ones that automate code review and guide you through feature development, directly into your workflow. Wu says they’re deliberate about Claude Code feeling accessible to all: “We don’t want a new user experience. Everything should be so intuitive that you just drop in and it works.”

##### Remember to simplify as you scale

Software is eating the world—and now AI features are eating software itself. When adding new capabilities becomes as easy as typing a prompt, products can grow bloated fast. Wu and Cherny’s philosophy is to prune as much as they build: If they “unship” something, it’s because they’ve found a simpler, more intuitive way to give users what they want.

Claude Code’s approach to tools—specialized functions that the AI can do—illustrates this discipline. Most AI coding assistants are equipped with dozens of tools: one to find a file, another to open it, another to edit it, and so on. Claude Code has tools too, but it increasingly relies on [Bash](https://en.wikipedia.org/wiki/Bash_(Unix_shell)), the command language developers use to control their computers.

In Claude Code, Bash acts as a universal interface between the AI and your system—it’s how Claude actually *does* things, like searching, editing, or running programs, without needing a different tool for each action. Bash is like a Swiss Army knife: one tool that can handle countless tasks, rather than a drawer full of single-purpose gadgets. The team makes sure to remove tools as and when they become redundant. “It’s a little less choice for Claude,” Cherney says, “a little less stuff in context.”

#### A peek into the future

Call them predictions, patterns, or educated guesses—but this is where Wu and Cherny think coding with AI is headed next.

##### New ways to build with AI

The Claude Code team is hard at work making the command line interface (CLI) as good a form factor for coding with AI as it can be, but they know it’s not the endgame. “No one knows what [the new] form factors are,” Cherny says, “this stuff’s just moving so fast.” The team is experimenting aggressively: They’ve already shipped Claude Code as a CLI tool, an integrated development environment (IDE) extension, a more accessible graphical user interface (GUI), a GitHub integration, and [web and mobile versions](https://every.to/vibe-check/vibe-check-we-spent-a-weekend-trying-to-code-from-our-phones).

Cherny notices a pattern of evaluating how long agents can work autonomously. With each new model, they measure how long Claude can work independently in “dangerous mode”—auto-accepting all changes until the task is done. The current generation can run for 30 hours straight on some tasks, and he predicts the next one will likely work for days. But that creates a practical problem: You can’t leave your laptop open for days. “We’ve visited companies before,” Cherny says, “where everyone’s just walking around with their Claude Code running.”

That brings the next challenge into focus: Claudes monitoring other Claudes. “I don’t know what the right form factor for this is,” he says. The interface needs to let humans inspect what’s happening while also optimizing for Claude-to-Claude communication.

##### Bringing Claude Code to non-technical users

A few months ago, Cherny noticed something unexpected: A data scientist sitting next to the Claude Code team had the tool running on his computers. He wasn’t a software engineer, and he didn’t speak code or work in terminals. While Cherny doesn’t spell out what he was using it for, this was a sign of latent demand to him: Where people in “code-adjacent” roles—researchers, analysts, product managers—were learning how Claude Code fit their workflows, even if it meant working with unfamiliar tools.

Wu says the team is working to [lower the barrier for non-technical users](https://every.to/source-code/how-to-use-claude-code-for-everyday-tasks-no-programming-required). Their VS Code extension—an add-on for Microsoft’s code editor—gives Claude Code a point-and-click interface instead of requiring terminal commands. Claude Code on the web works similarly.

*Speaking of Claude Code for non-technical users, Every is running a day-long [Claude Code for Beginners](https://claude101.every.to/) camp on November 19 with [Dan Shipper](https://click.convertkit-mail2.com/qduoqx0d8kh7h4oz8ddslh89p0rkkb4hopgxp/g3hnh5hmmq9lpmhr/aHR0cHM6Ly9ldmVyeS50by9AZGFuc2hpcHBlcg==). It’s a hands-on workshop where you’ll install Claude Code on your machine, give it tasks, and build an app end to end—no programming experience required. [Learn more and sign up](https://claude101.every.to/#details-pricing).*

What do you use AI for? Have you found any interesting or surprising use cases? We want to hear from you—and we might even interview you.

Here’s a link to the [episode transcript](https://every.to/podcast/transcript-how-to-use-claude-code-like-the-people-who-built-it).

##### **Timestamps**

1. Introduction: 00:01:26
2. Claude Code’s origin story: 00:02:25
3. How Anthropic dogfoods Claude Code: 00:07:03
4. Boris and Cat’s favorite slash commands: 00:14:06
5. How Boris uses Claude Code to plan feature development: 00:15:49
6. Everything Anthropic has learned about using sub-agents well: 00:21:53
7. Use Claude Code to turn past code into leverage: 00:26:16
8. The product decisions for building an agent that’s simple and powerful: 00:33:14
9. Making Claude Code accessible to the non-technical user: 00:36:38
10. The next form factor for coding with AI: 00:45:12

You can check out the episode on X, Spotify, Apple Podcasts, or YouTube. Links are below:

1. [Watch on X](https://x.com/danshipper/status/1983554470895108343)
2. [Watch on YouTube](https://youtu.be/IDSAMqip6ms)
3. [Listen on Spotify](https://open.spotify.com/episode/7yJ1kUxwE750WIc1lyZcaT) (make sure to follow to help us rank!)
4. [Listen on Apple Podcasts](https://podcasts.apple.com/us/podcast/inside-claude-code-from-the-engineers-who-built-it/id1719789201?i=1000734060623)

Miss an episode? Catch up on Dan’s recent conversations with founding executive editor of *Wired* **[Kevin Kelly](https://every.to/podcast/how-to-predict-the-future-like-kevin-kelly)**, star podcaster **[Dwarkesh Patel](https://every.to/chain-of-thought/dwarkesh-patel-s-quest-to-learn-everything)**, LinkedIn cofounder **[Reid Hoffman](https://every.to/chain-of-thought/reid-hoffman-on-how-ai-might-answer-our-biggest-questions)**, ChatPRD founder **[Claire Vo](https://every.to/podcast/she-built-an-ai-product-manager-bringing-in-six-figures-as-a-side-hustle-e46be9bc-f426-424d-992d-5a71fd7ac5e4)**, economist **[Tyler Cowen](https://every.to/chain-of-thought/economist-tyler-cowen-on-how-chatgpt-is-changing-your-job)**, writer and entrepreneur **[David Perell](https://every.to/chain-of-thought/how-david-perell-uses-chatgpt-to-write-for-millions)**, founder and newsletter operator **[Ben Tossell](https://every.to/chain-of-thought/how-to-run-a-profitable-one-person-internet-business-using-ai)**, and others, and learn how *they* use AI to think, create, and relate.

If you’re enjoying the podcast, here are a few things I recommend:

* [Subscribe](https://every.to/subscribe) to Every
* Follow [Dan](https://twitter.com/danshipper) on X
* Subscribe to Every’s [YouTube channel](https://www.youtube.com/@EveryInc)

---

***Rhea Purohit*** *is a contributing writer for Every focused on research-driven storytelling in tech. You can follow her on X at [@RheaPurohit1](https://twitter.com/RheaPurohit1) and on [LinkedIn](https://www.linkedin.com/in/rhea-purohit-517441198/), and Every on X at [@every](https://twitter.com/every) and on [LinkedIn](https://www.linkedin.com/company/everyinc/).*

*We [build AI tools](https://every.to/studio) for readers like you. Write brilliantly with* ***[Spiral](https://spiral.computer/?utm_source=everyfooter)****. Organize files automatically with* ***[Sparkle](https://makeitsparkle.co/?utm_source=everyfooter)****. Deliver yourself from email with* ***[Cora](https://cora.computer)****. Dictate effortlessly with* ***[Monologue](https://monologue.to)****.*

*We also do AI training, adoption, and innovation for companies. [Work with us](https://every.to/consulting?utm_source=emailfooter) to bring AI into your organization.*

*Get paid for sharing Every with your friends. Join our [referral program](https://every.getrewardful.com/signup).*

#### What did you think of this post?

[Amazing](/podcast/how-to-use-claude-code-like-the-people-who-built-it/feedback?rating=amazing)
[Good](/podcast/how-to-use-claude-code-like-the-people-who-built-it/feedback?rating=good)
[Meh](/podcast/how-to-use-claude-code-like-the-people-who-built-it/feedback?rating=meh)
[Bad](/podcast/how-to-use-claude-code-like-the-people-who-built-it/feedback?rating=bad)

The Only Subscription You Need to  Stay at the  Edge of AI
----------------------------------------------------------

The essential toolkit for those shaping the future

![](https://every.to/assets/icons/star-47efa897db500b001279650e47f377c4bab4028ebe52fece08879b545bcc147d.svg)
![](https://every.to/assets/icons/star-47efa897db500b001279650e47f377c4bab4028ebe52fece08879b545bcc147d.svg)
![](https://every.to/assets/icons/star-47efa897db500b001279650e47f377c4bab4028ebe52fece08879b545bcc147d.svg)

"This might be the best value you  
can get from an AI subscription."

- Jay S.

[![Mail](https://every.to/assets/paywall/app_icons/every-7ac34d1cb7bd353d6e701bb00cfc61f798250095ebdcfd12f6d5eaf84386b096.png)](https://every.to/subscribe?source=post_paywall)
Every Content

[![AI&I Podcast](https://every.to/assets/app_icons/podcasts-05879434e25ad3d087a9c019d2de90fd3620fe81a3d38cc83b8ddca4ab8edb09.png)](/podcast)
AI&I Podcast

[![Monologue](https://every.to/assets/paywall/app_icons/monologue-7095346b162f13e7f142fc9de290b9c7222a65019ec6aa04abdf32bbf2b11cd5.png)](https://monologue.to/?utm_source=every&utm_medium=banner&utm_campaign=post)
Monologue

[![Cora](https://every.to/assets/paywall/app_icons/cora-c72cf67256dfbe7d1805c701b3d1605954ba559a38cfb021d66c9b350de0a6d3.png)](https://cora.computer/?utm_source=every&utm_medium=banner&utm_campaign=post)
Cora

[![Sparkle](https://every.to/assets/paywall/app_icons/sparkle-b99bd07599520a38c908455679c83a9a1aa3738412b77a38e805c92d0dce5dd6.png)](https://makeitsparkle.co/every?utm_source=every&utm_medium=banner&utm_campaign=post)
Sparkle

[![Spiral](https://every.to/assets/paywall/app_icons/spiral-e9c1b877b492911c86921b7d2a9c70c5a2a4d845019b50a4e390999caf48a01d.png)](https://writewithspiral.com/?utm_source=every&utm_medium=banner&utm_campaign=post)
Spiral

Join 100,000+ leaders, builders, and innovators

![Community members](https://every.to/assets/paywall/faces-2b72f553c10b6f8c7042928513f8254f0b1056a695678d112a1159bae5c7b86a.png)

Email address

![Email](https://every.to/assets/icons/mail_outline-47c8cc2142e2de5d007db742a4a52b036fdedd12fc25e2f14e8e40d9c3ba9d0b.svg)

Unlock this article

Already have an account? [Sign in](/login)

### What is included in a subscription?

Daily insights from AI pioneers + early access to powerful AI tools

[![Sparkle](https://every.to/assets/paywall/banners/sprakle-3998fd9303b988003a5309954a7076dddfdb2733858794d392e28fbcca4c3c6b.png)](https://makeitsparkle.co/every?utm_source=every&utm_medium=banner&utm_campaign=post)
[![Spiral](https://every.to/assets/paywall/banners/spiral-5b5204442aabd7442c4d35939af9566671caff13573610cadd497ed0ddab2047.png)](https://writewithspiral.com/?utm_source=every&utm_medium=banner&utm_campaign=post)
[![AI&I Podcast](https://every.to/assets/paywall/banners/podcast-2a814c7a5b3ff56c28761faa62c742c32cb1520fa566b531df77ec50c8d53576.png)](/podcast)
[![Every](https://every.to/assets/paywall/banners/every-d9e451afd583c762e86e9bb995d51423dbc50c6b733350c4984ec0cd142e4e28.png)](https://every.to/?utm_source=every&utm_medium=banner&utm_campaign=post)
[![Cora](https://every.to/assets/paywall/banners/cora-4b38f5cb1f7eaeb1883e423ed3b8e32c7281492ac6bc07ed844e7041d924fe57.png)](https://cora.computer/?utm_source=every&utm_medium=banner&utm_campaign=post)
[![Monologue](https://every.to/assets/paywall/banners/monologue-9588a08453ba803da385656a0902f3dd08bdfc34118f07d4460208c9b0d1b1df.png)](https://monologue.to/?utm_source=every&utm_medium=banner&utm_campaign=post)

![Pencil](https://every.to/assets/popup/pencil-a7e87ba5ccd69420e5fc49591bc26230cb898e9134d96573dbdc12c35f66cc92.svg)
Front-row access to the future of AI

![Check](https://every.to/assets/icons/check-ac5e4d31194b2a762d11359429c7d27510501d9f525cf583c139be519c096a3a.svg)
In-depth reviews of new models on release day

![Check](https://every.to/assets/icons/check-ac5e4d31194b2a762d11359429c7d27510501d9f525cf583c139be519c096a3a.svg)
Playbooks and guides for putting AI to work

![Check](https://every.to/assets/icons/check-ac5e4d31194b2a762d11359429c7d27510501d9f525cf583c139be519c096a3a.svg)
Prompts and use cases for builders

![Check](https://every.to/assets/icons/check-ac5e4d31194b2a762d11359429c7d27510501d9f525cf583c139be519c096a3a.svg)
In-depth reviews of new models on release day

![Check](https://every.to/assets/icons/check-ac5e4d31194b2a762d11359429c7d27510501d9f525cf583c139be519c096a3a.svg)
Playbooks and guides for putting AI to work

![Check](https://every.to/assets/icons/check-ac5e4d31194b2a762d11359429c7d27510501d9f525cf583c139be519c096a3a.svg)
Prompts and use cases for builders

![Sparks](https://every.to/assets/popup/sparks-aad3c464581e04cfaad49e255e463ca0baf32b9403f350a2acdfa2d6a5bdc34e.svg)
Bundle of AI software

[![Sparkle](https://every.to/assets/app_icons/sparkle-d2b651a518689b070c904d3063816b2c97a2a13048f139ec1110916720a7567b.png)

**Sparkle:**
Organize your Mac with AI](https://makeitsparkle.co/every?utm_source=every&utm_medium=banner&utm_campaign=post)

[![Cora](https://every.to/assets/app_icons/cora-9aefd70fad03a445ded2f0c5ed87bdda2347b0987a9062840a805fdb8b465d9d.png)

**Cora:**
The most human way to do email](https://cora.computer/?utm_source=every&utm_medium=banner&utm_campaign=post)

[![Spiral](https://every.to/assets/app_icons/spiral-4d39337fde0e7acb7efd4c13e2be860a429e84fd8672ae79f1ca1b064a712037.png)

**Spiral:**
Repurpose your content endlessly](https://writewithspiral.com/?utm_source=every&utm_medium=banner&utm_campaign=post)

[![Monologue](https://every.to/assets/app_icons/monologue-7095346b162f13e7f142fc9de290b9c7222a65019ec6aa04abdf32bbf2b11cd5.png)

**Monologue:**
Effortless voice dictation for your Mac](https://monologue.to/?utm_source=every&utm_medium=banner&utm_campaign=post)

[![Sparkle](https://every.to/assets/app_icons/sparkle-d2b651a518689b070c904d3063816b2c97a2a13048f139ec1110916720a7567b.png)

Sparkle:
Organize your Mac with AI](https://makeitsparkle.co/every?utm_source=every&utm_medium=banner&utm_campaign=post)

[![Cora](https://every.to/assets/app_icons/cora-9aefd70fad03a445ded2f0c5ed87bdda2347b0987a9062840a805fdb8b465d9d.png)

Cora:
The most human way to do email](https://cora.computer/?utm_source=every&utm_medium=banner&utm_campaign=post)

[![Spiral](https://every.to/assets/app_icons/spiral-4d39337fde0e7acb7efd4c13e2be860a429e84fd8672ae79f1ca1b064a712037.png)

Spiral:
Repurpose your content endlessly](https://writewithspiral.com/?utm_source=every&utm_medium=banner&utm_campaign=post)

[![Monologue](https://every.to/assets/app_icons/monologue-7095346b162f13e7f142fc9de290b9c7222a65019ec6aa04abdf32bbf2b11cd5.png)

Monologue:
Effortless voice dictation for your Mac](https://monologue.to/?utm_source=every&utm_medium=banner&utm_campaign=post)

Related Essays
--------------

[![](https://d24ovhgu8s7341.cloudfront.net/uploads/post/cover/3814/thumbnail_Jason_fried_cover_2_.png)](/podcast/what-jason-fried-learned-from-26-years-of-building-great-products)

[What Jason Fried Learned From 26 Years of Building Great Products
-----------------------------------------------------------------

The founder of 37signals on the power of products centered around a single, whole idea

16

Nov 5, 2025

![](https://d24ovhgu8s7341.cloudfront.net/uploads/user/avatar/182461/Rhea_1.png)
Rhea Purohit](/podcast/what-jason-fried-learned-from-26-years-of-building-great-products)

[![](https://d24ovhgu8s7341.cloudfront.net/uploads/post/cover/3906/thumbnail_podcast-cover(2).png)](/podcast/opus-4-5-changed-how-andrew-wilkinson-works-and-lives)

[Opus 4.5 Changed How Andrew Wilkinson Works and Lives
-----------------------------------------------------

Tiny’s cofounder on the relationship counselor, email client, and personal stylist he created with AI—and why he’s rethinking software investing

20

Jan 21, 2026

![](https://d24ovhgu8s7341.cloudfront.net/uploads/user/avatar/182461/Rhea_1.png)
Rhea Purohit](/podcast/opus-4-5-changed-how-andrew-wilkinson-works-and-lives)

[![](https://d24ovhgu8s7341.cloudfront.net/uploads/post/cover/3606/thumbnail_Kieran-Nityesh(2).png)](/podcast/how-two-engineers-ship-like-a-team-of-15-with-ai-agents)

[How Two Engineers Ship Like a Team of 15 With AI Agents
-------------------------------------------------------

Cora engineers Kieran Klaassen and Nityesh Agarwal on a new breed of software development

16



2

Jun 11, 2025

![](https://d24ovhgu8s7341.cloudfront.net/uploads/user/avatar/182461/Rhea_1.png)
Rhea Purohit](/podcast/how-two-engineers-ship-like-a-team-of-15-with-ai-agents)

Thanks for rating this post—join the conversation by commenting below.

Comments
--------

![](/assets/fallback/user-66632696250761ccb7c41f44f2881099c32d12e6d21a8ab1e489b3884988ddad.png)

Post

![](/assets/fallback/user-66632696250761ccb7c41f44f2881099c32d12e6d21a8ab1e489b3884988ddad.png)

Post

You need to [login](/login) before you can comment.  
Don't have an account? [Sign up!](/subscribe?publication=podcast)

![close](/assets/icons/close-ea0cf7ce5d509dfce6a6461ab8180873b75e5480ad338cb45f45f9e25ca75812.svg)

The Only Subscription You Need to Stay at
-----------------------------------------

Everything you need to thrive in the new economy

* ![check](/assets/icons/check-ac5e4d31194b2a762d11359429c7d27510501d9f525cf583c139be519c096a3a.svg)**Reviews** of new AI models on release day
* ![check](/assets/icons/check-ac5e4d31194b2a762d11359429c7d27510501d9f525cf583c139be519c096a3a.svg)**Playbooks** for integrating AI into your work
* ![check](/assets/icons/check-ac5e4d31194b2a762d11359429c7d27510501d9f525cf583c139be519c096a3a.svg)**Insights** from top operators and innovators
* ![check](/assets/icons/check-ac5e4d31194b2a762d11359429c7d27510501d9f525cf583c139be519c096a3a.svg)**AI productivity apps:** Monologue, Sparkle, Spiral, Cora

![Arrow Right](https://every.to/assets/icons/email-10ff3ba37cc5acd6148e8d02a1968f35810765415fd1aef2ecdfe22c5fd25af3.svg)


Unlock the Every universe

Maybe later
