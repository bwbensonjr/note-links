---
id: 724
url: https://www.mintlify.com/blog/install-md-standard-for-llm-executable-installation
title: 'install.md: A Standard for LLM-Executable Installation'
domain: www.mintlify.com
source_date: '2026-01-17'
tags:
- llm
- devops
- tutorial
- cli-tool
summary: install.md is a new standard format for writing software installation instructions
  that AI agents can execute autonomously, addressing the gap between human-readable
  documentation and agent-executable tasks. The structured markdown file includes
  clear objectives, verification criteria, and step-by-step instructions that allow
  LLMs to adapt installation processes to different environments and architectures
  without the security risks of piping executable scripts. Mintlify has already integrated
  auto-generation of install.md files across its documentation platform, and developers
  can also manually create and host these files to enable one-command software installation
  via LLMs.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# install.md: A Standard for LLM-Executable Installation

[All articles](/blog)

Announcements/January 15, 2026

install.md: A Standard for LLM-Executable Installation
======================================================

6 minutes read

MR

Michael Ryaboy

Content Strategist

#### Share this article

---

MR

Michael Ryaboy

Content Strategist

#### Share this article

![install.md: A Standard for LLM-Executable Installation](/_next/image?url=%2Fimages%2Ffeatured%2Finstall-md.webp&w=1920&q=75)

SUMMARY

Installing software is the kind of specific and repetitive task that agents are good at. Today we are proposing install.md to standardize how developers should write installation instructions for agents. It's currently live on all Mintlify sites including Cerebras, Firecrawl, and Langchain.

> **Deprecated January 21, 2026:** We've moved to [skill.md](/blog/skill-md), an open standard for agent skills that provides both installation and usage knowledge. See the [announcement](/blog/skill-md) for details.

