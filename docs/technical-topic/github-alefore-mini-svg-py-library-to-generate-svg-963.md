---
id: 963
url: https://github.com/alefore/mini_svg/?tab=readme-ov-file
title: 'GitHub - alefore/mini_svg: Py library to generate SVG visualizations of scientific
  data · GitHub'
domain: github.com
source_date: '2026-03-27'
tags:
- github-repo
- python
- web-dev
- cli-tool
summary: 'mini_svg is a Python library that generates SVG visualizations for scientific
  data, supporting plot types including box plots, scatterplots, histograms, and line
  plots. It offers two main interfaces: a command-line tool that accepts JSON parameters
  and a Python API for in-process usage. The library is designed to be lightweight
  and simple for creating scientific data visualizations.'
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# GitHub - alefore/mini_svg: Py library to generate SVG visualizations of scientific data · GitHub

mini\_svg
=========

Simple py logic to generate SVG visualizations of scientific data
([example graphs](/alefore/mini_svg/blob/main/examples/README.md)).

The generated images tend to be significantly leaner
than what general (non-SVG specific) plotting software generates.
For example, a simple histogram is:

| Tool | Size | bzip2 Size |
| --- | --- | --- |
| gnuplot | 48K | 4.5K |
| matplotlib.pyplot | 49K | 7.9K |
| **mini\_svg** | 4.6K | 1.3K |

Plot types
----------

* [BoxPlot](/alefore/mini_svg/blob/main/docs/boxplot.md)
* [Scatterplot](/alefore/mini_svg/blob/main/docs/scatterplot.md)
* [Histogram](/alefore/mini_svg/blob/main/docs/histogram.md)
* [Lineplot](/alefore/mini_svg/blob/main/docs/lineplot.md)

Usage
-----

There's two main interfaces:

* As a command-line which receives parameters from a json file.
  See `.sh` files in [the examples directory](/alefore/mini_svg/blob/main/examples).
* From Python (in-process) through the functions exposed in `mini_svg`.
