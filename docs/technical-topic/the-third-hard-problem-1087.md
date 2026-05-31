---
id: 1087
url: https://mmapped.blog/posts/48-the-third-hard-problem
title: The third hard problem
domain: mmapped.blog
source_date: '2026-05-17'
tags:
- academic-paper
- compilers
summary: 'The article introduces "tree mapping" as a third hard problem in computer
  science: the challenge of embedding complex, interconnected webs of information
  into hierarchical tree structures that our brains naturally prefer. Through examples
  from file systems, writing, and architecture, the author demonstrates how this fundamental
  mismatch between the hierarchical organization we use (trees) and the non-linear
  nature of ideas and information (webs) creates persistent design challenges across
  computing and knowledge organization. While trees are efficient organizers that
  leverage our spatial intuition, they inevitably distort the true structure of complex
  systems that should exist in multiple places or categories simultaneously.'
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# The third hard problem

[The third hard problem](/posts/48-the-third-hard-problem.html)
===============================================================

✑2026-02-28[glasperlenspiel](/notes/glasperlenspiel.html)[programming](/notes/programming.html)


---

* [Spaces, trees, and webs](#spaces-trees-webs)
  + [File systems](#file-systems)
  + [Writing](#writing)
  + [Architecture](#architecture)
  + [Biology](#biology)
* [Conclusion](#conclusion)

---

According to a [classic joke](https://martinfowler.com/bliki/TwoHardThings.html) attributed to [Phil Karlton](https://www.karlton.org/karlton/),
computer science has only two hard problems: naming things and cache invalidation.
They are hard because no algorithm can solve them:
good names come from empathy and understanding,
and cache invalidation requires system thinking and careful analysis.
This article describes another such problem, pervasive and insidious yet rarely noticed:
mapping a general graph onto a hierarchical structure. I call it *tree mapping*.

[Spaces, trees, and webs](#spaces-trees-webs)
---------------------------------------------

Our brains evolved to be remarkably good at dealing with physical space.
We can intuitively orient ourselves in an unfamiliar city and draw an accurate map of a place we visited decades ago.
Naturally, we want to take advantage of this machinery in all aspects of our lives.

One of the defining features of a physical space is its hierarchical, localized structure.
We perceive each bit of space as self-contained and interacting only with nearby bits,
which enables a hierarchical view of the world in which objects form collections that can be understood as a whole:
particles form atoms, atoms form molecules, molecules form bodies, and so forth, up to galaxies and superclusters.

Hierarchies are so natural to us that they have become our dominant organizing tool.
We sort things and ideas into labeled boxes and put these into larger boxes.
It works for physical objects that can be in only one place at a time.
Ideas and information, however, resist taxonomies.
They form intricate *webs* that penetrate rigid boundaries.

[Trees](https://en.wikipedia.org/wiki/Tree_(abstract_data_type)) formalize hierarchies; they are among the most widely used structures in computer science.
Trees are intimately related to spaces as they are universal space organizers:
B-trees organize ordered key spaces in databases,
[k-d trees](https://en.wikipedia.org/wiki/K-d_tree) slice multi-dimensional spaces in graphics,
and abstract syntax trees organize linear token sequences in compilers.

⊕
Parsing is a space organization problem as it requires labeling token sequences with their syntactic roles.

![](/images/48-parsing.svg)

But with all their utility, trees can’t model webs directly.
Thus, *tree mapping* is a problem that requires embedding a web into a tree in a way that distorts the web structure.

Let’s look at a few examples.

### [File systems](#file-systems)

> The digital world thereby allows us to transcend the most fundamental rule of ordering the real world:
> Instead of everything having its place,
> it’s better if things can get assigned multiple places simultaneously.

David Weinberger, Everything Is Miscellaneous

Imagine receiving a bill from your dentist.
How do you file it?
In a common "archive" folder?
In a more specific "medical" folder?
In the "XXXX year taxes" project folder for future tax returns?
Or copy it and choose all the options at once?

The question might seem moot in the age of Dropbox and Google Drive.
Yet Victorian-era gentlemen might have pondered the same questions while sorting letters as we do while sorting virtual paper.
The user-facing design of our state-of-the-art distributed systems inherited most of the restrictions of the physical world.

Operating systems face the same dilemma:
should files be organized by the application they belong to or by type?
Windows and macOS traditionally preferred the former option, packaging applications into (mostly) self-contained bundles.
Most Linux systems embraced the latter approach,
so when you install a package,
its shreds lie all over the filesystem:
libraries go to `/usr/lib`, documentation — to `/usr/man`, configuration — to `/etc/`, and so forth.

This choice comes with a trade-off:
shredding packages simplifies tooling (`man` needs to look in only a handful of locations) and enables reuse, but complicates software management.
The pain of packaging and installing modern applications on Linux led to the development of macOS-inspired bundle formats,
such as [Snap](https://snapcraft.io/docs) and [Flatpak](https://flatpak.org/).

If you’ve ever tried to organize a non-trivial code repository,
you’ve likely run into the same issue.
Modern projects have components implemented in different languages, for example,
TypeScript on the frontend and Rust on the backend.
You can group files by the component they implement (`/acme/payments/index.ts` and `/acme/payments/main.rs`) or by language (`acme/ts/payments.ts` and `/acme/rs/payments.rs`).

⊕
Two common ways to organize a code repository:
by component (left) or by implementation language (right).

![](/images/48-repo-layouts.svg)

Slicing by component is easier for humans because it [reflects the organizational structure](https://en.wikipedia.org/wiki/Conway%27s_law),
but most tools don’t support this setup, forcing a technology-centric approach.
Google and a few other engineering organizations bit the bullet and organized their repositories by projects (`/search`, `/shopping`, `/maps`),
developing a plethora of language-agnostic build tools along the way
Google’s [Blaze](https://news.ycombinator.com/item?id=9257000) was among the first such tools.
It inspired [Pants](https://www.pantsbuild.org/), [Buck](https://buck.build/), and [Please](https://please.build/), and was later open-sourced as [Bazel](https://bazel.build/).
.

These dilemmas, however, are mostly self-inflicted.
There is no inherent reason for a digital file system to be a skeumorph of a shelf filled with folders.
Several projects experimented with web-like filesystems
([BeFS](https://en.wikipedia.org/wiki/Be_File_System) and [WinFS](https://en.wikipedia.org/wiki/WinFS), for example),
but none had a significant effect on the status quo.
However,
as tags and links enter the public consciousness through web services,
filesystems might follow the lead and evolve into webs over time.

### [Writing](#writing)

> the writer’s goal is to encode a web of ideas into a string of words using a tree of phrases.

Steven Pinker, The Sense of Style

Books are the epitome of hierarchy:
they have chapters that contain paragraphs with sentences composed of words made of letters,
all sliced into neat numbered pages.
Yet, the ideas we express on these pages are anything but linear or hierarchical.

Many stories appear linear:
the storyteller describes events in the order they occurred,
with chapter boundaries marking scene changes and time jumps.
But beneath every story lies a web of ideas.
Untangling this web into a sequence of words that recreates the web in another mind is the primordial struggle of every writer.

> Writing is easy. All you do is stare at a blank sheet of paper until drops of blood form on your forehead.

Gene Fowler

In fiction, the *web* involves relationships between characters and the emotional connections that the reader is meant to form with them.
Best fiction uses the limitations of the medium to its advantage, presenting events in an order that puzzles and engages the reader most.
Its ultimate goal is to deliver the joy of connecting the dots and assembling the complete web.

When the underlying web gets dense and abstract, however, the writer’s job becomes daunting, and so is the reader’s.
Math textbooks are a perfect example.
Math might seem like a Lego brick tower with simple concepts at the foundation and complexity gradually increasing toward the top.
Indeed, each coherent presentation of math starting with Euclid’s "[Elements](https://en.wikipedia.org/wiki/Euclid%27s_Elements)" follows this pattern.
Yet, the choice of foundational blocks is often arbitrary.
Mathematical concepts shift shape and gain nuance as you learn how they relate to everything else
I remember waking up a few months after finishing my [real analysis](https://en.wikipedia.org/wiki/Real_analysis) course
and realizing that I finally *understood* [limits](https://en.wikipedia.org/wiki/Limit_(mathematics)),
thanks to the [ordinary differential equations](https://en.wikipedia.org/wiki/Ordinary_differential_equation) course I was taking at the time.
Even my understanding of natural numbers seems to change with every textbook I read..
The selection of ideas and the order of their presentation shape the reader’s experience,
so no two math books have the same table of contents.

The next time you sit down to an empty design doc and don’t know where to start,
be kind to yourself.
You’re solving a hard problem.

### [Architecture](#architecture)

> The units of which an artificial city is made up are always organized to form a tree.

Christopher Alexander, [A City is not a Tree](https://www.patternlanguage.com/archive/cityisnotatree.html)

⊕
Panoramas of Levittown (left, public domain, source: [Wikipedia](https://commons.wikimedia.org/wiki/File:LevittownPA.jpg)) and Siena (right, copyright [Vyacheslav Argenberg](https://www.vascoplanet.com/) under [CC BY 4.0 license](https://creativecommons.org/licenses/by/4.0/deed.en)).![](/images/48-levittown-siena.webp)

In his 1965 essay, "[A City is not a Tree](https://www.patternlanguage.com/archive/cityisnotatree.html)",
architect and mathematician Christopher Alexander observed a distinction between designed and naturally grown cities,
classifying Levittown and Chandigarh as designed and Siena and Kyoto as naturally grown.
He argues that artificial cities feel stifled and lack a secret ingredient that gives natural cities a sense of life and comfort.

According to Christopher Alexander, the difference lies in the mathematical structure underpinning the city design.
Artificial cities are organized as trees:
they consist of isolated neighbourhoods, each with a housing complex, a school, and a shopping mall,
along with a few compartmentalized specialized areas, such as a cultural centre and an industrial zone.
Natural cities, on the other hand, have a [semilattice](https://en.wikipedia.org/wiki/Semilattice) structure,
which enables more fulfilling interactions to emerge.
In natural cities, the boundaries between aspects of life are blurred.
Work, leisure, and play coincide and interact.

The city design is a tree-mapping problem that demands embedding a semilattice of human relationships into a particular terrain.
No canonical mapping exists,
so it’s natural that Christopher Alexander couldn’t provide a universal blueprint for a natural city.

> You are no doubt wondering by now what a city looks like which is a semilattice, but not a tree.
> I must confess that I cannot yet show you plans or sketches.
> It is not enough merely to make a demonstration of overlap — the overlap must be the right overlap.

Christopher Alexander, [A City is not a Tree](https://www.patternlanguage.com/archive/cityisnotatree.html)

In other words, natural cities preserve deeper connections when they lay out the web of human lives within the hierarchy of quarters and buildings.
No algorithm can tell you what these connections are.

### [Biology](#biology)

[Biological taxonomy](https://en.wikipedia.org/wiki/Taxonomy_(biology)) is a field that classifies living organisms.
It started with the morphological taxonomy, which is based on easily observable traits, such as whether an animal has a spine or feeds its offspring milk.
This approach is error-prone because useful traits often [evolve independently](https://en.wikipedia.org/wiki/Convergent_evolution) in remote branches of the tree of life.

For example, [cephalopod eyes](https://en.wikipedia.org/wiki/Cephalopod_eye) are strikingly similar to those of vertebrates,
even though their common ancestor likely resembled a blind worm with a photoreceptive spot.
If [camera-type eyes](https://en.wikipedia.org/wiki/Eye#Spherical_lens_eye) defined a biological group,
its members would be a weird bunch.

History is full of actual misclassifications.
Fungi were classified as plants until they were given a separate kingdom in the mid-20th century.
Crocodiles and birds used to belong to sibling classes (*Reptilia* and *Aves*),
even though crocodiles are more closely related to birds than to other reptiles.

Morphological taxonomy is another case of tree-mapping because collections of traits form [concepts](https://en.wikipedia.org/wiki/Formal_concept_analysis),
and their inclusions form graphs that are more general than trees ([lattices](https://en.wikipedia.org/wiki/Lattice_(order))).
Jorge Luis Borges mocked such taxonomies in his essay, "[The Analytical Language of John Wilkins](https://www.crockford.com/wilkins.html)",
quoting a fictional ancient Chinese encyclopedia,
"The Celestial Emporium of Benevolent Knowledge":

> the animals are divided into:
> (a) belonging to the Emperor
> (b) embalmed
> (c) trained
> (d) piglets
> (e) sirens
> (f) fabulous
> (g) stray dogs
> (h) included in this classification
> (i) trembling like crazy
> (j) innumerables
> (k) drawn with a very fine camelhair brush
> (l) et cetera
> (m) just broke the vase
> (n) from a distance look like flies

Jorge Luis Borges, [The Analytical Language of John Wilkins](https://www.crockford.com/wilkins.html)

[Cladistics](https://en.wikipedia.org/wiki/Cladistics) is a modern system that classifies organisms based on their common ancestry and genetics.
Even though this mapping is imperfect due to [horizontal gene transfer](https://en.wikipedia.org/wiki/Horizontal_gene_transfer),
it’s more accurate and revealing than the traditional classification because it preserves existing connections rather than imposing artificial ones.

[Conclusion](#conclusion)
-------------------------

Now that you know about the problem,
you won’t have any trouble spotting it everywhere.
It lurks in database modeling challenges (I’m looking at you, MongoDB),
dooms object-oriented class hierarchies,
and underpins struggles with Rust’s borrow checker (object ownership graphs are trees, but object interactions are webs).
It’s responsible for the size of your `node_modules` directory and the layout of your cookbook.

The primary strategy for dealing with tree mapping is to be intentional.
We reach for hierarchies instinctively,
and we often don’t notice that we’re making a choice.
We must stop and ask:
What web is being flattened?
Which links are sacrifices?
And, most importantly, must the target medium be a tree in the first place?
