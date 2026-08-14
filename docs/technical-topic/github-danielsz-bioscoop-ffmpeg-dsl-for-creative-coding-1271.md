---
id: 1271
url: https://github.com/danielsz/bioscoop
title: 'GitHub - danielsz/bioscoop: FFmpeg DSL for creative coding · GitHub'
domain: github.com
source_date: '2026-08-11'
tags:
- github-repo
- lisp
- compilers
summary: Bioscoop is a Lisp-based DSL compiler that translates simplified Lisp syntax
  into FFmpeg filtergraphs, addressing the complexity and error-proneness of FFmpeg's
  native string-based syntax. It improves upon native FFmpeg by offering structural
  integrity through immutable data structures, composable architecture for reusable
  filter components, automatic label management, bidirectional transformation capabilities,
  and parametrization with iteration support. The tool enables creative video coding
  with enhanced maintainability, type safety, and the ability to generate complex
  filtergraphs programmatically—for example, a slideshow that would require 90 lines
  of FFmpeg syntax can be expressed in a few lines of Bioscoop code.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# GitHub - danielsz/bioscoop: FFmpeg DSL for creative coding · GitHub

[![https://clojars.org/com.github.danielsz/bioscoop/latest-version.svg](https://camo.githubusercontent.com/03dee5f2525da07879dda090d81d6a2c884962543e9d5c85f34ad5d4c058dbc6/68747470733a2f2f636c6f6a6172732e6f72672f636f6d2e6769746875622e64616e69656c737a2f62696f73636f6f702f6c61746573742d76657273696f6e2e737667)](https://camo.githubusercontent.com/03dee5f2525da07879dda090d81d6a2c884962543e9d5c85f34ad5d4c058dbc6/68747470733a2f2f636c6f6a6172732e6f72672f636f6d2e6769746875622e64616e69656c737a2f62696f73636f6f702f6c61746573742d76657273696f6e2e737667)

[![resources/logo.svg](/danielsz/bioscoop/raw/master/resources/logo.svg)](/danielsz/bioscoop/blob/master/resources/logo.svg)

This repository contains a language toolchain that processes a
simplified Lisp language and outputs FFmpeg’s filtergaphs.

From a notoriously complex and error-prone string-based syntax, the
filtergraph is reified into a first-class, composable unit. This in
turn enables (dramatic) improvements in creative freedom,
programmability, maintainability and reliability.

Creative coding with video
==========================

* [Quickstart for Clojurians](https://clojurecivitas.github.io/bioscoop/quickstart.html)
* [Documentation](https://danielsz.github.io/bioscoop/)
* [AST convergence](#ast-convergence)
* [Gallery](#gallery)
* [Roadmap](#roadmap)

[![](/danielsz/bioscoop/raw/master/gallery/itsallaboutfilters.jpeg)](/danielsz/bioscoop/blob/master/gallery/itsallaboutfilters.jpeg)

*Note*: This is not a wrapper for FFmpeg (or bindings). This is a language
solution for a language problem, ie. the excessive information density
of FFmpeg’s syntax.

Key Improvements Over Native FFmpeg Syntax
------------------------------------------

### **Structural Integrity Through Data-First Design**

**Problem**: FFmpeg filtergraphs are fragile string concatenations where a
single misplaced comma or bracket can cause cryptic failures.

**Solution**: Bioscoop represents filtergraphs as immutable data structures:

Instead of `"scale=1920:1080,overlay"`, users write:

```
(chain (scale {:width 1920 :height 1080})
       (overlay))
```

**Benefits**:

* **Type safety**: Parameters are validated before execution
* **Immutability**: Filtergraphs can be safely composed and transformed
* **Explicitness**: Parameter names are spelled out (compare and contrast
  with FFmpeg’s positional arguments).

### **Composable Architecture**

**Problem**: FFmpeg lacks native composition mechanisms, forcing
developers to manually manage complex filter concatenation.

**Solution**: Built-in composition protocol:

```
;; Seamless composition
(compose scale-graph overlay-graph crop-graph)
```

**Benefits**:

* **Modular design**: Complex pipelines built from simple components
* **Reusability**: Filtergraphs become first-class composable units
* **Testability**: Individual components can be tested in isolation

### **Decoupled Label Management**

**Problem**: FFmpeg’s label management is tightly coupled with
filtergraphs. Users have to manually label filtergraphs, it is
error-prone and difficult to debug.

**Solution**: Decoupling of labels and filtergraphs.

This is achieved internally by implementing filters as Clojure records
as the intermediate representation.

```
(defrecord Filter [name args input-labels output-labels])
```

User-facing syntax stays close the FFmpeg convention: input labels at
the left of a filterchain, output labels at the right.

```
;; This is equivalent: "[in]scale=1920:1080[scaled]"
[["in"] (scale {:width 1920 :height 1080}) ["out"]]
```

However, because filtergraphs are first-class, we can now write:

```
(defgraph scaled (scale {:with 1920 :height 1080})) ;; first-class filtergraph, independent of labels

(bioscoop [["in"] scaled ["out"]]) ;; attach labels to filtergraph
```

**Benefits**:

* **Decoupling:** Labels and filtergraphs can be handled separately
* **Automatic label generation**: No more manual label tracking
* **Label validation**: Prevents duplicate or missing labels
* **Metadata preservation**: Labels persist through transformations

### **Bidirectional Transformation**

**Problem**: FFmpeg filtergraphs are one-way - once created as strings,
they can’t be easily analyzed or modified.

**Solution**: Round-trip transformation capabilities:

```
;; Parse FFmpeg string to data structure
(def parsed (ffmpeg/parse "scale=1920:1080,overlay"))
;; Modify the data structure
(def modified (update-in parsed [:chains 0 :filters 0 :args] assoc :bioscoop.domain.specs.scale/width 800))
;; Render in our DSL
(to-dsl modified) "(chain (scale {:width 800, :height 1080}) (overlay))"
;; Render back to FFmpeg string
(to-ffmpeg modified) ; => "scale=width=800:height=1080,overlay"
```

**Benefits**:

* **Analysis**: Programmatically inspect and analyze existing filtergraphs
* **Transformation**: Modify filtergraphs without string manipulation
* **Migration**: Update old filtergraph syntax to new patterns

### Parameterization

In FFmpeg, filters take parameters. This is what makes them flexible,
expressive and powerful. However, those parameters need to be
hard-coded in the filtergraph expression. Not so with bioscoop.

```
(defn transition [duration offset i]
  (bioscoop [[(if (zero? i) (str "r" i) (str "s" i))] ;; logic in labels
             (xfade {:transition "fade" :duration duration :offset (+ i offset (* i offset))})
             [(str "t" (inc i))]]))
 
(to-ffmpeg (transition 4 5 9))
```

```
"[s9]xfade=transition=fade:duration=4:offset=59[t10]"
```

### Iteration

FFmpeg filtergraphs are static expressions. Every filter, every
connection, every label must be written out explicitly. There is no
mechanism in FFmpeg to express “apply this filter N times with varying
parameters” or “connect these N inputs in sequence”. The only
recourse is to generate the filtergraph string programmatically,
outside FFmpeg itself.

Bioscoop introduces `for` as a first-class construct of the language.
It produces a filtergraph by iterating over a range and merging the
results, all within the DSL itself.

```
(for [binding range] body...)
```

`range` is a sequence of positive integers. `body` is a DSL expression
evaluated repeatedly for each value of the binding, with the result
merged into a single filtergraph. All of Clojure’s arithmetic and
string functions are available inside the body.

The following example builds a slideshow of n images. Each image is
looped, then cross-faded into the next. In FFmpeg this would require
generating the filtergraph string by hand, with explicit labels for
every intermediate connection. In Bioscoop it is expressed directly:

```
(defn slideshow [n]
  (bioscoop
    (for [i (range 1 n)]
      [[(str i)] (loop {:loop 124 :size 1}) [(str "l" i)]])
    (for [i (range 1 n)]
      [[(if (= i 1) (str "v" i) (str "l" i))]
       (xfade {:transition "fade" :duration 1 :offset (+ (* i 4) 3)})
       [(str "v" i)]])))
```

```
"[1]loop=loop=124:size=1[l1];[2]loop=loop=124:size=1[l2];[3]loop=loop=124:size=1[l3];[4]loop=loop=124:size=1[l4];[5]loop=loop=124:size=1[l5];[6]loop=loop=124:size=1[l6];[7]loop=loop=124:size=1[l7];[8]loop=loop=124:size=1[l8];[9]loop=loop=124:size=1[l9];[v1]xfade=transition=fade:duration=1:offset=7[v1];[l2]xfade=transition=fade:duration=1:offset=11[v2];[l3]xfade=transition=fade:duration=1:offset=15[v3];[l4]xfade=transition=fade:duration=1:offset=19[v4];[l5]xfade=transition=fade:duration=1:offset=23[v5];[l6]xfade=transition=fade:duration=1:offset=27[v6];[l7]xfade=transition=fade:duration=1:offset=31[v7];[l8]xfade=transition=fade:duration=1:offset=35[v8];[l9]xfade=transition=fade:duration=1:offset=39[v9]"
```

A slideshow of ten images `(slideshow 10)` produces the
equivalent of ninety lines of hand-written FFmpeg filtergraph syntax.
Changing the number of images, the transition type, or the timing
requires changing a single argument.

Parameterized iteration composes naturally with the rest of the
language. Named graphs defined with `defgraph` can be used as loop
bodies. `let` bindings can compute values shared across iterations.
The loop variable is in scope for filter arguments, label expressions,
and any nested `for` form.

### **Spec-Driven Validation**

**Problem**: FFmpeg parameters are validated at runtime, often with
unclear error messages.

**Solution**: Values passed to the filters are validated through specs.

```
(s/def ::width (s/and int? pos?))
(s/def ::height (s/and int? pos?))
(s/def ::scale (s/keys :req-un [::width ::height]))

;; Validation happens before FFmpeg execution
```

**Benefits**:

* **Early error detection**: Catch invalid parameters before FFmpeg runs
* **Clear error messages**: Know exactly which parameter failed validation
* **Documentation**: Specs serve as living documentation for filter
  parameters (type help and the name of the filter to see the spec).

AST convergence
---------------

An IEEE Conference [paper](/danielsz/bioscoop/blob/master/paper/ast_convergence_paper.pdf) is available that expounds the concept. In a
nutshell, AST convergence is a technique to enable a single
transformation on the AST while processing multiple input
modalities. This is how Bioscoop manages to be an external DSL and an
internal one at the same time. It offers standalone compilation and
macro expansion without code duplication. This is achieved by having
the macro emitting the same parse tree than the parser.

1. **External DSL Path**: Text → Instaparse Parser → AST → `transform-ast`
2. **Internal DSL Path**: Clojure Forms → Macro → AST → `transform-ast`

In classic Lisp systems, external DSLs would typically use a separate
parser (like a PEG parser) while internal DSLs use macros that
directly generate target code. The key here is that both paths
converge on the same AST structure before the transformation phase.

Gallery
-------

The Association of Moving Image Archivists ([AMIA](https://amianet.org/)) provides Open Source
resources that support their mission. The following examples were
largely inspired by the [FFmpeg artschool](https://amiaopensource.github.io/ffmpeg-artschool/).

#### Cellular automata

[![gallery/cellauto.gif](/danielsz/bioscoop/raw/master/gallery/cellauto.gif)](/danielsz/bioscoop/blob/master/gallery/cellauto.gif)

FFmpeg syntax:

```
"cellauto=rule=110:start_full=false:stitch=true:size=1024x1024[cell];[0:v]format=pix_fmts=yuva420p[img];[cell][img]overlay"
```

Bioscoop program:

```
(require '[bioscoop.macro :refer [bioscoop defgraph]]
         '[bioscoop.built-in])

(defgraph cellular (cellauto {:rule 110 :start_full false :stitch true :size "1024x1024"}))

(defgraph presentation (compose [cellular ["cell"]]
                                [["0:v" ] (format {:pix_fmts "yuva420p"}) ["img"]]
                                [["cell"] ["img"] (overlay)]))

(def filtergraph #(to-ffmpeg presentation))
```

#### Blend

[![gallery/blend.gif](/danielsz/bioscoop/raw/master/gallery/blend.gif)](/danielsz/bioscoop/blob/master/gallery/blend.gif)

FFmpeg syntax:

```
"[1:v]format=gbrp10le[v1];[0:v]format=gbrp10le[v0];[v1][v0]scale2ref[v1][v0];[v0][v1]blend=all_mode=pinlight,format=yuv422p10le[v]"
```

Bioscoop program:

```
(require '[bioscoop.macro :refer [bioscoop defgraph]]
         '[bioscoop.built-in])

(defgraph formatting (format {:pix_fmts "gbrp10le"}))
(defgraph blending (chain (blend {:all_mode "pinlight"})
                          (format {:pix_fmts "yuv422p10le"})))

(def filtergraph #(to-ffmpeg (bioscoop (compose [["0:v"] formatting ["v0"]]
                                                [["1:v"] formatting ["v1"]]
                                                [["v1"] ["v0"] (scale2ref) ["s1"] ["s0"]]
                                                [["s0"] ["s1"] blending]))))
```

#### Bitplanes

[![gallery/jumpinjackflash.gif](/danielsz/bioscoop/raw/master/gallery/jumpinjackflash.gif)](/danielsz/bioscoop/blob/master/gallery/jumpinjackflash.gif)

Ffmpeg syntax:

```
"format=yuv420p10le|yuv422p10le|yuv444p10le|yuv440p10le,split=10[b0][b1][b2][b3][b4][b5][b6][b7][b8][b9];[b0]crop=iw/10:ih:(iw/10)*0:0,lutyuv=y=512:u=512:v=512:y=bitand(val\,pow(2\,10-1))*pow(2\,1)[b0c];[b1]crop=iw/10:ih:(iw/10)*1:0,lutyuv=y=512:u=512:v=512:y=bitand(val\,pow(2\,10-2))*pow(2\,2)[b1c];[b2]crop=iw/10:ih:(iw/10)*2:0,lutyuv=y=512:u=512:v=512:y=bitand(val\,pow(2\,10-3))*pow(2\,3)[b2c];[b3]crop=iw/10:ih:(iw/10)*3:0,lutyuv=y=512:u=512:v=512:y=bitand(val\,pow(2\,10-4))*pow(2\,4)[b3c];[b4]crop=iw/10:ih:(iw/10)*4:0,lutyuv=y=512:u=512:v=512:y=bitand(val\,pow(2\,10-5))*pow(2\,5)[b4c];[b5]crop=iw/10:ih:(iw/10)*5:0,lutyuv=y=512:u=512:v=512:y=bitand(val\,pow(2\,10-6))*pow(2\,6)[b5c];[b6]crop=iw/10:ih:(iw/10)*6:0,lutyuv=y=512:u=512:v=512:y=bitand(val\,pow(2\,10-7))*pow(2\,7)[b6c];[b7]crop=iw/10:ih:(iw/10)*7:0,lutyuv=y=512:u=512:v=512:y=bitand(val\,pow(2\,10-8))*pow(2\,8)[b7c]; [b8]crop=iw/10:ih:(iw/10)*8:0,lutyuv=y=512:u=512:v=512:y=bitand(val\,pow(2\,10-9))*pow(2\,9)[b8c];[b9]crop=iw/10:ih:(iw/10)*9:0,lutyuv=y=512:u=512:v=512:y=bitand(val\,pow(2\,10-10))*pow(2\,10)[b9c]; [b0c][b1c][b2c][b3c][b4c][b5c][b6c][b7c][b8c][b9c]hstack=10,format=yuv422p10le,drawgrid=w=iw/10:h=ih:t=2:c=cyan@1"
```

Bioscoop program:

```
(require '[bioscoop.macro :refer [bioscoop defgraph]]
         '[bioscoop.built-in])

(defn n-formatting [n]
  (bioscoop [(chain (format {:pix_fmts "yuv420p10le|yuv422p10le|yuv444p10le|yuv440p10le"})
                    (split {:outputs 10})) [(for [i n] (str "b" i))]]))

(defn n-stack [n]
  (bioscoop [[(for [i (range n)] (str "b" i "c"))]
             (chain (hstack {:inputs 10})
                    (format {:pix_fmts "yuv422p10le"})
                    (drawgrid {:width "iw/10" :height "ih" :thickness "2" :color "cyan@1"}))]))

(defn n-bitplane [n]
  (bioscoop (for [i (range n)]
              [[(str "b" i)] (chain (crop {:out_w "iw/10" :out_h "ih" :x (str "(iw/10)*" i) :y "0"})
                                    (lutyuv {:y (str "'bitand(val,pow(2,10-" (inc i) "))*pow(2," (inc i) ")'") :u "512" :v "512"}))
               [(str "b" i "c")]])))

(def filtergraph
  #(to-ffmpeg (bioscoop (let [n 10]
                          (compose (n-formatting n) (n-bitplane n) (n-stack n))))))
```

#### Lagfun

[![gallery/lagfun.gif](/danielsz/bioscoop/raw/master/gallery/lagfun.gif)](/danielsz/bioscoop/blob/master/gallery/lagfun.gif)

Ffmpeg syntax:

```
"format=gbrp10[formatted];[formatted]split[a][b];[a]lagfun=decay=.99:planes=1[a];[b]lagfun=decay=.98:planes=2[b];[a][b]blend=all_mode=screen:c0_opacity=.5:c1_opacity=.5,format=yuv422p10le[out]"
```

Bioscoop program:

```
(require '[bioscoop.macro :refer [bioscoop defgraph]]
         '[bioscoop.built-in])

(defgraph formatting (chain (format {:pix_fmts "gbrp10"})
                            (split {:outputs 2})) )

(defn n-fun [n]
  (bioscoop (for [i (range n)]
              [[(str "i" i)] (lagfun {:decay (double (/ (- 99 i) 100)) :planes (inc i)}) [(str "o" i )]])))


(defgraph blending (chain (blend {:all_mode "screen" :c0_opacity 0.5 :c1_opacity 0.6})
                          (format {:pix_fmts "yuv422p10le"})))

(def filtergraph #(to-ffmpeg (bioscoop (compose [formatting ["i0"] ["i1"]]
                                                (n-fun 2)
                                                [["o0"] ["o1"] blending]))))
```

*Note*: Instead of the top-level `defgraph`, Bioscoop also allows for local bindings with a `let`.

```
(def filtergraph #(to-ffmpeg
                   (bioscoop
                     (let [formatting (chain (format {:pix_fmts "gbrp10"})
                                             (split {:outputs 2}))
                           blending (chain (blend {:all_mode "screen" :c0_opacity 0.5 :c1_opacity 0.6})
                                           (format {:pix_fmts "yuv422p10le"}))]
                       (compose [formatting ["i0"] ["i1"]]
                                (n-fun 2)
                                [["o0"] ["o1"] blending])))))
```

### Published projects

If you have created something with Bioscoop, please send me a link to
your project for inclusion below.

#### Dance Me to the End of Love

Presentation of photography work with the Ken Burns effect. Click on
the image below to play a Youtube video.

[![Dance Me to the End of Love](https://camo.githubusercontent.com/109e7c4b5fe113b09efa7646ce7cf0152ec0d4921a1e1e434ed65ff4c0f92954/687474703a2f2f696d672e796f75747562652e636f6d2f76692f4357645a332d58683376512f302e6a7067)](http://www.youtube.com/watch?feature=player_embedded&v=CWdZ3-Xh3vQ)

###### Afor Gashum: Afifon (Kite)

Afor Gashum is a leftfield post-shoegaze/ post-punk band based in Tel
Aviv. From the forthcoming album Voices from Gaza, whose songs were
inspired by texts written by residents of Gaza under Israel’s attack.

[![Dance Me to the End of Love](https://camo.githubusercontent.com/3d1b83f5ddb0a608ad827473942e6a35b1df673b09d1744db5bf27965b14777b/687474703a2f2f696d672e796f75747562652e636f6d2f76692f466d62433630486944366b2f302e6a7067)](http://www.youtube.com/watch?feature=player_embedded&v=FmbC60HiD6k)

###### Mouth and Foot - Here Our Story Ends (Kan Sipurenu Tam)

The Mouth and Foot is an Israeli rock band, a kind of a “side project”
of The Top Hat Carriers band that survived after the breakup of the
parent band in 1992 and continues to operate. The band’s music
combines serious and complex songwriting in the spirit of nonsensical
recording, the use of cheap musical instruments and childish humor.
This original combination and sticking to a [set of rules](https://mouthonline.github.io/) created a
“cult” of loyal fans around the band.

[![Dance Me to the End of Love](https://camo.githubusercontent.com/65f2fcfaf96da8b6bdfbae4090be29fe38e84e05aa408d03f2a2d77b1ab198c7/687474703a2f2f696d672e796f75747562652e636f6d2f76692f475555347a71656c6559592f302e6a7067)](http://www.youtube.com/watch?feature=player_embedded&v=GUU4zqeleYY)

Roadmap
-------

While the language proper is feature-complete, no binary is shipping
yet (you can build it yourself). The `bioscoop` macro wraps the compiler
in a Clojure environment, and exposes the functionality in a REPL. If
you are familiar with Clojure, then your needs are met. If you are not
and wished you could work with the standalone compiler, please let me
know that you are interested. Please consider becoming a sponsor to
voice that interest. Thank you!

* ☑ Bioscoop language toolchain
* ☑ CLI for the standalone compiler (GraalVM binary)
* ☐ More FFmpeg filters
