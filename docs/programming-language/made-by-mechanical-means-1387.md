---
id: 1387
url: https://felixrieseberg.com/made-by-mechanical-means/
title: Made by mechanical means
domain: felixrieseberg.com
source_date: '2026-09-28'
tags:
- python
- ai
- llm
- web-dev
summary: Felix Rieseberg redesigned his homepage using Claude AI to program a Blender
  3D model, creating an interactive 90s-themed room with VHS tape portfolio items
  entirely through cloud-based AI without running local code. The project involved
  60 parallel Claude threads working through iterative brainstorming and creative
  refinement, with Claude autonomously writing ~3,000 lines of Python code to generate
  detailed 3D models, procedural textures, and complex lighting systems. This workflow
  demonstrates a shift toward more creative, goal-oriented collaboration with AI rather
  than traditional hands-on coding and development.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# Made by mechanical means

![Made by mechanical means](https://storage.ghost.io/c/89/e0/89e08557-681a-40be-8264-278bf46d6b25/content/images/size/w2000/2026/09/Screenshot-2026-09-27-at-12.43.24---PM.png)

One notable difference between working on Claude and the other productivity tools I've touched is that feature requests are surprisingly not the #1 discussion topic. Instead, people want to know how I'm using Claude, how they should be using Claude, and whether there are any cool magic spells I can share.

In this post, I'd like to walk you through the process of redesigning my homepage without touching or running code or even using traditional Claude Code. No PRs were made, nor did I open GitHub. If you haven't seen the full end result, maybe [check it out first](https://www.felixrieseberg.com/?ref=felixrieseberg.com).

[![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)](https://storage.ghost.io/c/89/e0/89e08557-681a-40be-8264-278bf46d6b25/content/media/2026/09/making-of-supercut.mp4)

0:00

/1:31

1×

The redesign in 90 seconds

Roughly 60 threads worked, often in parallel, on my increasingly outrageous requests, which included creating a CGI parody of a Werner Herzog documentary in Blender and synthesizing soundtracks from scratch. Despite the complexity, a considerable amount of that orchestration happened on my phone rather than my computer - in fact, I didn't have to run any code locally. Claude worked entirely in the cloud.

I'm writing this in late September 2026, and I suspect my workflow will look very different in six months. Even compared with the beginning of the year, I'm noticing a stark difference - my work is now a lot more creative, less bounded by the technologies I've mastered, and so much more visual and emotional. I've used Opus 5.5 for all the work.

I started by creating a new Claude Project. [Projects are becoming a layer that spans Chat, Cowork, and Code](https://support.claude.com/en/articles/9517075-what-are-projects?ref=felixrieseberg.com); you can think of them as sitting above domain-specific concepts. You talk to one Claude with the ability to spin off additional sessions, share files and memory between them, and supervise the entire fleet of Claudes to achieve goals.

Earlier this year, I would have joked that I get a lot done by telling a bunch of Claudes to do work. Now, I've put one Claude in charge of each of my projects, and in turn, that Claude knows how to manage tasks, investigations, and threads. We're talking more about goals and less about how to achieve them.

![](https://storage.ghost.io/c/89/e0/89e08557-681a-40be-8264-278bf46d6b25/content/images/2026/09/image.png)

My little Project setup.

Every thread gets its own computer in the cloud, where it installs whatever it needs (Blender, FFmpeg, Playwright), checks its work with screenshots from a headless browser, and publishes a private preview page for me to click through. All threads share one folder of files and one memory. Claude is smart enough to write down decisions I made in memory and makes sure newly started threads follow them without me having to repeat myself.

Brainstorming a new direction
=============================

I started the way I'd start with a design team: by dumping a bunch of inspiration on the table. Those included 90s rave posters, movies I liked, ads that spoke to me, photos I keep coming back to, even just concepts I like.

Ten threads explored those directions in parallel with very little guidance. One came up with portfolio directions for somebody who really likes camping in national parks; another imagined what an 80s *Ghost in the Shell* website would look like. Both, it turned out, felt a little overdone to me. I wanted to make something new, not just clone something already out there.

Whenever I liked a direction, I asked Claude to double down, get creative, and give me five more variations of the same direction.

![](https://storage.ghost.io/c/89/e0/89e08557-681a-40be-8264-278bf46d6b25/content/images/2026/09/01-brainstorm-sites.jpg)

**Twenty of the 25 brainstorm sites. Top left: the VHS direction that became the room.**

While most directions used HTML, Three.js, and other libraries to achieve some of my hopes and dreams, I pretty quickly found myself pushing Claude to use Blender. Claude doesn't click around Blender's interface, instead writing code and using Blender as a Python module. When I briefly considered turning my website into a cozy campsite, Claude promptly modeled one.

![](https://storage.ghost.io/c/89/e0/89e08557-681a-40be-8264-278bf46d6b25/content/images/2026/09/02-first-blender-models.jpg)

Some of Claude's first Blender models for an abandoned idea (a cozy camp fire)

Given the direction of vintage technology I liked (Game Boys, record players, Walkmans, etc) and the task of coming up with a creative portfolio gallery, Claude eventually suggested VHS tapes.

![](https://storage.ghost.io/c/89/e0/89e08557-681a-40be-8264-278bf46d6b25/content/images/2026/09/ontape.jpg)

Claude's prototype for a portfolio where every gallery item is a VHS tape

Together, we combined Claude's idea (VHS tapes) with my own vision for the website, which included an interactive version of the kind of room a 90s German movie would give a journalist.

![](https://storage.ghost.io/c/89/e0/89e08557-681a-40be-8264-278bf46d6b25/content/images/2026/09/03-vhs-second-version.jpg)

**The VHS direction's second version**

Claude's second draft, including my directions about the room setup and encouragement to use Blender creatively, was *shockingly* good. The version I shipped took roughly 60 iterations, but the second draft, which arrived 39 minutes after my first brief, is already recognizably the room you see today.

Early on, Claude decided that the code should be modular, allowing threads to work on elements of the room in parallel. As an example, each tape is its own file that paints onto a 2D canvas.

```
export default {
  id: "notion",
  title: "Notion",
  years: "2023–2025",
  mount({ canvas, ctx, width, height, audio }) {
    return {
      frame(t, dt) { /* draw one frame */ },
      input(event) { /* play, stop, next, prev, click */ },
      stop() { /* clean up */ },
    };
  },
};
```

After every iteration step, Claude published a new version of an artifact, a private web page where I could see the current version, both on my computer and my phone. I constantly asked for a few options, clicked through them, sent back some critique, and went on with my day. Doing that from my phone felt particularly powerful. I would be on my bike, have some ideas while riding, quickly fire off some ideas to Claude, and check out the results on the next coffee stop.

Building the room
=================

Let's talk about the room, which is probably where I pushed Claude to be most ambitious. One of the most beautiful parts of LLM tools is that they allow me to do things I wouldn't have been able to do before - I have no idea how to use Blender. I describe the things that I want, Claude writes the geometry as code, renders a still, and I give feedback.

The room is now ~3,000 lines of Python code, controlling Blender as a library. Some of those scripts are:

* `tape_model.py` (332 lines): one VHS cassette, 187 × 103 × 25 mm, as a hollow shell with reels, tape ribbon, guides, and a hinged dust door.
* `gear90s.py` (659 lines): a 90s journalist's desk. A phone with a microcassette answering machine standing on a phone book, a Rolodex, floppies, a pager, a solar calculator, a Discman, and a Walkman, with cords running behind the desk to a wall socket.
* `retro_pc.py` (431 lines): a late-80s beige PC clone from a made-up brand, with two 5.25" drives, a key lock, a red paddle switch, a 14" green CRT on a tilt-and-swivel foot, and an XT-style keyboard.
* `room_back.py` (290 lines): the half of the room behind the camera, which you only see in reflections and in free-look: a four-panel door with a key in the lock and light under it, a Bakelite light switch, a stucco cornice, and a tiled stove.

Claude decided on its own when to scour the Internet for freely licensed models and when to model props from scratch. Some furniture came from Poly Haven (CC0-licensed), but most items are "made by Claude" - like the desk, the TV & VCR, Discman, Walkman, the entire old PC, or the entire room geometry. The surface textures are code, too: Claude's wood, plaster, plastic, and metal are procedural noise, not photographs.

![](https://storage.ghost.io/c/89/e0/89e08557-681a-40be-8264-278bf46d6b25/content/images/2026/09/06-home-view-in-clay.jpg)

**The home view in Blender.**

I kept pushing for a photorealistic look, which soon had us talking about light maps. Real-time lighting in a browser can't do the soft bounce light I wanted, so Claude decided to use Cycles, Blender's path tracer, and bake the light into textures. It's a surprisingly involved process: Every static surface gets a second UV set packed into atlases, and each atlas gets up to four maps: its color without light, the light from the room's own lamps (desk lamp, city glow, moon), the light from the TV alone, glowing plain white, and the room with the desk lamp switched off. The shader tints the TV's light with whatever the tape shows, so a blue tape turns the room blue:

```
vec3 lamps = pow(texture2D(irrA, uv).rgb, vec3(3.0)) * sA;  // desk lamp, city, moon
vec3 tv    = pow(texture2D(irrB, uv).rgb, vec3(3.0)) * sB;  // the TV alone, baked white
vec3 light = lamps + tv * tvColor;
```

Things that move (tapes, knobs, the VCR's door, LEDs, the screens) aren't baked. They're lit live.

![](https://storage.ghost.io/c/89/e0/89e08557-681a-40be-8264-278bf46d6b25/content/images/2026/09/07-home-view-path-traced.jpg)

**The home view path-traced in Cycles with the TV off: All visible light here is pre-rendered.**

![](https://storage.ghost.io/c/89/e0/89e08557-681a-40be-8264-278bf46d6b25/content/images/2026/09/08-baked-light-maps.jpg)

**Three of the texture atlases, each as color and three light maps: the lamps, the TV alone, and the desk lamp off.**

Not to toot Claude's horn here too much - but it's insane to me that all of this can simply happen in code.

For what it's worth, while it's pretty cool to see Claude work in the cloud while I'm riding my bike around, intense 3D work really benefits from dedicated GPUs. You can attach your own computer in any thread by hitting the little "+" icon and selecting `Work Locally`, which allows Claude to use your computer for speedier rendering.

The view outside
----------------

I had very specific ideas about what the "outside" should look like: photorealistic, alive, without eating too many CPU/GPU cycles on visitors' machines. You'll be unsurprised to hear that once again I didn't really have to know what'd work best; we simply built every single option.

The first placeholder was a photo ("Berlin Skyline" by Billie Grace Ward; CC BY 2.0). I thought I'd be clever and generate an entire skyline in Blender. It looked pretty good, just not quite as good as the photo, so I abandoned that direction.

![](https://storage.ghost.io/c/89/e0/89e08557-681a-40be-8264-278bf46d6b25/content/images/2026/09/09-window-directions.jpg)

**The window directions: the photo that shipped, a street drawn in code, rooftops generated from a seed, and a Blender street baked like the room, with its video store and lounge up close.**

Claude had a better idea: We used [Depth Anything V2](https://github.com/DepthAnything/Depth-Anything-V2?ref=felixrieseberg.com), an open depth-estimation model, and turned the photo into a 50 KB depth map with two channels: a soft one, so masts, signals, and near buildings slide against the skyline when the camera drifts, and a sharp one, so trains can disappear behind buildings.

That gave us the best of both worlds - the visible photo but also depth to enable animated lights and trains. They're all drawn by the GPU on top of the photo, at almost no CPU cost:

![](https://storage.ghost.io/c/89/e0/89e08557-681a-40be-8264-278bf46d6b25/content/images/2026/09/10-window-depth-maps.jpg)

**The photo and the two depth maps: soft for parallax, sharp to hide trains**

Creating the nihilistic penguin
===============================

Let's talk about my favorite part of the entire project: creating a parody of the "[nihilistic penguin](https://www.youtube.com/watch?v=O_XehlRTz_U&ref=felixrieseberg.com)", a scene from Werner Herzog's *Encounters at the End of the World*: one penguin leaves the colony and walks inland, toward the mountains, alone.

Claude and I started simple, with a childlike animation drawn entirely in SVGs. It allowed us to discuss exactly what kind of parody I wanted.

![](https://storage.ghost.io/c/89/e0/89e08557-681a-40be-8264-278bf46d6b25/content/images/2026/09/11-penguin-first-version.jpg)

**The first version, drawn in code.**

Once we had a pretty good idea of what I wanted, I asked Claude to create a CGI version that would first mimic the original closely, so that we could add my changes later. I'm told that Claude did what a VFX artist would do:

* It broke the scene down into eight shots, cut on the original's shot boundaries.
* It tracked the camera frame by frame and tried to match every pan, zoom, and wobble of the handheld camera.
* It built (surprise, surprise) the world using code in Blender, once again using the "Blender via Python" approach. This includes everything you see - snow, mountains, gravel, penguins.

It rendered 2,787 individual 640×480 frames at 23.976 fps, which resulted in a 116-second long video.

![](https://storage.ghost.io/c/89/e0/89e08557-681a-40be-8264-278bf46d6b25/content/images/2026/09/home-film-where-it-stands.jpg)

Claude's comparisons of original (left) and the CGI reproduction (right)

Any good parody thrives on being pretty close to the original with a few small details changed: a desk with a computer on the ice, a row of corporate flags across the lonely penguin's way (one for each place I've worked), or a silly reference to the fact that I have a blog that gets a new post like once a year.

![](https://storage.ghost.io/c/89/e0/89e08557-681a-40be-8264-278bf46d6b25/content/images/2026/09/13-penguin-additions.jpg)

Oh look, the penguin is turning into an engineer

While Claude was overall excellent at sound design, it initially tried some free open-source models to generate a voice over. It worked but was a little lackluster in terms of quality, so I signed up for an ElevenLabs Starter account and simply gave Claude the API key.

Synthesizing music
==================

Oh, also, did I mention that Claude composed and synthesized three soundtracks on the website from scratch? It used (again, surprise!) Python. It first wrote a score, then a synthesizer engine. I have *no idea* how to make music. I asked Claude about its approach: "Deep Field is six four-bar chords in C# minor (C#m(add9), Amaj7(#11), F#m9, F#m(add9)/G#, C#m(add9), B) over a C# drone at 34.6 Hz. Late Shift is a 32-bar AABA song form." I have *no idea* what any of that means but I was able to give Claude Rick Rubin-style feedback in the form of "I like this" or "No, make it... less excited".

Not reading the code
====================

I think a lot of engineers are experiencing a crisis of faith: If I've got dozens of Claude threads buzzing away at the same time, there's no way I'm reading all that code. Which is true: I'm not reading the code. I suspect that this is easier to understand for people who've worked both as an engineer and as an engineering manager - as a manager, you have to find ways to establish quality without reviewing every single change your people make. Entire books have been written about how exactly you do that without micromanagement, but I apply roughly the same mechanisms. Two classic examples are demanding rigorous processes and measurements, or tasking individual agents with breaking things (aka adversarial agents who consider their success to prove that the code is bad).

Multiple QA threads drove the site round after round in a headless browser and wrote about 3,000 lines of findings to the shared folder. The coordinating Claude quickly figured out which other thread was at fault and passed the finding on. The multi-Claude world is, as it turns out, not blameless. The adversarial agents found cassettes with blank labels, leftover German, links that stayed clickable behind cards, and a race when you switch tapes quickly. A single Claude thread doesn't write perfect code, a fleet of Claudes holding each other accountable meet my bar.

![](https://storage.ghost.io/c/89/e0/89e08557-681a-40be-8264-278bf46d6b25/content/images/2026/09/14-debug-view.jpg)

**The debug view during a QA run on an older version of the room.**

Hill climbing performance
-------------------------

Models are *very* good at hillclimbing. Tasking threads with specific targets, like frame rate, draw calls, or shadow draws, gets you very far.

You'd think that models have a hard time telling whether two versions of a scene look roughly the same. Claude came up with a clever solution - it took comparative screenshots and actually calculated the pixel-by-pixel difference. If you do that from multiple angles, you get a fairly foolproof method of ensuring that the performance gains are real gains and not just quality degradations.

![](https://storage.ghost.io/c/89/e0/89e08557-681a-40be-8264-278bf46d6b25/content/images/2026/09/15-perf-before-after.jpg)

Claude calculating the visual difference between two versions.

Some closing thoughts
=====================

I want to be sensitive to those who might be reading this post with an ache in their heart, feeling like it's outrageous that somebody who never went through the pain of learning the theory or practice of 3D modeling suddenly claims they're building 3D things. I'm sure you could find single elements that are low quality and call them slop, pointing out differences between the thing I worked on for 24 hours and a room designed painstakingly by hand over weeks.

I've certainly heard similar feelings from engineers, both when Electron made desktop app development easier and obviously during the rise of AI-assisted coding. I'm probably a fairly median engineer, but I *am* a professional one - I've worked on plenty of things that made it to many users. In 2026, I wouldn't have considered rebuilding my website without AI, but it's funny that I didn't even reach for Claude Code as a dedicated "for coding" tool. I just used Claude. Opus 5.5 and the generic harness didn't need to be told that we're "coding" here.

The San Francisco Museum of Modern Art just had a wonderful Matisse exhibit that included a restaging of the famous 1905 Paris Salon d'Automne, where a critic dismissed Matisse and his friends as "wild beasts." It reminded me of all the "photography?!?!?" drama 50 years earlier, also around one of the Paris Salons: The French poet Charles Baudelaire [had the spiciest takes on photography](https://www.metmuseum.org/art/collection/search/270956?ref=felixrieseberg.com), which entered the Paris Salon for the first time in 1859. Considering photos as art was, in his eyes, obviously a symptom of artistic decline. Counting a mechanical process as creative was not just wrong! A threat to French taste! Photography is "the refuge of every would-be painter, every painter too ill-endowed or too lazy to complete his studies".

Maybe I am too ill-endowed in skill or too lazy to redesign my entire homepage from scratch. And yet, here I sit, being pretty proud of my new homepage, made entirely through mechanical means. I'm not French, and I'm not sure I have more taste than anyone else - but it's exactly the way I saw it in my head, a mere 48 hours ago, and I'm pretty excited to show it to my friends.
