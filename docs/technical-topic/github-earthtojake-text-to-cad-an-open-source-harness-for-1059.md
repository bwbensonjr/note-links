---
id: 1059
url: https://github.com/earthtojake/text-to-cad
title: 'GitHub - earthtojake/text-to-cad: An open source harness for generating CAD
  models · GitHub'
domain: github.com
source_date: '2026-05-04'
tags:
- github-repo
- ai
- llm
- python
summary: Text-to-CAD is an open-source framework that enables AI coding agents like
  Codex and Claude to generate 3D CAD models from text descriptions. It provides a
  complete workflow including model generation, export to multiple formats (STEP,
  STL, 3MF, etc.), inspection through CAD Explorer, and iterative editing capabilities.
  The project includes bundled skills for CAD design, robot descriptions, and motion
  planning, with local execution support and no backend requirements.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# GitHub - earthtojake/text-to-cad: An open source harness for generating CAD models · GitHub

[![Demo of the CAD skill generating and previewing CAD geometry](/earthtojake/text-to-cad/raw/main/assets/text-to-cad-demo.gif)](/earthtojake/text-to-cad/blob/main/assets/text-to-cad-demo.gif)
  

```
 ██████╗ █████╗ ██████╗       ███████╗██╗  ██╗██╗██╗     ██╗     ███████╗
██╔════╝██╔══██╗██╔══██╗      ██╔════╝██║ ██╔╝██║██║     ██║     ██╔════╝
██║     ███████║██║  ██║      ███████╗█████╔╝ ██║██║     ██║     ███████╗
██║     ██╔══██║██║  ██║      ╚════██║██╔═██╗ ██║██║     ██║     ╚════██║
╚██████╗██║  ██║██████╔╝      ███████║██║  ██╗██║███████╗███████╗███████║
 ╚═════╝╚═╝  ╚═╝╚═════╝       ╚══════╝╚═╝  ╚═╝╚═╝╚══════╝╚══════╝╚══════╝
```

A skills library for CAD, robotics, and hardware design agents

