---
id: 866
url: https://unsung.aresluna.org/unsung-heroes-flickrs-urls-scheme/
title: 'Unsung heroes: Flickr’s URLs scheme – Unsung'
domain: unsung.aresluna.org
source_date: '2026-02-24'
tags:
- web-dev
- tutorial
summary: Flickr's URL design in the late 2000s was remarkably user-friendly and elegant,
  featuring clean, readable paths without redundant parameters or cryptic syntax that
  made URLs easily editable, shareable, and predictable. This thoughtful approach
  taught valuable lessons about URL structure as a user interface element, allowing
  users to navigate efficiently through keyboards, guess URLs intuitively, and modify
  links on the fly without verification. The article celebrates this often-overlooked
  design choice as an inspiration for good URL design practices that remain relevant
  today.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# Unsung heroes: Flickr’s URLs scheme – Unsung

Half of my education in URLs as user interface came from Flickr in the late 2000s. Its URLs looked like this:

`flickr.com/photos/mwichary/favorites`  
`flickr.com/photos/mwichary/sets`  
`flickr.com/photos/mwichary/sets/72177720330077904`  
`flickr.com/photos/mwichary/54896695834`  
`flickr.com/photos/mwichary/54896695834/in/set-72177720330077904`

This was incredible and a breath of fresh air. No redundant `www.` in front or awkward `.php` at the end. No parameters with their unpleasant `?&=` syntax. No `%` signs partying with hex codes. When you shared these URLs with others, you didn’t have to retouch or delete anything. When Chrome’s address bar started autocompleting them, you knew exactly where you were going.

This might seem silly. The *user interface* *of URLs*? Who types in or edits URLs by hand? But keyboards are still the most efficient entry device. If a place you’re going is where you’ve already been, typing a few letters might get you there much faster than waiting for pages to load, clicking, and so on. It might get you there even faster than sifting through bookmarks. Or, if where you’re going is up in hierarchy, well-designed URL will allow you to drag to select and then backspace a few things from the end.

Flickr allowed to do all that, and all without a touch of a Shift key, too.

Any URL being easily editable required for it to be easily *readable*, too. Flickr’s were. The link names were so simple that seeing the menu…

![](_media/unsung-heroes-flickrs-urls-scheme/1.1088w.avif)

…told you exactly what the URLs for each item were.

In the years since, the rich text dreams didn’t materialize. We’ve continued to see and use naked URLs everywhere. And this is where we get to one other benefit of Flickr URLs: they were short. They could be placed in an email or in Markdown. Scratch that, they could be placed in a *sentence.* And they would never get truncated today on Slack with that frustrating middle ellipsis (which occasionally leads to someone copying the shortened and now-malformed URL and sharing it further!).

It was a beautiful and predictable scheme. Once you knew how it worked, you could *guess* other URLs. If I were typing an email or authoring a blog post and I happened to have a link to your photo in Flickr, I could also easily include a link to your Flickr homepage just by editing the URL, without having to jump back to the browser to verify.

Flickr is still around and most of the URLs above will work. In 2026, I can think of a few improvements. I would get rid of `/photos`, since Flickr is already about photos. I would also try to add a human-readable slug at the end, because…  
`flickr.com/mwichary/sets/72177720330077904-alishan-forest-railway`  
…feels easier to recall than…  
`flickr.com/photos/mwichary/sets/72177720330077904`

(Alternatively, I would consider getting rid of numerical ids altogether and relying on name alone. Internet Archive does it at e.g. `archive.org/details/leroy-lettering-sets`, but that has some serious limitations that are not hard to imagine.)

But this is the benefit of hindsight and the benefit of things I learned since. And I started learning and caring right here, with Flickr, in 2007. Back then, by default, URLs would look like this:

`www.flickr.com/Photos.aspx?photo_id=54896695834&user_id=mwichary&type=gallery`

Flickr’s didn’t, because someone gave a damn. The fact they did was inspiring; most of the URLs in things I created since owe something to that person. (Please let me know who that was, if you know! My grapevine says it’s [Cal Henderson](https://en.wikipedia.org/wiki/Cal_Henderson), but I would love a confirmation.)

Feb 15, 2026

* [popular 12](tags/popular/)* [unsung heroes 1](tags/unsung-heroes/)* [web 16](tags/web/)
