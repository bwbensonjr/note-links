---
id: 1413
url: https://antonfrolov.substack.com/p/i-hired-an-illustrator-to-draw-my
title: I hired an illustrator to draw my house. Now it's my Home Assistant dashboard.
domain: antonfrolov.substack.com
source_date: '2026-10-09'
tags:
- tutorial
- web-dev
summary: An illustrator-drawn floor plan of the author's house now serves as his Home
  Assistant dashboard, with animated devices like a flickering fireplace, glowing
  garden lights, and running air conditioners that the whole family enjoys using.
  The author describes how he briefed the artist with an architectural plan, reference
  photos, and a technical spec requesting layered, shared-canvas WebP and PNG files
  with day and night versions. He then explains how the Home Assistant picture-elements
  card uses state-based images, conditional day/night layers, and tap actions to bring
  the illustration to life.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-5-5
---

# I hired an illustrator to draw my house. Now it's my Home Assistant dashboard.

I hired an illustrator to draw my house. Now it's my Home Assistant dashboard.
==============================================================================

### A flickering fireplace, a softly lit garden, and a smart home the whole family finally enjoys.

[![Anton Frolov's avatar](https://substackcdn.com/image/fetch/$s_!bK-9!,w_36,h_36,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7b7fd87b-e35d-4d77-94aa-73c253f3d48a_1589x1589.jpeg)](https://substack.com/@antonfrolov)

[Anton Frolov](https://substack.com/@antonfrolov)

Oct 05, 2026

52

2

Share

[![](https://substackcdn.com/image/fetch/$s_!huqE!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fea228abe-574d-4d58-9922-775c987f1f7b_1920x1080.webp)](https://substackcdn.com/image/fetch/$s_!huqE!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fea228abe-574d-4d58-9922-775c987f1f7b_1920x1080.webp)

The fireplace flickers, the garden lights glow, and the air conditioner in the bedroom is quietly blowing — not only in my house, but in a hand-drawn picture of it. This is my Home Assistant dashboard, and for the first time, it’s one the whole family actually enjoys using.

For the last year I’ve been automating my home with Home Assistant, the open-source smart home platform. I tried to automate as much as possible, so things just work without anyone touching them. When everyone leaves, all the air conditioners switch off. The garden sprinkler calculates its run time from the weather: longer on hot days, skipped entirely when it rains.

Thanks for reading! Subscribe for free to receive new posts and support my work.

But some things still need a human. The garden lights are the best example. They can only be turned on from an app, either the manufacturer’s or Home Assistant’s. And I made it worse myself: a timer in Home Assistant turns garden lights off automatically after a while. When it’s about to run out, the lights start blinking, giving you time to open the app and extend it while they’re still on. The problem? Nobody else in the household wanted to use the Home Assistant app, or the dashboard I had at the time.

[![](https://substackcdn.com/image/fetch/$s_!Cytd!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7604122e-686c-4135-82cf-be4166c4c45d_2958x1672.png)](https://substackcdn.com/image/fetch/$s_!Cytd!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7604122e-686c-4135-82cf-be4166c4c45d_2958x1672.png)

Original dashboard

I could have installed a physical switch, but that wouldn’t solve the timer. And some devices are simply easier to control from an app. Try starting the sprinkler with the button on the unit itself, then running out of the garden before you get soaked.

So I thought: why not build a dashboard so cool that everyone would *want* to use it?

I looked through a lot of dashboards and fell for the idea of a floor plan: an interactive map of the house that mirrors the real one. Most of the ones I found were 3D, built either with Home Assistant custom cards or in third-party modelling software, and I found one article about a [pixel-art floor plan](https://strawberrysec.net/homelab/Home-Assistant-Pixel-Floorplan/).

[![](https://substackcdn.com/image/fetch/$s_!ziZE!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9b056f5c-ea21-4c0f-90eb-31895c662a0a_1800x1240.png)](https://substackcdn.com/image/fetch/$s_!ziZE!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9b056f5c-ea21-4c0f-90eb-31895c662a0a_1800x1240.png)

3D and pixel-art floor plan styles (illustrations generated for this article)

The 3D plans didn’t quite click for me. In most of the ones I saw, the model itself was a static picture, and everything interactive was a layer of icons on top of it.[1](#footnote-1) The pixel-art approach was charming, but it meant either drawing everything yourself or placing library sprites one by one in a graphical editor.

### Finding an artist

I liked the pixel-art idea enough to go looking for an artist, and soon realised that finding and booking a good one is harder than it sounds. Artists specialise, and each has a style of their own. Popular artists are easier to find, but likely they are already booked for months in advance and even if they are free, artwork itself is going to take anything from few weeks to few months. On top of that, a dashboard is an unusual commission: the artist has to understand what it is and what it needs technically, not just paint a nice picture.

Luckily, I was recommended an amazing environment artist whose portfolio was already full of beautifully illustrated spaces. I loved their style, and after a few messages back and forth I was sure we were on the same page about the end goal. The pixel-art idea died a natural death: I’d found someone whose style appealed to me even more, and who already knew how to draw a room.

To get us started, I put together a package for the artist:

* **A simple architectural plan** of the house. It had no furniture on it, so I marked that in myself.
* **Photos of the rooms**, as a reference for what’s really there.
* **Illustrations I found online**, as references for style and colour.
* **Examples of other dashboards**, so the artist could see what the end result was for.
* **A short technical spec**: the requirements, which files and formats I needed back, and a note on each of the resources above explaining what it was for.
* **Paint colour codes** from our last renovation. Nice to have rather than essential, since colours can be matched from the photos.

I want to say a bit more about the technical part of the brief, because the rest of the article builds on it. Ask for PNGs with transparency (WebP for animations), a day and a night version of every floor, and every device on its own layer: a still image for “off” and a short loop of frames for “on” (eight was plenty), in both day and night lighting. Most importantly, every file should be exported on one shared canvas of the same size, with each piece sitting exactly where it belongs in the house rather than cropped to itself. That one rule saves days of lining things up later, which I learned the hard way.

A couple of notes from my own build. For the garden I ended up with three versions: day, night, and night with the lights on. And I originally asked for the animations as PNG sprite sheets, but ended up converting the frames to animated WebP myself, so you might as well ask the artist for WebP from the start.

Finding an artist, working out what the dashboard needed and preparing all the documentation was probably the bulk of the work on this project. That makes total sense, because the artwork is the project! When the dashboard is an illustration, with states shown as animations and the UI reduced to a few icons and sensor readings, there simply isn’t much left to design or code.

### How it works

Once the illustration is ready, it’s time to put it to work. Fortunately, Home Assistant makes this fairly easy: under the hood, it’s one stock card and a couple of tricks.

The card is `picture-elements`. The illustration is its background (`image:`), and everything that changes, the devices and the status readouts, is placed on top of it as `elements:`, each at its own position. Of the [element types](https://www.home-assistant.io/dashboards/picture-elements/#elements) it supports, I mostly used `image` for the devices, `icon` and `state-label` for the status readouts, and `conditional` to show or hide elements depending on state.

The first trick is how a device comes alive. An `image` element can change its picture with the device’s state (`state_image`): while the AC is off it shows a still frame, and when it’s on, the animated WebP. The browser simply plays the animation, so no custom code is involved.

```
type: picture-elements
image: /local/floorplan/ground/ground_day.webp
elements: 
    - type: conditional
      conditions:
        - entity: input_boolean.dashboard_night
          state: 'on'
      elements:
        - type: image
          image: /local/floorplan/ground/ground_night.webp
    - type: conditional
      conditions:
        - entity: input_boolean.dashboard_night
          state: 'off'
      elements:
        - type: image
          entity: climate.main_room_ac
          image: /local/floorplan/ground/ac_living_off.webp
          state_image:
            cool: /local/floorplan/ground/ac_living_on.webp
            heat: /local/floorplan/ground/ac_living_on.webp
            heat_cool: /local/floorplan/ground/ac_living_on.webp
            auto: /local/floorplan/ground/ac_living_on.webp
            dry: /local/floorplan/ground/ac_living_on.webp
            fan_only: /local/floorplan/ground/ac_living_on.webp
          tap_action:
            action: more-info
```

The second trick is day and night. I created a helper to switch between day and night modes, and an automation that flips it at sunset and sunrise. It's easy to set up, and being able to flip it by hand is very useful while testing. The night illustration is laid on top of the day one as a `conditional` element, and each device gets a day and a night version the same way.

[![](https://substackcdn.com/image/fetch/$s_!bvPz!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe58fc895-2ce5-4eb3-8ba6-f99fbbe88211_1920x1080.webp)](https://substackcdn.com/image/fetch/$s_!bvPz!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe58fc895-2ce5-4eb3-8ba6-f99fbbe88211_1920x1080.webp)

Tapping an interactive device like the AC opens Home Assistant's own control dialog for it (`tap_action` set to `more-info`). That was the simplest option, since there was no dialog to design. The only exception is the garden irrigation. It's a single icon on the dashboard, but behind it are several independent valves and timers that together make up the smart irrigator. There's no single screen for all of that, so there's no default dialog to open. I built one with [Browser Mod](https://github.com/thomasloven/hass-browser_mod), a custom integration installed from HACS that, among other things, lets you open your own pop-up dialogs on a Home Assistant page.

The `image` property reference your images with URL or local path, so you need to host them somewhere, I decided to place them on Home Assistant box itself and serve from there. To do that you need to create folder `/config/www` if it doesn’t exist yet and reboot Home Assistant. Then place your files in `/config/www` so `/local/floorplan/ground/ac_living_off.webp` becomes `/config/www/floorplan/ground/ac_living_off.webp` .

I wanted the dashboard on the TV from the start, so it had to run in the TV’s own browser. Early on I read that the browser on LG’s webOS didn’t support WebP, which would have sunk the whole animation approach. It turned out not to be true. The claim most likely comes from the TV’s built-in photo viewer, not its browser, and a single test image was enough to prove it. If you read the same thing about your TV, try it before you believe it.

The real problem was elsewhere. webOS wouldn’t let me set a web page as the screensaver, or make the browser open a specific page by default, so getting to the dashboard would always take a few clicks with the remote. That’s exactly the kind of friction I was trying to remove. In the end I went around the TV’s software altogether. The Home Assistant box sits next to the TV anyway, so I installed the [HAOS Kiosk Display](https://github.com/puterboy/HAOS-kiosk/) add-on and plugged it into one of the TV’s HDMI inputs. Now the dashboard is just another input on the TV, always open and always on the right page.

### One screen for the whole house

On the TV I wanted to see everything at once: both floors and the garden on a single screen. But each floor also deserved a view of its own, for when you only care about one. So I built a separate view for every floor and the garden, and then a “Full” view that brings them all together.

This is where the shared canvas from the brief paid off. Each view is cut out of the same master canvas, so all I had to remember was where each piece came from. To build the full view, every floor goes back to its original position, and they line up by themselves, like layers in an image editor. Two details made it look right: the garden sits underneath the house rather than on top of it, and the first floor is lifted slightly above the ground floor, so the house looks a little “exploded” and you can see into both levels.

[![](https://substackcdn.com/image/fetch/$s_!FM8h!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2995ce1b-d168-4616-90f2-5eb25bbede14_1920x1080.webp)](https://substackcdn.com/image/fetch/$s_!FM8h!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2995ce1b-d168-4616-90f2-5eb25bbede14_1920x1080.webp)

The harder part was reusing the floors themselves. I didn’t want to configure every device twice, once for its floor and once for the full view, but the Home Assistant UI editor has no way to share elements between cards. So I switched the dashboard to YAML mode. The configuration lives in files, and each floor’s elements sit in their own file, which both the floor view and the full view include. A room is edited once and changes everywhere. A nice bonus: after one restart to register the dashboard, editing those files only needs a browser refresh. The price is losing the visual editor, which wasn’t a big deal since most of work of each floor was already over by that time.

One more limitation: a `picture-elements` card can’t contain other cards. So the full view stacks the floor cards on top of each other with `vertical-stack` and positions them with card-mod, a popular HACS plugin that lets you style cards with CSS.

### Putting it all together

With the full view ready, the files uploaded and the kiosk set up, it was finally time to try it out. In my case, that meant turning on the TV and switching to the right input. I still remember everyone’s excitement seeing it for the first time: comparing the illustration with the real rooms, and switching devices on and off to see which ones the picture would react to.

These days the dashboard runs for a few hours in the morning and in the evening. Fortunately, my TV can be controlled from Home Assistant, so a schedule switches it to the dashboard during those hours, as long as nobody is watching anything. I also added [Kiosk Mode](https://github.com/NemesisRE/kiosk-mode) from HACS to get rid of Home Assistant menu on TV, making it pure dashboard experience.

The one disappointment is that the TV remote can’t control the dashboard over HDMI, so on the TV it’s for looking, not touching. Funnily enough, that worked in my favour. Remember how this all started, with nobody in the family wanting to use the Home Assistant app? Once the dashboard was on the TV, they installed the app on their phones or bookmarked the dashboard on their computers, so they could actually tap things. The individual floor views work well on a phone, while the full view needs at least a laptop-sized screen.

For now, I’m happy with the arrangement: the whole house at a glance on the TV, and the app for when I need to change something.

*Dashboard illustrations by [Owen Yeconiel](https://linktr.ee/owenyeconiel).*

Thanks for reading! Subscribe if you want to see more detailed articles on creating Home Assistant dashboard.

[1](#footnote-anchor-1)

That was the state of guides and articles when I was researching this, in May 2026. Even then, people were posting impressive dashboards on Reddit, and there is now far more written about building 3D and 3D-style dashboards, including handing most of the work to AI tools.

52

2

Share
