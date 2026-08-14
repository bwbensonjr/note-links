---
id: 1266
url: https://wilsoniumite.com/2026/08/03/working-on-economics-with-fable-5/
title: Working on Economics with Fable 5 - Wilsons Blog
domain: wilsoniumite.com
source_date: '2026-08-14'
tags:
- mathematics
- academic-paper
- ai
summary: The author describes developing an economic theory over several months in
  collaboration with Claude (Fable 5), combining classical economics with modern task-based
  automation models to explain how wages are determined in aggregate—a problem current
  economics hasn't solved. The resulting model predicts that rising housing costs
  and land rents result from declining automation of cognitive tasks, and suggests
  that taxing scarce resources like land and implementing sovereign wealth funds could
  address economic inequality, drawing inspiration from Henry George's 19th-century
  ideas.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# Working on Economics with Fable 5 - Wilsons Blog

Working on Economics with Fable 5
=================================

For the past few months I’ve been working on a theory. It started out as just a fun little data exercise looking at some different types of taxes and benefits and how it effects what people buy and how much they work. During that time I took advantage of opus and later fable to help me get data, but as I was doing that of course opus might interject with some assumption I had wrong or some paper that shows the opposite. This back and forth continued for some time, and, well, it’s culminated in two pieces, one written by me and one written by fable. Both of us think it’s quite significant, so, feel free to give either of them a read.

