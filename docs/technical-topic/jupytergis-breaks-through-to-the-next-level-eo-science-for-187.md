---
id: 187
url: https://eo4society.esa.int/2025/10/16/jupytergis-breaks-through-to-the-next-level/
title: JupyterGIS breaks through to the next level - eo science for society
domain: eo4society.esa.int
source_date: '2025-10-24'
tags:
- web-dev
- devops
- database
summary: JupyterGIS, a browser-based GIS platform launched in June 2024, has significantly
  advanced with major new features including a WebAssembly-powered GDAL processing
  toolbox for geospatial operations, enhanced vector tile support with symbology editing,
  and improved visualization capabilities with flexible colormaps and multiband imagery
  support. The platform now integrates a STAC browser for streamlined satellite data
  discovery, supports additional formats like GeoParquet and PMTiles, and offers a
  refined user interface with better map controls and automatic legend generation.
  These updates enable researchers and analysts to perform collaborative, real-time
  geospatial analysis and visualization directly in the browser without installation,
  with ongoing development planned for deeper QGIS integration and story mapping features.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# JupyterGIS breaks through to the next level - eo science for society

JupyterGIS breaks through to the next level
===========================================

[Data Infrastructure](https://eo4society.esa.int/category/tools-and-platforms/data-infrastructure/), [Toolboxes](https://eo4society.esa.int/category/tools-and-platforms/toolboxes/)
 October 16, 2025

Launched in June 2024, [JupyterGIS](https://eo4society.esa.int/projects/jupytergis/) was introduced as a collaborative, web-based GIS environment built on the JupyterLab framework. Its objective is to bring QGIS-inspired workflows into the browser, enabling real-time collaborative editing, seamless integration with notebooks, and support for core geospatial data formats.

When it was [first announced earlier this year](https://blog.jupyter.org/real-time-collaboration-and-collaborative-editing-for-gis-workflows-with-jupyter-and-qgis-d25dbe2832a6), JupyterGIS already delivered:

* Real-time collaborative editing (Google Docs-style)
* Visualisation of raster & vector data
* Symbology editing and spatio-temporal animations
* Programmatic map control via a Python API.

Thanks to contributions from the community and support from partner organizations, JupyterGIS has advanced significantly and now offers an expanded range of features for analysis, visualization, and collaboration.

**Enhanced vector tile capabilities**

Support for vector tiles has been strengthened, including full compatibility with the *pmtiles* format.

Other key updates include:

* An *identify tool* that inspects vector tiles to display features and associated properties.
* A *symbology panel* that applies graduated, categorized, and canonical symbology to vector tile layers.

These improvements enhance the interpretability and styling of geospatial datasets directly in the browser.

[![](https://eo4society.esa.int/wp-content/uploads/2025/10/screenshot-1-667x400.png)](https://eo4society.esa.int/wp-content/uploads/2025/10/screenshot-1.png)

The identify tool in action with a pmtiles vector dataset.

[![](https://eo4society.esa.int/wp-content/uploads/2025/10/screenshot-2-667x400.png)](https://eo4society.esa.int/wp-content/uploads/2025/10/screenshot-2.png)

The symbology panel in action, allowing for different notations.

**A new processing toolbox**

One of the most significant updates is a new browser-based processing toolbox powered by a WebAssembly (WASM) build of the Geospatial Data Abstraction Library (GDAL).

Available tools include:

* *Buffer*: computes a buffer around geometries of a vector dataset.
* *Convex Hull*: calculates the convex hull for each feature of an input layer.
* *Dissolve*: combines features of vector layers into new features
* *Bounding Boxes*: calculates the bounding box for each feature in an input layer.
* *Centroid*: creates a new layer with the centroids of the geometries of an input layer.
* *Concave Hull*: computes the concave hull for each feature of an input point layer.

This toolbox has been designed for extensibility, with a JSON schema that allows additional GDAL operations to be integrated in a straightforward manner.

[![](https://eo4society.esa.int/wp-content/uploads/2025/10/screenshot-3-667x400.png)](https://eo4society.esa.int/wp-content/uploads/2025/10/screenshot-3.png)

Using the processing tool to compute the convex hulls of geometries.

**Symbology enhancements**

Visualization of geospatial data has become more flexible and expressive through several enhancements:

* *Viridis* is now the default colormap, providing perceptually uniform visualization.
* *Multiband symbology* is now available for GeoTIFFs.
* *Canonical symbology* defined in GeoJSON files can be applied automatically.
* *Colormaps* can now be *reversed*, allowing greater flexibility for data interpretation and visualization.
* In the case of *point layers*, color and marker size can be styled independently, and bound to different data.

[![](https://eo4society.esa.int/wp-content/uploads/2025/10/screenshot-4-667x400.png)](https://eo4society.esa.int/wp-content/uploads/2025/10/screenshot-4.png)

Setting color and radius based on data.

**Integration with SpatioTemporal Asset Catalogs (STAC)**

A SpatioTemporal Asset Catalog (STAC) browser is now embedded into JupyterGIS, streamlining access to different data collections. Users can select specific platforms and sensors, choose data products and processing levels, and set temporal and spatial constraints.

It is now possible to search across multiple datasets simultaneously. Users can click on any result to add it directly as a layer to their JupyterGIS project. This creates a seamless workflow from data discovery to visualization, making it easier for researchers and analysts to find and integrate relevant satellite imagery and geospatial datasets into their Jupyter notebooks.

Currently, the STAC Browser only supports the Geodes STAC API but support for all STAC catalogs is under way.

[![](https://eo4society.esa.int/wp-content/uploads/2025/10/screenshot-5-667x400.png)](https://eo4society.esa.int/wp-content/uploads/2025/10/screenshot-5.png)

Browsing a STAC access catalog from JupyterGIS.

**Support for more data types**

The range of supported geospatial data formats is now broadened with *GeoParquet* and *PMTiles***,** enabling efficient columnar storage and fast analytical queries for GeoParquet, and highly compact, streaming-friendly vector tile delivery for PMTiles.

**User experience and interface improvements**

The interface has been refined for a smoother workflow:

* *Integrated control panels* (layer list, filters, layer properties, etc.), reducing back and forth between the JupyterLab side-panels and the JupyterGIS UI. It also improves the “single document” scenario, allowing it to interact with JupyterGIS controls when opening a GIS document from the classic Jupyter Notebook UI.
* An improved *toolbar design*, with cleaner icons and better usability.
* A new feature to center the map on your *current location*.
* *Map annotations* now link to the map: clicking an annotation automatically re-centers and zooms to the location.
* *Full-screen* mode support.

**Legends for vector layers**

JupyterGIS now automatically generates legends for vector layers, ensuring consistent interpretation:

* Legends are dynamically updated to reflect current symbology.
* Customizations such as reversed colormaps are preserved.

[![](https://eo4society.esa.int/wp-content/uploads/2025/10/screenshot-6-667x400.png)](https://eo4society.esa.int/wp-content/uploads/2025/10/screenshot-6.png)

Displaying legends in the layers panel.

**JupyterGIS tiler extension**

An extension for JupyterGIS enables the creation of JupyterGIS layers from *xarray variables* in Jupyter kernels, with support for lazy evaluation, bridging geospatial workflows with powerful array-based computation.

The package, called JupyterGIS-tiler, is available in GitHub [here](https://github.com/geojupyter/jupytergis-tiler) and can be installed from PyPI with *pip install jupytergis-tiler*.

**Looking ahead**

Development will continue to expand JupyterGIS in several directions:

* Extension of the GDAL-based processing toolbox.
* Deeper integration with QGIS and a richer Python API for automation.
* A Story Maps Editor and Viewer to enable interactive communication of geospatial information through text, imagery, and maps.

In the meantime, feel free to try JupyterGIS directly in your browser with [JupyterLite](https://jupytergis.readthedocs.io/en/latest/lite/lab/index.html), no installation required.

Opportunities for engagement also include:

* Checking out [documentation](https://jupytergis.readthedocs.io) for tutorials and the Python API.
* Discussions via the [GeoJupyter Zulip channel](https://geojupyter.org) or the bi-weekly GeoJupyter hackathon.
* Contributions to the development [repository](https://github.com/geojupyter/jupytergis).

The JupyterGIS community continues to grow, and active participation from researchers, developers, and educators worldwide is encouraged.

[platforms](https://eo4society.esa.int/tag/platforms/)

SHARE
