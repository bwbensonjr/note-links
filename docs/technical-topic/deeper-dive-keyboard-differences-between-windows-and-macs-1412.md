---
id: 1412
url: https://unsung.aresluna.org/deeper-dive-keyboard-differences-between-windows-and-macs/
title: 'Deeper dive: Keyboard differences between Windows and Macs – Unsung'
domain: unsung.aresluna.org
source_date: '2026-10-09'
tags:
- web-dev
- tutorial
summary: This article is a reference guide to the many differences in keyboard handling
  between Windows and Macs, which matter especially for web apps that must support
  both platforms. It covers differing key names (Backspace vs. Delete, Enter vs. Return),
  modifier keys (Control vs. Command, plus Mac's extra Control and Option keys), symbol
  versus word legends, shortcut notation, function key usage, and special character
  input via Option or AltGr. The key takeaway is that developers and users should
  be careful with assumptions about keys and shortcuts, since platform conventions
  and even character assignments can vary.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-5-5
---

# Deeper dive: Keyboard differences between Windows and Macs – Unsung

Over the years, I learned about many gotchas and strange differences between keyboard handling on Mac and Windows – pertinent especially to web apps, which use the same codebase to cater to both. I thought it might be helpful to someone if I compile them all in one place.

This post is meant to be a reference, and there aren’t any cute or riveting stories hiding inside – if this seems boring to you, feel free to skip to the next one!

##### Different names for keys

What Windows calls Backspace, Mac calls Delete. What Windows calls Delete, Macs call Forward Delete. (This means saying “Delete” without specifying the platform might actually be confusing.)

What Windows calls ⏎ Enter, Mac calls ⏎ Return. However, Macs also have an ⌤ Enter, although only on a numeric keypad (previously, it was even there [on laptops](https://en.wikipedia.org/wiki/PowerBook_G3#/media/File:Apple_PowerBook_G3_500_Pismo-2763.jpg)!). On keyboards without the physical Enter key, you can simulate it via Fn+Return.

In most Mac software, Enter and Return do the same thing. There are a few exceptions – for example, Photoshop adds a new line on Return but commits on Enter, and some classic pro apps like Cubase or Pro Tools do different things, too – but it seems to be a dying tradition. (If you are curious about the history of Return and Enter, [I wrote about it once](https://aresluna.org/the-day-return-became-enter/).)

Windows customarily calls the secondary key Numpad Enter. I don’t believe Fn+Enter works to simulate it.

Generally, third-party keyboards use Windows verbiage – so, Backspace and Enter. If a keyboard offers Mac conventions at all, they usually only extend to modifier keys.

##### Modifier keys

⌃ Control on Windows is the equivalent to ⌘ Command on a Mac. (Paste, for example, is ⌃V on Windows and ⌘V on a Mac.) But, confusingly, Apple devices still have a Control key, too. This was originally meant for terminal applications, but these days many GUI apps use it as an extra modifier key of much lesser significance than Control on Windows.

This means that for apps, Windows devices offer Ctrl, Alt, and Shift – and Macs offer ⌘ Command, ⌥ Option, ⌃ Control, and ⇧ Shift. That’s one more modifier key, and thus more space to breathe. (We’re not counting the Windows key or the [🌐 Globe/Fn key](https://aresluna.org/fn/) since those are technically reserved by the operating system.)

Some keyboards offer extra key caps you can swap to match the platform, for example:

![](_media/deeper-dive-keyboard-differences-between-windows-and-macs/1.1088w.avif)





![](_media/deeper-dive-keyboard-differences-between-windows-and-macs/2.1088w.avif)

Others cover all the bases on fixed key caps, in an awkward way:

![](_media/deeper-dive-keyboard-differences-between-windows-and-macs/3.1088w.avif)





![](_media/deeper-dive-keyboard-differences-between-windows-and-macs/4.1088w.avif)

Many stick with Windows-only legends.

##### Words vs. symbols

Apple devices rely more on symbols on their keys and in their menus, although they don’t do so consistently. Here are all of them:

* ⇧ Shift
* ⌃ Control
* ⌥ Option
* ⌘ Command
* ⏎ Return
* ⌤ Enter
* 🌐 Globe/Fn
* ⇥ Tab
* ⎋ Esc (not printed on keyboards, for some reason)
* ⌫ Delete
* ⌦ Forward Delete
* ⌧ Clear
* ≣ Contextual Menu (only on full-size keyboards)
* ⇞ Page Up (only on full-size keyboards)
* ⇟ Page Down (only on full-size keyboards)
* ↖ Home (only on full-size keyboards)
* ↘ End (only on full-size keyboards)

Actually, I lied about the last four. On modern Apple keyboards, they are:

* ↑ Page Up
* ↓ Page Down
* ⤒ Home
* ⤓ End

Reusing the regular arrows for Page Up and Down is one of a few perplexing decisions from Apple’s keyboard designers. The arrow key symbols look like this – ◀▶▲▼ – but only on Apple keyboards. Here is an older and a newer Apple keyboard showing what happened:

![](_media/deeper-dive-keyboard-differences-between-windows-and-macs/5.1088w.avif)





![](_media/deeper-dive-keyboard-differences-between-windows-and-macs/6.1088w.avif)

(Luckily, the confusing dual arrow key situation only happens on less popular, full-size keyboards.)

Historically, Apple keyboards used symbols more on non-US keyboards, but starting with the 2026 models, they unified when they show symbols and when they show symbols and legends, across all keyboards. (The only key with just a text legend is Esc, making the appearance of ⎋ in menus extra puzzling.)

---

Windows keyboards typically use words – this is why in tight quarters you sometimes see shortenings like Ctrl, Bkspc, PrtSc, Del, PgUp, Win, and so on. (I don’t think Apple ever abbreviates their legends with the exception of Esc for Escape.) In some countries, the legends are translated – as an example, in Germany, Ctrl sometimes appears as Strg.

The symbols that crossed over to Windows side are:

* ⇧ for Shift
* ⇪ or 🔒 or a similar symbol for Caps Lock (on non-US keyboards)
* ⏎ for Enter – note the same arrow as Mac’s ⏎ Return
* ← for Backspace – note a different arrow than Mac’s ⌫ Delete
* ⇥ for Tab (you can also sometimes see ⭾, which is a symbol representing Tab and Reverse Tab together; Reverse Tab used to be a separate key on some 1970s terminals)
* ⊞ for Windows key – the style of the logo will be different depending on the age of the keyboard, roughly matching the Windows logo at the time; some keyboards also use a more abstract shape, or call the key Start or System instead of Windows
* ≣ for contextual menu key (a.k.a. Application Key) – just as Apple added that key on its large keyboards, Microsoft started removing it in favor of [emoji key](https://www.theverge.com/2019/10/11/20909475/microsoft-office-key-emoji-key-keyboards), [Office key](https://www.theverge.com/2019/10/11/20909475/microsoft-office-key-emoji-key-keyboards), and then [Copilot key](https://blogs.windows.com/windowsexperience/2024/01/04/introducing-a-new-copilot-key-to-kick-off-the-year-of-ai-powered-windows-pcs/)
* ⌃ for Control (especially in nerdy contexts)

I have not seen any other popular symbols on the Windows side of the aisle, and I am not even sure if the above would be widely understood. But here’s an example:

![](_media/deeper-dive-keyboard-differences-between-windows-and-macs/7.1088w.avif)

([I wrote a bit more about Mac symbols before](https://unsung.aresluna.org/shift-and-option-and-splat-and-escape/), and also about [the rare Canadian symbols](https://unsung.aresluna.org/key-symbols-we-lost-to-time-pt-2-the-mac-side/).)

##### How to show shortcuts

In menus and other places, Windows joins the key combinations/​shortcuts with a plus, but Apple just glues them together:

* Windows: Shift+A, Ctrl+Shift+G, Ctrl+F11, Alt+Enter
* Mac: ⇧A, ⌃⇧G, ⌘F11, ⌥⏎

Here is the same Chrome menu on Windows and on macOS:

![](_media/deeper-dive-keyboard-differences-between-windows-and-macs/8.1088w.avif)





![](_media/deeper-dive-keyboard-differences-between-windows-and-macs/9.1088w.avif)

(In other words, you’d never say “⌃V is Paste on Windows” like I did above.)

##### Function keys

Both Windows and Macs have function keys.

On Windows, traditionally those were claimed by the operating system or the apps as shortcuts. Here are some examples of well-known function key assignments:

* Alt+F4 – close the app
* F1 – help
* F11 – maximize window
* F12 – dev tools in browsers

On Macs, traditionally the apps didn’t reach for function keys, as those were reserved solely for the users to do stuff with. (However, some combination of ⌃ and function keys are used by the operating system for accessibility options, and I occasionally see apps use function keys these days.)

Windows keyboards top off at F12, but some Mac keyboards reuse the three special PC keys, and even take over the unnecessary Num Lock/​Caps Lock/​Scroll Lock island, and end up going up to F19:

![](_media/deeper-dive-keyboard-differences-between-windows-and-macs/10.1088w.avif)

##### Access to extra characters

In text fields, Apple has a system where pressing ⌥ with printing keys outputs more characters, for example ⌥Q outputs œ, and ⌥7 outputs a ¶ pilcrow. Additionally, ⇧ works in this context, so for example ⌥⇧Q outputs Œ, and ⌥⇧7 outputs a ‡ double dagger.

![](_media/deeper-dive-keyboard-differences-between-windows-and-macs/11.1088w.avif)

Note that not only letters, but basically all printing keys have secret ⌥ and ⌥⇧ assignments. (Also note some of these are [dead keys](https://en.wikipedia.org/wiki/Dead_key).)

Also, ⌥ assignments vary per location! The above was U.S. English, here’s Polish with a lot of differences:

![](_media/deeper-dive-keyboard-differences-between-windows-and-macs/12.1088w.avif)

This means it’s best to avoid ⌥-based shortcuts in text fields, since they might conflict with some important character.

By the way, while the above two are just mock-ups, on some physical keyboards (here: British English), some of the important ⌥ invocations are actually printed on keys:

![](_media/deeper-dive-keyboard-differences-between-windows-and-macs/13.1088w.avif)


---

Windows doesn’t have the above feature. However, Windows has an alternative feature where typing Alt+numpad keys allows to enter any character by its code. (For example, Alt+0128 outputs €. Num Lock has to be enabled. I don’t think it’s possible to do it without a numeric keypad present.)

Mac has a version of this feature, but it requires adding Unicode Hex Input keyboard and switching to it beforehand. Then, pressing ⌥20AC outputs €.

##### Right Alt key on Windows

While Mac modifier keys are completely symmetrical, Windows makes an exception for Alt. On many non-US keyboards, right Alt is also known as [AltGr](https://en.wikipedia.org/wiki/AltGr_key), and does something similar to ⌥ on a Mac: it outputs letters when pressed in combination with printing keys.

For example, on Polish keyboards AltGr+A = ą, AltGr+C = ć, AltGr+Shift+A = Ą, and so on with 15 more combinations. Many other keyboards do similar things.

The way it differs from ⌥ on a Mac is that these are usually reserved for core letters and punctuation necessary for each language, rather than the typographical smorgasbord that Apple provides.

For legacy reasons, and also for keyboards that do not have a physical AltGr key, you can also invoke all these using Ctrl+Alt combinations instead (so, Ctrl+Alt+A = ą). This means that just as you have to be careful about ⌥-based shortcuts in text fields on a Mac, so you should be of [Ctrl+Alt-based shortcuts on Windows](https://aresluna.org/the-curious-case-of-the-disappearing-polish-s/).

Just like on Macs, on some keyboards, selected AltGr options will be printed in the corners or fronts of keys:

![](_media/deeper-dive-keyboard-differences-between-windows-and-macs/14.1088w.avif)

##### Text fields

Text fields in Mac OS apps and web browsers/​websites use some of the standard Unix/​Linux shortcuts based on the ⌃ Control key:

* ⌃A – move to the beginning of the line
* ⌃E – move to the end of the line
* ⌃F – move to the right, or forwards (hold ⌥ to jump through words)
* ⌃B – move to the left, or backwards (hold ⌥ to jump through words)
* ⌃N – move down or to the next command
* ⌃P – move up or to the previous command
* ⌃L – scroll the window so that the text cursor is in the vertical middle
* ⌃H – delete (backspace)
* ⌃D – forward delete
* ⌃K – delete (kill) to the end of the line
* ⌃T – swap (transpose) the adjacent characters
* ⌃O – insert new line, but (contrary to Return) do not move the cursor there

You can combine many of the above with holding ⇧ to extend the selection.

A small group of vocal users love these.

---

Windows still supports Shift+Delete for cut, Ctrl+Insert for copy, and Shift+Insert for paste. I am not sure how many people use these.

---

On a Mac, in simple input fields, ↑ and ↓ jumps to the beginning and end (same as ⌘←→). This often conflicts with command line history, autocomplete pop-ups, and so on.

Windows doesn’t have this convention, and Home and End serve this purpose instead.

---

Macs support the iPhone-inspired convention of holding a key to show related accented characters, instead of triggering auto-repeat. Windows doesn’t have this feature.

![](_media/deeper-dive-keyboard-differences-between-windows-and-macs/15.1088w.avif)

##### Differing shortcut conventions worth knowing about

On a Mac, redo is typically ⌘⇧Z. On Windows, it’s typically Ctrl+Y.

On a Mac, refresh (in browsers, etc.) is typically ⌘R. On Windows, it’s typically F5, although browsers support Ctrl+R, too, and seem to be shifting to that being the default.

##### Reserved keys

Windows’s eponymous ⊞ Windows key is reserved solely for the use of the operating system, and so is Mac’s 🌐 Fn/​Globe key. (Although I am not 100% sure of that as I found one place you can create 🌐 shortcuts as a user – I’m just not certain if it’s intentional.)

However, each platform also has a lot of shortcut combinations that are effectively unavailable, for example ⌘⇥ and ⌘M on a Mac, or Alt+Tab and Ctrl+Shift+Escape on Windows.

These official lists can help:

* [Mac keyboard shortcuts](https://support.apple.com/en-us/102650)
* [Keyboard shortcuts in Windows](https://support.microsoft.com/en-us/accessibility/windows/keyboard-shortcuts-in-windows)

If you’re a web app, you will compete for shortcuts with the operating system (like any app would), but also with the browser itself. You can typically take over shortcuts like [⌘S](https://aresluna.org/the-curious-case-of-the-disappearing-polish-s/) or ⌘P, but depending on the browser or the platform, some might be sacred and unavailable. No Mac browser will allow a website to claim ⌘Q, ⌘W, or ⌘T. Safari won’t allow a web app to override ⌘R. Arc browser won’t allow to override ⌘⇧C. (This is not a complete list.)

##### Jumping around

Tabbing and Shift tabbing is customarily used to jump between UI elements, but it behaves slightly differently in native apps.

On Windows, tabbing jumps through all elements:

[![







](_media/deeper-dive-keyboard-differences-between-windows-and-macs/17-keyed-thumbnail.avif)](_media/deeper-dive-keyboard-differences-between-windows-and-macs/17-keyed-safari.2096w.mov)

On Mac, Tab jumps only to elements that require keyboard to operate (such as input fields). You can toggle a System Settings preference and ask macOS to mimic Windows behaviour – see the last toggle below – but it’s not supported well everywhere.

![](_media/deeper-dive-keyboard-differences-between-windows-and-macs/18.1088w.avif)


---

PgUp and PgDn work differently:

* On Windows, they move the text cursor a screen up or down.
* On a Mac, they scroll the view up and down, but they do not move the text cursor if it’s present (so, they are more an equivalent of clicking on the scrollbar chute).

Similarly, Home and End work differently:

* On Windows, they scroll the contents (and move the cursor if present) to the top or the bottom of a view, or move the cursor to the beginning or the end of an input field.
* On a Mac, in views they scroll to the beginning or end *without moving the cursor.* In input fields, Home/End do nothing, but you can use ⌘←→ to accomplish the same.

On both platforms, Fn+↑↓ does PgUp/​PgDn, and Fn+←→ does Home/End. (Do you see how confusing it is to say that given that ↑↓ already mean PgUp/Dn on a Mac?)

---

Windows has a tradition of enabling access to menus and visible controls by pressing Alt and letter keys. This has [evolved over time](https://unsung.aresluna.org/a-tiny-bit-old-windows-got-right/) and is not as consistent as it used to be, but it might be worth knowing about.

##### Less popular keys

On a 100-plus-key keyboard, Windows might have:

* Insert – still used in some contexts for overtyping
* Print Screen – today taken over by screenshotting
* [Num Lock](https://aresluna.org/this-is-a-story-of-a-figma-bug/) and [Scroll Lock](https://unsung.aresluna.org/lock-scroll-with-a-vengeance/)
* Pause/​Break

![](_media/deeper-dive-keyboard-differences-between-windows-and-macs/19.1088w.avif)

Macs have:

* Help – rarely used, and now abandoned in favor of…
* ≣ Contextual Menu – shows the same menu as right click would
* ⌧ Clear – a [deterministic backspace](https://unsung.aresluna.org/deterministic-vs-idempotent/), these days seldomly different than the actual Delete key

![](_media/deeper-dive-keyboard-differences-between-windows-and-macs/20.1088w.avif)

Macs never had arrow keys on a numeric keypad nor a Num Lock key to enable it. (I’m breaking my promise! [Here’s a fun bug story about Num Lock](https://aresluna.org/this-is-a-story-of-a-figma-bug/).)

In a strange twist of fate, it’s not only third-party keyboards that favor Windows legends. Some of Apple’s keyboards in between 1980s and 2000s showed PC legends, too! (This was to court PC compatibility of then-beleaguered Macs.) Here’s the classic Apple Extended Keyboard, showing legends for Insert, Delete (naming it Del to avoid confusion with its own), Print Screen, Scroll Lock, Pause, Num Lock, and Alt:

![](_media/deeper-dive-keyboard-differences-between-windows-and-macs/21.1088w.avif)

Did I miss anything or make a mistake? [Let me know](https://unsung.aresluna.org/about/)!

[Oct 8, 2026](deeper-dive-keyboard-differences-between-windows-and-macs/)

* [deeper dives 3](tags/deeper-dives/ "Longer-than-usual posts, going deeper into a particular product or area")* [keyboard 57](tags/keyboard/ "Keyboards, keyboard shortcuts, modifier keys, and layouts")* [mac os 37](tags/mac-os/ "Apple’s operating system macOS")* [reference 6](tags/reference/ "Books or sites that are specifically references of things useful in UX design")* [windows 12](tags/windows/ "The operating system Microsoft Windows")
