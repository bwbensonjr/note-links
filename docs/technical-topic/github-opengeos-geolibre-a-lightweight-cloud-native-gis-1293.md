---
id: 1293
url: https://github.com/opengeos/GeoLibre
title: 'GitHub - opengeos/GeoLibre: A lightweight, cloud-native GIS platform for visualizing,
  exploring, and analyzing geospatial data. It runs in the web browser, on the desktop,
  on mobile, and inside Jupyter notebooks. · GitHub'
domain: github.com
source_date: '2026-08-20'
tags:
- github-repo
- web-dev
- database
- python
summary: GeoLibre is a free, open-source GIS platform that enables users to visualize,
  explore, and analyze geospatial data across multiple environments including web
  browsers, desktop applications, mobile devices, and Jupyter notebooks, while keeping
  data local and private. It features over 1,000 geoprocessing tools that run directly
  in the browser via WebAssembly, covering terrain analysis, hydrology, LiDAR processing,
  remote sensing, and vector analysis without requiring server installation or data
  transmission. Built with modern web technologies like React, MapLibre GL JS, and
  DuckDB-WASM Spatial, GeoLibre supports planetary mapping, 3D visualization, spatial
  SQL queries, and is available across Windows, macOS, Linux, iOS, and Android platforms.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# GitHub - opengeos/GeoLibre: A lightweight, cloud-native GIS platform for visualizing, exploring, and analyzing geospatial data. It runs in the web browser, on the desktop, on mobile, and inside Jupyter notebooks. · GitHub

GeoLibre
========

