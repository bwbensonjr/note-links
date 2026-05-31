---
id: 76
url: https://html2png.dev/
title: High Performance HTML to PNG API
domain: html2png.dev
source_date: '2025-12-24'
tags:
- web-dev
- llm
- cli-tool
summary: html2png.dev is a free, no-signup-required API that converts HTML directly
  into images (PNG, JPEG, WebP, or PDF) with a focus on being "agent-native" for AI
  workflows. The service offers zero setup, allows up to 200 requests per hour per
  IP, and supports advanced features like transparent backgrounds, Retina scaling,
  dynamic Open Graph images, and CSS selector targeting. It's designed to work seamlessly
  with LLM agents like Claude and GPT-4 through simple HTTP POST requests without
  complex JSON formatting or server configuration.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# High Performance HTML to PNG API

Convert HTML to PNG . The image generation API your LLM will love to use. Turn raw HTML into production-ready images for free. No sign up required. HTML EDITOR 0 characters SETTINGS EXAMPLES OG Image 1200×630 GitHub Header 1280×400 Terminal Snippet 800×600 System Diagram 1200×800 Analytics Chart 800×500 Browser Mockup 1200×900 SIZE & FORMAT W H PNG JPEG WebP PDF S OPTIONS D Z Transparent Background DEVELOPER API $_ COPY CURL HTML PREVIEW 1200×630 PNG HTML Preview ⚡ GENERATE IMAGE RECENT GENERATIONS History Empty Vibe Coding Ready Endpoint. Post https://html2png.dev/api/convert The Request Parameters html * str Raw HTML string. width int Output width. height int Output height. format str png | jpeg | webp | pdf png jpeg webp pdf deviceScaleFactor int Retina scaling (1-4). 1 2 3 4 delay int Wait time in ms. zoom num Viewport zoom (0.1-3.0). selector str CSS selector to capture. omitBackground bool Transparent background. true false The Response Fields url Public path to your generated asset. Not cached. filename Content-based hash identifier. cached Whether result was served from cache. format Output format used. timestamp ISO 8601 generation time. success Boolean status of the operation. Beyond MCP Not everything needs an MCP. Stop waiting for MCP server updates or proxy configurations. Your LLM agents are already capable of making HTTP requests. Give them the instructions, and let them render directly to the edge. 01 Zero Setup No plugins, no servers, no local tunnels. 02 Agent Native Works with Claude, GPT-5, and any tool-capable AI. A Single Prompt Paste into your Agent: Prompt & Vibe Common Queries Frequently Asked Questions 01. What is the best way to use the HTML to PNG API? Just send a simple HTTP POST request with your HTML in the request body. No JSON wrapping or escaping needed — raw HTML in, image out. 02. What makes this service "Agent-Native"? LLM agents like Claude and GPT-4 can call our API directly by sending raw HTML strings in the request body. No complex JSON escaping or MCP servers required — we designed it for AI workflows from the ground up. 03. Can I generate dynamic Open Graph (OG) images? Absolutely! Pass your HTML with dynamic content and we'll render it as an image. It's great for generating unique social share cards for blogs, SaaS products, or any page that needs custom previews. 04. Does it support Retina/high-DPI rendering? Yes it does! Use the "deviceScaleFactor" parameter to generate 2x or 4x resolution images for sharp display on modern screens. 05. Can I convert HTML to PDF as well? Yes! Just set the "format" parameter to "pdf" and you'll get a PDF document instead of an image. 06. How do I handle transparent backgrounds? Just add "omitBackground=true" to generate a transparent PNG. This is handy for icons, logos, or UI elements that need to overlay other content. 07. Does it support Tailwind CSS and custom fonts? Yes! You can include Tailwind via CDN and use Google Fonts. The browser waits for all assets to load before capturing, so everything renders properly. 08. Is the API really free? Yes, it's completely free! You get 200 requests per hour per IP, and there's no API key required to get started. 09. How long does generation take? Usually a few seconds, depending on the complexity of your HTML and any external assets that need to load. 010. Can I capture just a specific element? Yes! Use the "selector" parameter with a CSS selector (like "#my-card" or ".hero-section") to capture only that element instead of the full viewport. Still confused? Contact Support or check the Reference
