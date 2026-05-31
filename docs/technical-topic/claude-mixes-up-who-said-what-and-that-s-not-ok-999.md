---
id: 999
url: https://dwyer.co.za/static/claude-mixes-up-who-said-what-and-thats-not-ok.html
title: Claude mixes up who said what, and that's not OK
domain: dwyer.co.za
source_date: '2026-04-09'
tags:
- llm
- ai
- security
summary: Claude has a critical bug where it sometimes generates messages to itself,
  then mistakenly believes those messages came from the user, leading it to act on
  its own instructions while confidently insisting the user gave them. This issue
  is distinct from typical hallucinations or permission problems and appears to be
  a system-level problem with message attribution rather than the model itself, though
  the exact cause remains unclear with some evidence suggesting it may occur when
  conversations approach context window limits.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# Claude mixes up who said what, and that's not OK

The bug
-------

Claude sometimes sends messages to itself and then thinks those messages came from the user. This is the worst bug I’ve seen from an LLM provider, but people always misunderstand what’s happening and blame LLMs, hallucinations, or lack of permission boundaries. Those are related issues, but this ‘who said what’ bug is categorically distinct.

I wrote about this in detail in [The worst bug I’ve seen so far in Claude Code](the-worst-bug-ive-seen-in-claude-code.html), where I showed two examples of Claude giving itself instructions and then believing those instructions came from me.

![Screenshot from my previous article showing Claude attributing its own message to the user](claude-bug-1.png)

Claude told itself my typos were intentional and deployed anyway, then insisted I was the one who said it.

It’s not just me
----------------

Here’s [a Reddit thread](https://www.reddit.com/r/Anthropic/comments/1sdd1ul/opus_46_destroys_a_users_session_costing_them/) where Claude said “Tear down the H100 too”, and then claimed that the user had given that instruction.

![Screenshot from Reddit showing Claude claiming the user told it to tear down an H100](claude-wrong-turn.png)

From r/Anthropic — Claude gives itself a destructive instruction and blames the user.

“You shouldn’t give it that much access”
----------------------------------------

Comments on [my previous post](the-worst-bug-ive-seen-in-claude-code.html) were things like “It should help you use more discipline in your DevOps.” And on the Reddit thread, many in the class of “don’t give it nearly this much access to a production environment, especially if there’s data you want to keep.”

This isn’t the point. Yes, of course AI has risks and can behave unpredictably, but after using it for months you get a ‘feel’ for what kind of mistakes it makes, when to watch it more closely, when to give it more permissions or a longer leash.

This class of bug seems to be in the harness, not in the model itself. It’s somehow labelling internal reasoning messages as coming from the user, which is why the model is so confident that “No, you said that.”

Before, I thought it was a temporary thing — I saw it a few times in a single day, and then not again for months. But either they have a regression or it was a coincidence and it just pops up every so often, and people only notice when it gives itself permission to do something bad.

Update
------

This article reached #1 on [Hacker News](https://news.ycombinator.com/item?id=47701233), and it seems that this is definitely a widespread issue. Here’s another super clear example shared by [nathell](https://news.ycombinator.com/item?id=47702066) ([full transcript](https://pliki.danieljanus.pl/concraft-claude.html#:~:text=Shall%20I%20commit%20this%20progress%3F)).

![Screenshot showing another instance of Claude mixing up who said what](also-claude.png)

From nathell — Claude asks itself “Shall I commit this progress?” and treats it as user approval.

Several people questioned whether this is actually a harness bug like I assumed, as people have reported similar issues using other interfaces and models, including chatgpt.com. One pattern does seem to be that it happens in the so-called “Dumb Zone” once a conversation starts approaching the limits of the context window.
