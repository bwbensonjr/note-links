---
id: 1359
url: https://dbtcharts.com/blog/charts-built-for-chat/
title: Charts built for Chat · dbt Charts
domain: dbtcharts.com
source_date: '2026-09-15'
tags:
- web-dev
- ai
- devops
- github-repo
summary: dbt Labs has open-sourced dbt Charts, a declarative YAML-based language for
  building dashboards that works seamlessly with AI agents and traditional development
  workflows. The tool addresses the gap between messy, uncontrolled AI-generated code
  and overly restrictive BI tool interfaces by putting charts into code, allowing
  them to be versioned, audited, and governed alongside data transformations in Git.
  Alongside the open-source language, dbt Charts.com is launching as a hosted platform
  offering hosting, access control, and conversational analytics capabilities built
  on top of the core language.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# Charts built for Chat · dbt Charts

[Blog](/blog/) ·
14 September 2026 · [Dave Fowler](https://thingsilearned.com/about/)

Charts built for Chat
=====================

We’re open sourcing [dbt Charts](https://github.com/dbt-labs/dbt-charts), a declarative language for dashboards, so that even the dashboards you build by chatting with an agent can be governed.

AI for data is here, and the long-promised self-serve analytics is finally
happening. Anyone with a data connection can chat a report into existence in
an afternoon, and the first results are impressive.

The frictions show up fast, though. By default an agent turns one simple report
into a pile of files: HTML, CSS, and JavaScript, a couple of chart libraries,
and a React or Streamlit app once it has to be live. Tracing a result back to
its source means following it through several languages and files, which is
slow for people to audit and costs the agent time and tokens on every change.

BI tools went the other way and bolted copilots onto their UI-first apps. That
keeps the AI on governed rails, but narrow ones: the agent can do only what the
UI exposes.

So today you choose between the messy freedom of code and the narrow control
of a BI tool.
We built a third option: [skip ahead](#charts-leave-the-bi-tool), or read on
for how BI got here.

Unbundling BI
-------------

As dbt Labs founder Tristan Handy wrote recently in
[BI’s Second Unbundling](https://roundup.getdbt.com/p/bis-second-unbundling):

> When I started in data, BI tools were full-stack. Everything happened inside
> one product: data ingestion, transformation, compute, caching, semantics,
> visualization, identity. The BI tool *was* the data stack. MicroStrategy,
> Cognos, etc: they’re not just visualization tools, they’re integrated data
> platforms.
>
> Then the modern data stack happened. From ~2015 to 2022, the infrastructure
> layers of that BI bundle got pulled out and turned into purpose-built
> infrastructure. Compute went to the Big 5. Ingestion went to Fivetran.
> Transformation went to dbt. The BI tool was left with: visualization,
> interactive analytical interfaces, semantic definitions (sometimes!),
> identity and access management, and web hosting.

1. <
2. 2
3. 0
4. 12
5. 01234567890123456

1. Warehousing
   Big 5
2. E
   L
   T
   Extract
   Load
   Transform

BI
everything else

What that unbundling left behind is the BI tool we know today, and charts
are its biggest piece. They stayed in the UI for good reason: for most people, clicking is quicker than writing YAML. But more and more charts won’t be made by
people. As the front end and user of everything becomes increasingly a chat agent, this
preference flips. Agents are fluent in code, SQL, and Git, and clumsy in someone
else’s UI. So charts need to move to where agents work: into code.

Charts leave the BI tool
------------------------

Today we’re taking the next step in unbundling BI: we’re open sourcing
[dbt Charts](https://github.com/dbt-labs/dbt-charts), which takes charts out of
the BI tool and puts them in code, specifically a new structured YAML language
that can declare a full interactive dashboard in one auditable YAML file. Chat
freely with an agent, and what it makes has the freedom of code while staying
easy to read.

2026.8

1. Warehousing
   Big 5
2. E
   L
   T
   Extract
   Load
   Transform
3. New
   C
   Chart

BI
a few bits

In dbt Charts, SQL remains the language for declaring WHAT data you want to see,
and we wrap that in YAML to declare HOW you want to see it.

We’ve spent a long time distilling the language to a few core, extensible
elements: deep in what they can express, easy to organize and read. The YAML
wraps more than SQL. Markdown carries the prose, and Jinja, as in dbt, carries
variables and macros.

Here’s a small example: one variable (a UI filter), one query and one chart.

```
variables:
  status:
    column: main.documents.status

queries:
  doc_growth: |
    SELECT DATE_TRUNC('month', created_at) AS month,
           SUM(COUNT(*)) OVER (ORDER BY month)
             AS num_docs
    FROM main.documents
    WHERE {{ filter('status', status) }}
    GROUP BY 1

charts:
  growth:
    title: Documents created, all time
    type: area
    query: doc_growth
    x: month
    y: num_docs

rows:
  - growth
```

![Documents created, all time: an area chart that climbs from 184 to 58,440, rendered from the board above](/assets/img/blog/documents-growth.svg?v=6a2812b1ec8a6c6df5e1e606787cddf238c495be90c46b7fcd3ca79387e50133)

That file is the whole board. The CLI renders any board file to static SVG,
or to HTML, PNG, PDF, and even the terminal, on your laptop or in CI, and
serves a folder of them as a site:

```
dct render charts/documents.yml --format svg   # or html, png, pdf, terminal
dct serve
```

Those few elements go deep: over 1,100 config options today, across
[sixteen chart types](https://docs.dbtcharts.com/charts/extensibility/) and the
[composed charts](https://docs.dbtcharts.com/charts/extensibility/#composed-charts)
built from them. And like any good language, it can express complex layouts
and visuals.

You rarely set those options by hand. Styles cascade: a chart inherits from its
board, the board from its theme, and a theme is one line to switch. A board can
also `extends:` another board, so a house style or a standard report is written
once and inherited everywhere. Boards stay short, and theming stays cheap.

[![A complete commercial performance board with KPIs, bars, a donut, a line chart, and a table](/assets/img/home/growth-review.svg)](/assets/img/home/growth-review.svg)

*A complete dbt Charts board, rendered from one easy-to-read YAML file.*

Deep integration with dbt
-------------------------

You don’t have to use dbt Charts with a dbt project, but when you do, a lot
unlocks. The chart layer sits directly on the transform layer, and the deeper
the integration, the easier it is to change both.

With dbt Charts, your `charts/` directory lives next to your `models/` in the
same Git repo, so a change to a model and its charts ships on one branch,
through one CI run, and breaks before it reaches production.

```
your_dbt_project/
  .git/
  dbt_project.yml
  models/
  charts/          # new folder in a dbt repo for your dashboards
    revenue.yml
```

Queries reach models through `ref()`, resolved from your manifest, so a renamed
model or a missing column fails the pull request that broke it,
before `dbt run` rebuilds the warehouse:

```
dbt parse && dct validate charts/
```

Support for the dbt Semantic Layer is planned, so a board can use a metric as
the project defines it instead of restating its SQL. Follow
[dbt-labs/dbt-charts#1](https://github.com/dbt-labs/dbt-charts/issues/1).

Built for chat
--------------

Agents can be quite blind, and they do best with a tight feedback loop.
dbt Charts gives them one: strict validation of both the YAML and the SQL, and
an extensive set of visualization checks that flag problems before anyone sees
the board:

```
$ dct render charts/revenue.yml
WARN-BAR-BAND-WIDTH-TOO-NARROW
182 bands x 2 series across 640px
Fix: roll up to a coarser grain.

WARN-TABLE-COLUMNS-OVERFLOW
Table needs 980px but only 640px is available.
Fix: drop columns or widen the slot.
```

A beautiful, cohesive reporting system
--------------------------------------

We hope dbt Charts, like dbt before it, becomes the open standard language for
its layer of the data stack. We designed it for a future where humans and AI
build together, and we wanted it to look like that future, not like another
dashboard grid. We recruited [RJ Andrews](https://infowetrust.com/about), a
data graphic designer, author, and historian, to design the charts. His grasp of the craft’s history is what makes the result feel new: it reaches past the dashboard era to
what charts looked like when people drew them with care.

Many tools cheat with cards and boxes that fake alignment at the cost of visual
noise and lost space. We worked out the spacing, sizing, and layout of every
chart, on its own and next to its neighbors.

![A dbt Charts board: showcase/general/dundersign-commercial-finance](/assets/img/language/wall-showcase-general-dundersign-commercial-finance.svg)![A dbt Charts board: showcase/general/one-dataset-nine-ways](/assets/img/language/wall-showcase-general-one-dataset-nine-ways.svg)![A dbt Charts board: showcase/boards/dundersign-support-operations](/assets/img/language/wall-showcase-boards-dundersign-support-operations.svg)![A dbt Charts board: showcase/boards/quarterly-business-review](/assets/img/language/wall-showcase-boards-quarterly-business-review.svg)![A dbt Charts board: showcase/charts/composed-chart-shapes](/assets/img/language/wall-showcase-charts-composed-chart-shapes.svg)

The result is a cohesive system of charts that feels a level above current BI.

dbtCharts.com: a BI platform built on dbt Charts
------------------------------------------------

Alongside the open-source language, today we’re launching
[dbtCharts.com](https://dbtcharts.com) in public beta: a hosted platform for the
rest of BI. With charts pulled out, what remains is chiefly hosting, access
control, and a UI. By their nature these perhaps can’t be unbundled, or at least
shouldn’t be, so the platform handles them on top of the open-source language.

variables:queries:charts:rows:ChatUIHosting & AccessdbtCharts.comBI platformdbt ChartsOpen chart language: YAML and SQL
Semantic layerOptional
dbt modelsTransformation
Your warehouseData
same dbtGit repo

The platform connects to your warehouse and adds conversational analytics, a visual
editor for the finishing touches, version history, and sharing with permissions
for users and groups, so the people reading a board don’t need a warehouse
login.

And of course, these charts were built for chat. The platform has first-class
conversational analytics: like Claude or ChatGPT, but with permissioned
read-only access to your warehouse and an expert analyst’s skills and tools
built in.
Explore by chatting with charts, and at any point click in to fine-tune and
save the board.

[![A chart selected in the visual design controls, its background palette open, in the real dbt Charts workspace, with the Commercial performance board and an illustrative AI conversation.](/assets/img/home/cloud-growth-review.png?v=4220fc50e4def8d138528c713e8f7a9cd083f2ea5632f362755700c8a86d7d0b)](/assets/img/home/cloud-growth-review.png?v=4220fc50e4def8d138528c713e8f7a9cd083f2ea5632f362755700c8a86d7d0b)
[![The board definition in the real dbt Charts workspace, with the Commercial performance board and an illustrative AI conversation.](/assets/img/home/cloud-code-context.png?v=3c5c718032cc79b928d88106f51ee355123524e1693e7965d83ceea7ace44f34)](/assets/img/home/cloud-code-context.png?v=3c5c718032cc79b928d88106f51ee355123524e1693e7965d83ceea7ace44f34)
[![Saved board history in the real dbt Charts workspace, with the Commercial performance board and an illustrative AI conversation.](/assets/img/home/cloud-history.png?v=47b204644e288baf3dce220da6e2d4f38c7e3641860dd2a6bbdc69fa6c590e80)](/assets/img/home/cloud-history.png?v=47b204644e288baf3dce220da6e2d4f38c7e3641860dd2a6bbdc69fa6c590e80)
[![Choosing the people and teams to share the board with in the real dbt Charts workspace, with the Commercial performance board and an illustrative AI conversation.](/assets/img/home/cloud-settings-sharing.png?v=95a570e47e468c93847f0cbeb3a5107b58dc148e3fe87d2a96f75c8b945dd419)](/assets/img/home/cloud-settings-sharing.png?v=95a570e47e468c93847f0cbeb3a5107b58dc148e3fe87d2a96f75c8b945dd419)

One board. Every way to work.
 Design
 YAML
 History
 Sharing

Pause

Play

Because it’s built on the open language, every change, from chat, the visual
editor, or code, lands in the same YAML in your Git repo. Nothing is locked in: the same board runs on your laptop, in CI, and on
the platform, and teams can self-serve, agent in hand, without creating a
second, hidden data stack.

Try the beta
------------

The dbt Charts language is open source under the Apache 2.0 license, and you can
author, render, and serve boards locally without creating an account. Install it
yourself, or hand your coding agent one line:

Terminal
`uv tool install dbt-charts`

Claude / AI
`Make charts of this with dbt Charts. Start with: uv tool install dbt-charts && dct skills intro`

* Code: [github.com/dbt-labs/dbt-charts](https://github.com/dbt-labs/dbt-charts)
* Docs: [docs.dbtCharts.com](https://docs.dbtcharts.com)
* Hosted BI: [dbtCharts.com](https://dbtcharts.com)
* Community: [#dbt-charts](https://getdbt.slack.com/archives/C0C1SFL0QN5) on the [dbt Community Slack](https://www.getdbt.com/community/join-the-community)

dbt Charts is pre-1.0 and still changing. When the grammar changes, boards
migrate as they parse, so the boards you write today keep rendering. Try it, tell us what is missing[[1](https://github.com/dbt-labs/dbt-charts/issues/1)][[2](https://github.com/dbt-labs/dbt-charts/issues/2)], join the discussion in [#dbt-charts](https://getdbt.slack.com/archives/C0C1SFL0QN5) on Slack, and help us build the chart layer
that open data infrastructure has been waiting for.
