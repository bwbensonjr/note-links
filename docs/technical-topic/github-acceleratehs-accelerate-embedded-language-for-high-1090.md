---
id: 1090
url: https://github.com/AccelerateHS/accelerate
title: 'GitHub - AccelerateHS/accelerate: Embedded language for high-performance array
  computations · GitHub'
domain: github.com
source_date: '2026-05-16'
tags:
- github-repo
- haskell
- compilers
- distributed-systems
summary: Accelerate is an embedded language for Haskell that enables high-performance
  computing on multi-dimensional arrays through online compilation and execution on
  various architectures including GPUs and multicore CPUs. The library provides a
  functional programming interface for collective array operations like maps and reductions,
  with multiple backend options (LLVM, CUDA, PTX) and extensive add-on packages for
  specialized tasks like FFT, BLAS operations, and image processing. It is well-documented
  with numerous examples, academic publications, and an active community supporting
  its development and application to scientific computing problems.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# GitHub - AccelerateHS/accelerate: Embedded language for high-performance array computations · GitHub

[![henlo, my name is Theia](https://github.com/AccelerateHS/accelerate/raw/master/images/accelerate-logo-text-v.png?raw=true)](https://github.com/AccelerateHS/accelerate/raw/master/images/accelerate-logo-text-v.png?raw=true)

High-performance parallel arrays for Haskell
============================================

[![CI](https://github.com/tmcdonell/accelerate/actions/workflows/ci.yml/badge.svg)](https://github.com/tmcdonell/accelerate/actions/workflows/ci.yml)
[![Gitter](https://camo.githubusercontent.com/37b71e1ce183f4ee630f818196f982c56f4c223c1d829b4d6baa0c3a07fdcf9f/68747470733a2f2f696d672e736869656c64732e696f2f6769747465722f726f6f6d2f6e776a732f6e772e6a732e737667)](https://gitter.im/AccelerateHS/Lobby)
[![Hackage](https://camo.githubusercontent.com/49930a0fa1a1a1876e2d7797ab84e00b4f5b12306eb438b9987898b1597003fe/68747470733a2f2f696d672e736869656c64732e696f2f6861636b6167652f762f616363656c65726174652e737667)](https://hackage.haskell.org/package/accelerate)
[![Stackage LTS](https://camo.githubusercontent.com/ec2ad572c19dd7d91ecc5762f29084b815e522e911318aa4d34f10cf14886b1d/68747470733a2f2f737461636b6167652e6f72672f7061636b6167652f616363656c65726174652f62616467652f6c7473)](https://stackage.org/lts/package/accelerate)
[![Stackage Nightly](https://camo.githubusercontent.com/058812881714159e127414c4f392ac674cef5ff4e482f4f38d1ca5af29e828c8/68747470733a2f2f737461636b6167652e6f72672f7061636b6167652f616363656c65726174652f62616467652f6e696768746c79)](https://stackage.org/nightly/package/accelerate)

`Data.Array.Accelerate` defines an embedded language of array computations for high-performance computing in Haskell. Computations on multi-dimensional, regular arrays are expressed in the form of parameterised collective operations (such as maps, reductions, and permutations). These computations are online-compiled and executed on a range of architectures.

For more details, see our papers:

* [Accelerating Haskell Array Codes with Multicore GPUs](https://github.com/tmcdonell/tmcdonell.github.io/raw/master/papers/acc-cuda-damp2011.pdf)
* [Optimising Purely Functional GPU Programs](https://github.com/tmcdonell/tmcdonell.github.io/raw/master/papers/acc-optim-icfp2013.pdf) ([slides](https://speakerdeck.com/tmcdonell/optimising-purely-functional-gpu-programs))
* [Embedding Foreign Code](https://github.com/tmcdonell/tmcdonell.github.io/raw/master/papers/acc-ffi-padl2014.pdf)
* [Type-safe Runtime Code Generation: Accelerate to LLVM](https://github.com/tmcdonell/tmcdonell.github.io/raw/master/papers/acc-llvm-haskell2015.pdf) ([slides](https://speakerdeck.com/tmcdonell/type-safe-runtime-code-generation-accelerate-to-llvm)) ([video](https://www.youtube.com/watch?v=snXhXA5noVc))
* [Streaming Irregular Arrays](https://github.com/tmcdonell/tmcdonell.github.io/raw/master/papers/acc-seq2-haskell2017.pdf) ([video](https://www.youtube.com/watch?v=QIWSqp7AaNo))

There are also slides from some presentations on Accelerate:

* [Embedded Languages for High-Performance Computing in Haskell](https://speakerdeck.com/mchakravarty/embedded-languages-for-high-performance-computing-in-haskell)
* [GPGPU Programming in Haskell with Accelerate](https://speakerdeck.com/tmcdonell/gpgpu-programming-in-haskell-with-accelerate) ([video](http://youtu.be/ARqE4yT2Z0o)) ([workshop](https://speakerdeck.com/tmcdonell/gpgpu-programming-in-haskell-with-accelerate-workshop))

Chapter 6 of Simon Marlow's book [Parallel and Concurrent Programming in Haskell](http://chimera.labs.oreilly.com/books/1230000000929) contains a tutorial introduction to Accelerate.

[Trevor's PhD thesis](https://github.com/tmcdonell/tmcdonell.github.io/raw/master/papers/TrevorMcDonell_PhD_Thesis.pdf) details the design and implementation of frontend optimisations and CUDA backend.

**Table of Contents**

* [An Embedded Language for Accelerated Array Computations](#an-embedded-language-for-accelerated-array-computations)
  + [A simple example](#a-simple-example)
  + [Availability](#availability)
  + [Additional components](#additional-components)
  + [Requirements](#requirements)
  + [Documentation](#documentation)
  + [Examples](#examples)
  + [Who are we?](#who-are-we)
  + [Mailing list and contacts](#mailing-list-and-contacts)
  + [Citing Accelerate](#citing-accelerate)
  + [What's missing?](#whats-missing)

A simple example
----------------

As a simple example, consider the computation of a dot product of two vectors of single-precision floating-point numbers:

```
dotp :: Acc (Vector Float) -> Acc (Vector Float) -> Acc (Scalar Float)
dotp xs ys = fold (+) 0 (zipWith (*) xs ys)
```

Except for the type, this code is almost the same as the corresponding Haskell code on lists of floats. The types indicate that the computation may be online-compiled for performance; for example, using `Data.Array.Accelerate.LLVM.PTX.run` it may be on-the-fly off-loaded to a GPU.

Availability
------------

Package *Accelerate* is available from:

* Hackage: [accelerate](http://hackage.haskell.org/package/accelerate) - just add it to your cabal file
* GitHub: [AccelerateHS/accelerate](https://github.com/AccelerateHS/accelerate) - get the source with `git clone https://github.com/AccelerateHS/accelerate.git`

To install the Haskell toolchain try [GHCup](https://www.haskell.org/ghcup/).

Additional components
---------------------

The following supported add-ons are available as separate packages:

* [accelerate-llvm-native](https://github.com/AccelerateHS/accelerate-llvm): Backend targeting multicore CPUs
* [accelerate-llvm-ptx](https://github.com/AccelerateHS/accelerate-llvm): Backend targeting CUDA-enabled NVIDIA GPUs. Requires a GPU with compute capability 3.0 or greater (see the [table on Wikipedia](https://en.wikipedia.org/wiki/CUDA#Supported_GPUs))
* [accelerate-examples](https://github.com/AccelerateHS/accelerate-examples): Computational kernels and applications showcasing the use of Accelerate as well as a regression test suite (supporting function and performance testing)
* Conversion between various formats:
  + [accelerate-io](https://hackage.haskell.org/package/accelerate-io): For copying data directly between raw pointers
  + [accelerate-io-array](https://hackage.haskell.org/package/accelerate-io-array): Immutable arrays
  + [accelerate-io-bmp](https://hackage.haskell.org/package/accelerate-io-bmp): Uncompressed BMP image files
  + [accelerate-io-bytestring](https://hackage.haskell.org/package/accelerate-io-bytestring): Compact, immutable binary data
  + [accelerate-io-cereal](https://hackage.haskell.org/package/accelerate-io-cereal): Binary serialisation of arrays using [cereal](https://hackage.haskell.org/package/cereal)
  + [accelerate-io-JuicyPixels](https://hackage.haskell.org/package/accelerate-io-JuicyPixels): Images in various pixel formats
  + [accelerate-io-repa](https://hackage.haskell.org/package/accelerate-io-repa): Another Haskell library for high-performance parallel arrays
  + [accelerate-io-serialise](https://hackage.haskell.org/package/accelerate-io-serialise): Binary serialisation of arrays using [serialise](https://hackage.haskell.org/package/serialise)
  + [accelerate-io-vector](https://hackage.haskell.org/package/accelerate-io-vector): Efficient boxed and unboxed one-dimensional arrays
* [accelerate-fft](https://github.com/AccelerateHS/accelerate-fft): Fast Fourier transform implementation, with FFI bindings to optimised implementations
* [accelerate-blas](https://github.com/tmcdonell/accelerate-blas): BLAS and LAPACK operations, with FFI bindings to optimised implementations
* [accelerate-bignum](https://github.com/tmcdonell/accelerate-bignum): Fixed-width large integer arithmetic
* [colour-accelerate](https://github.com/tmcdonell/colour-accelerate): Colour representations in Accelerate (RGB, sRGB, HSV, and HSL)
* [containers-accelerate](http://hackage.haskell.org/package/containers-accelerate): Hashing-based container types
* [gloss-accelerate](https://github.com/tmcdonell/gloss-accelerate): Generate [gloss](https://hackage.haskell.org/package/gloss) pictures from Accelerate
* [gloss-raster-accelerate](https://github.com/tmcdonell/gloss-raster-accelerate): Parallel rendering of raster images and animations
* [hashable-accelerate](http://hackage.haskell.org/package/hashable-accelerate): A class for types which can be converted into a hash value
* [lens-accelerate](https://github.com/tmcdonell/lens-accelerate): [Lens](https://hackage.haskell.org/package/lens) operators for Accelerate types
* [linear-accelerate](https://github.com/tmcdonell/linear-accelerate): [Linear](https://hackage.haskell.org/package/linear) vector spaces in Accelerate
* [mwc-random-accelerate](https://github.com/tmcdonell/mwc-random-accelerate): Generate Accelerate arrays filled with high quality pseudorandom numbers
* [numeric-prelude-accelerate](https://github.com/tmcdonell/numeric-prelude-accelerate): Lifting the [numeric-prelude](https://hackage.haskell.org/package/numeric-prelude) to Accelerate
* [wigner-ville-accelerate](https://github.com/Haskell-mouse/wigner-ville-accelerate): Wigner-Ville time-frequency distribution.

These are all available on Hackage.

Documentation
-------------

* Haddock documentation is included and linked with the individual package releases on [Hackage](http://hackage.haskell.org/package/accelerate).

* The idea behind the HOAS (higher-order abstract syntax) to de-Bruijn conversion used in the library is [described separately](https://github.com/mchakravarty/hoas-conv).

Examples
--------

### accelerate-examples

The [accelerate-examples](https://github.com/AccelerateHS/accelerate-examples) package provides a range of computational kernels and a few complete applications. The examples include:

* An implementation of [canny edge detection](https://en.wikipedia.org/wiki/Canny_edge_detector)
* An interactive [mandelbrot set](https://en.wikipedia.org/wiki/Mandelbrot_set) generator
* An [N-body simulation](https://en.wikipedia.org/wiki/N-body) of gravitational attraction between solid particles
* An implementation of the [PageRank](https://en.wikipedia.org/wiki/Pagerank) algorithm
* A simple [ray-tracer](https://en.wikipedia.org/wiki/Ray_tracing)
* A particle based simulation of stable fluid flows
* A cellular automata simulation
* A "password recovery" tool, for dictionary lookup of MD5 hashes

To run these, either get the source from Hackage using `cabal get accelerate-examples` or clone the [git repository](https://github.com/AccelerateHS/accelerate-examples), then use `cabal run` on the individual executables.

[![Mandelbrot](https://camo.githubusercontent.com/73190f2bdabd88a497f7c1fefda34ea3b09e2146b8c1b05ed8e773ca8cc0531c/68747470733a2f2f692e696d6775722e636f6d2f3554627370316a2e6a7067 "accelerate-mandelbrot")](https://i.imgur.com/RgXRqsc.jpg)
[![Raytracer](https://camo.githubusercontent.com/b9153858e1d0b94f1d4eb43086eb79561e08615dc3d2198d7dcc4858b9139dbf/68747470733a2f2f692e696d6775722e636f6d2f376f68684b6d392e6a7067 "accelerate-ray")](https://i.imgur.com/ZNEGEJK.jpg)

### LULESH

[LULESH-accelerate](https://github.com/tmcdonell/lulesh-accelerate) is in implementation of the Livermore Unstructured Lagrangian Explicit Shock Hydrodynamics (LULESH) mini-app. [LULESH](https://codesign.llnl.gov/lulesh.php) represents a typical hydrodynamics code such as [ALE3D](https://wci.llnl.gov/simulation/computer-codes/ale3d), but is a highly simplified application, hard-coded to solve the Sedov blast problem on an unstructured hexahedron mesh.

[![LULESH mesh](https://camo.githubusercontent.com/1dfa69a6e089bb8c50fc0cc3b1aeac51031d869ec1dfe7193cd972dc9b8c1869/68747470733a2f2f692e696d6775722e636f6d2f62496b4f444b642e6a7067)](https://camo.githubusercontent.com/1dfa69a6e089bb8c50fc0cc3b1aeac51031d869ec1dfe7193cd972dc9b8c1869/68747470733a2f2f692e696d6775722e636f6d2f62496b4f444b642e6a7067)

### Additional examples

Accelerate users have also built some substantial applications of their own.
Please feel free to add your own examples!

* Jonathan Fraser, [GPUVAC](https://github.com/GeneralFusion/gpuvac): An explicit advection magnetohydrodynamics simulation
* David van Balen, [Sudokus](https://github.com/dpvanbalen/Sudokus): A sudoku solver
* Trevor L. McDonell, [lol-accelerate](https://github.com/tmcdonell/lol-accelerate): A backend to the Λ ○ λ ([Lol](https://hackage.haskell.org/package/lol)) library for ring-based lattice cryptography
* Henning Thielemann, [patch-image](http://hackage.haskell.org/package/patch-image): Combine a collage of overlapping images
* apunktbau, [bildpunkt](https://github.com/abau/bildpunkt): A ray-marching distance field renderer
* klarh, [hasdy](https://github.com/klarh/hasdy): Molecular dynamics in Haskell using Accelerate
* Alexandros Gremm used Accelerate as part of the [2014 CSCS summer school](http://user.cscs.ch/blog/2014/cscs_usi_summer_school_2014_30_june_10_july_2014_in_serpiano_tessin/index.html) ([code](https://github.com/agremm/cscs))

Who are we?
-----------

The Accelerate team (past and present) consists of:

* Manuel M T Chakravarty ([@mchakravarty](https://github.com/mchakravarty))
* Gabriele Keller ([@gckeller](https://github.com/gckeller))
* Trevor L. McDonell ([@tmcdonell](https://github.com/tmcdonell))
* Robert Clifton-Everest ([@robeverest](https://github.com/robeverest))
* Frederik M. Madsen ([@fmma](https://github.com/fmma))
* Ryan R. Newton ([@rrnewton](https://github.com/rrnewton))
* Joshua Meredith ([@JoshMeredith](https://github.com/JoshMeredith))
* Ben Lever ([@blever](https://github.com/blever))
* Sean Seefried ([@sseefried](https://github.com/sseefried))
* Ivo Gabe de Wolff ([@ivogabe](https://github.com/ivogabe))
* Tom Smeding ([@tomsmeding](https://github.com/tomsmeding))

The maintainer and principal developer of Accelerate is Trevor L.
McDonell [trevor.mcdonell@gmail.com](mailto:trevor.mcdonell@gmail.com).

Mailing list and contacts
-------------------------

* Mailing list: [`accelerate-haskell@googlegroups.com`](mailto:accelerate-haskell@googlegroups.com) (discussions on both use and development are welcome)
* Sign up for the mailing list at the [Accelerate Google Groups page](http://groups.google.com/group/accelerate-haskell)
* Bug reports and issues tracking: [GitHub project page](https://github.com/AccelerateHS/accelerate/issues)
* Chat with us on [gitter](https://gitter.im/AccelerateHS/Lobby)

Citing Accelerate
-----------------

If you use Accelerate for academic research, you are encouraged (though not
required) to cite the following papers:

* Manuel M. T. Chakravarty, Gabriele Keller, Sean Lee, Trevor L. McDonell, and Vinod Grover.
  [Accelerating Haskell Array Codes with Multicore GPUs](https://github.com/tmcdonell/tmcdonell.github.io/raw/master/papers/acc-cuda-damp2011.pdf).
  In *DAMP '11: Declarative Aspects of Multicore Programming*, ACM, 2011.
* Trevor L. McDonell, Manuel M. T. Chakravarty, Gabriele Keller, and Ben Lippmeier.
  [Optimising Purely Functional GPU Programs](https://github.com/tmcdonell/tmcdonell.github.io/raw/master/papers/acc-optim-icfp2013.pdf).
  In *ICFP '13: The 18th ACM SIGPLAN International Conference on Functional Programming*, ACM, 2013.
* Robert Clifton-Everest, Trevor L. McDonell, Manuel M. T. Chakravarty, and Gabriele Keller.
  [Embedding Foreign Code](https://github.com/tmcdonell/tmcdonell.github.io/raw/master/papers/acc-ffi-padl2014.pdf).
  In *PADL '14: The 16th International Symposium on Practical Aspects of Declarative Languages*, Springer-Verlag, LNCS, 2014.
* Trevor L. McDonell, Manuel M. T. Chakravarty, Vinod Grover, and Ryan R. Newton.
  [Type-safe Runtime Code Generation: Accelerate to LLVM](https://github.com/tmcdonell/tmcdonell.github.io/raw/master/papers/acc-llvm-haskell2015.pdf).
  In *Haskell '15: The 8th ACM SIGPLAN Symposium on Haskell*, ACM, 2015.
* Robert Clifton-Everest, Trevor L. McDonell, Manuel M. T. Chakravarty, and Gabriele Keller.
  [Streaming Irregular Arrays](https://github.com/tmcdonell/tmcdonell.github.io/raw/master/papers/acc-seq2-haskell2017.pdf).
  In Haskell '17: The 10th ACM SIGPLAN Symposium on Haskell, ACM, 2017.

Accelerate is primarily developed by academics, so citations matter a lot to us.
As an added benefit, you increase Accelerate's exposure and potential user (and
developer!) base, which is a benefit to all users of Accelerate. Thanks in advance!

What's missing?
---------------

Here is a list of features that are currently missing:

* Preliminary API (parts of the API may still change in subsequent releases)
* Many more features... contact us!