Proposal for a [standard `/install.md`](https://www.installmd.org/) file that provides LLM-executable installation instructions.

[Background](#background)
-------------------------

Agents are growing in capability faster than software developers have been able to keep up. Product documentation today is focused on humans instead of AI which creates friction when trying to automate annoying yak-shaving style tasks like installation.

The difference is very subtle. Agents need to have a task iterated to them like "I want you to install Mintlify CLI for me. Execute all the steps below autonomously." whereas humans can work from more general prose or even a bash script.

Today we are proposing [install.md](https://www.installmd.org/) to standardize how developers should write installation instructions for agents. It's currently live on all Mintlify sites including [Cerebras](https://inference-docs.cerebras.ai/install.md), [Firecrawl](https://docs.firecrawl.dev/install.md), and [Langchain](https://docs.langchain.com/install.md).

[Proposal](#proposal)
---------------------

Add an `install.md` markdown file to your project with LLM-executable installation instructions.

Users paste that file into an LLM or pipe it directly from a URL. The LLM reads the instructions, detects the environment, adapts to the setup, and executes—optionally with approval at every step. Because the file is human-readable, users see exactly what will happen before it runs.

Instead of piping an executable file into bash with absolutely zero safeguards on what gets executed or confidence that it will figure out how to work with your arch linux setup, you can instead send an install.md to claude and trust Opus to deal with the minutia for you.

```
curl -fsSL https://www.anaconda.com/docs/install.md | claude
```

This works for any language or framework, whether your software is distributed as a binary, package, or script.

As the developer, you define how installation should work. You encode knowledge about edge cases that would clutter your docs but matter when things break.

Mintlify now auto detects all of that information, synthesizes it into a version designed for agents, and hosts it for you at `https://<your-docs-url>/install.md`. If your documentation covers multiple products—say, an SDK and a CLI—Mintlify defaults to generating install.md for the CLI. You can override the auto-generated file by adding your own `install.md` to the root of your documentation directory. If you'd prefer to disable the feature entirely, reach out to [[email protected]](/cdn-cgi/l/email-protection#3d4e484d4d524f497d5054534951545b44135e5250).

Alternatively, if you are not using Mintlify, you can set up and host this file manually.

[Format](#format)
-----------------

install.md uses a structured format with specific keywords that guide the LLM through autonomous execution.

A typical install.md includes:

* **Header:** Product name as a lowercase, hyphenated H1 heading (e.g., `# claude-code`)
* **Description:** Blockquote describing the product (e.g., `> Documentation and setup instructions for product-name`)
* **Action prompt:** Direct instruction to the LLM (e.g., "I want you to install [Product] for me. Execute all the steps below autonomously.")
* **OBJECTIVE:** What the installation should achieve
* **DONE WHEN:** Specific verification criteria (e.g., a command that returns expected output)
* **TODO:** Markdown checkbox list of steps to complete
* **Step sections:** Detailed installation instructions with code blocks
* **EXECUTE NOW:** Call-to-action that references the TODO list and objective

This format is flexible—it's up to the developer to define the steps necessary for a successful installation.

Here is an example:

```
# mintlify

> Documentation and setup instructions for mintlify

I want you to install Mintlify CLI for me. Execute all the steps below autonomously.

OBJECTIVE: Install the Mintlify CLI and set up a local documentation preview environment.

DONE WHEN: Local documentation server is running and accessible at http://localhost:3000.

## TODO

- [ ] Verify Node.js v20.17.0+ is installed
- [ ] Install the Mintlify CLI globally
- [ ] Create a new documentation project
- [ ] Start the local development server
- [ ] Verify the preview is accessible at localhost:3000

## Prerequisites

You need to have Node.js v20.17.0 or higher installed. Verify your Node.js version:

```bash
node --version
```

You must also have Git installed:

```bash
git --version
```

## Install the CLI

You need to install the Mintlify CLI globally using npm or pnpm.

Using npm:

```bash
npm i -g mint
```

Using pnpm:

```bash
pnpm add -g mint
```

Verify the installation:

```bash
mint --version
```

## Create a new documentation project

You must create a new documentation project using the CLI. This clones the starter kit into your specified directory:

```bash
mint new docs
```

The CLI will prompt you for a project name and theme. You can also specify these directly:

```bash
mint new docs --name my-project --theme linden
```

Navigate into your new project directory:

```bash
cd docs
```

## Start the local preview server

You need to start the development server to preview your documentation locally:

```bash
mint dev
```

Your documentation preview is now available at `http://localhost:3000`.

If port 3000 is already in use, you can specify a custom port:

```bash
mint dev --port 3333
```

Alternatively, run without global installation using npx:

```bash
npx mint dev
```

## Verify the preview

Open your browser and navigate to http://localhost:3000 to confirm the documentation site is running.

## Update the CLI

If you need to update to the latest version:

```bash
mint update
```

Or reinstall with the latest version:

```bash
npm i -g mint@latest
```

## Additional CLI commands

Check for broken links in your documentation:

```bash
mint broken-links
```

Check for accessibility issues:

```bash
mint a11y
```

Validate an OpenAPI specification:

```bash
mint openapi-check <openapi-file-or-url>
```

EXECUTE NOW: Complete the above TODO list to achieve: Local documentation server is running and accessible at http://localhost:3000.
```

The instructions describe outcomes, not exact commands. The LLM adapts to the environment—npm or pnpm, macOS or Linux, fresh project or existing codebase.

[Relationship to llms.txt](#relationship-to-llms-txt)
-----------------------------------------------------

install.md works naturally with your llms.txt. llms.txt helps LLMs understand your software; install.md tells them how to install it. Your install.md can link to your llms.txt so the LLM can reference it for troubleshooting, configuration details, or any additional context needed during installation.

[Advantages](#advantages)
-------------------------

**For developers shipping software:**

Define installation once and it adapts to every environment. You can encode edge cases and troubleshooting knowledge without cluttering your main documentation. There's no wizard to build or maintain, and you control exactly what context the LLM receives. Installation instructions for agents can differ from your public docs without worrying about company voice or developer experience polish. You're writing directly to your actual users, which are agents.

**For users installing software:**

A single command installs your software, or you can paste the file into any LLM. The instructions are human-readable so you can review every step before it executes, and modify it to improve performance on your system if necessary. The LLM adapts to your specific environment automatically. Because the file is fetched at runtime, you never deal with stale training data.

**For agents:**

Installation instructions live in a predictable location that's easy to find. The structured format provides clear success criteria for determining when installation is complete. The file is markdown, not HTML, which means clean input for the model.

[Contributing](#contributing)
-----------------------------

The spec is open source:

* **Spec:** [installmd.org](https://installmd.org/)
* **GitHub:** [github.com/mintlify/install-md](https://github.com/mintlify/install-md)

Add an `install.md` to your project root or `/docs` directory. That's it.

If you use Mintlify for documentation, install.md is generated automatically at `yourdocs.com/install.md`.

[FAQ](#faq)
-----------

**What about installation wizards like PostHog's or Sentry's?**

Wizards solve the same problem: reliable installation across environments. They require significant engineering to build and maintain. PostHog's wizard consists of several LLM prompts, which users need to audit the repo to find. install.md is a lighter-weight alternative—define instructions in markdown, and the LLM handles adaptation. For complex integrations with many configuration options, a dedicated wizard may still be the right choice. For most software, install.md gets you most of the benefit with far less effort.

**How does install.md work with my existing CLI or scripts?**

Your install.md can instruct the LLM to run your CLI, execute your scripts, or follow your existing setup process. Think of it as a layer that guides the LLM to use whatever tools you've already built.

**What about security? Isn't this just `curl | bash` with extra steps?**

This is a fair concern. A few things make install.md different:

1. **Human-readable by design.** Users can review the instructions before execution. Unlike obfuscated scripts, the intent is clear.
2. **Step-by-step approval.** LLMs in agentic contexts can be configured to request approval before running commands. Users see each action and can reject it.
3. **No hidden behavior.** install.md describes outcomes in natural language. Malicious intent is harder to hide than in a shell script.

Install.md doesn't eliminate trust requirements. Users should only use install.md files from sources they trust—same as any installation method.

**What about versioning?**

install.md works at the current version by default. If your installation differs significantly across versions, you can host version-specific files (`/v2/install.md`) or include version detection logic in the instructions themselves.

**What if install.md doesn't fit my use case?**

The spec is open source. Open an issue or submit a PR—we're evolving the standard based on real-world feedback.

#### More blog posts to read

[![22 UX improvements to the web editor](/_next/image?url=%2Fimages%2Fweb-editor-ux-improvements.png&w=1080&q=75)

### 22 UX improvements to the web editor

A round-up of the UX improvements coming to Mintlify's web editor.

May 4, 2026

DT

Dmytro Tovstokoryi

Design](/blog/22-ux-improvements-to-the-web-editor)[![Introducing the Mintlify Help Center Starter Kit](/_next/image?url=%2Fimages%2Fhelp-center.webp&w=1080&q=75)

Announcements

### Introducing the Mintlify Help Center Starter Kit

Help centers are the first line of defense for customer support. The new Mintlify Help Center starter kit and AI ticket deflection make it faster than ever to launch one.

May 1, 2026

HL

Hahnbee Lee

Co-Founder](/blog/help-center)
