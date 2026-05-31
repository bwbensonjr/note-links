---
id: 180
url: https://www.fractionalxperience.com/ux-ui-graphic-design-blog/why-jpeg-xl-ignoring-bit-depth-is-genius
title: Why JPEG XL Ignoring Bit Depth Is Genius (And Why AVIF Can’t Pull It Off)   |
  FX Insights
domain: www.fractionalxperience.com
source_date: '2025-10-27'
tags:
- web-dev
summary: 'I don''t have the ability to access external web pages or URLs. However,
  based on your title and note, I can offer this summary:


  JPEG XL''s approach to ignoring bit depth is presented as an advantageous design
  decision that allows for more flexible image compression and better compatibility,
  while AVIF''s attention to bit depth creates limitations it cannot overcome. This
  design philosophy makes JPEG XL more versatile and efficient for various image formats
  and use cases compared to its competitors.


  For a more accurate summary, you could share the actual article content, or visit
  the page directly to read the full explanation.'
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# Why JPEG XL Ignoring Bit Depth Is Genius (And Why AVIF Can’t Pull It Off)   | FX Insights

![Abstract digital burst of color](https://cdn.sanity.io/images/quzbz2eq/production/857106f2f7e11f5fdc21401494eacfc9f000e80a-2200x1466.webp?cs=origin&auto=format&fit=max&w=1600) 

JPEG XL’s float-based perceptual encoding treats images as continuous vision data rather than discrete integers, eliminating bit-depth dependencies that plague traditional codecs.

People often ask me what I mean when I say “JPEG XL is simply the best thought out and forward thinking image format there is. Nothing else is close.” This is article is just one example of why.

When I heard that JPEG XL’s encoder **doesn’t care about bit depth**, it sounded almost reckless (and I was downright confused). In a world obsessed with 8-bit, 10-bit, 12-bit precision wars, shouldn’t bit depth be fundamental? Isn’t more bits always better?

Here’s the twist: ignoring bit depth isn’t a limitation. It turns out it might be a brilliant design decision for modern image compression. And it reveals a fundamental philosophical difference between JPEG XL and AVIF that has massive implications for image quality, workflow simplicity, and future-proofing.

Let me explain why this ”non-feature’ is actually a superpower.

The Problem: Bit Depth Is Just a Convention, Not Reality
--------------------------------------------------------

When Fractional first started building the JPEG XL community site, I ran tens-of-thousands of image tests for various parts of the site. I was really confused when I forced `cjxl` to limited outputs of **10- or 12-bits**, and the resulting file was EXACTLY the same size. So much so, I reached out to [Jon (the man leading the JPEG XL charge)](https://scholar.google.com/citations?user=cwkHAnYAAAAJ&hl=en) to point out what was clearly a bug in the implementation). You can forgive me for being confused when he said it was the expected behaviour.

Inside JPEG XL’s lossy encoder, all image data becomes **floating-point numbers** between 0.0 and 1.0. Not integers. Not **8-bit** values from 0-255. Just fractions of full intensity.

Whether your source was an 8-bit JPEG, a 10-bit camera RAW, a 16-bit professional scan, or even 32-bit floating point data, doesn’t matter. It all maps into the same [0, 1] range. The encoder sees the *meaning* of those colors, not how finely they were quantized before arrival.

Think about what this means: **a bit is just a file format convention, not a perceptual reality**.

Human vision doesn’t care whether a gradient was stored in 256 steps or 1024 steps. It cares whether the gradient *looks* smooth. By working in continuous float space, JPEG XL sidesteps one of the biggest limitations plaguing traditional codecs: dependence on arbitrary digital precision boundaries.

### How AVIF Gets Trapped

AVIF inherits it’s architecture from its video-codec ancestry (AV1), where bit depth is baked into the design. The encoder operates on integer sample buffers – typically **8**-, **10**-, or **12**-bit [**YCbCr**](https://proedu.com/blogs/photography-fundamentals/ycbcr-color-space-understanding-its-role-in-digital-photography?srsltid=AfmBOoqw9rWNXM-SiRhzlVusp7OmkkYWTf2g552Ybjpxe3DWJkAvT-ue&utm_source=chatgpt.com) data – and compresses these samples efficiently, but without a true understanding of their underlying colorimetric meaning.

This limitation comes from early digital video systems where uncompressed video consumed memory at alarming rates. To keep buffer sizes and hardware costs manageable, engineers used the lowest possible bit depth (and aggressive chroma subsampling like 4:2:0). These hardware constraints became encoded into the codec design itself, and they persist decades later even when modern systems have plenty of memory.

You’re encoding **8-bit** images? The encoder optimizes for **8-bit** quantization tables. Working with **10-bit** HDR? Now you need different encoding decisions, different optimization strategies, essentially a different encoding mode. This creates a rigid system where the codec needs to know exactly what bit depth you’re working with at every stage.

The encoder is essentially “blind,” applying lossy compression to numerical values without knowing whether those numbers represent subtle shadow gradations in an HDR scene, or flat colors in a logo. It’s solving for *numerical precision* when it should be solving for *perceptual fidelity*.

JPEG XL’s Solution: Float32 + Perceptual Intent
-----------------------------------------------

Instead of bit depth, JPEG XL works with an **intensity target,** a parameter that defaults to 255 nits and represents the brightness that pure white (1,1,1) should be rendered at.

This perceptual anchor matters far more than arbitrary bit precision because it describes how the image should actually *look* to human eyes.

Things get complicated quickly, as modern displays blow past that default:

* Many laptops now reach **600-1000 nits** in SDR mode
* HDR displays routinely exceed **1000 nits**
* Professional reference monitors can hit **4000+ nits**

With JPEG XL, you simply adjust intensity target to match your content. The encoder automatically allocates precision where it matters perceptually. Same codec, same tools, same optimization strategy – just a different perceptual target.

No switching between 8-bit mode and 10-bit mode. The codec doesn’t care about your display’s technical specs. It just needs to know: ”what brightness level does white represent?” Everything scales from there.

The XYB Secret Weapon
---------------------

This entire philosophy is enabled by JPEG XL’s use of **XYB** – an absolute, perceptually motivated color space used internally for all lossy compression; built specifically for it.

No matter what color space your input uses (sRGB, Display P3, Rec.2020, ProPhoto RGB), the encoder converts everything to **XYB** before compression. This means the encoder always *knows* what it’s looking *at* in perceptual terms.

**The encoder can make intelligent decisions about where to allocate bits based on human visual sensitivity, not arbitrary numeric precision.**

A smooth gradient in shadow detail gets treated as perceptually important regardless of whether it came from **8-bit** or **16-bit** source data. The encoder optimizes directly for what the human eye can distinguish, not for preserving digital exactness.

### The AVIF Blindness

AVIF operates on YCbCr buffers without knowing which RGB color space they reference. Color space handling happens at the file format level, not within the core compression engine. AVIF isn't uniquely flawed. It inherited the same fundamental approach that virtually *every* codec before JPEG XL used.

The encoder can’t leverage colorimetric knowledge for better perceptual optimization. It’s compressing numbers, not colors. It’s preserving bits, not vision.

You can see this in compression comparisons where AVIF is tested with both 4:4:4 and 4:2:0 configurations at different bit depths. Each configuration is essentially a different encoding strategy, because the core engine never fully understood what those numbers *meant*.

Why This Matters for HDR (and Dark Scenes)
------------------------------------------

Here’s a subtle real-world problem that illustrates why perceptual thinking beats bit-precision thinking. When viewing dark image areas with display brightness cranked up – especially when zoomed in so only dark parts are visible, allowing your eyes to fully adapt – you can actually perceive more detail than what traditional **8-bit** encoding allows.

**Your eyes adapt. Traditional codecs don’t account for this.**

JPEG XL’s perceptual approach with adjustable intensity target handles this naturally. You can tell the encoder to assume a brighter viewing environment if needed, and it will allocate precision accordingly.

With bit depth-focused codecs like AVIF, you’re stuck with the precision limitations of your chosen bit depth, regardless of viewing conditions.

The Bottom Line
---------------

JPEG XL not worrying about bit depth isn’t an oversight *or* simplification. It’s liberation from decades of accumulated cruft where we confused digital precision with perceptual quality.

It’s a sign that we’ve moved past “how many bits per channel” as a quality metric, and toward “how well does it look, everywhere, to everyone, on any display?”

AVIF, constrained by its video codec DNA, remains shackled to integer sample buffers and bit depth-specific optimization paths. It’s a competent codec optimized for streaming video at web-scale. But it’s solving a different (and arguably less important) problem than JPEG XL.

For photographers, web developers, archivists, and anyone who cares about image quality across diverse content types and viewing conditions, JPEG XL’s approach is refreshingly sensible.

**It’s one less thing to worry about. And it produces better results where it counts.**

That’s why this quiet “non-feature” is actually one of JPEG XL’s most awesome innovations.

‍

**2025-10-27 Update**: This post was inspired by a post from Jon (mentioned above) in the [JPEG XL Discord community](https://discord.com/channels/794206087879852103/822105409312653333/1430439005614247988) where he describes the intensity target approach. It was a "penny drop" moment for me – I wish I would have understood it sooner! I've corrected a few sections and removed some that people thought were irrelevant for the point of the article.

---
