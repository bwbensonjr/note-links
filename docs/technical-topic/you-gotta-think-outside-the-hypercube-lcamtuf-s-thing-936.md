---
id: 936
url: https://lcamtuf.substack.com/p/you-gotta-think-outside-the-hypercube
title: You gotta think outside the hypercube - lcamtuf’s thing
domain: lcamtuf.substack.com
source_date: '2026-03-14'
tags:
- tutorial
- academic-paper
- physics
summary: This article explains how to mathematically model and visualize a tesseract
  (four-dimensional hypercube) by building up from basic principles starting with
  a 2D square, then extending to a 3D cube, and finally to the 4D tesseract using
  constraint-based coordinate equations. The author then demonstrates how to rotate
  4D objects and project them onto a 2D computer screen using various projection methods
  like cavalier and cabinet projection, each with different visual trade-offs. The
  piece provides a comprehensive technical guide to understanding what tesseract visualizations
  mean and how they're actually generated.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# You gotta think outside the hypercube - lcamtuf’s thing

You gotta think outside the hypercube
=====================================

### A closer look at the tesseract and the ways we can render it on the screen.

Jan 26, 2026

33

5

1

Share

If you’re a nerd, you probably have encountered visualizations of a *tesseract:* a four-dimensional equivalent of a cube. Heck, various representations of the shape have made it into blockbuster sci-fi films, music videos, and more.

What might be harder to grasp is what these images mean or how they’re generated. You can find a handful of tesseract rendering demos on GitHub, but they all take different approaches, produce different results, and don’t really explain what’s going on.

In this article, we’ll take a look at the hypercube from first principles — and then, figure out how to map this beast to a computer screen.

### It’s hip to be square

To build a mathematical model of the hypercube, let’s start with a square. If we get it right, our approach will generalize to three dimensions and produce a cube; if it does, it ought to extend to the hyperspace too.

More specifically, we’ll try to model the *edges* of a square — i.e., the line segments that connect the vertices in the four corners. For our purposes, a see-through wireframe model will work better than a solid.

For a 2D square with dimensions 2*a×2a*, the horizontal edges can be described as a collection of points that satisfy two criteria:

\(\begin{array}{c}
|x| \leq a \\
|y| = a
\end{array}\)

In essence, we’re saying that we want to include points for which the *y* coordinate is equal to either *-a* (the lower edge) or *+a* (the upper edge); and where the *x* coordinate spans anywhere between *-a* and *+a*:

