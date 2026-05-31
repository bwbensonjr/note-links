---
id: 761
url: https://maplibre.org/news/2026-01-23-mlt-release/
title: 'Announcing MapLibre Tile: a modern and efficient vector tile format | MapLibre'
domain: maplibre.org
source_date: '2026-01-26'
tags:
- web-dev
- database
- github-repo
summary: MapLibre has announced MapLibre Tile (MLT), a new vector tile format designed
  as a modern successor to Mapbox Vector Tile that addresses challenges with growing
  geospatial data volumes and next-generation source formats. MLT offers significant
  improvements including up to 6x better compression ratios, faster decoding performance
  through lightweight encodings, and support for 3D coordinates and complex data types,
  while maintaining feature parity with MVT 1. The format is available now for use
  in MapLibre GL JS and MapLibre Native, with demo tiles and conversion tools available
  for experimentation, and Planetiler supporting MLT generation for production use.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# Announcing MapLibre Tile: a modern and efficient vector tile format | MapLibre

Jan 23, 2026 Categories: Announcements Authors: Bart Louwers Ramya Ragupathy Today we are happy to announce MapLibre Tile (MLT), a new modern and efficient vector tile format. What is MapLibre Tile? MapLibre Tile (MLT) is a succesor to Mapbox Vector Tile (MVT) . It has been redesigned from the ground up to address the challenges of rapidly growing geospatial data volumes and complex next-generation geospatial source formats, as well as to leverage the capabilities of modern hardware and APIs. MLT is specifically designed for modern and next-generation graphics APIs to enable high-performance processing and rendering of large (planet-scale) 2D and 2.5 basemaps. This current implementation offers feature parity with MVT 1 while delivering on the following: Improved compression ratio : up to 6x on large tiles, based on a column-oriented layout with recursively applied (custom) lightweight encodings. This leads to reduced latency, storage, and egress costs and, in particular, improved cache utilization. Better decoding performance : fast, lightweight encodings that can be used in combination with SIMD/vectorization instructions. In addition, MLT was designed to support the following use cases in the future: Improved support for 3D coordinates , i.e. elevation. Improved processing performance , based on storage and in-memory formats that are specifically designed for modern graphics APIs, allowing for efficient processing on both CPU and GPU. The formats are designed to be loaded into GPU buffers with little or no additional processing. Support for linear referencing and m-values to efficiently support the upcoming next-generation source formats such as Overture Maps (GeoParquet). Support complex types , including nested properties, lists and maps. As with any MapLibre project, the future of MLT is decided by the needs of the community. There are a lot of exciting ideas for other future extensions and we welcome contributions to the project . For a more in-depth exploration of MLT have a look at the following slides , watch this talk or read this publication by MLT inventor Markus Tremmel. When can I use it? For the adventurous, the answer is: today . Both MapLibre GL JS and MapLibre Native now support MLT sources. You can use the new encoding property on sources in your style JSON with a value of mlt for MLT vector tile sources. To try out MLT, you have the following options: The easiest way to try out MLT is to use the MLT-based demotiles style . You can also try out the encoding server that converts existing (MVT-based) styles and vector tile sources to MLT on the fly. This is mostly a tool for development. To create tiles for production, you could use Planetiler , as the upcoming version will support generating MLTs. Refer to this page for a complete and up-to-date list of integrations and implementations. If you are an integrator working on supporting MLT, feel free to add your own project there. We would love to hear your experience with using MLT! Join the #maplibre-tile-format channel on our Slack or create an Issue or Discussion on the tile spec repo . Acknowledgements MapLibre Tile came to be thanks to a multi-year collaboration between academia, open source and enterprise. Thank you to everyone who was involved! We are very proud that our community can innovate like this. Special thanks go to Markus Tremmel for inventing the format, Yuri Astrakhan for spearheading the project, Tim Sylvester for the C++ implementation, Harel Mazor, Benedikt Vogl and Niklas Greindl for working on the JavaScript implementation. Also thanks to Microsoft and AWS for financing work on MLT. Footnotes One exception: unlike MVT, MLT does not support layers where a value in a column changes type from feature to feature. ↩
