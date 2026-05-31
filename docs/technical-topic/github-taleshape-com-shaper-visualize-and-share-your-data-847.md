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

Shaper Open Source, SQL-driven Data Dashboards powered by DuckDB. Build analytics dashboards simply by writing SQL: SELECT ' Sessions per Week ' ::LABEL; SELECT date_trunc( ' week ' , created_at)::XAXIS, category::CATEGORY, count ()::BARCHART_STACKED, FROM dataset GROUP BY ALL ORDER BY ALL; Learn more: https://taleshape.com/shaper/docs/ Features Business Intelligence Open Source & Self-Hosted SQL-First and AI-Ready Git-Based Workflow Query across Data Sources Embedded Analytics White-Labeling & custom styles Row-level security via JWT tokens Embed Without IFrame through JS & React SDKs Automated Reporting Generate PDF, PNG, CSV & Excel Scheduled Alerts & Reports Sharable Password-Protected Links Quickstart The quickest way to try out Shaper without installing anything is to run it via Docker : docker run --rm -it -p5454:5454 taleshape/shaper Then open http://localhost:5454/new in your browser. For more, checkout the Getting Started Guide . To run Shaper in production, see the Deployment Guide . Support and Managed Hosting Shaper itself is completely free and open source. But we offer managed hosting and proactive support. Find out more: Plans and Pricing Get in touch Feel free to open an issue or start a discussion if you have any questions or suggestions. Also follow along on BlueSky or LinkedIn . And subscribe to our newsletter to get updates about Shaper. Contributing See CONTRIBUTING.md Release Notes See Github Releases License and Copyright Shaper is licensed under the Mozilla Public License 2.0 . Copyright © 2024-2026 Taleshape OÜ
