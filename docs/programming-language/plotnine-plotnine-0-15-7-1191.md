---
id: 1191
url: https://plotnine.org/
title: Plotnine – plotnine 0.15.7
domain: plotnine.org
source_date: '2026-06-23'
tags:
- python
- web-dev
- tutorial
summary: Plotnine is a Python data visualization package built on the grammar of graphics
  system, offering syntax similar to the popular R package ggplot2. It enables users
  to create visualizations efficiently—from simple single-line plots to fully customized
  publication-ready figures—with sensible defaults for elements like legends and color
  palettes, while allowing complete customization of every aspect including layers,
  themes, and styling. The package is demonstrated through examples using Anscombe's
  Quartet, showcasing how visualizations can be iteratively built and refined using
  declarative syntax.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# Plotnine – plotnine 0.15.7

From ad-hoc plots to publication-ready figures.
-----------------------------------------------

Turn your data into beautiful visualizations using the grammar of graphics.

![](./homepage/img/plotnine-logo-border.png)

[Get started](./guide/overview.html)

[API reference](./reference)

[Cheatsheet](https://github.com/rstudio/cheatsheets/blob/main/plotnine.pdf)

[![](gallery/img/large/anscombes-quartet.png)

![](gallery/img/small/anscombes-quartet.png)](gallery/anscombes-quartet.html)
[![](gallery/img/large/an-elaborate-range-plot.png)

![](gallery/img/small/an-elaborate-range-plot.png)](gallery/an-elaborate-range-plot.html)
[![](gallery/img/large/annotated-heatmap.png)

![](gallery/img/small/annotated-heatmap.png)](gallery/annotated-heatmap.html)
[![](gallery/img/large/coal-production.png)

![](gallery/img/small/coal-production.png)](gallery/coal-production.html)
[![](gallery/img/large/faithfully-waiting-to-erupt.png)

![](gallery/img/small/faithfully-waiting-to-erupt.png)](gallery/faithfully-waiting-to-erupt.html)
[![](gallery/img/large/pecking-orders-and-prime-cuts.png)

![](gallery/img/small/pecking-orders-and-prime-cuts.png)](gallery/pecking-orders-and-prime-cuts.html)
[![](gallery/img/large/infant-deaths-in-north-carolina.png)

![](gallery/img/small/infant-deaths-in-north-carolina.png)](gallery/infant-deaths-in-north-carolina.html)
[![](gallery/img/large/periodic-table.png)

![](gallery/img/small/periodic-table.png)](gallery/periodic-table.html)
[![](gallery/img/large/a-change-in-rank.png)

![](gallery/img/small/a-change-in-rank.png)](gallery/a-change-in-rank.html)
[![](gallery/img/large/temperature-over-the-year.png)

![](gallery/img/small/temperature-over-the-year.png)](gallery/temperature-over-the-year.html)
[![](gallery/img/large/the-plots-that-want-to-be-together.png)

![](gallery/img/small/the-plots-that-want-to-be-together.png)](gallery/the-plots-that-want-to-be-together.html)
[![](gallery/img/large/territories-of-westeros.png)

![](gallery/img/small/territories-of-westeros.png)](gallery/territories-of-westeros.html)
[![](gallery/img/large/bar-plot-with-2-variables.png)

![](gallery/img/small/bar-plot-with-2-variables.png)](gallery/bar-plot-with-2-variables.html)
[![](gallery/img/large/violins-boxes-points-and-lines.png)

![](gallery/img/small/violins-boxes-points-and-lines.png)](gallery/violins-boxes-points-and-lines.html)
[![](gallery/img/large/same-color-different-shade.png)

![](gallery/img/small/same-color-different-shade.png)](gallery/same-color-different-shade.html)
[![](gallery/img/large/please-i-want-some-more-labels.png)

![](gallery/img/small/please-i-want-some-more-labels.png)](gallery/please-i-want-some-more-labels.html)
[![](gallery/img/large/a-century-of-screams.png)

![](gallery/img/small/a-century-of-screams.png)](gallery/a-century-of-screams.html)
[![](gallery/img/large/weather-forecast.png)

![](gallery/img/small/weather-forecast.png)](gallery/weather-forecast.html)

![](./images/logo-512.png)

###

### A grammar of graphics for Python

Plotnine is a data visualization package for Python based on the grammar of graphics, a coherent system for describing and building graphs. The syntax is similar to [ggplot2](https://ggplot2.tidyverse.org), a widely successful R package.

Let’s explore Plotnine’s features and walk through a typical workflow by visualizing Anscombe’s Quartet—four small datasets with different distributions but nearly identical descriptive statistics. They’re perhaps the best argument for visualizing data. You can see the final result belowon the right.

![](./homepage/features/img/sneak.png)

###

### Get started quickly

With Plotnine you can create ad-hoc plots with just a single line of code.

```
from plotnine import * 
from plotnine.data import anscombe_quartet 

ggplot(anscombe_quartet, aes(x="x", y="y")) + geom_point()
```

Our data contains two continuous variables, so let’s start with a basic scatter plot.

It doesn’t make much sense just yet; we need a way to distinguish between the four datasets.

![](./homepage/features/img/start.png)

###

### Sensible defaults

Legends, labels, breaks, color palettes. Many elements are added automatically based on the data.

```
(
    ggplot(anscombe_quartet, aes("x", "y", color="dataset"))
    + geom_point()
)
```

By coloring each point according to the dataset it belongs to, the plot automatically gets a legend. The colors are chosen automatically as well. But don’t worry, as we’ll see later, everything can be adjusted.

It’s still rather messy, so let’s try a different approach.

![](./homepage/features/img/auto.png)

###

### Subset declaratively

Any data visualization can be repeated across multiple panels without writing a for loop.

```
(
    ggplot(anscombe_quartet, aes("x", "y", color="dataset"))
    + geom_point()
    + facet_wrap("dataset")
)
```

That’s better. The panels make the use of color redundant, so that’s something we need to fix.

![](./homepage/features/img/facet.png)

###

### Visualizations have layers

The data and the mapping of columns are inherited, but can be changed per layer.

```
(
    ggplot(anscombe_quartet, aes("x", "y", color="dataset"))
    + geom_point()
    + geom_smooth(method="lm", se=False, fullrange=True)
    + facet_wrap("dataset")
)
```

These scatter plots with trend lines clearly supports Anscombe’s point: that datasets with different distributions can have the same descriptive statistics.

When you’re doing exploratory data analysis, this plot might be good enough. But when you want to publish this, you may want to customize it further.

![](./homepage/features/img/layer.png)

###

### Override any default

Anything that you see, can be adjusted.

```
(
    ggplot(anscombe_quartet, aes("x", "y"))
    + geom_point(color="sienna", fill="darkorange", size=3)
    + geom_smooth(method="lm", se=False, fullrange=True,
                  color="steelblue", size=1)
    + facet_wrap("dataset")
    + scale_y_continuous(breaks=(4, 8, 12))
    + coord_fixed(xlim=(3, 22), ylim=(2, 14))
    + labs(title="Anscombe’s Quartet")
)
```

Here we change the sizes and colors, improve the breaks, and add a title.

![](./homepage/features/img/adjust.png)

###

### Plotnine goes to eleven

Finally, customize the theme to match your personal style or your organization’s brand.

```
(
    ggplot(anscombe_quartet, aes("x", "y"))
    + geom_point(color="sienna", fill="orange", size=3)
    + geom_smooth(method="lm", se=False, fullrange=True,
                  color="steelblue", size=1)
    + facet_wrap("dataset")
    + labs(title="Anscombe’s Quartet")
    + scale_y_continuous(breaks=(4, 8, 12))
    + coord_fixed(xlim=(3, 22), ylim=(2, 14)) 
    + theme_tufte(base_family="Futura", base_size=16)
    + theme(
        axis_line=element_line(color="#4d4d4d"),
        axis_ticks_major=element_line(color="#00000000"),
        axis_title=element_blank(),
        panel_spacing=0.09,
    )
)
```

There you have it, we started with a single line of code, and incrementally improved and customized our data visualization.

Curious how you can start creating these kinds of visualizations with your own data? In the next section we cover how to install Plotnine.

![](./homepage/features/img/final.png)

[Next: Installation](./guide/install.html)

##### Links

* [View on PyPI](https://pypi.org/project/plotnine/)
* [Source Code](https://github.com/has2k1/plotnine)
* [License](./license.html)

##### Developers

* Hassan Kibirige

##### Funded By

[![](images/posit-logo-2024-offwhite.svg)](https://posit.co)

The Open Source Data Science Company
