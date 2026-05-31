---
id: 1126
url: https://specification.website/
title: The Website Specification
domain: specification.website
source_date: '2026-05-31'
tags:
- web-dev
- security
- tutorial
- devops
summary: The Website Specification is a comprehensive, platform-agnostic technical
  checklist covering 128 topics across ten categories that define what makes a good
  website, including foundations, SEO, accessibility, security, performance, and privacy
  standards sourced from widely-accepted web standards like WHATWG, W3C, and WCAG.
  The specification is designed to be used by both humans and AI agents for auditing,
  learning, and improving websites, with full documentation available on GitHub and
  accessible through open APIs including an MCP server and Agent Skill. Users can
  browse topics to understand why each feature matters and how to implement it, with
  the entire resource built collaboratively and continuously updated through community
  contributions.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# The Website Specification

What a good website does. A platform-agnostic specification of the technical features every decent website should have — from <title> to /.well-known/security.txt , from WCAG contrast to llms.txt . Written for humans and agents. Browse all 128 topics → Get the checklist ★ on GitHub Categories Ten areas, mapped to widely-accepted standards. All topics → Foundations 14 The HTML, head, and document basics every page needs. SEO 13 Search visibility — robots.txt, sitemaps, canonicals, structured data. Accessibility 20 WCAG-aligned rules so people of all abilities can use the site. Security 12 Headers, transport, and policies that keep visitors safe. Well-Known URIs 9 Standard, agreed-upon paths under /.well-known/. Agent Readiness 18 Things that make a site legible to AI agents and crawlers. Performance 19 Core Web Vitals, caching, images, fonts, network behaviour. Privacy 6 Consent, signals, and respecting visitor choice. Resilience 5 Graceful failure — error pages, offline, redirects. Internationalisation 12 Language, locale, direction, and translated content. Standards, not opinions Each topic links back to the source standard — WHATWG, W3C, IETF RFCs, WCAG, MDN, and the organisations defining the modern web. Platform agnostic Whether you ship WordPress, Drupal, TYPO3, Next.js, Astro, Hugo, a Django app, or plain HTML, the spec is the spec. Implementation hints follow it, not the other way round. Built in the open Every page has an Edit on GitHub link. PRs welcome. Sources credited on every page. Let your agent query the spec. The whole spec is available as an open MCP server — read-only, no auth — plus a published Agent Skill that teaches any compatible agent when and how to use it. Per-page Markdown is available via /llms.txt and Accept: text/markdown on any spec URL. Connect MCP → Agent Skill llms.txt Agent-readiness spec → { "mcpServers": { "specification-website": { "transport": "http", "url": "https://mcp.specification.website/mcp" } } } How to use this site 01 Audit Run through the checklist . Each item is a “does the site do this — yes or no.” 02 Learn Click into any item for what it is, why it matters, and how to implement it. 03 Improve Found a gap, a stale fact, or a missing topic? Open a PR. Sources required.
