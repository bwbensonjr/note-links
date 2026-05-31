---
id: 485
url: https://www.dbreunig.com/2025/05/03/duckdb-is-the-most-impactful-geospatial-software-in-a-decade.html
title: DuckDB is Probably the Most Important Geospatial Software of the Last Decade
domain: www.dbreunig.com
source_date: '2025-05-04'
tags:
- database
- sql
summary: DuckDB's spatial extension has become one of the most important geospatial
  tools of the past decade by dramatically lowering the barrier to entry for working
  with geo data. By embedding geospatial capabilities into a generalist data tool
  with just a few lines of SQL, DuckDB has made spatial analysis accessible to casual
  users and data generalists who previously faced significant setup complexity, thereby
  expanding the geospatial audience and driving renewed interest in the field. The
  extension's key advantage is its elimination of transitive dependencies and seamless
  integration of standard open-source GIS packages, making geospatial workflows more
  stable and approachable than ever before.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# DuckDB is Probably the Most Important Geospatial Software of the Last Decade

May 3, 2025 GEO DUCKDB UX DuckDB is Probably the Most Important Geospatial Software of the Last Decade What happens when you embed geospatial capabilities in generalist data tools? More people engaging with geo data. I just returned from the inaugural Cloud-Native Geospatial conference . It was fantastic, I highly recommend you jump in if Jed and team organized another. One of the core questions discussed in the breakouts and in the halls was how to broaden the geospatial audience. How can we better communicate geo data’s utility, in all industries and domains? Many tactics and case studies were debated, but the one I kept coming back to is that of DuckDB. This chart could’ve been pretty bleak! Interest in “geospatial” (a term that functions well as a proxy for similar terms) declined and flatlined until late 2023 – right when DuckDB released their spatial extension . Now, all the standard caveats about correlation and causation apply, but I’m inclined to believe this chart. DuckDB lowers the barriers to working with geo data to two lines : install spatial ; load spatial ; If the extension is already installed, it’s only one line. Prior to this, getting up and running from a cold-start might’ve required installing or even compiling severall OSS packages, carefully noting path locations, standing up a specialized database… Enough work that a data generalist might not have bothered, or their IT department might not have supported it. With DuckDB spatial, it became possible for casual geospatial work to occur. All within SQL… And that makes the ecosystem bigger. As I discussed the spatial extension and this chart between sessions at the Cloud Native Geospatial conference, I wondered: would Overture Maps Foundation have the usage it has today without DuckDB spatial? Maybe…but probably not. I’m excited to help those spikes at the end of the chart continue upward. Update: There’s a good discussion going on Hacker News about this, with Max from the DuckDB team piping in with his thoughts : I think a big part is that duckdbs spatial extension provides a SQL interface to a whole suite of standard foss gis packages by statically bundling everything (including inlining the default PROJ database of coordinate projection systems into the binary) and providing it for multiple platforms (including WASM). I.E there are no transitive dependencies except libc. Yes, DuckDB does a whole lot more, vectorized larger-than-memory execution, columnar compressed storage and a ecosystem of other extensions that make it more than the sum of its parts. But while Ive been working hard on making the spatial extension more performant and more broadly useful (I designed a new geometry engine this year, and spatial join optimization just got merged on the dev-branch), the fact that you can e.g. convert too and from a myriad of different geospatial formats by utilizing GDAL, transforming through SQL, or pulling down the latest overture dump without having the whole workflow break just cause you updated QGIS has probably been the main killer feature for a lot of the early adopters. I’m very grateful for the complexity his team has taken on in order to remove it from the user’s experience.
