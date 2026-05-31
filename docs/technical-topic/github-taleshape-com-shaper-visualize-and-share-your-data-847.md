---
id: 847
url: https://github.com/taleshape-com/shaper
title: 'GitHub - taleshape-com/shaper: Visualize and share your data. All in SQL.
  Powered by DuckDB.'
domain: github.com
source_date: '2026-02-18'
tags:
- github-repo
- sql
- database
- web-dev
summary: Shaper is an open-source, SQL-powered dashboard tool built on DuckDB that
  allows users to create analytics dashboards by writing SQL queries with special
  visualization syntax. It offers features including self-hosted deployment, multi-data
  source querying, automated reporting, embedded analytics, and JWT-based security,
  with a free open-source version and optional managed hosting available. Users can
  quickly get started using Docker or explore comprehensive documentation for production
  deployments and advanced customization options.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# GitHub - taleshape-com/shaper: Visualize and share your data. All in SQL. Powered by DuckDB.

Shaper
======

**Open Source, SQL-driven Data Dashboards powered by DuckDB.**

> **Need a secure, compliant setup for sensitive data?** Maintain 100% data sovereignty while we handle the operations and infrastructure. [Get a managed, private Shaper instance with expert support.](https://taleshape.com/plans-and-pricing)

---

Build analytics dashboards simply by writing SQL:

```
SELECT 'Sessions per Week'::LABEL;
SELECT
  date_trunc('week', created_at)::XAXIS,
  category::CATEGORY,
  count()::BARCHART_STACKED,
FROM dataset
GROUP BY ALL ORDER BY ALL;
```

[![Screenshot](https://camo.githubusercontent.com/21bf933c68121b3fea75033265252a1d3d97198fe60105b3b9f86c6dbb377fcc/68747470733a2f2f74616c6573686170652e636f6d2f696d616765732f73657373696f6e5f64617368626f6172642e706e67)](https://taleshape.com/shaper/docs/)

Learn more:
<https://taleshape.com/shaper/docs/>

Features
--------

**Data Visualization**

* **Open Source** & Self-Hosted
* **SQL-First** and AI-Ready
* **Git-Based** Workflow
* Query across **Data Sources**

**Embedded Analytics**

* **White-Labeling** & custom styles
* **Row-level security** via JWT tokens
* Embed **Without IFrame** through JS & React SDKs

**Automated Reporting**

* Generate **PDF, PNG, CSV & Excel**
* Scheduled **Alerts & Reports**
* Sharable **Password-Protected Links**

Quickstart
----------

The quickest way to try out Shaper without installing anything is to run it via [Docker](https://www.docker.com/):

```
docker run --rm -it -p5454:5454 taleshape/shaper
```

Then open <http://localhost:5454/new> in your browser.

For more, checkout the [Getting Started Guide](https://taleshape.com/shaper/docs/getting-started/).

To run Shaper in production, see the [Deployment Guide](https://taleshape.com/shaper/docs/deploy-to-production/).

Managed Hosting and Expert Support
----------------------------------

Shaper is 100% free and open source. Through **Taleshape**, we provide managed deployments and fractional data engineering for teams in regulated industries that need to move fast while maintaining strict data sovereignty:

* **Managed Private Cloud**: Dedicated, isolated instances in our cloud or your own infrastructure. We handle updates, security, and 24/7 monitoring.
* **Fractional Data Team**: Proactive support for integrations, custom dashboard development, and compliance readiness (HIPAA, GDPR, SOC2).

[**View Plans and Pricing**](https://taleshape.com/plans-and-pricing)

Get in touch
------------

Feel free to open an [issue](https://github.com/taleshape-com/shaper/issues) or start a [discussion](https://github.com/taleshape-com/shaper/discussions) if you have any questions or suggestions.

Also follow along on [BlueSky](https://bsky.app/profile/taleshape.bsky.social) or [LinkedIn](https://www.linkedin.com/company/taleshape/).

And subscribe to our [newsletter](https://taleshape.com/newsletter) to get updates about Shaper.

Contributing
------------

See [CONTRIBUTING.md](/taleshape-com/shaper/blob/main/CONTRIBUTING.md)

Release Notes
-------------

See [Github Releases](https://github.com/taleshape-com/shaper/releases)

License and Copyright
---------------------

Shaper is licensed under the [Mozilla Public License 2.0](https://github.com/taleshape-com/shaper/blob/main/LICENSE).

Copyright © 2024-2026 Taleshape OÜ
