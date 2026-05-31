---
id: 355
url: https://mcp-b.ai/
title: MCP Web | Model Context Protocol for the Browser
domain: mcp-b.ai
source_date: '2025-07-10'
tags:
- web-dev
- ai
- llm
- cli-tool
summary: '# MCP-B Summary


  MCP-B (Model Context Protocol for the Browser) enables AI assistants to directly
  call website functions instead of relying on screen-reading automation. By adding
  ~50 lines of code to a website, developers can expose structured APIs to AI assistants
  using the user''s existing browser session—eliminating the need for API keys, OAuth,
  or complex configuration. This approach delivers 10,000x performance improvements
  over traditional browser automation, completing tasks in milliseconds while maintaining
  security through existing authentication methods.'
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# MCP Web | Model Context Protocol for the Browser

The WebMCP company

Websites publish tools. Agents call them.
=========================================

MCP-B maintains the reference implementation of the W3C WebMCP standard, ships the Char agent platform, and consults on deploying browser-based agents.

Book a demo

WebMCP PackagesMCP-B ExtensionCharConsulting

PolyfillReactTypesregisterTool.ts

1// Register a tool for AI agents

2navigator.modelContext.registerTool({

3 name: 'search\_products',

4 description: 'Search the catalog',

5 inputSchema: {

6 type: 'object',

7 properties: {

8 query: { type: 'string' }

9 }

10 },

11 execute: (params) =>

12 catalog.search(params.query),

13});

[→Get started

Install the polyfill and register your first tool](https://docs.mcp-b.ai)[npm@mcp-b/webmcp-polyfill

Core polyfill for navigator.modelContext](https://www.npmjs.com/package/@mcp-b/webmcp-polyfill)[npm@mcp-b/react-webmcp

React hooks for WebMCP tools](https://www.npmjs.com/package/@mcp-b/react-webmcp)[npm@mcp-b/transports

Tab, iframe, and extension transports](https://www.npmjs.com/package/@mcp-b/transports)[npm@mcp-b/webmcp-types

TypeScript definitions, zero runtime](https://www.npmjs.com/package/@mcp-b/webmcp-types)[→W3C Spec

The formal WebMCP specification](https://webmachinelearning.github.io/webmcp/)

Already in production

WebMCP is shipping inside the world's largest companies.

![Google](/logos/google.svg)

![Microsoft](/logos/microsoft.svg)

![Amazon](/logos/amazon.svg)

![JPMorgan Chase](/logos/jpmorgan.svg)

![Adobe](/logos/adobe.svg)

![Target](/logos/target.svg)

Char Alpha

Your own personalized  company agent
------------------------------------

Start with the Char extension template, or plug Char into your existing internal agent UI. Reach out if you want integration help.

### Bring your company agent to the browser in minutes

Clone the Char extension template, connect your internal agent, and start testing in a real browser with the same auth and UI your team already uses.

 [Talk to us](#demo/consulting)

$git clone char-extension-template

Cloning template...

Resolving deltas: 100% (1234/1234), done.

Installing dependencies...

Connecting Char agent...

✓ Template ready

Clone the Char template extension

Start with a working extension shell that opens directly into your app and gets your company agent running in the browser quickly.

CustomerList.tsx

import { useState } from 'react';

import { useWebMCP } from '@mcp-b/react-webmcp';

import { z } from 'zod';

export function CustomerList() {

const [selectedCustomerId, setSelectedCustomerId] = useState<string | null>(null);

+

+  useWebMCP({

+  name: 'open\_customer',

+  inputSchema: { customerId: z.string() },

+  handler: async ({ customerId }) => {

+  setSelectedCustomerId(customerId);

+  return `Opened customer ${customerId}`;

+  },

+  });

return <div>{selectedCustomerId ?? 'No customer selected'}</div>;

}

Apply suggestion

Wrap React logic in WebMCP tools

Add WebMCP tools to your frontend apps with @mcp-b/react-webmcp, then use a coding agent to build and test those tools in a real browser.

Ready to put agents in the browser?
-----------------------------------

Talk to us about WebMCP integration, Char alpha access, or consulting on your agent deployment.

Book a demo