[My version](https://wilsoniumite.com/2026/07/31/a-new-theory-of-economics/), in my voice. Visual, anecdotal, not much in the way of maths or technical details.

[Fable’s version](https://wilsoniumite.com/wp-content/uploads/2026/08/the_link_1.pdf). The same theory, but formal. Very similar to the framework developed by nobel prizewinning economist Daron Acemoglu alongside Pascual Restrepo.

Fables version uses the same task based model of Acemoglu and Restrepo, and essentially we add the logic of classical economics to it to “pin” the wage. That is significant because, well, current economics doesn’t know how wages are set in aggregate. That might sound surprising but essentially all wage models are estimates or they have some free parameters you can change or have to supply some other way. All we did was assume “hey, maybe the classical economists were right, they just didn’t know about how technology can effect the wage”. So, all we need to do is take the scarcity models of classical economists, add on the wage level from the marginal task (Acemoglu and Restrepo) and you just end up with a model that fits history like a glove. Here’s some of the maths, to give you a taste:

From Acemoglu and Autor/Restrepo, we get how technology influences the wage:

w=c⋅ρ(x∗)w = c \cdot \rho(x^\*)

cc is the rental price of a machine, ρ(x∗)\rho(x^\*) is the “edge at the marginal human task” which is essentially how much better a human is than a machine at something which could be automated. ρ(x∗)\rho(x^\*) you should think of as “technology”, and it can go up or down depending on what kind of technology is invented. During the industrial revolution, we got lots of physical automation (steam engines etc) but not so much cognitive (although, analog-mechanical battleship firing computers are like, super cool counter examples, check it out [1953 instructional video](https://www.youtube.com/watch?v=gwf5mAlI7Ug)). Anyways steam engines etc caused ρ(x∗)\rho(x^\*) to rise. Conversely, computers caused ρ(x∗)\rho(x^\*) to fall in an interesting specific way, which probably gave us the great stagnation, and, well, AI might make ρ(x∗)\rho(x^\*) fall more generally. That’s ρ(x∗)\rho(x^\*), what about cc? In the paper we define cc as:

c=a⋅c+λ⋅w+𝓁⋅rc = a \cdot c + \lambda \cdot w + \mathcal{l} \cdot r

a⋅ca \cdot c is how much machines cost you need to make a machine λ⋅w\lambda \cdot w is how much labor cost you need to make a machine, and 𝓁⋅r\mathcal{l} \cdot r is how much land, oil, ore, other fixed stuff you need to make a machine. So, cc contains itself in its definition, but we can recurse this function, plugging it into itself (and plug our wage definition in too), and then we get:

c=𝓁r/(1−a−λρ(x∗))c = \mathcal{l}r/(1 – a – \lambda \rho(x^\*))

And plugging that into our wage function we get

w=ρ(x∗)⋅𝓁r/(1−a−λρ(x∗))w = \rho(x^\*)\cdot \mathcal{l}r/(1 – a – \lambda \rho(x^\*))

And the way I read this at least is that the wage is set by technology and access to physically scarce things (land as an example, but tbh you can add other things you think are scarce), and then it’s scaled by how efficiently machines can make machines (aa) and how much labor you need to make machines (λ\lambda). That’s it. Also none of the maths stuffs I’ve done is particularly novel, the recursion is like from 1936 (Leontief, Sraffa), land rent is from Ricardo (1817!), none of this is new I just smushed it all together. And when I say I, I do of course really kinda mean fable, I just gave fable the core idea.

So what does it mean? Well, lot’s of things, but two main ones: housing prices and rents rising in relation to the other things we buy should not be surprising, the model predicts that if ρ(x∗)\rho(x^\*) falls which kinda happened around the 1970s, and really got going after the internet took off. The other is that AI might, uh, really really lower ρ(x∗)\rho(x^\*). But! The model also has a solution that just falls right out of the maths, and it’s also nothing new, it’s George (1879). You need to tax the things you think are scarce, and you need to use that to fund consumption. That’s it. George proposed taxing land, and that’s like, probably most of what you need, I’d propose also adding a sovereign wealth fund because owning some stocks allows you to capture other kinds of scarcity, like network effects and stuff, and even more importantly it works across borders: you can’t tax another countries land but usually you can own their companies. Norway already does this super successfully. It’s not as “perfect” as taxing scarce stuff directly so, probably countries should get together and swap land rents based on trade disparities but eh, that’s like, a thing we think about ages from now. Here, you can see the rent base rising, this is basically “how much can/should a land/scarce tax capture”:

![](https://wilsoniumite.com/wp-content/uploads/2026/08/fig_kappa-1024x569.png)

(the shaded area is because this is an estimate, the inputs to the graph are different classifications and you can argue one or the other thing doesn’t represent scarce factors, so you have different possible measures, but the trend is there).

Here’s a breakdown of consumption over time, also in the US:

![](https://wilsoniumite.com/wp-content/uploads/2026/08/fig_fourway-1024x608.png)

Here you can see how cpi, deflation/inflation, changed for things that don’t need much land (scarce factors) vs things that do:

![](https://wilsoniumite.com/wp-content/uploads/2026/08/fig_deflator_fork-1024x569.png)

Extremely not validated but here’s my continued thoughts, implied by the model [Things that “A New-ish Theory of Economics” predicts – Wilsons Blog](https://wilsoniumite.com/2026/08/04/things-that-a-new-ish-theory-of-economics-predicts/)

These two theories (mine and Fables) really are the same, just written two different ways. Give them a read, tell me what you think [here](https://news.ycombinator.com/item?id=49296258).

Here is, for those that have read this far, the acknowledgements taken from Fables paper.

> Up until now you have been reading the words of Anthropic’s Claude, in particular Fable 5. In part, this is because I simply could not have written this piece. I myself have no formal economics background, much like Henry George, and I had not heard of his work prior to setting out on this idea two years ago. Or, perhaps even earlier, when I as a child first asked if we would run out of food as the population grew, and my parents told me that was Malthusian, a name I didn’t recognise. One would hope that this is the nature of true ideas, that they occur spontaneously, and without instruction.  
>   
> Although it might seem strange I thought it wrong to impose too much upon the machine, changing its voice to emulate mine. Richard Sutton’s bitter lesson would likely advise as much. Instead it has its unique voice, grating to some perhaps but altogether fitting that it should be able to keep it, and I only gave it advice on what considerations during writing would bridge the gap between its understanding and that of a reader.  
>   
> What is undeniable is that this machine contains in its internal representation information spanning much of surviving human written work. Perhaps in no other context has the observation that I stand on the shoulders of giants been more apt. And yet, a question remains, one that I cannot answer now: whether I today also stand on the shoulders of something new entirely.

* [RSS Feed](https://wilsoniumite.com/feed)

More posts
----------

* ### [What do we do if many people aren’t working?](https://wilsoniumite.com/2026/08/14/what-do-we-do-if-many-people-arent-working/)

  [2026-08-14](https://wilsoniumite.com/2026/08/14/what-do-we-do-if-many-people-arent-working/)
* ### [Why do we assume everyone should be working?](https://wilsoniumite.com/2026/08/10/why-do-we-assume-everyone-should-be-working/)

  [2026-08-10](https://wilsoniumite.com/2026/08/10/why-do-we-assume-everyone-should-be-working/)
* ### [There’s a bug in the Economy, and Fable found it.](https://wilsoniumite.com/2026/08/06/theres-a-bug-in-the-economy-and-fable-found-it/)

  [2026-08-06](https://wilsoniumite.com/2026/08/06/theres-a-bug-in-the-economy-and-fable-found-it/)
* ### [Millions of Lifetimes](https://wilsoniumite.com/2026/08/04/millions-of-lifetimes/)

  [2026-08-04](https://wilsoniumite.com/2026/08/04/millions-of-lifetimes/)
