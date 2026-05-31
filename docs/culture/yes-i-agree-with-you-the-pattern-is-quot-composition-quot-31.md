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

|  |  |  |  |
| --- | --- | --- | --- |
| |  |  |  | | --- | --- | --- | |  | **[Hacker News](news)**[new](newest) | [past](front) | [comments](newcomments) | <ask> | <show> | <jobs> | <submit> | [login](login?goto=item%3Fid%3D46524197) | |
|
| |  |  |  | | --- | --- | --- | |  |  | [santiagobasulto](user?id=santiagobasulto) [4 months ago](item?id=46524197)  | [parent](item?id=46523901) | [context](item?id=46476915#46524197) | [favorite](fave?id=46524197&auth=974d72123d86089fe91af0e7f6c3d3f9723fe1b7) | on: [Rust is beyond object-oriented, part 3: Inheritanc...](item?id=46476915 "Rust is beyond object-oriented, part 3: Inheritance (2023)")   Yes I agree with you. The pattern is "composition" vs "inheritance". Defining a "thing" as "what it can do" instead of "what it is". Instead of saying that "a duck is a Bird which in turn is an Animal which in turn is a LivingThing" (Duck -> Bird -> Animal -> LivingThing) you focus on what a duck can do: a duck "quacks, swims, etc": ```     class Duck(Swimmable, Quackable, FishEatable...) ```  I think there's still a place for "inheritance" based approach for APIs that need to be very strict about subtyping: would be hard to express covariance/invariance/contravariance without it. | |  | |  | |
| |  | | --- | |  |    [Guidelines](newsguidelines.html) | [FAQ](newsfaq.html) | [Lists](lists) | [API](https://github.com/HackerNews/API) | [Security](security.html) | [Legal](https://www.ycombinator.com/legal/) | [Apply to YC](https://www.ycombinator.com/apply/) | [Contact](mailto:hn@ycombinator.com) |