[Docs](https://www.cadskills.xyz) | [Demo](https://demo.cadskills.xyz)

[![GitHub stars](https://camo.githubusercontent.com/483a68b31c066e4c9f4e54d0c527bacaddd4a8b25e60a772a963e08ca0e9ca98/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f73746172732f6561727468746f6a616b652f746578742d746f2d6361643f7374796c653d666f722d7468652d6261646765266c6f676f3d676974687562266c6162656c3d5374617273)](https://github.com/earthtojake/text-to-cad/stargazers)
[![GitHub forks](https://camo.githubusercontent.com/822e15c663388490982f00583d6419201e6da9d6d9fcd6a61e66623f4305f62c/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f666f726b732f6561727468746f6a616b652f746578742d746f2d6361643f7374796c653d666f722d7468652d6261646765266c6f676f3d676974687562266c6162656c3d466f726b73)](https://github.com/earthtojake/text-to-cad/network/members)
[![License: MIT](https://camo.githubusercontent.com/1736263e7abccd5448e130c257555354792cbceae6b18535e86d6157f95b906f/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4c6963656e73652d4d49542d626c75653f7374796c653d666f722d7468652d6261646765)](/earthtojake/text-to-cad/blob/main/LICENSE)
[![Follow @earthtojake](https://camo.githubusercontent.com/71aa579d5b8c8577b320ff9f5ba4401e950412e03a09897badf083799bcce26f/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f466f6c6c6f772d2534306561727468746f6a616b652d3030303030303f7374796c653d666f722d7468652d6261646765266c6f676f3d78)](https://x.com/earthtojake)
[![Python](https://camo.githubusercontent.com/e4d90793a7a8a7dc0a59944095510b17c0a33c6951761f9b6512b71381c5f9eb/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f507974686f6e2d332e31312b2d3337373641423f7374796c653d666f722d7468652d6261646765266c6f676f3d707974686f6e266c6f676f436f6c6f723d7768697465)](/earthtojake/text-to-cad/blob/main/skills/cad/requirements.txt)
[![build123d](https://camo.githubusercontent.com/7336eebe51a647330ce7dc9c4cd23213e77389ac973d932e35d63273802a1e32/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6275696c64313233642d4341442d3030413637363f7374796c653d666f722d7468652d6261646765)](https://github.com/gumyr/build123d)
[![OCP](https://camo.githubusercontent.com/f0f53e2673073ec2d9166c6ddc746da473554e69409b44955465db89ab903eb8/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4f43502d4f70656e436173636164652d3246383045443f7374796c653d666f722d7468652d6261646765)](/earthtojake/text-to-cad/blob/main/skills/cad/requirements.txt)
[![STEP](https://camo.githubusercontent.com/0a61465822765abeff56654649fe9732428f8cf4bf70770bbec8f9a092798998/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f535445502d4578706f72742d3441353536383f7374796c653d666f722d7468652d6261646765)](/earthtojake/text-to-cad/blob/main/skills/cad/SKILL.md)
[![STL](https://camo.githubusercontent.com/9c794e0ce1620fdefa858964e9a0499a64beeccb67e1a3fed947832b109f3403/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f53544c2d4578706f72742d3441353536383f7374796c653d666f722d7468652d6261646765)](/earthtojake/text-to-cad/blob/main/skills/cad/SKILL.md)
[![3MF](https://camo.githubusercontent.com/b021f62a2c58f0bc30a171476deb9dceb7c7af51792c5a82f35d8b603dfed2d3/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f334d462d4578706f72742d3441353536383f7374796c653d666f722d7468652d6261646765)](/earthtojake/text-to-cad/blob/main/skills/cad/SKILL.md)
[![URDF](https://camo.githubusercontent.com/ffe00c8cbd22ba6caa8b8c79d45efd9e042564fef16fecf192ca18fbd151fcc2/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f555244462d526f626f74732d3642343643313f7374796c653d666f722d7468652d6261646765)](/earthtojake/text-to-cad/blob/main/skills/urdf/SKILL.md)
[![SDF](https://camo.githubusercontent.com/f216cd7540f471c8da4c7a3a18fe572fbaf529cbd9c4f146d30a6c257d366165/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f5344462d53696d756c6174696f6e2d3642343643313f7374796c653d666f722d7468652d6261646765)](/earthtojake/text-to-cad/blob/main/skills/sdf/SKILL.md)
[![SRDF](https://camo.githubusercontent.com/fcbc5f2ef571b479f906550fbc1dae78e00ce0d907c3a30638f1a0a642fe98be/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f535244462d4d6f76654974322d3642343643313f7374796c653d666f722d7468652d6261646765)](/earthtojake/text-to-cad/blob/main/skills/srdf/SKILL.md)

CAD Skills
==========

CAD Skills is a library of agent skills for generating, inspecting, sourcing,
slicing, and handing off CAD and robot-description artifacts from local project
files.

🧰 Skills
--------

Install the library to give agents focused workflows for CAD, fabrication,
robot description files, simulation, and local review.

| Skill | Summary | Source |
| --- | --- | --- |
| CAD | Creates and edits CAD models from plain-language or image requests, with STEP as the main output along with options to export to STL, 3MF and GLB. | [skills/cad](/earthtojake/text-to-cad/blob/main/skills/cad/SKILL.md) |
| CAD Viewer | Shows local browser previews for CAD, G-code, and robot files. | [skills/cad-viewer](/earthtojake/text-to-cad/blob/main/skills/cad-viewer/SKILL.md) |
| step.parts | Finds off-the-shelf STEP parts like screws, bearings, motors, and connectors. | [skills/step-parts](/earthtojake/text-to-cad/blob/main/skills/step-parts/SKILL.md) |
| URDF | Writes robot structure files with links, joints, limits, inertials, and meshes. | [skills/urdf](/earthtojake/text-to-cad/blob/main/skills/urdf/SKILL.md) |
| SRDF | Adds MoveIt planning groups, end effectors, poses, and collision rules to a URDF. | [skills/srdf](/earthtojake/text-to-cad/blob/main/skills/srdf/SKILL.md) |
| SDF | Creates simulator models and worlds with frames, physics, sensors, and lights. | [skills/sdf](/earthtojake/text-to-cad/blob/main/skills/sdf/SKILL.md) |
| SendCutSend | Checks DXF and STEP files before upload to SendCutSend. | [skills/sendcutsend](/earthtojake/text-to-cad/blob/main/skills/sendcutsend/SKILL.md) |
| G-code | Slices supported mesh files into validated, printer-profiled FDM `.gcode` with real slicer CLIs. | [skills/gcode](/earthtojake/text-to-cad/blob/main/skills/gcode/SKILL.md) |
| Bambu Labs | Dry-runs, uploads, and cautiously starts local Bambu Lab print jobs from validated `.gcode`. | [skills/bambu-labs](/earthtojake/text-to-cad/blob/main/skills/bambu-labs/SKILL.md) |

💻 Installation
--------------

For production use, install or clone from `main`; that branch contains the
generated skill/plugin outputs needed by provider installers.

### Skills

Install CAD Skills with the Skills CLI:

```
npx skills install earthtojake/text-to-cad
```

This is the preferred installation path. It installs the individual skills
directly for supported agents.

### Plugins

Provider-native plugin installs are also available for Codex and Claude Code:

```
# Codex
codex plugin marketplace add earthtojake/text-to-cad
codex plugin add cad@text-to-cad
```

```
# Claude Code
claude plugin marketplace add earthtojake/text-to-cad
claude plugin install cad@text-to-cad
```

Restart your agent if newly installed skills do not appear. For local
development, branch from `develop`, open PRs against `develop`, and use the symlink
workflow in [CONTRIBUTING.md](/earthtojake/text-to-cad/blob/main/CONTRIBUTING.md).

📸 Screenshots
-------------

|  |  |  |
| --- | --- | --- |
| [CAD skill demo showing generated geometry in CAD Viewer](/earthtojake/text-to-cad/blob/main/assets/text-to-cad-demo.gif) [**CAD**](/earthtojake/text-to-cad/blob/main/skills/cad/SKILL.md) | [URDF skill demo showing robot description output in CAD Viewer](/earthtojake/text-to-cad/blob/main/assets/urdf-demo.gif) [**URDF**](/earthtojake/text-to-cad/blob/main/skills/urdf/SKILL.md) | [SRDF MoveIt2 skill demo showing inverse kinematics in CAD Viewer](/earthtojake/text-to-cad/blob/main/assets/srdf-moveit2-demo.gif) [**SRDF / MoveIt2**](/earthtojake/text-to-cad/blob/main/skills/srdf/SKILL.md) |

🧪 Benchmarks
------------

The repo stores heavyweight assets in `assets/**` and `benchmarks/**` through Git LFS and excludes those trees from default LFS pulls so lightweight clones do not fetch GIF assets. Benchmark markdown remains normal Git for readable diffs. To hydrate only the benchmark assets locally, run:

```
git lfs pull --include="benchmarks/**"
```

| # | Target | Prompt | Output |
| --- | --- | --- | --- |
| 1 | [Rectangular calibration block with four holes](/earthtojake/text-to-cad/blob/main/benchmarks/01-rectangular-calibration-block.md) | Create a centered 100 x 60 x 20 mm block with four 8 mm vertical through-holes. Add only a 2 mm chamfer on the top outer perimeter. | [Rectangular calibration block orbit gif](/earthtojake/text-to-cad/blob/main/benchmarks/benchmark_01_rectangular_calibration_block.gif) |
| 2 | [Circular flange with bolt-hole pattern](/earthtojake/text-to-cad/blob/main/benchmarks/02-circular-flange.md) | Create an 80 mm diameter, 10 mm thick circular flange with a 30 mm central through-bore. Add six 6 mm through-holes on a 60 mm bolt circle and fillet the outside circular edges. | [Circular flange orbit gif](/earthtojake/text-to-cad/blob/main/benchmarks/benchmark_02_circular_flange.gif) |
| 3 | [L-bracket with gussets and two hole directions](/earthtojake/text-to-cad/blob/main/benchmarks/03-l-bracket.md) | Create an L-bracket from a base plate and rear vertical plate. Add vertical base holes, horizontal back-plate holes, two triangular gussets, and a filleted base/back transition. | [L-bracket orbit gif](/earthtojake/text-to-cad/blob/main/benchmarks/benchmark_03_l_bracket.gif) |
| 4 | [Stepped shaft with keyway](/earthtojake/text-to-cad/blob/main/benchmarks/04-stepped-shaft-keyway.md) | Create a 120 mm shaft along X with 20/30/20 mm diameter stepped sections. Add end chamfers and a shallow rectangular keyway on top of the middle section. | [Stepped shaft orbit gif](/earthtojake/text-to-cad/blob/main/benchmarks/benchmark_04_stepped_shaft_keyway.gif) |
| 5 | [Open-top electronics enclosure with bosses](/earthtojake/text-to-cad/blob/main/benchmarks/05-open-top-electronics-enclosure.md) | Create a hollow open-top enclosure with 3 mm walls and floor. Add four internal standoffs with centered blind holes and 2 mm outside vertical corner fillets. | [Open-top electronics enclosure orbit gif](/earthtojake/text-to-cad/blob/main/benchmarks/benchmark_05_open_top_electronics_enclosure.gif) |
| 6 | [Aerospace-style clevis bracket with lightening cutouts](/earthtojake/text-to-cad/blob/main/benchmarks/06-clevis-bracket-lightening-cutouts.md) | Create a symmetric clevis bracket with a base plate, two rounded lugs, base mounting holes, and a horizontal lug bore. Add triangular lightening cutouts, reinforcing ribs, and rounded transitions. | [Clevis bracket orbit gif](/earthtojake/text-to-cad/blob/main/benchmarks/benchmark_06_clevis_bracket_lightening_cutouts.gif) |
| 7 | [Radial-engine-style cylinder with cooling fins](/earthtojake/text-to-cad/blob/main/benchmarks/07-radial-engine-cylinder.md) | Create a vertical engine-cylinder form with a central barrel, 12 cooling fins, a base flange, and a top cap. Add a 35 degree angled spark-plug boss with a coaxial through-hole. | [Radial-engine-style cylinder orbit gif](/earthtojake/text-to-cad/blob/main/benchmarks/benchmark_07_radial_engine_cylinder.gif) |
| 8 | [Centrifugal impeller with backward-curved blades](/earthtojake/text-to-cad/blob/main/benchmarks/08-centrifugal-impeller.md) | Create a centrifugal impeller with a backplate, hub, and through-bore. Add 12 fused backward-curved blades sweeping about 45 degrees from root to tip. | [Centrifugal impeller orbit gif](/earthtojake/text-to-cad/blob/main/benchmarks/benchmark_08_centrifugal_impeller.gif) |
| 9 | [Spiral staircase with helical handrail](/earthtojake/text-to-cad/blob/main/benchmarks/09-spiral-staircase.md) | Create a miniature spiral staircase with a central column, base disk, and 20 rising wedge treads. Add a one-revolution helical handrail and vertical balusters at the tread outer ends. | [Spiral staircase orbit gif](/earthtojake/text-to-cad/blob/main/benchmarks/benchmark_09_spiral_staircase.gif) |
| 10 | [Simplified planetary gear stage](/earthtojake/text-to-cad/blob/main/benchmarks/10-planetary-gear-stage.md) | Create a flat planetary gear assembly with separate sun, planet, ring, carrier, and pin bodies. Use simplified trapezoidal teeth and place three planets around the sun on a 42 mm radius circle. | [Planetary gear stage orbit gif](/earthtojake/text-to-cad/blob/main/benchmarks/benchmark_10_planetary_gear_stage.gif) |

🛠️ Contributing
---------------

Development happens from the `develop` branch; open PRs against `develop`, not `main`.
For local contribution workflow, skill linking, and validation guidance, see
[CONTRIBUTING.md](/earthtojake/text-to-cad/blob/main/CONTRIBUTING.md).
