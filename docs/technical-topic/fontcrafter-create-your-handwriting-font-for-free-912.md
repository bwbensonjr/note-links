---
id: 912
url: https://arcade.pirillo.com/fontcrafter.html
title: 'FontCrafter: Create Your Handwriting Font for Free'
domain: arcade.pirillo.com
source_date: '2026-03-09'
tags:
- cli-tool
- web-dev
- tutorial
summary: FontCrafter is a free, browser-based tool that converts your handwritten
  samples into installable fonts (OTF, TTF, WOFF2, Base64 formats) without requiring
  account creation or uploading data to servers. The process involves printing a template,
  filling it with handwriting samples using a felt-tip pen, scanning the page, and
  uploading it to the app where character detection and font generation occur entirely
  locally on your device. The tool includes advanced features like automatic ligature
  generation, contextual alternates, extended character support, and kerning adjustment—all
  completely free, with commercial use rights retained by the user.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# FontCrafter: Create Your Handwriting Font for Free

FontCrafter: Create Your Handwriting Font for Free
==================================================

×

About FontCrafter
-----------------

FontCrafter turns your handwriting into a real, installable font — entirely in your browser. No accounts, no uploads to servers, no cost.

Still have questions? [Here's our FAQ.](#)

#### How does it work?

Drop in a scan of your handwriting. The app detects each character, traces vector outlines, and builds a working OpenType font file you can install anywhere. Everything runs locally — your handwriting never leaves your device.

#### Who is it for?

Anyone who wants a personal handwriting font — designers, teachers, content creators, or anyone who thinks their handwriting deserves to be a typeface.

[Handwriting Fontalizer — Turn any handwriting photo into a template](https://arcade.pirillo.com/handwriting-fontalizer.html)
[More of My Apps](https://arcade.pirillo.com/)
[Follow Chris Pirillo](https://chris.pirillo.com/)
[Learn How to Make Apps](https://ctrlaltcreate.live/)
[Donate to Me Here](https://www.paypal.com/donate/?hosted_button_id=UMWCDWGVXVHZU)
[Support My Patreon](https://patreon.com/ChrisPirillo)

×

Frequently Asked Questions
--------------------------

#### Is FontCrafter really free?

Yes — completely free with no hidden limits. There's no account required, no watermarks, no feature gates, and no premium tier. You get full access to OTF, TTF, WOFF2, and Base64 exports, plus ligature generation. Your font files are yours to keep and use however you want.

#### Do I need to create an account?

No. FontCrafter requires zero signup. Open the page, load your scan, build your font, download it. No email, no password, no account whatsoever.

#### Is my handwriting uploaded to a server?

No. Everything runs locally in your browser using JavaScript. Your scan never leaves your device — no server processing, no cloud storage, no data collection. This is a fully client-side application.

#### What font formats can I export?

FontCrafter exports four formats: **OTF** (OpenType, best for desktop apps like Word and Photoshop), **TTF** (TrueType, universal compatibility), **WOFF2** (compressed web font for websites), and **Base64** (for embedding directly in CSS). All formats are generated locally.

#### Does FontCrafter support ligatures?

Yes. FontCrafter can auto-generate ligatures — connected letter pairs like "ff," "fi," "th," and "st" that make your font flow naturally. It also supports contextual alternates, cycling between your handwriting variants for a more organic feel. Many competing tools charge for ligature support.

#### How is this different from Calligraphr?

Calligraphr requires an account and processes your handwriting on their servers. Ligatures and advanced features require a paid subscription ($8/month). FontCrafter is 100% free, requires no account, processes everything locally in your browser, and includes ligatures, contextual alternates, and color font effects (drop shadows and ink texture) at no cost. FontCrafter also exports WOFF2 and Base64 formats that Calligraphr doesn't offer.

#### What kind of pen should I use?

A dark felt-tip pen (0.5mm or thicker) gives the best results. Ballpoints are often too faint, and thick markers can bleed. Keep your strokes inside the boxes with a little breathing room from the edges.

#### Can I use my font commercially?

The font is generated from your own handwriting, so you own it. You can use it for personal projects, commercial work, branding, merchandise — anything. Just make sure the handwriting is yours or you have permission from the person whose handwriting was used.

#### Do I have to print the template?

No. If you can't print the template or want to use existing handwriting, [Handwriting Fontalizer](https://arcade.pirillo.com/handwriting-fontalizer.html) lets you snap a photo of any handwriting sample and converts it into a FontCrafter-compatible template. Write your characters on white paper, take a photo, assign each letter, and download a template PNG you can upload here.

×

Under the Hood
--------------

Everything below happens entirely in your browser. No server, no WebAssembly binary, no hidden dependencies — just JavaScript running on your device.

#### The Processing Pipeline

When you drop in a scan, FontCrafter runs a multi-stage image processing pipeline: adaptive thresholding to isolate ink from paper, connected-component blob detection to find individual characters, Suzuki-Abe contour tracing to extract outlines, Ramer-Douglas-Peucker (RDP) simplification to reduce point count, Chaikin corner-cutting for smooth curves, and cubic Bézier fitting to produce clean vector paths. The entire pipeline is tuned for handwriting — pen pressure variation, stroke overlap, and ink bleed are all accounted for.

#### Font Architecture

FontCrafter builds fully compliant OpenType fonts from scratch — not a template with swapped glyphs, but real font table construction. The standard font uses CFF (Compact Font Format) outlines with cubic Bézier curves at 1000 UPM (units per em). Metrics are calculated from your actual handwriting: ascender, descender, cap height, and x-height are derived from the scanned characters, not hard-coded values.

#### OpenType Features

Your font includes a GSUB (Glyph Substitution) table with two key features. **Contextual Alternates (calt):** FontCrafter stores up to 3 handwriting variants per character and builds lookup rules that cycle between them as you type, so repeated letters never look identical — the same trick professional handwriting fonts use. **Ligatures (liga):** Common letter pairs like ff, fi, fl, th, and st are composited from your existing characters with overlap and kerning adjustments, then injected as ligature substitutions. Both features are baked into the font binary — they work in any app with OpenType support (Word, Pages, Photoshop, InDesign, Figma, CSS).

#### Kerning

FontCrafter generates kern pairs using a class-based approach. Characters are grouped by shape (round letters like O, C, G share one class; diagonal letters like A, V, W share another), then pair-specific adjustments are applied so combinations like AV, To, and WA sit together naturally. You can choose tight, normal, or loose spacing — each adjusts the kern values proportionally.

#### Composite & Extended Characters

The standard font can exceed 500 glyphs, most generated automatically. Accented characters (à, ñ, ü, ø, and 100+ more) are built by compositing your base letters with programmatically positioned diacritical marks. Extended characters — smart quotes, fractions, currency symbols, circled letters, superscripts — are constructed by combining, scaling, flipping, and repositioning your existing strokes. Nothing is pulled from a system font or generic template.

#### Color Fonts (COLR/CPAL)

The color font option builds a COLR (Color Outline) table with a CPAL (Color Palette) for multi-layer rendering. Drop shadows use a duplicate glyph layer offset and painted with the shadow color beneath the primary layer. Ink texture uses a noise-based edge erosion algorithm to create an organic, hand-inked look with two color layers. Duo-tone splits each glyph horizontally with a configurable split point. These are real COLRv0 fonts — they render natively in Chrome, Edge, Firefox, Safari, and any app that supports OpenType color fonts.

#### Output Formats

**OTF (OpenType/CFF):** Cubic Bézier outlines, best quality for desktop apps — Word, Photoshop, InDesign, Figma. **TTF (TrueType):** Quadratic Bézier outlines converted from CFF, maximum compatibility across platforms and older software. **WOFF2:** Brotli-compressed OTF wrapped in a web font container — typically 30-50% smaller than raw OTF, optimized for CSS @font-face. **Base64:** The full OTF binary encoded as a base64 data URI, ready to paste directly into a CSS @font-face rule — zero external file dependencies. All four formats are generated client-side using ArrayBuffer construction and binary table assembly.

#### What You Don't Get (Yet)

FontCrafter doesn't currently support: variable fonts (OpenType fvar), hinting/instruction programs (TrueType bytecode), right-to-left scripts, CJK character sets, or multi-page template scanning. These may come in future updates.

×

What's New
----------

FontCrafter is actively developed and improved. Have a feature request, found a bug, or just want to say hi? Reach out to [[email protected]](/cdn-cgi/l/email-protection#086b607a617b4878617a61646467266b6765).

March 28, 2026

* Higher resolution output — your scan now stays at its original resolution instead of being downscaled, producing noticeably smoother curves and finer stroke detail in the finished font
* Better corner mark detection — scans with extra paper margin, faint marks, or only 2 visible marks now align correctly instead of locking onto the wrong features
* Grayscale grid line cleanup — templates printed on black-and-white printers no longer bleed grid lines into your glyphs
* Saved projects from older versions import correctly — polished characters are automatically scaled to match the new higher resolution

March 26, 2026

* Descender spacing fixed — letters like y, g, j, and q now tuck their tails under the previous character instead of leaving a gap
* Save and restore your entire project — export saves your scan, settings, and all tweaks as a single .fontcrafter.json file. Drop it back in to pick up where you left off
* Template line cleanup improved — dashed baseline fragments and box label bleed are caught by position-aware filtering, even on JPEG-compressed scans where color detection can't help
* Cell cropping tightened at the top edge — printed character labels from the template header no longer sneak into your glyphs

March 24, 2026

* Edit characters now has erase AND draw modes — erase stray marks or draw in missing parts with one click
* Universal DPI support — templates at any resolution are automatically normalized so registration marks line up perfectly
* Baseline positioning is now WYSIWYG — the amber line matches exactly what the font builder computes
* Lowercase descenders use data-driven positioning — they only descend if your handwriting actually extends below the baseline

March 22, 2026

* Fine-tune letter sizes — per-character sizing modal lets you visually compare and resize any letter that looks too big or too small
* Handwriting Fontalizer integration — can't print the template? Use any handwriting photo instead
* FontCrafter app family — 8 free browser tools that use your font, featured at the top and after download
* The old "Even out letter sizes" checkbox has been replaced by the new sizing modal — more control, better results

March 16, 2026

* Erase stray marks — zoom into any character and erase specks, grid lines, or pen trails with undo
* Faded corner marks no longer break your scan — FontCrafter infers missing marks from the other three
* Faded baseline dashes no longer leak into your font on phone scans
* Simplified letter positioning — the baseline editor is now the single tool for adjusting where letters sit

March 14, 2026

* Uppercase/lowercase fonts now build correctly on first try
* Periods, commas, and small punctuation are now detected even when drawn very small
* Cleaner glyph previews — tiny dot artifacts from PDF imports no longer appear
* PDF uploads process faster using a background worker

March 13, 2026

* Drag-to-adjust letter positioning — tap any letter and drag it up or down on the baseline
* Download Everything — one ZIP with all font formats, your settings, and your original scan
* Export & import settings — save your template + every tweak as a ZIP, import it later
* High-res scans no longer crash — large images are automatically downscaled

March 12, 2026

* Overhauled letter spacing — T, V, W now tuck properly next to lowercase
* New smoothing slider — 5 levels to control how polished your curves look
* Faint ink rescue — light pen strokes that were being lost are now preserved
* Fixed cutouts in W, M, and rounded characters at thin stroke points

March 9, 2026

* Colored paper support — scans on pink, green, or blue-lined paper now process correctly
* Purple and violet ink no longer gets mistaken for grid lines

March 8, 2026

* A4 template support for international users
* Templates now print as crisp vector PDFs instead of blurry PNGs
* FAQ section with structured data for better search visibility

March 7, 2026

* Auto-generated ligatures — ff, fi, fl, th, st and more for natural handwriting flow
* Contextual alternates — your font cycles through all 3 handwriting variants automatically
* 500+ glyphs per font — accented characters, smart quotes, fractions, and currency symbols
* Color font effects — drop shadows, ink textures, and duo-tone using OpenType COLR/CPAL

March 6, 2026

* FontCrafter launched — scan your handwriting, get a real installable font
* Exports to OTF, TTF, WOFF2, and Base64 — works everywhere
* No account, no uploads, no cost — runs entirely in your browser

×

Fine-Tune Letter Positions
--------------------------

Every character is shown at its natural position. The amber line shows where the font baseline will be — characters above it sit on the line, parts below it will descend. If it looks right, don't touch it.

Offset: —

Reset All
Done

×

Fine-Tune Letter Sizes
----------------------

Click a character, then use **[** **]** or the buttons to resize. Small adjustments (±5–10%) look best.

Size:
−
—
+
Reset

Reset All
Done

×

Mark the Four Corners
---------------------

Drag each colored marker onto the matching ⊕ crosshair on your scan. A magnifier will appear while dragging so you can place it precisely.

① Top-left
 ② Top-right
 ③ Bottom-left
 ④ Bottom-right

![Your scan]()

1

2

3

4

Re-process with these marks →

?

Turn Your Handwriting  
Into a Real Font — Free

**It's easier than you think. Print, write, scan — done.**

* Your handwriting becomes a downloadable & installable font
* What you make is yours — works on every platform and the web
* Natural variation — your letters won't look robotic or identical every time
* Letters connect naturally — ff, th, st flow like real writing
* Optional drop shadows and ink texture effects baked right into the font
* 100+ special characters auto-generated — like fractions, accents, and currency
* No account, no server, 100% private — everything happens in your browser
* [Typography Nerd? See what's under the hood](#)·[Updated Mar 28 — see what's changed](#)

Then use your font immediately — directly in your browser with our free app family!

[QuoteCrafterShareable quote images](https://arcade.pirillo.com/quote-crafter.html)
[LetterCrafterPersonal letters & notes](https://arcade.pirillo.com/letter-crafter.html)
[CertificateCrafterAwards & diplomas](https://arcade.pirillo.com/certificate-crafter.html)
[CardCrafterBusiness cards](https://arcade.pirillo.com/card-crafter.html)
[GreetingCrafterGreeting cards](https://arcade.pirillo.com/greeting-crafter.html)
[WeddingCrafterWedding invitations](https://arcade.pirillo.com/wedding-crafter.html)
[LabelCrafterLabels & stickers](https://arcade.pirillo.com/label-crafter.html)
[EnvelopeCrafterPrintable envelopes](https://arcade.pirillo.com/envelope-crafter.html)

**PenSend** — type in your handwriting font & share from your phone

[iPhone](https://apps.apple.com/us/app/pensend-your-handwriting-font/id6761138244)
·
[Android](https://play.google.com/store/apps/details?id=com.fontcrafter.pensend)
·
[Web](https://arcade.pirillo.com/pensend.html)

### START

1. **Print** the template at 100% scale — or open it on-device.
2. **Fill in every box** — felt-tip pen on paper, or stylus on screen. One character per row, three times each.
3. **Drop the file below** — scan, photograph, or save your digital version.

Keep strokes inside the boxes with breathing room. Your natural variation across rows is what makes the font look real. For lowercase: Row 1 uppercase, Row 2 lowercase, Row 3 your choice. If scanning: flat on a table, even lighting, no wrinkles or shadows.

Download Template (US Letter)
Download Template (A4)

Having trouble? Try an alternative template

Light Guide

Grid lines bleeding into your font? This version uses small corner marks instead of full boxes.

US Letter
A4

Printer-Friendly

Corner marks getting cut off by your printer? This version pulls them inward so nothing gets clipped.

US Letter
A4

No Printer?

Write on plain paper, snap a photo, and let [Handwriting Fontalizer](https://arcade.pirillo.com/handwriting-fontalizer.html) build a compatible template.

### LOAD

Drop your completed scan or a saved FontCrafter project below. JPG, PNG, PDF, high-res photo, or a .fontcrafter.json export. Everything is processed on your device. Nothing is uploaded or stored.

**Drop your scan or saved project here**, or click to browse

![Your scanned handwriting template]()

Not happy with a character? Touch it up in any image editor, or use correction tape and re-scan.

Make Sure All Four Corner Marks Are Visible, Then Continue →

Import saved settings
Previously exported? You can also drop the ZIP in the upload area above.

2 Verify

Processing your handwriting…

### INSPECT

**Green = good.** Click any character to swap it for a different version from your scan. Small imperfections are fine — they give your font personality.

Row 1

Row 2

Row 3

Scan Complete

Characters look off? Fix it Continue with All Characters →

3 Customize

### GENERAL

Name your font and choose how your three rows should be used. Enable **letter connections** for natural-looking handwriting flow.

What do you want to call this font?

Your name (optional — embedded in font metadata)

What did you put in each row?

Row 1

Uppercase
Lowercase

Row 2

Uppercase
Lowercase
Blank

Row 3

Uppercase
Lowercase
Blank

Row 2 will be used as your lowercase. Adjust how much to shrink it — set to 1.00 if you already wrote Row 2 smaller than Row 1.

Lowercase size

1.00

Clean up stray ink marks

Removes tiny specks that bled through from adjacent boxes. Won't affect dots on i, j, or punctuation.

Outline smoothing Medium


FaithfulSmoother

Controls how much the outlines are smoothed. Lower keeps your natural wobble, higher produces cleaner curves.

### POLISHING (Clean Up)

Erase stray marks, grid lines, or specks that survived automatic cleanup. This shows exactly what goes into your font — not just the preview.

Auto-remove tiny specks

Removes tiny specks that bled through from adjacent boxes. Won't affect dots on i, j, or punctuation.

Edit characters

Opens every character as it will appear in your font. Zoom in to erase stray marks or draw in missing parts.

Edit Characters×

Click any character to zoom in. Erase stray marks or draw in missing parts. Dashed borders mean you've edited it.

Edit×

Undo
Reset
Done

### POSITIONING (Baselines)

Control where each letter sits relative to the baseline — drag them individually or shift common ones in bulk.

Adjust letter positions

See all your letters on a baseline and drag any of them up or down — all 3 rows.

### SIZING (Per-Character)

Adjust individual characters that look too big or too small compared to their neighbors.

Fine-tune letter sizes

See all your letters side by side and resize any that don't match. Changes carry through to your font automatically on next build.

### CONNECTIONS (Ligatures)

Common letter pairs like *ff*, *fi*, *th*, and *st* will connect so your font flows naturally. Turn this off if you want each letter separate.

No letter connections

Auto-connect letter pairs (recommended)

Letter pairs to connect:


Comma-separated pairs. Lowercase and uppercase versions included — remove any you don't need.

### SPACING (Kerning)

Adjusts the space between certain letter pairs so they look right. AV, To, and WA are common ones.

Adjust letter spacing automatically (recommended)

Tight

Normal

Loose

### OUTPUT

Pick one. You can always come back and build the other.

Standard font — up to 500+ characters, including extended and accented letters

Single color font — up to 500+ characters with your pen color baked in

Multi-color font — up to 350+ characters with built-in color effects (processing takes longer)

Pick a color — it will be baked directly into the font file.

Font color

#cc0000

The options below are built automatically from your handwritten characters.

Most extended characters (smart quotes, fractions, currency, circled letters, etc.)

Most accented characters for European languages (à, ñ, ü, ø, etc.)

The options below are built automatically from your handwritten characters. Nothing extra to draw — FontCrafter creates them by combining, flipping, and resizing the letters you already wrote.

Most extended characters (smart quotes, fractions, currency, circled letters, etc.)

Most accented characters for European languages (à, ñ, ü, ø, etc.)

Drop shadow

Ink texture

Duo-tone split

Rainbow gradient

Flag stripes

Labelmaker

Color fade

Letter color

#1a1a1a

Shadow color

#ff9100

Stroke color

#1a1a1a

Edge color

#999999

Texture spread 5%


SubtleHeavy

Top color

#1a1a1a

Bottom color

#cc3333

Split position 50%


LowerHigher

Split angle 0°


HorizontalFull rotation

Gradient angle 0°


HorizontalFull rotation

Stripe colors

+ Add
− Remove

Stripe angle 0°


HorizontalFull rotation

Tape color

#2a2722

Letter color

#f6f1e9

Start color

#ff2266

End color

#2244ff

Fade angle 0°


HorizontalFull rotation

Create and Download Your Font →

Building your font…

4 Download Font

### PREVIEW

See how your font looks with sample text, or type anything you like below.

Without Ligatures
With Ligatures

UppercaseTHE QUICK BROWN FOX JUMPS OVER A LAZY DOG.  
Lowercasesphinx of black quartz, judge my vow?  
Mixed CaseBoth Fickle Dwarves Can Jinx My Pig Quiz!  
  
• $11.38 + tax & a 5.69% tip = more than $20.74  
• (I love Star Wars) [Yes] {Maybe} <OK>  
• That’s what I said! “Really?”  
• arcade.pirillo.com \* chris.pirillo.com  
• He scored 7/8 on the quiz — not bad~  
• Order #4053: 2x @$16.99 each | Total: $33.98  
• Is it \_really\_ 100^2 = 10,000‽  
• "Yes," she said, 'it's a go;' then walked away.

Your font includes **contextual alternates** (calt) — consecutive characters will automatically cycle between your 3 handwriting variants. This works in apps with OpenType support but may not appear in this preview.

### Try Your Font

Click here to try it for yourself...

If you found this useful, I'd appreciate [donations](https://www.paypal.com/donate/?hosted_button_id=UMWCDWGVXVHZU) & [patrons](https://patreon.com/ChrisPirillo) (to keep iterating)!

### DOWNLOAD

**OTF** for desktop apps, **TTF** for universal compatibility, **WOFF2** for websites, **Base64** for CSS embedding.

I confirm that the handwriting / content used to generate this font is **my own or I have explicit permission** from the owner to create and use it. I understand that I am solely responsible for how I use the generated font and I release FontCrafter, Chris Pirillo, and LockerGnome from any liability related to the font's creation, distribution, or use. You also confirm that no signatures were used in your template for generating this file.

Then use your font immediately — directly in your browser with our free app family!

[QuoteCrafterShareable quote images](https://arcade.pirillo.com/quote-crafter.html)
[LetterCrafterPersonal letters & notes](https://arcade.pirillo.com/letter-crafter.html)
[CertificateCrafterAwards & diplomas](https://arcade.pirillo.com/certificate-crafter.html)
[CardCrafterBusiness cards](https://arcade.pirillo.com/card-crafter.html)
[GreetingCrafterGreeting cards](https://arcade.pirillo.com/greeting-crafter.html)
[WeddingCrafterWedding invitations](https://arcade.pirillo.com/wedding-crafter.html)
[LabelCrafterLabels & stickers](https://arcade.pirillo.com/label-crafter.html)
[EnvelopeCrafterPrintable envelopes](https://arcade.pirillo.com/envelope-crafter.html)

**PenSend** — type in your handwriting font & share from your phone

[iPhone](https://apps.apple.com/us/app/pensend-your-handwriting-font/id6761138244)
·
[Android](https://play.google.com/store/apps/details?id=com.fontcrafter.pensend)
·
[Web](https://arcade.pirillo.com/pensend.html)

.OTF

OpenType — best for desktop

↓ Download

.TTF

TrueType — universal

↓ Download

.WOFF2

Web font — smallest file

↓ Download

Base64

CSS @font-face embed

↓ Copy

Download Everything (.zip)

All font formats + your settings in one ZIP — ready to use or re-import later.

Want to come back and rebuild this font later — or try different settings with the same template?

Export template + settings

Saves your scan and all your tweaks as a ZIP. Import it next time to skip straight to download.

Get notified when I ship new features and tools:

Start Over[Support](https://www.paypal.com/donate/?hosted_button_id=UMWCDWGVXVHZU)
[Patreon](https://patreon.com/ChrisPirillo)
