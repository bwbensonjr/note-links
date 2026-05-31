---
id: 31
url: https://news.ycombinator.com/item?id=46524197
title: Yes I agree with you. The pattern is &quot;composition&quot; vs &quot;inheritance&quot;.
  Defining a ... | Hacker News
domain: news.ycombinator.com
source_date: '2026-01-07'
tags:
- social-media
- web-dev
summary: This Hacker News comment discusses the debate between composition and inheritance
  in object-oriented programming. The author advocates for composition (defining objects
  by their behaviors/capabilities) over inheritance hierarchies, while acknowledging
  that inheritance still has value for APIs requiring strict subtyping rules and variance
  handling (covariance/invariance/contravariance).
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# Yes I agree with you. The pattern is &quot;composition&quot; vs &quot;inheritance&quot;. Defining a ... | Hacker News

Hacker News new | past | comments | ask | show | jobs | submit login santiagobasulto 5 days ago | parent | context | favorite | on: Rust is beyond object-oriented, part 3: Inheritanc... Yes I agree with you. The pattern is "composition" vs "inheritance". Defining a "thing" as "what it can do" instead of "what it is". Instead of saying that "a duck is a Bird which in turn is an Animal which in turn is a LivingThing" (Duck -> Bird -> Animal -> LivingThing) you focus on what a duck can do: a duck "quacks, swims, etc": class Duck(Swimmable, Quackable, FishEatable...) I think there's still a place for "inheritance" based approach for APIs that need to be very strict about subtyping: would be hard to express covariance/invariance/contravariance without it. Guidelines | FAQ | Lists | API | Security | Legal | Apply to YC | Contact
