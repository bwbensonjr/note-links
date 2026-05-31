---
id: 100
url: https://eavan.blog/posts/beautiful-sandpiles.html
title: Beautiful Abelian Sandpiles
domain: eavan.blog
source_date: '2025-12-13'
tags:
- academic-paper
- physics
summary: Abelian sandpiles are mathematical models on grids where sand grains topple
  between cells when a cell contains four or more grains, creating intricate symmetric
  patterns. The key insight is that these sandpiles form an abelian group—meaning
  the order of toppling operations doesn't matter—which connects them to abstract
  algebra and group theory. The blog explores how sandpiles can be added together
  and reveals that the "identity sandpile" (the special element that leaves other
  sandpiles unchanged when added) displays beautiful, nearly fractal-like patterns.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# Beautiful Abelian Sandpiles

Beautiful Abelian Sandpiles
---------------------------

Published 2025-12-9

I can't remember where I first saw them, but ever since, I have been unable to forget them: abelian sandpiles. I'm far from the only [one](https://nullprogram.com/blog/2020/04/30/). They're remarkably simple, yet produce lovely symmetric patterns. I loved them so much that I adorned the title banner of this blog with an animation of an abelian sandpile. But what exactly are abelian sandpiles? How do they work? And how many pretty, mesmerizing pictures can we make with these things?

Let's start with an explanation. An abelian sandpile lives on a grid. On each grid cell there can be any number of grains of sand. But if there are four or more grains of sand on a single cell, then the grains topple over into the four neighbouring cells. Toppling might cause other grid cells to have four or more grains of sand, so they also must topple. This repeats until all cells have three grains of sand or fewer, at which point the abelian sandpile is said to be stable. If a cell topples on the edge of the grid, then a grain "falls off" the edge and only the neighbours of the cell that are in the grid gain a grain of sand. This ensures that toppling always finishes in a final stable sandpile. Try adding grains to the grid below to see how the rules work.

Reset

Repeatedly adding grains of sand to the center gives a smaller version of the animation that lives on the top of my blog. If you try this, then it doesn't take long before you start seeing the some grid configurations repeat.

Notice how when there are many neighbouring cells with three grains of sand, adding one more grain of sand causes a cascade of toppling and the final stable pattern is hard to predict. You might wonder how we should handle cases where there are multiple grid cells that need to be toppled. Since toppling one cell affects its neighbours then we need to be careful about the order we topple cells. Or do we?

This brings me neatly to the "Abelian" term. From here on, I will be referring to abelian sandpiles as just sandpiles. In the context of Group Theory, an abelian group is both associative and commutative. In "English", this means that order doesn't matter. This is precisely analogous to addition of numbers. When you are summing a set of numbers, no matter in which order you add them together, you will get the same result.

As it turns out, the same is true of toppling cells in our sandpile, which is part of the reason why it carries the name "Abelian". This might seem like a quirky observation that I can use to simplify my toppling implementation. Which is true. However, it also gives us a connection to a rich field of Mathematics: namely "Abstract Algebra" & "Group Theory". We will use this later to generate a nice pattern, but for now let's simply focus on the fact that the toppling order is irrelevant. I won't be proving that toppling order is irrelevant, but I will at least demonstrate it.

In the sandpile widget above, you can build a sandpile by adding one grain at a time, and toppling is done eagerly as soon as a cell has more than 4 grains of sand. Since I've now claimed that toppling order is irrelevant, we can consider a different way of building a sandpile. We can add all the grains of sand at the beginning, allowing cells to temporarily have 4 grains of sand or more. Then, when we're done, we can topple all the cells that have 4 grains or more. You can try this in the widget below. On the left you can place all the sand you want and on the right you'll see the usual view of what the sandpile looks like when toppling is done eagerly. When you're done adding sand, you can press "Topple" to topple all the sand in a random order. At the end, the left sandpile and the right sandpile will be equal.

Topple
Reset

No matter when we do the toppling we always get the same result. We can dump as much sand onto the grid as we like and just do all the toppling at the end. This lets us explore another interesting idea. What happens if we add one sandpile to another?

Let's say we have two sandpiles *A* and *B*. We can then create a new sandpile *A + B* by doing the element-wise sum of grid cells and then toppling the sand at the end. You can think of this as dumping all the sand in *B* onto *A* and then toppling.

The reason we want to add whole sandpiles directly is because, again, it lets us reach into the mathematical theory of groups. I mentioned earlier that because sandpiles form an abelian group, we add them in any order, but there's more that we can use. All groups *must* have something analogous to the number zero, where adding zero to a number has no effect. This means there must be a sandpile that when "added" to another sandpile leaves the other sandpile unchanged. This special sandpile has a name: the identity sandpile. You might think that this is just the empty sandpile, with no sand in any grid cell, but this is not the case. This is because the empty sandpile is excluded from the abelian group, by definition. In fact, many sandpiles are excluded from the abelian group because they don't have the right properties.

Let's take a short break to look at some animated sandpiles on different square grids. As you watch sand being added to each grid, can you spot anything that's different about the empty grid compared to other sandpiles encountered? By the time you read this, you might need to reset the grids to see the empty grid. Don't forget to take a moment to appreciate the nice geometric patterns that emerge.

Reset

You might notice that some sandpiles repeat and some sandpiles are never seen again. The empty grid is one such sandpiles that never repeats. This makes perfect sense. At every step we are adding sand to the grid. We occasionally lose sand due to it "falling off" the edges of the grid, but we can never lose all the sand on the grid by adding more sand. So once we've added some sand to the grid, we can never get back to the empty grid. We can call the patterns that repeat "recurrent" and the patterns that don't repeat "transient".

It is precisely the recurrent sandpiles that have the nice properties required to make them an abelian group. Since the empty sandpile is transient, it is not included. Therefore, the group rules don't apply to the empty sandpile and the empty sandpile is not allowed to be the special identity sandpile.

But this makes the identity sandpile even more interesting. If it can't be the empty sandpile, then what kind of sandpile could leave a different sandpile unchanged when adding them together. Since it must be a recurrent sandpile, then it must be mostly filled with sand, but how should this sand be arranged?

A proper explanation would go well beyond the scope of this blog post, so let's skip to the conclusion: pretty pictures. Below you can see what the idendity sandpile looks like for different grids, including rectangular ones. It might take a few seconds for larger grids. Mess around and see if you can find something that you like.

Grid Width:

5
Grid Height:

5

Calculate

The rules of abelian groups guarantee that these identity sandpiles must exist, but they tell us nothing about how beautiful they are. These identity sandpiles are almost fractal like in nature, with their repeating triangular patterns. In fact, they may actually become fractals as the size of the grid tends to infinity, but not much is known about the scaling limits of the identity sandpile at the time of writing. For now, we'll just have to appreciate their beauty in the finite case. Perhaps if you're looking for a pattern to tile a bathroom in the future, think of the humble sandpile.

If you want to learn more about sandpiles, there is also an excellent [Numberphile video](https://www.youtube.com/watch?v=1MtEUErz7Gg) you can watch.
