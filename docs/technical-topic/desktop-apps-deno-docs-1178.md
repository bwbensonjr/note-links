---
id: 1178
url: https://docs.deno.com/runtime/desktop/
title: Desktop apps | Deno Docs
domain: docs.deno.com
source_date: '2026-06-22'
tags:
- web-dev
- typescript
- tutorial
- devops
summary: Deno Desktop is an upcoming feature (coming in Deno 2.9) that converts Deno
  projects into self-contained desktop applications with small binaries, full Node
  compatibility, and built-in auto-updates. It offers key advantages over competing
  solutions like Electron and Tauri, including framework auto-detection for popular
  web frameworks, in-process communication between backend and UI, and cross-compilation
  capabilities. The feature emphasizes simplicity—developers can take existing web
  projects and run them as desktop apps with minimal code changes, using either the
  OS's native webview for smaller binaries or an optional bundled Chromium backend
  for consistent rendering across platforms.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# Desktop apps | Deno Docs

On this page

* [Why deno desktop](#why-deno-desktop)
* [Hello, desktop](#hello%2C-desktop)
* [What's in this section](#what's-in-this-section)

`deno desktop` turns a Deno project (anything from a single TypeScript file to a
Next.js app) into a self-contained desktop application. The output is a
redistributable binary that bundles your code, the Deno runtime, and a web
rendering engine into one bundle per platform.

Coming in Deno 2.9

`deno desktop` ships in Deno v2.9.0 and is not in a stable release yet. To try
it now, run `deno upgrade canary` to install the
[`canary`](/runtime/reference/cli/upgrade/) build. The command, configuration
keys, and TypeScript APIs may still change before the feature is stable.

Why `deno desktop` [Jump to heading#](#why-deno-desktop)
--------------------------------------------------------

Web technology is the most widely-known UI toolkit in the world. Desktop apps
built on web stacks (Electron, Tauri, Electrobun) take advantage of that, but
each has tradeoffs you have to live with: huge binaries, missing platform
support, no JavaScript ecosystem, no built-in update story, no framework
integration.

`deno desktop` is opinionated about those tradeoffs:

* **Small by default, full Node compatibility.** The default WebView backend
  uses the operating system's own webview for small binaries, and you still have
  the entire npm ecosystem available through Deno's Node compat layer. Opt into
  the bundled Chromium (CEF) backend when you need identical rendering across
  macOS, Windows, and Linux.
* **Framework auto-detection.** Point `deno desktop` at a Next.js, Astro, Fresh,
  Remix, Nuxt, SvelteKit, SolidStart, TanStack Start, or Vite SSR project and it
  runs: the production server in release mode, the dev server with hot reload
  under `--hmr`. No code changes are required to take an existing web project to
  the desktop.
* **In-process bindings instead of IPC.** Backend and UI communication goes
  through in-process channels, not socket-based IPC. Values are still encoded as
  they cross the call boundary, but there is no cross-process round-trip between
  your Deno code and the webview.
* **Cross-compile from one machine.** The same machine can build for macOS,
  Windows, and Linux. Backends are downloaded as needed, not built locally.
* **Built-in binary-diff auto-update.** Ship a single `latest.json` manifest and
  bsdiff patches; the runtime polls, applies, and rolls back automatically on
  failed launches.

Hello, desktop [Jump to heading#](#hello%2C-desktop)
----------------------------------------------------

Create a one-file desktop app:

main.ts

```
Deno.serve(() =>
  new Response("<h1>Hello, desktop</h1>", {
    headers: { "content-type": "text/html" },
  })
);
```

>\_

```
deno desktop main.ts
```

The compiled binary opens a window pointed at a local HTTP server bound to your
[`Deno.serve()`](/api/deno/~/Deno.serve) handler. Run it directly:

>\_

```
./main      # macOS / Linux
.\main.exe  # Windows
```

[`Deno.serve()`](/api/deno/~/Deno.serve) automatically binds to the address the
webview navigates to, so you do not need to pass a port or hostname. See
[HTTP serving](/runtime/desktop/serving/) for details.

What's in this section [Jump to heading#](#what's-in-this-section)
------------------------------------------------------------------

* [Configuration](/runtime/desktop/configuration/): the `desktop` block in
  `deno.json`.
* [Backends](/runtime/desktop/backends/): CEF, webview, raw; how to choose.
* [HTTP serving](/runtime/desktop/serving/):
  [`Deno.serve()`](/api/deno/~/Deno.serve) integration and the serving model.
* [Frameworks](/runtime/desktop/frameworks/): Next.js, Astro, Fresh, Remix,
  Nuxt, SvelteKit, and others.
* [Windows](/runtime/desktop/windows/):
  [`Deno.BrowserWindow`](/api/deno/~/Deno.BrowserWindow) lifecycle, multiple
  windows, events.
* [Bindings](/runtime/desktop/bindings/): calling Deno code from the webview via
  `bindings.<name>()`.
* [Menus](/runtime/desktop/menus/): application and context menus.
* [Tray and dock](/runtime/desktop/tray_and_dock/): system status icons and the
  macOS dock.
* [Dialogs](/runtime/desktop/dialogs/): `prompt()`, `alert()`, `confirm()` as
  native popups.
* [Notifications](/runtime/desktop/notifications/): native OS notifications via
  the Web `Notification` API.
* [Hot module replacement](/runtime/desktop/hmr/): `--hmr` for framework and
  non-framework apps.
* [DevTools](/runtime/desktop/devtools/): unified DevTools attached to both the
  Deno runtime and the webview.
* [Auto-update](/runtime/desktop/auto_update/):
  [`Deno.autoUpdate()`](/api/deno/~/Deno.autoUpdate), manifests, bsdiff,
  rollback.
* [Error reporting](/runtime/desktop/error_reporting/): capturing uncaught
  exceptions and panics.
* [Distribution](/runtime/desktop/distribution/): cross-compilation, output
  formats, installers.
* [Comparison](/runtime/desktop/comparison/): how `deno desktop` relates to
  Electron, Tauri, Electrobun, Dioxus.
* [`deno desktop` CLI reference](/runtime/reference/cli/desktop/): the command,
  its flags, and the `deno.json` `desktop` schema.
