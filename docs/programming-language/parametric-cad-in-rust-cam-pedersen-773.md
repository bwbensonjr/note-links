---
id: 773
url: https://campedersen.com/vcad
title: Parametric CAD in Rust - Cam Pedersen
domain: campedersen.com
source_date: '2026-01-27'
tags:
- rust
- cli-tool
- github-repo
summary: vcad is a parametric CAD library written in Rust that lets engineers design
  physical parts using code instead of clicking through GUI programs. Users create
  geometry by composing primitives (cubes, cylinders, etc.) with boolean operations,
  then export to STL or glTF formats—allowing rapid iteration by simply changing parameters
  and recompiling. The tool is designed for AI agents to generate parts automatically,
  with strong type safety and testing capabilities that traditional CAD files lack.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# Parametric CAD in Rust - Cam Pedersen

I keep designing physical parts for [our robots](https://muni.works). Motor mounts, sensor brackets, wheel hubs. Every time, the workflow is the same: open a GUI CAD program, click around for an hour, export an STL, realize the bolt pattern is 2mm off, repeat.

I wanted to write my parts the way I write firmware. In Rust. With types. With version control. With the ability to change one number and regenerate everything.

So I built [vcad](https://vcad.io).

```
cargo add vcad
```



The idea
--------

A part is just geometry with a name. You create primitives, combine them with boolean operations, and export. That's it.

```
use vcad::{centered_cube, centered_cylinder, bolt_pattern};

let plate = centered_cube("plate", 120.0, 80.0, 5.0);
let bore = centered_cylinder("bore", 15.0, 10.0, 64);
let bolts = bolt_pattern(6, 50.0, 4.5, 10.0, 32);

let part = plate - bore - bolts;
part.write_stl("plate.stl").unwrap();
```

That minus sign is a real boolean difference. `+` is union. `&` is intersection. Operator overloads make CSG feel like arithmetic.

![Rendered mounting plate with center bore and bolt pattern](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fplate.e621cd8a.png&w=3840&q=75&dpl=dpl_3VF4CwwpRfV4s8Ra1eFn2x7ZaWZq)

The plate above has a center bore, four corner mounting holes, and a six-bolt circle pattern. Twelve lines of code. One STL file. Done.

What you can build
------------------

The API is small on purpose. Primitives, booleans, transforms, patterns. That's the whole language. But it composes well.

An L-bracket with mounting holes in both faces:

```
let base = centered_cube("base", 60.0, 40.0, 4.0);
let wall = centered_cube("wall", 60.0, 4.0, 36.0)
    .translate(0.0, -18.0, 20.0);
let bracket = base + wall - base_holes - wall_holes;
```

![Rendered L-bracket with mounting holes](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fbracket.116b5ee4.png&w=3840&q=75&dpl=dpl_3VF4CwwpRfV4s8Ra1eFn2x7ZaWZq)

A flanged hub with a bolt circle:

```
let hub = centered_cylinder("hub", 15.0, 20.0, 64);
let flange = centered_cylinder("flange", 30.0, 4.0, 64)
    .translate(0.0, 0.0, -10.0);
let part = hub + flange - bore - bolt_pattern(6, 45.0, 3.0, 8.0, 32);
```

![Rendered flanged hub with bolt circle](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fhub.ebc63e06.png&w=3840&q=75&dpl=dpl_3VF4CwwpRfV4s8Ra1eFn2x7ZaWZq)

A radial vent pattern cut from a disc — one slot, repeated eight times:

```
let slot = centered_cube("slot", 15.0, 2.0, 10.0);
let vents = slot.circular_pattern(20.0, 8);
let panel = centered_cylinder("panel", 35.0, 3.0, 64) - vents;
```

![Rendered radial vent panel](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fvent.09f35e4c.png&w=3840&q=75&dpl=dpl_3VF4CwwpRfV4s8Ra1eFn2x7ZaWZq)

Every part here is parametric. Change the bolt count, the radius, the wall thickness — one number changes and the whole part regenerates. No clicking. No undo. Just recompile.

Multi-material export
---------------------

STL is fine for 3D printing, but it throws away all material information. For visualization, vcad exports glTF scenes with PBR materials defined in TOML:

```
let materials = Materials::parse(r#"
    [materials.body]
    color = [0.32, 0.72, 0.95]
    metallic = 0.1
    roughness = 0.5

    [materials.antenna]
    color = [0.95, 0.3, 0.35]
    metallic = 0.3
"#).unwrap();

let mut scene = Scene::new("mascot");
scene.add(body, "body");
scene.add(antenna_ball, "antenna");
export_scene_glb(&scene, &materials, "mascot.glb").unwrap();
```

![vcad mascot — a friendly robot built from CSG primitives](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fmascot.4a695c9b.png&w=3840&q=75&dpl=dpl_3VF4CwwpRfV4s8Ra1eFn2x7ZaWZq)

That's our mascot. Entirely CSG. A rounded cube intersected with a sphere for the body, spheres for eyes, cylinders for arms. Eight materials, seventeen parts, one GLB file.

Why Rust
--------

The geometry engine is [manifold](https://github.com/elalish/manifold), which guarantees watertight meshes from boolean operations. The Rust bindings give us zero-cost abstractions over the C++ core — the operator overloads compile down to direct manifold calls. No garbage collection pauses. No floating point surprises from a scripting layer.

But honestly, the main reason is the toolchain. `cargo test` runs 21 unit tests that verify volumes, surface areas, bounding boxes, and export round-trips. `cargo clippy` catches issues before they become parts with holes in the wrong place. Types prevent you from passing a radius where a diameter was expected.

CAD files *should* be code. Code has tests, reviews, diffs, and CI. An STL file has... bytes.

Built for agents
----------------

One thing I care about that most CAD tools don't: vcad is designed to be used by AI coding agents.

The [README](https://github.com/ecto/vcad) has full API tables, a cookbook with copy-pasteable recipes, and a section on [Blender MCP](https://github.com/ahujasid/blender-mcp) integration. An agent can read the docs, generate a part, export it, import it into Blender, position a camera, and render a preview — all in one conversation.

Every render in this post was made that way. Claude generated the geometry with vcad, imported each STL/GLB into Blender via MCP, set up studio lighting, and rendered to PNG. No human touched Blender.

The feedback loop is: describe a part → code generates → mesh exports → render previews → iterate. All in the terminal.

Try it
------

```
cargo add vcad
```

* **Docs:** [docs.rs/vcad](https://docs.rs/vcad)
* **Source:** [github.com/ecto/vcad](https://github.com/ecto/vcad)
* **Site:** [vcad.io](https://vcad.io)

It's MIT licensed. The first version is 0.1 — there's a lot more to build. Fillets, chamfers, threads, an interactive web GUI. But the core is solid: primitives, booleans, transforms, export. Everything you need to stop clicking and start typing.

Go make something.
