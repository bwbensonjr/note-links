---
id: 938
url: https://ayosec.github.io/ffmpeg-drawvg/
title: FFmpeg - drawvg - FFmpeg - drawvg
domain: ayosec.github.io
source_date: '2026-03-20'
tags:
- cli-tool
- tutorial
- web-dev
summary: The drawvg filter for FFmpeg (available since version 8.1) allows users to
  render vector graphics on top of video frames using a custom scripting language
  called VGS (Vector Graphics Script). VGS is designed to be concise and easy to use,
  with syntax inspired by PostScript, SVG, and other languages, and supports dynamic
  graphics through FFmpeg expressions for computing coordinates, accessing frame metadata,
  and reading pixel colors. The page provides practical examples demonstrating how
  to use drawvg for creating progress indicators, transitions, pixelization effects,
  and wave distortions by combining it with other FFmpeg filters.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# FFmpeg - drawvg - FFmpeg - drawvg

drawvg filter for FFmpeg
========================

drawvg is a [FFmpeg filter](https://ffmpeg.org/ffmpeg-filters.html), available since [8.1](http://ffmpeg.org/index.html#pr8.1), to render vector graphics
on top of video frames.

FFmpeg must be configured with the `--enable-cairo` flag. You can see the
enabled flags by running `ffmpeg -version`.

The render is done by executing a script written in its own language, called VGS
(*Vector Graphics Script*). The script consists of a series of commands to
describe 2D graphics, which are rasterized using the [Cairo](https://www.cairographics.org/) library.

VGS is not intended to be used as a general-purpose language. Since its scope is
limited, it prioritizes being concise and easy to use. The syntax is heavily
inspired by languages like [Magick Vector Graphics](https://imagemagick.org/script/magick-vector-graphics.php), or
[SVG's `<path>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/path). Some features of the syntax (like using whitespaces
to separate arguments) are also present in languages like
[TCL](https://en.wikipedia.org/wiki/Tcl) or
[shell scripts](https://en.wikipedia.org/wiki/Shell_script).
Many command names are taken from [PostScript](https://en.wikipedia.org/wiki/PostScript). VGS is fully documented in the
[language reference](https://ayosec.github.io/ffmpeg-drawvg/playground/docs/langref.html).

Scripts can use [FFmpeg expressions](https://ffmpeg.org/ffmpeg-utils.html#Expression-Evaluation) to describe graphics dynamically, so they
can compute coordinates based on frame dimensions, frame metadata, generate
random values, read pixel colors, etc.

Examples
--------

This is a short list of examples to showcase how to integrate the drawvg filter with other filters in FFmpeg.

The [Playground](https://ayosec.github.io/ffmpeg-drawvg/playground) has a gallery with more examples, focused on the capabilities of the VGS language.

### Progress Indicator

The variable `t` can be used to compute one of the angles of the [arcn](https://ayosec.github.io/ffmpeg-drawvg/playground/docs/langref.html#cmd_arcn) command. Then, we can create an animation like this:

[](https://ayosec.github.io/ffmpeg-drawvg/playground/docs/outputs/example-Sde_owQVLWbF0siN.webm)

The script can be rendered directly on top of a video:

Output

[](https://ayosec.github.io/ffmpeg-drawvg/playground/docs/outputs/example-jlReCLPh1bWjR0zZ.webm)

`progress.vgs`

```
setvar T 3
setvar R (h / 6)

translate (w - R - 5) (R + 5)

moveto 0 0
arcn 0 0 R
    (3 * PI / 2 - (PI * 2 * mod(t - ts, T) / T))
    (-PI / 2)

setcolor red@0.6
fill
```

Shell

```
ffmpeg \
    -an \
    -ss 12 -t 3 -i bigbuckbunny.mov \
    -vf 'crop=iw-1, drawvg=file=progress.vgs, format=yuv420p' \
    -c:v libvpx-vp9 \
    output.webm
```

This example uses clips from the [Big Buck Bunny movie](https://peach.blender.org/download/), available under [CC BY 3.0](http://creativecommons.org/licenses/by/3.0/) license.

### Using Frame Metadata

The [cropdetect](https://ffmpeg.org/ffmpeg-filters.html#cropdetect) filter calculates the necessary cropping parameters to remove black borders around a video. These parameters are added to each frame as [metadata](https://trac.ffmpeg.org/wiki/FilteringGuide#FilterMetadata).

drawvg can access the output of [cropdetect](https://ffmpeg.org/ffmpeg-filters.html#cropdetect) with the [getmetadata](https://ayosec.github.io/ffmpeg-drawvg/playground/docs/langref.html#cmd_getmetadata) command. The following example draws a red rectangle to represent the calculated area by [cropdetect](https://ffmpeg.org/ffmpeg-filters.html#cropdetect).

Output

[](https://ayosec.github.io/ffmpeg-drawvg/playground/docs/outputs/example-qIPk1-BPAJOwKCi0.webm)

`cropdetect.vgs`

```
getmetadata cdx lavfi.cropdetect.x
getmetadata cdy lavfi.cropdetect.y
getmetadata cdw lavfi.cropdetect.w
getmetadata cdh lavfi.cropdetect.h

rect cdx cdy cdw cdh
setcolor red@0.5
setlinewidth 10
stroke
```

Shell

```
ffmpeg \
    -an \
    -i highway.mp4 \
    -vf 'cropdetect, drawvg=file=cropdetect.vgs, format=yuv420p' \
    -c:v libvpx-vp9 \
    output.webm
```

This example uses the video [Night Drive on Highway with Passing Cars](https://www.pexels.com/video/night-drive-on-highway-with-passing-cars-31940329/), free to use by the [pexels license](https://www.pexels.com/license/).

### CircleCrop Transition

This example creates a transition similar to the [`circlecrop` transition](https://trac.ffmpeg.org/wiki/Xfade#:~:text=circlecrop) of the [xfade](https://ffmpeg.org/ffmpeg-filters.html#xfade) filter, but the circle can be positioned anywhere, not only at the center of the frame.

Output

[](https://ayosec.github.io/ffmpeg-drawvg/playground/docs/outputs/example-0TY6WIhNGmxGQVkA.webm)

`circlecrop.vgs`

```
rect 0 0 w h
setvar d (sin(PI / 2 * (t - ts)))
circle (4 * w / 5) (3 * h / 5) (max(w, h) * (1 - d))
eofill
```

`circlecrop.filter`

```
crop = iw-1 ,
drawvg = file=circlecrop.vgs : enable='gt(t,0.8)' ,
format = yuv420p
```

Shell

```
ffmpeg \
    -an \
    -ss 14 -t 4.2 -i bigbuckbunny.mov \
    -/vf circlecrop.filter \
    -c:v libvpx-vp9 \
    output.webm
```

This example uses clips from the [Big Buck Bunny movie](https://peach.blender.org/download/), available under [CC BY 3.0](http://creativecommons.org/licenses/by/3.0/) license.

### Custom Transitions

Another way to create custom transitions is to use the [alphamerge](https://ffmpeg.org/ffmpeg-filters.html#alphamerge) and [overlay](https://ffmpeg.org/ffmpeg-filters.html#overlay) filters, with a mask rendered with a drawvg script.

This is the output of the drawvg script:

[](https://ayosec.github.io/ffmpeg-drawvg/playground/docs/outputs/example-fcoEsyI1r5WjOVL5.webm)

[alphamerge](https://ffmpeg.org/ffmpeg-filters.html#alphamerge) can set these frames as the alpha channel of a video. Then, use [overlay](https://ffmpeg.org/ffmpeg-filters.html#overlay) to put the video with the mask on top of another one.

Output

[](https://ayosec.github.io/ffmpeg-drawvg/playground/docs/outputs/example-DZEVqfDXIiIlMsCi.webm)

`transition.vgs`

```
setvar BARS 7
setvar DURATION 2

setvar IB (1 / BARS)
setvar P ((t - ts) / DURATION)

scalexy w h
translate 0 0.5

repeat BARS {
    setvar bar (BARS * (P - i / BARS))
    if (lt(bar, 0)) {
        break
    }

    rect 0 (if(mod(i, 2), 0.5 - bar, -0.5)) IB bar
    translate IB 0
}

fill
```

`transition.filter`

```
[0] split [mask-bg] [mask-delay] ;

[mask-bg] drawvg = file=transition.vgs [bars] ;

[mask-delay] [bars] concat [mask] ;

[1] [mask] alphamerge [a] ;

[2] [a]
    overlay = enable='lt(t,4)' ,
    crop = iw-1 ,
    format = yuv420p
```

Shell

```
ffmpeg \
    -f lavfi -i 'color=white:s=853x480:r=24:d=2' \
    -ss 16 -t 4 -i bigbuckbunny.mov \
    -ss 7:51 -t 6 -i bigbuckbunny.mov \
    -/filter_complex transition.filter \
    -an \
    -c:v libvpx-vp9 \
    output.webm
```

This example uses clips from the [Big Buck Bunny movie](https://peach.blender.org/download/), available under [CC BY 3.0](http://creativecommons.org/licenses/by/3.0/) license.

### Reading Colors

The function `p(x, y)` returns the color of a pixel at the given coordinates. It can be used to apply pixelization to a frame, similar to the [pixelize](https://ffmpeg.org/ffmpeg-filters.html#pixelize) filter.

Instead of rectangles, the shape used for pixelization are rhombuses, and each one has a thin border to highlight its outline.

The output below shows the original frame on the left, and the frame updated by the drawvg script on the right:

Output

[](https://ayosec.github.io/ffmpeg-drawvg/playground/docs/outputs/example-wOdQRUn5nsnOEipR.webm)

`pixelate.vgs`

```
setvar SIZE 20

setvar MID (SIZE / 2)

repeat (h / SIZE + 1) {
    save

    if (mod(i, 2)) {
        translate SIZE 0
    }

    setvar COL i

    repeat (w / SIZE + 1) {
        setvar px (p(0, 0))

        if (isnan(px)) {
            setvar px (p(-MID, 0))
        }

        if (isnan(px)) {
            setvar px (p(0, -MID))
        }

        if (not(isnan(px))) {
            setcolor px
        }

        moveto (-SIZE) 0
        lineto 0 (-SIZE), SIZE 0, 0 SIZE
        closepath

        preserve
        fill

        setcolor black@0.1
        stroke

        translate (SIZE * 2) 0
    }

    restore

    translate 0 SIZE
}
```

`pixelate.filter`

```
[0] scale = iw/1.5 : -2 , split [a] [b] ;

[a]
    pixelize ,
    drawvg = file=pixelate.vgs ,
    pad = iw*2+30 : ih+20 : iw+20 : ih+10
    [a0] ;

[a0] [b]
    overlay = 10 : 10 ,
    format = yuv420p
```

Shell

```
ffmpeg \
    -an \
    -ss 1 -t 18 -i bigbuckbunny.mov \
    -/filter_complex pixelate.filter \
    -c:v libvpx-vp9 \
    output.webm
```

This example uses clips from the [Big Buck Bunny movie](https://peach.blender.org/download/), available under [CC BY 3.0](http://creativecommons.org/licenses/by/3.0/) license.

### Waves Effect

drawvg can be combined with the [displace](https://ffmpeg.org/ffmpeg-filters.html#displace) filter to create a wave effect:

[](https://ayosec.github.io/ffmpeg-drawvg/playground/docs/outputs/example-tqpJV0xGD0Pv9aRs.webm)

First, a drawvg script renders horizontal rectangles with different shades of gray. Then, [boxblur](https://ffmpeg.org/ffmpeg-filters.html#boxblur) is used to soften the transition between rectangles. This image is used as the `xmap` input for [displace](https://ffmpeg.org/ffmpeg-filters.html#displace). The output below contains the intermediate images.

Output

[](https://ayosec.github.io/ffmpeg-drawvg/playground/docs/outputs/example-GbPAqEJVSyl7qQM0.webm)

`waves.vgs`

```
scalexy w (h / 20)

translate 0 (sin(4 * t))

repeat 20 {
    setvar T (mod((t - ts) + randomg(1), 0.75) / 0.75)
    setvar T (2 * abs(T - floor(T + 0.5)))

    setvar a (T / 16 + 0.45)
    setrgba a a a 1

    rect 0 i 1 1
    fill
}
```

`waves.filter`

```
[0] crop = iw-1, split [source0] [source1] ;

[source0]
    drawvg = rect 0 0 w h setcolor gray fill ,
    loop = -1 : 1 : 0 ,
    split
    [gray0] [gray1] ;

[gray0]
    drawvg = file=waves.vgs ,
    split
    [xmap_src0] [xmap_src1] ;

[xmap_src0]
    boxblur = h/40 ,
    split
    [xmap0] [xmap1] ;

[source1] [xmap1] [gray1]
    displace = mirror ,
    pad = iw*2+30 : ih*2+30 : 10:10
    [pad0] ;

[pad0] [xmap_src1] overlay = 10 : h+20 [pad1] ;

[pad1] [source1] overlay = w+20 : 10 : shortest=1 [pad2] ;

[pad2] [xmap0]
    overlay = w+20 : h+20 : shortest=1 ,
    drawtext = text='drawvg' : y=h-20 : x=20 : y_align=baseline : fontsize=32 : fontcolor=white ,
    drawtext = text='boxblur' : y=h-20 : x=w/2+20 : y_align=baseline : fontsize=32 : fontcolor=white ,
    drawtext = text='Source' : y=h/2-20 : x=w/2+20 : y_align=baseline : fontsize=32 : fontcolor=white ,
    format = yuv420p
```

Shell

```
ffmpeg \
    -an \
    -ss 5 -t 10 -i bigbuckbunny.mov \
    -/filter_complex waves.filter \
    -c:v libvpx-vp9 \
    output.webm
```

This example uses clips from the [Big Buck Bunny movie](https://peach.blender.org/download/), available under [CC BY 3.0](http://creativecommons.org/licenses/by/3.0/) license.