[![Launch GeoLibre Web](https://camo.githubusercontent.com/d2d7a2639fb0b3576cbcb74d558b433ce3062a16909e4b0e2a27e80ed1a5324b/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4c61756e63682d47656f4c696272652532305765622d677265656e2e737667)](https://web.geolibre.app/)
[![GeoLibre shared project](https://camo.githubusercontent.com/7ea0e58dee89f356fa43d746cd1b51a08b642e924820b496426ba714928fc132/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f47656f4c696272652d73686172652d677265656e2e737667)](https://share.geolibre.app)
[![GeoLibre plugins](https://camo.githubusercontent.com/f4d8f168b09a83d570abfa985dd9f510cfb29a92c1fe23f11b4a0bab1c082eae/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f47656f4c696272652d706c7567696e732d677265656e2e737667)](https://plugins.geolibre.app)
[![image](https://camo.githubusercontent.com/9c35ecae3576967b0e9ca52481edf948709dc9419b031a7d53a7b0dc155b25ba/68747470733a2f2f696d672e736869656c64732e696f2f707970692f762f67656f6c696272652e737667)](https://pypi.python.org/pypi/geolibre)
[![R package](https://camo.githubusercontent.com/e57db5d5dad38c51539f504e397d342e8348fae012c1f6bd33dad0fc38d4ad06/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f522d7061636b6167652d3237364443333f6c6f676f3d72266c6f676f436f6c6f723d7768697465)](https://r.geolibre.app/)
[![image](https://camo.githubusercontent.com/eff96fda6b2e0fff8cdf2978f89d61aa434bb98c00453ae23dd0aab8d1451633/68747470733a2f2f636f6c61622e72657365617263682e676f6f676c652e636f6d2f6173736574732f636f6c61622d62616467652e737667)](https://colab.research.google.com/github/opengeos/GeoLibre/blob/main/python/examples/getting-started.ipynb)
[![image](https://camo.githubusercontent.com/7162b23ef830765b0b5c7bab707641b5ad7e94b7512f5d986f5d3b8d815a07ff/68747470733a2f2f696d672e736869656c64732e696f2f636f6e64612f766e2f636f6e64612d666f7267652f67656f6c696272652e737667)](https://anaconda.org/conda-forge/geolibre)
[![Conda Recipe](https://camo.githubusercontent.com/6bfd95ccf30f0766422da22bd19f1715d6d4ffa4b15fb6fba44c92704388fe94/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f7265636970652d67656f6c696272652d677265656e2e737667)](https://github.com/conda-forge/geolibre-feedstock)
[![Microsoft Store](https://camo.githubusercontent.com/12e259e452a9e85c1eec1f93f1d305e7919d17ff931ac421cdda35ba8b1021dd/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4d6963726f736f667425323053746f72652d47656f4c696272652d3030373844343f6c6f676f3d77696e646f7773)](https://apps.microsoft.com/detail/9nwt67rv531x)
[![Mac App Store](https://camo.githubusercontent.com/41439366d17968f70a328f6160105dd0e2598f3a72730fff5d6956ad23d5dd54/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4d616325323041707025323053746f72652d47656f4c696272652d3044393646363f6c6f676f3d6170706c65266c6f676f436f6c6f723d7768697465)](https://apps.apple.com/app/geolibre-desktop/id6796848769)
[![App Store](https://camo.githubusercontent.com/c07ba65798d5227ef16b32481d556a6c2f8d0cdb67218e114af3d4a0e98b5e44/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f41707025323053746f72652d47656f4c696272652d3044393646363f6c6f676f3d61707073746f7265266c6f676f436f6c6f723d7768697465)](https://apps.apple.com/app/geolibre/id6796039674)
[![Google Play](https://camo.githubusercontent.com/ba26627b26f1e542dfba580def85bf164bc1023d658fdf16d75a960b7bf69b21/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f476f6f676c65253230506c61792d47656f4c696272652d3031383735463f6c6f676f3d676f6f676c65706c6179266c6f676f436f6c6f723d7768697465)](https://play.google.com/store/apps/details?id=org.geolibre.app)
[![Chrome Web Store](https://camo.githubusercontent.com/e047fed6cbb996f0f2bd76252bfd59d87f33311143284a740c9dbc6b1032ad42/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4368726f6d6525323057656225323053746f72652d47656f4c696272652d3432383546343f6c6f676f3d676f6f676c656368726f6d65266c6f676f436f6c6f723d7768697465)](https://chromewebstore.google.com/detail/open-data-in-geolibre/joinecgbfoldanidcoakpjgkbaceaooj)
[![AUR version](https://camo.githubusercontent.com/cd34223bef54da45c70f0bc1a17fc7a2ef98636a77dd844a26eda3936bc2194c/68747470733a2f2f696d672e736869656c64732e696f2f6175722f76657273696f6e2f67656f6c696272652d62696e3f6c6f676f3d617263686c696e7578266c6162656c3d415552)](https://aur.archlinux.org/packages/geolibre-bin)
[![FlatPark](https://camo.githubusercontent.com/5ff06607d3e21bd0599856d93941b0a06c78bfa81ae3581e8d823f38f3c20d22/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f466c61745061726b2d47656f4c696272652d3441393044393f6c6f676f3d666c617470616b)](https://flatpark.org/apps/app.geolibre.GeoLibre/)
[![image](https://camo.githubusercontent.com/fdf2982b9f5d7489dcf44570e714e3a15fce6253e0cc6b5aa61a075aac2ff71b/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4c6963656e73652d4d49542d79656c6c6f772e737667)](https://opensource.org/licenses/MIT)
[![DOI](https://camo.githubusercontent.com/4335515305e0f909a9ac4f4ff736119e5b5d6367f789ab25dafc7f2bb611f567/68747470733a2f2f7a656e6f646f2e6f72672f62616467652f444f492f31302e353238312f7a656e6f646f2e32303738353430302e737667)](https://doi.org/10.5281/zenodo.20785400)
[![Ask DeepWiki](https://camo.githubusercontent.com/0f5ae213ac378635adeb5d7f13cef055ad2f7d9a47b36de7b1c67dbe09f609ca/68747470733a2f2f6465657077696b692e636f6d2f62616467652e737667)](https://deepwiki.com/opengeos/GeoLibre)

A free and open-source, lightweight, cloud-native GIS platform for visualizing, exploring, and analyzing geospatial data. It runs everywhere you do, in the web browser, on the desktop, on mobile, and inside Jupyter notebooks, all while keeping your data local and private.

It also ships **1,000+ geoprocessing tools** that run *entirely in your browser* on WebAssembly — terrain, hydrology, LiDAR, remote sensing, and vector analysis with no server, no install, and no data ever leaving your machine.

GeoLibre is built with **Tauri v2**, **React**, **TypeScript**, **MapLibre GL JS**, **DuckDB-WASM Spatial**, and **deck.gl**. The same workspace runs as a native desktop app, native Android and iOS apps, in any modern web browser, and adapts responsively to mobile and small screens.

* **[Launch GeoLibre Web](https://web.geolibre.app/)** — the full app in your browser, nothing to install
* **[Download the desktop app](https://geolibre.app/downloads/)** — Windows, macOS, and Linux installers
* **[Get it on the Mac App Store](https://apps.apple.com/app/geolibre-desktop/id6796848769)** — the sandboxed macOS build
* **[Get it on the App Store](https://apps.apple.com/app/geolibre/id6796039674)** — the native iOS app for iPhone and iPad
* **[Get it on Google Play](https://play.google.com/store/apps/details?id=org.geolibre.app)** — the native Android app
* **[Get the Chrome extension](https://chromewebstore.google.com/detail/open-data-in-geolibre/joinecgbfoldanidcoakpjgkbaceaooj)** — open datasets you find on any webpage in GeoLibre
* **[Use the Python package](https://geolibre.app/python/)** — embed and control the full app in Jupyter notebooks
* **[Use the R package](https://r.geolibre.app/)** — build interactive maps in RStudio, Quarto, R Markdown, and Shiny
* **[1,000+ geoprocessing tools](https://geolibre.app/user-guide/processing/#whitebox-toolbox)** — the full toolbox, in the browser
* **[Get started](https://geolibre.app/getting-started/)** — install, run from source, and configure
* **[Features](https://geolibre.app/features/)** — the complete feature list

Demos
-----

**Click any screenshot to open it at full resolution, or any animation to play the full-quality video.**

### 3D Tiles

[![GeoLibre demo showing 3D Tiles rendered on a MapLibre map](https://camo.githubusercontent.com/a4ce5864f7f0c877b44194682659618f3af1218a45c6c51707396ba60ee18349/68747470733a2f2f6173736574732e67656f6c696272652e6170702f696d616765732f47656f4c696272652d64656d6f2e77656270)](https://assets.geolibre.app/images/GeoLibre-demo.webp)

[Open the live project](https://share.geolibre.app/giswqs/3d-tiles)

### NYC buildings and subways

Manhattan building footprints extruded in 3D and colored by construction era, with the MTA subway lines and stations on top and a legend generated automatically from the layers' symbology.

[![Manhattan buildings extruded in 3D and colored by construction era, with MTA subway lines and stations and an auto-generated legend](https://camo.githubusercontent.com/a974122a7c51b570fa3e81078f07043ad110af177ccaef953e1715462a25156d/68747470733a2f2f6173736574732e67656f6c696272652e6170702f696d616765732f6e79632d6275696c64696e67732e77656270)](https://assets.geolibre.app/images/nyc-buildings.webp)

The animation below runs the Time Slider along the buildings' construction year, from 1850 to 2025, so Manhattan fills in era by era. Click it to play the full-quality video.

[![Animation of Manhattan buildings appearing by construction year as the Time Slider advances from 1850 to 2025](https://camo.githubusercontent.com/098f838f756d14e8e72dfdfc14488d3f0ed9c11c88ec0c1dbeff7cf8b5dd50e9/68747470733a2f2f6173736574732e67656f6c696272652e6170702f64656d6f732f6e79632d6275696c64696e67732d6769662e676966)](https://assets.geolibre.app/demos/nyc-buildings.webm)

[Open the live project](https://share.geolibre.app/giswqs/nyc-buildings-and-subways)

### Planetary basemaps

GeoLibre is not limited to Earth. Planetary basemaps from OpenPlanetaryMap and USGS Astrogeology cover the Moon, Mars, Mercury, Venus, the Galilean moons (Io, Europa, Ganymede, Callisto), Titan, Pluto, and Charon, with a per-project ellipsoid so distance, area, and scale measurements match the body you are mapping. The deep-space starfield behind each globe comes from the Atmosphere Effects plugin.

|  |  |  |
| --- | --- | --- |
| [GeoLibre globe view of Earth over a starfield backdrop](https://assets.geolibre.app/images/earth.webp) | [GeoLibre globe view of the Moon over a starfield backdrop](https://assets.geolibre.app/images/moon.webp) | [GeoLibre globe view of Mars over a starfield backdrop](https://assets.geolibre.app/images/mars.webp) |
| **Earth** | **Moon** | **Mars** |
| [GeoLibre globe view of Mercury over a starfield backdrop](https://assets.geolibre.app/images/mercury.webp) | [GeoLibre globe view of Pluto over a starfield backdrop](https://assets.geolibre.app/images/pluto.webp) | [GeoLibre globe view of Venus over a starfield backdrop](https://assets.geolibre.app/images/venus.webp) |
| **Mercury** | **Pluto** | **Venus** |
| [GeoLibre globe view of Europa over a starfield backdrop](https://assets.geolibre.app/images/europa.webp) | [GeoLibre globe view of Callisto over a starfield backdrop](https://assets.geolibre.app/images/callisto.webp) | [GeoLibre globe view of Charon over a starfield backdrop](https://assets.geolibre.app/images/charon.webp) |
| **Europa** | **Callisto** | **Charon** |

Switch bodies from the planet switcher in the Layers panel. See [Demos](https://geolibre.app/demos/) for more.

### Video tutorials

* [GeoLibre 1.0: A Free, Open-Source Cloud-Native GIS That Runs Anywhere (Browser, Desktop & Jupyter)](https://youtu.be/87Cm0QagtxI)
* [Geoprocessing in the Browser: 700+ Free GIS Tools in GeoLibre, Zero Install](https://youtu.be/W32bIQO_nG8)
* [GeoLibre + GeoLens: A Modern GIS Stack for Self-Hosting Geospatial Data](https://youtu.be/kQqgrxXGd4o)

Geoprocessing: 1,000+ tools, zero install
-----------------------------------------

[![The GeoLibre Whitebox toolbox running locally with WebAssembly, listing the full catalog of 1,000+ tools with the Regularize Building Footprints tool selected](https://camo.githubusercontent.com/0a72f72b16a76a0a608d0626d5f7a0c3f28ce8773ce74010760603656f00d794/68747470733a2f2f6173736574732e67656f6c696272652e6170702f696d616765732f7768697465626f782e77656270)](https://assets.geolibre.app/images/whitebox.webp)

**Processing → Whitebox Toolbox** opens a toolbox of **1,000+ geoprocessing tools** that
execute in the browser through a WebAssembly runtime with native raster and
vector I/O. There is no Python sidecar to install and no server to call — the
tools, your data, and the results all stay on your machine, so the full toolbox
is available on [GeoLibre Web](https://web.geolibre.app/), on the desktop app,
and on Android alike.

The tools come from the [Whitebox Next Gen](https://github.com/opengeos/Whitebox-Next-Gen-ArcGIS)
suite plus GeoLibre's own WASM tools, and are browsable by category straight from
the Processing menu:

| Category | Tools | Examples |
| --- | --- | --- |
| **Vector** | 313 | overlays, buffers, joins, cleaning, topology, generalization |
| **Raster** | 256 | algebra, filters, reclassification, zonal and focal statistics |
| **Remote sensing** | 154 | spectral indices, band math, classification, change detection |
| **Hydrology** | 100 | flow accumulation, watersheds, stream networks, depression filling |
| **Terrain** | 99 | slope, aspect, hillshade, curvature, ruggedness, viewsheds |
| **LiDAR** | 65 | point-cloud filtering, ground classification, DEM/DSM generation |
| **Conversion** | 49 | format translation to cloud-native GeoParquet, PMTiles, and COG |
| **Network** | 26 | connectivity, cost distance, and routing analysis |
| **Projection** | 4 | reprojection for raster and vector data |

Any tool is deep-linkable with a `?tool=` URL parameter that preselects it and
pre-fills its form. See the [Processing Tools guide](https://geolibre.app/user-guide/processing/#whitebox-toolbox)
for details, and [Geoprocessing in the Browser](https://youtu.be/W32bIQO_nG8) for
a video walkthrough.

Documentation
-------------

Full documentation, including the User Guide and Tutorials, is published at
**[geolibre.app](https://geolibre.app)**.

* **[Getting Started](https://geolibre.app/getting-started/)** - use GeoLibre on the web, desktop, Android, iOS, or in Jupyter; run it from source; run it with Docker; and configure optional credentials.
* **[Features](https://geolibre.app/features/)** - the complete, feature-by-feature list of what GeoLibre can do today.
* **[Demos](https://geolibre.app/demos/)** - a visual tour: 3D Tiles, 3D city data, planetary basemaps, the SQL Workspace, and embeds.
* **[Downloads](https://geolibre.app/downloads/)** - installers and package managers for Windows, macOS, and Linux.
* **[User Guide](https://geolibre.app/user-guide/interface/)** - a feature-by-feature reference for the interface, adding data, layers, styling, the attribute table, map controls, processing, the SQL Workspace, data integrations, plugins, settings, and embedding.
* **[Tutorials](https://geolibre.app/tutorials/)** - hands-on, end-to-end workflows: your first map, cloud-native data, vector analysis, terrain analysis, spatial SQL, and sharing and embedding.
* **Reference**
  + [Architecture](/opengeos/GeoLibre/blob/main/docs/architecture.md)
  + [Android](/opengeos/GeoLibre/blob/main/docs/android.md)
  + [iOS](/opengeos/GeoLibre/blob/main/docs/ios.md)
  + [Project format](/opengeos/GeoLibre/blob/main/docs/project-format.md)
  + [Plugin API](/opengeos/GeoLibre/blob/main/docs/plugin-api.md)
  + [UI Profiles](/opengeos/GeoLibre/blob/main/docs/ui-profiles.md)
  + [Internationalization](/opengeos/GeoLibre/blob/main/docs/i18n.md)
  + [Python package (Jupyter)](/opengeos/GeoLibre/blob/main/docs/python.md)
  + [R package (RStudio, Quarto, and Shiny)](/opengeos/GeoLibre/blob/main/docs/r.md)
  + [Notebook Panel](/opengeos/GeoLibre/blob/main/docs/notebook.md)
  + [Roadmap](/opengeos/GeoLibre/blob/main/docs/roadmap.md)
  + [Contributing](/opengeos/GeoLibre/blob/main/docs/contributing.md)
  + [How to Cite](/opengeos/GeoLibre/blob/main/docs/citation.md)
  + [Become a Sponsor](/opengeos/GeoLibre/blob/main/docs/sponsor.md)

Contributions are welcome. See the [Contributing](/opengeos/GeoLibre/blob/main/docs/contributing.md) guide
for the development setup, repository layout, and quality gate.

Sponsor
-------

GeoLibre is free and open source, and stays that way. If it is useful to you or your team, sponsorship is the most direct way to keep development, hosting, and cross-platform distribution going.

* [**GitHub Sponsors**](https://github.com/sponsors/giswqs) - monthly or one-time, billed through your GitHub account.
* [**Buy Me a Coffee**](https://buymeacoffee.com/giswqs) - a quick one-off contribution, no account required.

See the [Become a Sponsor](https://geolibre.app/sponsor/) page for what sponsorship supports and for other, free ways to help.

Acknowledgements
----------------

GeoLibre is built on the free and open-source geospatial and web communities — including MapLibre GL JS, deck.gl, DuckDB-WASM Spatial, Turf.js, Tauri, React, and many more. See the full [Acknowledgements](https://geolibre.app/acknowledgements/) page for the complete list of projects and community contributors.

* The **Atmosphere Effects** plugin (deep-space backdrop, parallax starfield, comets, and the globe atmosphere halo) adapts the technique and visual design from [Leonel Dias](https://leoneljdias.github.io/)'s article [*Globe atmosphere, halo, and comets*](https://leoneljdias.github.io/posts/globe-atmosphere-halo-comets/) — the layered Canvas 2D approach, the halo gradient and "screen" blend, the limb-sampling that keeps the halo aligned under pitch, and the starfield/comet parameters.
* **Community contributors** — thanks to [**Ryanphoenix**](https://github.com/Ryanphoenix) for many valued contributions, including issue reports, feedback, and improvements.
* **Beta testers** — thanks to [**René van der Velde**](https://github.com/renevandervelde) (Netherlands) for early testing, detailed bug reports, and feature requests.

Citation
--------

If you use GeoLibre in your work, please cite it. GeoLibre is archived on [Zenodo](https://zenodo.org/), which mints a DOI for every release. The concept DOI below always resolves to the latest version.

[![DOI](https://camo.githubusercontent.com/4335515305e0f909a9ac4f4ff736119e5b5d6367f789ab25dafc7f2bb611f567/68747470733a2f2f7a656e6f646f2e6f72672f62616467652f444f492f31302e353238312f7a656e6f646f2e32303738353430302e737667)](https://doi.org/10.5281/zenodo.20785400)

> Wu, Q. (2026). GeoLibre: A lightweight, cloud-native GIS platform for visualizing, exploring, and analyzing geospatial data. Zenodo. <https://doi.org/10.5281/zenodo.20785400>

You can also use GitHub's **"Cite this repository"** button (which reads [`CITATION.cff`](/opengeos/GeoLibre/blob/main/CITATION.cff)) to copy a ready-made APA or BibTeX entry. See the [How to Cite](https://geolibre.app/citation/) page for more formats.

License
-------

[MIT](/opengeos/GeoLibre/blob/main/LICENSE)