[![](https://substackcdn.com/image/fetch/$s_!alK2!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbb299481-ef67-4d13-baca-b0344fd8ce57_2000x1111.jpeg)](https://substackcdn.com/image/fetch/$s_!alK2!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbb299481-ef67-4d13-baca-b0344fd8ce57_2000x1111.jpeg)

*One half of a square.*

To construct the remaining vertical edges, we can just flip the criteria around, constraining *x* to one of two values and allowing *y* to span a range. This nets us the following combined formula:

\(\begin{array}{r l}
\textrm{Horizontal lines: } & |x| \leq a, \quad |y| = a \\
\textrm{Vertical lines: } & |x| = a, \quad |y| \leq a \\
\end{array}\)

The method is easy to generalize to a cube. We start by constructing a rectangle in the *x-y* plane using the earlier approach, except we add a third modulo constraint so that we end up with two images at the *-a* and *+a* offsets in the *z* axis:

\(\begin{array}{r l}
\textrm{Horizontal lines: } & |x| \leq a, \quad |y| = a, \quad |z| =a \\
\textrm{Vertical lines: } & |x| = a, \quad |y| \leq a, \quad |z| =a \\
\end{array}\)

What’s still missing are four edges oriented in the *z* direction that connect the corresponding corners of the two squares. We can add this with a third rule:

\(\begin{array}{r l}
\textrm{Horizontal lines: } & |x| \leq a, \quad |y| = a, \quad |z| =a \\
\textrm{Vertical lines: } & |x| = a, \quad |y| \leq a, \quad |z| =a \\
z \textrm{ lines: } & |x| = a, \quad |y| = a, \quad |z| \leq a \\
\end{array}\)

Note that each of these rules produces four line segments because there 22 possible combinations for the coordinates constrained by the equality relationship. For example, for horizontal lines, we can have the following pairs of *y* and *z* values: (*-a, -a)*, (*-a, +a)*, (*+a, -a)*, and (*+a, +a)*.

From here, the extension to the fourth dimension should be clear. I’m going to sensibly label the dimension 🌀; with this done, we just add a fourth constraint to each of the existing 3D rules and then add connecting segments in the fourth dimension:

\(\begin{array}{r l}
x \textrm{ lines: } & |x| \leq a, \quad |y| = a, \quad |z| =a \quad |🌀| = a \\
y \textrm{ lines: } & |x| = a, \quad |y| \leq a, \quad |z| =a \quad |🌀| = a \\
z \textrm{ lines: } & |x| = a, \quad |y| = a, \quad |z| \leq a \quad |🌀| = a \\
\textrm{🌀 lines: } & |x| = a, \quad |y| = a, \quad |z| = a \quad |🌀| \leq a
\end{array}\)

This time around, each rule nets us 23 = 8 line segments, so the tesseract has 4·8 = 32 edges. These edges connect 16 vertices.

### Defining rotations

Most visualization of the tesseract spin the figure around. This allows the shape to be examined from different angles and makes for some mind-bending visuals. But what does it mean to rotate an object in 4D?

In a two-dimensional space, there’s only one type of rotation; it transposes coordinates in the XY plane. The following demonstrates the effect of rotating a point originally placed on the *x* axis around the center of the coordinate system:

[![](https://substackcdn.com/image/fetch/$s_!TRvf!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5086b2ef-7009-4fdd-a620-da86a71bfac1_2000x1300.jpeg)](https://substackcdn.com/image/fetch/$s_!TRvf!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5086b2ef-7009-4fdd-a620-da86a71bfac1_2000x1300.jpeg)

*The trigonometric solution to the simplest case of XY rotation.*

From basic trigonometry, the new *x* coordinate of the rotated point is the adjacent of a right triangle with an angle *α* and a hypotenuse of *xorig*. The new *y* is the opposite of that same triangle. If we want to start with a non-zero *y* coordinate for the point, we need add a small tweak:

\(\begin{array}{c}
x\_{new} = x\_{orig} \cdot cos(\alpha) - y\_{orig} \cdot sin(\alpha) \\
y\_{new} = y\_{orig} \cdot cos(\alpha) + x\_{orig} \cdot sin(\alpha)
\end{array}\)

In three dimensions, we have a lot more freedom. We can obviously spin things around in the XY plane (around the *z* axis), XZ (around *y*), or in YZ (around *x*). It is also possible to dream up more complex rotations that touch all three coordinates at once, but they don’t add much value. They can be deconstructed into a sequence of planar rotations in XY, XZ, and YZ.

Given this observation, in four dimensions, we should probably still stick to the primitive of planar rotations that modify just two axes at a time. The only difference is that we get additional X🌀, Y🌀, and Z🌀 planes to use.

For ease of viewing and for consistency with 3D models, we’ll focus on spinning things in the XZ plane — a “turntable” animation:

\(\begin{array}{c}
x\_{new} = x\_{orig} \cdot cos(\alpha) + z\_{orig} \cdot sin(\alpha) \\
z\_{new} = z\_{orig} \cdot cos(\alpha) - x\_{orig} \cdot sin(\alpha)
\end{array}\)

That said, we’ll also pay a brief visit the Z🌀 rotation plane. It plays by similar rules:

\(\begin{array}{c}
z\_{new} = z\_{orig} \cdot cos(\alpha) - 🌀\_{orig} \cdot sin(\alpha) \\
🌀\_{new} = 🌀\_{orig} \cdot cos(\alpha) + z\_{orig} \cdot sin(\alpha)
\end{array}\)

### Projecting 4D to 2D

Our next challenge is figuring out how to project four-dimensional coordinates onto a two-dimensional drawing surface, such as a computer screen.

In standard geometries, Cartesian axes are orthogonal to each other — that is, there is a 90° rotation that can take you between any two dimensions. On a two-dimensional surface, we can only pull this off with two axes; that said, there are several imperfect ways to make do.

#### Cavalier projection

If we were to ask a random person to come up with a 3D-to-2D projection on the spot, they would probably suggest drawing the *z* axis as a diagonal line on a 2D plane, as shown below:

[![](https://substackcdn.com/image/fetch/$s_!9iRJ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fde4d7fcc-2d16-4081-83d4-bd779a54a9f1_2000x1300.jpeg)](https://substackcdn.com/image/fetch/$s_!9iRJ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fde4d7fcc-2d16-4081-83d4-bd779a54a9f1_2000x1300.jpeg)

*The cavalier projection.*

To convert the model-space *z* value to screen coordinates, we can use trigonometry to project the component onto the real *x* and *y* axes:

\(\begin{array}{c}
x\_{screen} = x\_{model} + z\_{model} \cdot cos(45^\circ) \\
y\_{screen} = y\_{model} + z\_{model} \cdot sin(45^\circ)
\end{array}\)

Alas, if you attempt this projection with a regular three-dimensional cube, you will immediately notice that it looks off:

[![](https://substackcdn.com/image/fetch/$s_!rzAm!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F876874d9-f4be-43e2-b5f4-7b92f47c83be_1080x1080.png)](https://substackcdn.com/image/fetch/$s_!rzAm!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F876874d9-f4be-43e2-b5f4-7b92f47c83be_1080x1080.png)

*The problem with cavalier.*

The viewer-facing edges in the XY plane are exactly the same length as the *z* edge; nevertheless, it’s hard to shake the impression that the dimensions are off and the cube is stretched.

#### Cabinet projection

To address this issue, we need to shorten the projected *z*-axis edges, crudely approximating the length contraction that we expect in real life. To do this, we divide the *z* component by an ad hoc scaling factor, typically 2:

\(\begin{array}{c}
x\_{screen} = x\_{model} + z\_{model} \cdot \frac{cos(45^\circ)}{2} \\
y\_{screen} = y\_{model} + z\_{model} \cdot \frac{sin(45^\circ)}{2}
\end{array}\)

The cabinet projection is ubiquitous in informal sketches and technical drawings, and it does look good at first blush. That said, consider the following video of a cube that is rotated in the XZ plane:

Note that the shape looks OK at first, but then gets weirdly squished near the rotation angle of 70°; this is because the projection gives us incorrect visual cues that the shape is facing us — the back edges appear to be tucked squarely behind the front — while in reality, the shape is still at an angle in relation to the viewer.

The root of the problem is that the axes are not oriented in a way that would be possible in real life. If we constructed a model of 3D axes out of sticks, the only way for the *z* axis to appear at a 45° angle — or indeed, to be visible at all — is if at least one of the other axes is not parallel to the camera plane*:*

[![](https://substackcdn.com/image/fetch/$s_!uwHh!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F026f5fbe-cbcd-424c-a6e6-4cc9a1e50239_2000x1281.jpeg)](https://substackcdn.com/image/fetch/$s_!uwHh!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F026f5fbe-cbcd-424c-a6e6-4cc9a1e50239_2000x1281.jpeg)

*An issue with the cabinet projection.*

#### Isometric projection

This brings us to the isometric projection — a physically-plausible arrangement that places the model axes 60° apart:

[![](https://substackcdn.com/image/fetch/$s_!tEXA!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F19fdb5e5-3e55-438f-8ba8-e56998cad6ba_2000x1264.jpeg)](https://substackcdn.com/image/fetch/$s_!tEXA!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F19fdb5e5-3e55-438f-8ba8-e56998cad6ba_2000x1264.jpeg)

*One of the possible isometric views.*

The math for this projection is still simple. The screen *x* coordinate is dictated by model *x* multiplied by *cos(*30°*)* — that’s the angle between the model *x* axis and the real one. The value is also influenced in the same way but with an opposite sign by the model *z* axis, so we get:

\(x\_{screen} = (x\_{model} - z\_{model}) \cdot cos(30^\circ) \)

Meanwhile, on the *y* side, we need to account for the projected sine component of *x* and *z:*

\(y\_{screen} = y\_{model} + (x\_{model} + z\_{model}) \cdot sin(30^\circ) \)

Both trigonometric expressions can be further divided by √2 if the goal is to match the model- and screen-lengths of a horizontal line drawn in the model XY plane and then rotated by 45° around the *y* axis. That said, it’s seldom a necessity.

The following video shows a cube rotated in the XZ plane in an isometric projection:

This looks great and it seems natural to extend the scheme to four dimensions simply by cramming another axis, giving us a progression of *x, y, z,* and 🌀 axes spaced 45° apart:

[![](https://substackcdn.com/image/fetch/$s_!xkVm!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F823c4b22-c1d4-4a11-9625-bf4ea63cc9ec_2000x1300.jpeg)](https://substackcdn.com/image/fetch/$s_!xkVm!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F823c4b22-c1d4-4a11-9625-bf4ea63cc9ec_2000x1300.jpeg)

*An extension of isometric projection to 4D?*

Yet, some readers might notice that with this modification, we’re back to the earlier “cavalier” scenario: our *x, y,* and *z* axes are now separated by an impossible angle of 45°. In other words, the projection should give us *something*, but it will distort some 3D shapes in undesirable ways.

Still, let’s keep going. In the new model, we calculate screen *x* as:

\(x\_{screen} = -🌀\_{model} + (x\_{model} - z\_{model}) \cdot cos(45^\circ)\)

The projected model *y* axis is orthogonal to to screen *x*, so it doesn’t appear in this formula. As for the *y* coordinate, we need:

\(y\_{screen} = y\_{model} + (x\_{model} + z\_{model}) \cdot sin(45^\circ)\)

As before, since the projected model 🌀 axis is orthogonal to screen *y*, it doesn’t appear in the second equation.

Let’s put this projection to real use. Here’s the video of a tesseract rotating in the XZ plane:

It looks pretty, but it isn’t particularly informative: the projection makes the object change shape in ways that seem difficult to parse. The shape appears to be intersecting itself, but it’s hard to pinpoint what’s what.

#### Rectilinear one-point perspective

A simpler but surprisingly powerful projection method is to keep model *x* and *y* in the same plane as the screen, but divide the values of these coordinates in proportion to the distance in *z*. This produces a familiar vanishing-point perspective:

A fairly natural extension of this technique to the fourth dimension is to divide the *x* and *y* coordinates twice: first by a *z-*dependent factor and then by a 🌀-dependent one. This nets probably the most recognizable visualization of a tesseract:

If you want food for thought, consider the real-world appearance of a wireframe 3D cube when its shadow from a nearby overhead light is cast onto a 2D surface:

[![](https://substackcdn.com/image/fetch/$s_!Punz!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F73d9c28a-f287-4b29-abc2-40d701fcdf60_1409x1012.jpeg)](https://substackcdn.com/image/fetch/$s_!Punz!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F73d9c28a-f287-4b29-abc2-40d701fcdf60_1409x1012.jpeg)

*It’s deja vu all over again.*

This both helps make some sense of the nested-cube visualization of the tesseract, and signals that our algorithm is directionally correct. That said, the approach we’ve taken is also a bit of a cop-out: by commingling model *z* and 🌀, we make these dimensions indistinguishable.

#### Fisheye perspective

At first blush, the tesseract visualization might look just like two nested 3D cubes connected in the corners. To reduce edge overlaps and better hint at the underlying shenanigans, we can switch to a curvilinear “fisheye” perspective, reminiscent of what you can see through a peephole or other low-quality, wide-angle lens. In this approach, point coordinates are reduced based on their Euclidean distance from a single reference point representing the camera. For a regular cube, we get:

But of course, we’re here to look at the tesseract:

The shading and the drawing order of the points is decided by the Euclidean distance to the viewing plane; this allows us to spot that the edges of the smaller, “inner” cube appear to pass behind the edges of the larger one:

[![](https://substackcdn.com/image/fetch/$s_!ngOa!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F925bb8c4-fbbc-4661-9bfb-ce76d7bce0ce_1080x1080.png)](https://substackcdn.com/image/fetch/$s_!ngOa!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F925bb8c4-fbbc-4661-9bfb-ce76d7bce0ce_1080x1080.png)

*Could it be…?*

Still, as noted earlier, the disappointing part of the mapping is that it commingles two dimensions; can we distinguish them better without ending up with a visual disaster?

#### Mixed isometric + vanishing point

Sort of?… Instead of trying to come up with a single projection for all four axes, we could always use a conventional isometric view for *x, y,* and *z,* and then use the vanishing-point approach to represent 🌀.

The result is a remarkably stable and easy-to-parse view of the tesseract when rotated in the YZ plane:

This also brings us to a somewhat less-correct rendering of the hypercube spinning in the *Z*🌀 plane that can be found on Wikipedia and in some YouTube videos. If we change screen depth calculations to only account for the *z* coordinate (i.e., completely ignore model 🌀), we obtain the following:

If you squint your eyes, this appears to show the tesseract passing through itself back-to-front as it rotates in the fourth dimension. I altered the proportions of the projection to make the effect easier to see.

---

*👉 For more articles about math, [visit this page](https://lcamtuf.substack.com/p/algorithms-and-math-trivia). In particular, you might enjoy:*

[![Folks, we have the best π](https://substackcdn.com/image/fetch/$s_!_Drc!,w_140,h_140,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7ada872d-41dd-495e-917a-2dfdf67d4859_2332x1224.png)

#### Folks, we have the best π

[lcamtuf](https://substack.com/profile/92541588-lcamtuf)

·

September 15, 2025

[Read full story](https://lcamtuf.substack.com/p/folks-we-have-the-best)](https://lcamtuf.substack.com/p/folks-we-have-the-best)

[![Approximation game](https://substackcdn.com/image/fetch/$s_!LOrW!,w_140,h_140,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd00a99e4-9662-4741-ab87-e875937230b7_2500x1250.png)

#### Approximation game

[lcamtuf](https://substack.com/profile/92541588-lcamtuf)

·

Feb 28

[Read full story](https://lcamtuf.substack.com/p/approximation-game)](https://lcamtuf.substack.com/p/approximation-game)

[![How many dimensions is this?](https://substackcdn.com/image/fetch/$s_!fjE0!,w_140,h_140,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F32743c32-71ca-45b1-b161-971d3bbedf10_1000x563.webp)

#### How many dimensions is this?

[lcamtuf](https://substack.com/profile/92541588-lcamtuf)

·

September 3, 2025

[Read full story](https://lcamtuf.substack.com/p/how-many-dimensions-is-this)](https://lcamtuf.substack.com/p/how-many-dimensions-is-this)

*I write well-researched, original articles about geek culture, electronic circuit design, algorithms, and more. If you like the content, please subscribe.*

33

5

1

Share
