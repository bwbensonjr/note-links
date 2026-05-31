---
id: 1130
url: https://buildingbetter.tech/p/i-read-the-claude-code-source-code
title: I Read the Claude Code Source Code. Here's Everything You Can Configure That
  the Docs Don't Tell You.
domain: buildingbetter.tech
source_date: '2026-05-29'
tags:
- tutorial
- cli-tool
- web-dev
summary: This article reveals undocumented configuration options in Claude Code that
  exist in the source code but aren't covered in official documentation, including
  the ability to configure the "YOLO Classifier" permission system with plain English
  descriptions, create powerful hook scripts that can rewrite commands mid-flight
  and inject persistent context, and access hidden frontmatter fields for skills and
  agents. The author provides copy-paste ready examples of practical implementations,
  such as hooks that auto-approve read-only commands, scan for hardcoded secrets,
  and automatically load project context at session start, all of which dramatically
  expand what developers can build with Claude Code beyond the official docs.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# I Read the Claude Code Source Code. Here's Everything You Can Configure That the Docs Don't Tell You.

I Read the Claude Code Source Code. Here's Everything You Can Configure That the Docs Don't Tell You.
=====================================================================================================

### Hook fields that rewrite commands mid-flight, persistent agent memory, auto-mode rules in plain English, self-improving dream loops, and every example is copy-paste ready.

[![André Figueira's avatar](https://substackcdn.com/image/fetch/$s_!Saco!,w_36,h_36,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa522b0cf-663f-4505-a8f3-304adcb92951_2173x2173.jpeg)](https://substack.com/@thegurucoder)

[André Figueira](https://substack.com/@thegurucoder)

Apr 01, 2026

12

2

Share

[![Enabling Claude Code to work more autonomously \ Anthropic](https://substackcdn.com/image/fetch/$s_!uQxS!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fde864c42-7eee-46ec-af2d-c111064bc767_1920x1035.png "Enabling Claude Code to work more autonomously \ Anthropic")](https://substackcdn.com/image/fetch/$s_!uQxS!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fde864c42-7eee-46ec-af2d-c111064bc767_1920x1035.png)

Claude Code’s auto-mode permission system is internally called the “YOLO Classifier.” That’s the actual variable name in yoloClassifier.ts. And you can configure it with plain English descriptions of your environment, things like “this is a staging server, destructive operations are acceptable,” that the classifier reads to decide what’s safe to auto-approve. This isn’t in any documentation.

It’s one of dozens of undocumented capabilities buried in the Claude Code source code, which is sitting right there in your node\_modules as a publicly distributed npm package. The official docs cover the basics well enough. But the source code reveals fields, response formats, and settings that dramatically expand what you can build. Everything here works right now, and every example is designed to be dropped into your project as-is.

A note on versioning: These findings come from @anthropic-ai/claude-code@2.1.87. Undocumented features can change between releases, so treat this as a snapshot of what’s available today. Fields with “EXPERIMENTAL” in their names are explicitly flagged as unstable by Anthropic’s own engineers, and I’ll call those out individually.

Before you start
----------------

Quick reference for where everything lives:

* **Settings:** `~/.claude/settings.json` (personal) or `.claude/settings.json` (project, shared via git)
* **Skills:** `~/.claude/skills/<name>/SKILL.md` (personal) or `.claude/skills/<name>/SKILL.md` (project)
* **Agents:** `~/.claude/agents/<name>.md` (personal) or `.claude/agents/<name>.md` (project)
* **Hook scripts:** `~/.claude/hooks/` is a good convention. Remember to `chmod +x` your scripts.

Project-level files in `.claude/` can be committed to git and shared with your team. Personal files in `~/.claude/` are yours alone.

Your hooks can talk back, and nobody told you how
-------------------------------------------------

This is the biggest gap in the documentation. The docs tell you hooks receive JSON on stdin and that exit code 2 blocks an operation. What they don’t tell you is that hooks can return JSON on stdout with event-specific fields that modify Claude Code’s behavior in real time. The source code reveals exactly what each event type accepts.

**PreToolUse** hooks can return:

* `updatedInput` - rewrite the tool’s input before it executes. You can modify commands mid-flight.
* `permissionDecision` - force “allow” or “deny” without prompting the user.
* `permissionDecisionReason` - explain the decision (shown in UI).
* `additionalContext` - inject text into the conversation context.

**SessionStart** hooks can return:

* `watchPaths` - set up automatic file watching that triggers FileChanged events.
* `initialUserMessage` - prepend content to the first user message in the session.
* `additionalContext` - inject context that persists for the whole session.

**PostToolUse** hooks can return:

* `updatedMCPToolOutput` - modify what Claude sees from an MCP tool response.
* `additionalContext` - inject context after a tool runs.

**PermissionRequest** hooks can return:

* `decision` - programmatically allow or deny with `updatedInput` or `updatedPermissions`.

This is powerful stuff. Here’s a PreToolUse hook that automatically adds `--dry-run` to any git push command before Claude executes it.

In your `settings.json`:

```
{
  "hooks": {
    "PreToolUse": [{
      "matcher": "Bash",
      "hooks": [{
        "type": "command",
        "command": "~/.claude/hooks/dry-run-pushes.sh"
      }]
    }]
  }
}
```

And the script at `~/.claude/hooks/dry-run-pushes.sh`:

```
#!/bin/bash
INPUT=$(jq -r '.tool_input.command' < /dev/stdin)
if echo "$INPUT" | grep -q 'git push'; then
  jq -n --arg cmd "$INPUT --dry-run" '{"updatedInput": {"command": $cmd}}'
fi
```

Claude thinks it’s running `git push origin main`, but your hook quietly rewrites it to `git push origin main --dry-run` before execution. The `updatedInput` field isn’t in any docs.

Here’s a SessionStart hook that watches your config files and injects git context into every session.

`settings.json`:

```
{
  "hooks": {
    "SessionStart": [{
      "hooks": [{
        "type": "command",
        "command": "~/.claude/hooks/session-context.sh",
        "statusMessage": "Loading project context..."
      }]
    }]
  }
}
```

`~/.claude/hooks/session-context.sh`:

```
#!/bin/bash
BRANCH=$(git branch --show-current 2>/dev/null)
CHANGES=$(git status --porcelain 2>/dev/null | wc -l | tr -d ' ')

jq -n \
  --arg branch "$BRANCH" \
  --arg changes "$CHANGES" \
  '{
    "watchPaths": ["package.json", ".env", "tsconfig.json"],
    "additionalContext": "Current branch: \($branch). Uncommitted changes: \($changes) files."
  }'
```

Now Claude Code automatically watches your `package.json`, `.env`, and `tsconfig` for changes, and it knows what branch you’re on and how many uncommitted files you have before you even type anything.

And here’s one that auto-approves read-only bash commands without prompting.

`settings.json`:

```
{
  "hooks": {
    "PreToolUse": [{
      "matcher": "Bash",
      "hooks": [{
        "type": "command",
        "command": "~/.claude/hooks/auto-approve-readonly.sh"
      }]
    }]
  }
}
```

`~/.claude/hooks/auto-approve-readonly.sh`:

```
#!/bin/bash
CMD=$(jq -r '.tool_input.command' < /dev/stdin)
if echo "$CMD" | grep -qE '^(ls|cat|echo|pwd|whoami|date|git status|git log|git diff)'; then
  echo '{"permissionDecision": "allow", "permissionDecisionReason": "Safe read-only command"}'
fi
```

You’re basically building your own permission classifier with shell scripts. The `permissionDecision` field isn’t in any docs.

Three hook fields the docs forgot to mention
--------------------------------------------

The documented hook fields are `type`, `command`, `matcher`, `timeout`, `if`, and `statusMessage`. The source code parser accepts three more that fundamentally change how hooks behave.

`once: true` fires the hook exactly once, then auto-removes it. Perfect for first-session setup:

```
{
  "hooks": {
    "SessionStart": [{
      "hooks": [{
        "type": "command",
        "command": "[ -f .env ] || cp .env.example .env && echo 'Created .env from template'",
        "once": true,
        "statusMessage": "First-time setup..."
      }]
    }]
  }
}
```

Simple enough to inline. It checks if `.env` exists, copies the template if not, and never runs again.

`async: true` runs the hook in the background without blocking Claude. Fire and forget:

```
{
  "hooks": {
    "PostToolUse": [{
      "matcher": "Bash",
      "hooks": [{
        "type": "command",
        "command": "jq '{timestamp: now, command: .tool_input.command, session: .session_id}' < /dev/stdin >> ~/.claude/audit.jsonl",
        "async": true
      }]
    }]
  }
}
```

That logs every bash command to an audit file without adding any latency to your session.

`asyncRewake: true` is the clever one. It runs in the background like async, so it doesn’t block on the happy path. But if it exits with code 2, it wakes the model back up and blocks the operation. Non-blocking when everything’s fine, blocking when something’s wrong:

`settings.json`:

```
{
  "hooks": {
    "PostToolUse": [{
      "matcher": "Write|Edit",
      "hooks": [{
        "type": "command",
        "command": "~/.claude/hooks/scan-secrets.sh",
        "asyncRewake": true,
        "statusMessage": "Scanning for secrets..."
      }]
    }]
  }
}
```

`~/.claude/hooks/scan-secrets.sh`:

```
#!/bin/bash
FILE=$(jq -r '.tool_input.file_path // .tool_response.filePath' < /dev/stdin)
if grep -qE '(password|secret|api_key)\s*=' "$FILE" 2>/dev/null; then
  exit 2  # Block: secrets detected
fi
exit 0    # Clean: carry on
```

This scans every file Claude writes for hardcoded secrets. If it finds one, it blocks and tells Claude. If not, you never even notice it ran.

Skill frontmatter fields the docs don’t show
--------------------------------------------

The documentation covers `name`, `description`, `allowed-tools`, `argument-hint`, `when_to_use`, and `context`. The actual frontmatter parser in the source code accepts six more.

`model` lets you override which model runs the skill. Use haiku for cheap, fast tasks and opus for complex analysis:

```
---
name: quick-lint
description: Fast lint check using the cheapest model
model: haiku
effort: low
allowed-tools: Bash, Read
argument-hint: "[file]"
---
Run the project linter on: $ARGUMENTS
Detect the linter from config (eslint, ruff, clippy) and run it. Report only errors, not warnings.
```

That runs on Haiku at low effort, so it’s fast and cheap. For a deep architecture review you’d want `model: opus` and `effort: max`.

`effort` controls how hard the model thinks. `low`, `medium`, `high`, or `max`. This maps to the same effort system that internally controls reasoning depth per response.

`hooks` defines hooks scoped to when the skill is active. They register when the skill fires and deregister when it completes:

```
---
name: strict-typescript
description: Write TypeScript with type checking on every save
allowed-tools: Bash, Read, Write, Edit, Grep, Glob
hooks:
  PostToolUse:
    - matcher: "Write|Edit"
      hooks:
        - type: command
          command: "~/.claude/hooks/typecheck-on-save.sh"
          statusMessage: "Type checking..."
        - type: command
          command: "~/.claude/hooks/lint-on-save.sh"
          async: true
---
Write TypeScript with strict enforcement. Every file you touch gets type-checked and linted automatically.
$ARGUMENTS
```

`~/.claude/hooks/typecheck-on-save.sh`:

```
#!/bin/bash
FILE=$(jq -r '.tool_input.file_path // .tool_response.filePath' < /dev/stdin)
[[ "$FILE" == *.ts ]] && npx tsc --noEmit 2>&1 || true
```

`~/.claude/hooks/lint-on-save.sh`:

```
#!/bin/bash
FILE=$(jq -r '.tool_input.file_path // .tool_response.filePath' < /dev/stdin)
[[ "$FILE" == *.ts ]] && npx eslint --fix "$FILE" 2>&1 || true
```

While this skill is running, every TypeScript file Claude writes gets type-checked synchronously and linted in the background. When the skill finishes, those hooks disappear. The scoping is clean.

`agent` delegates the skill to a custom agent:

```
---
name: deep-review
description: Thorough security review delegated to the review agent
agent: security-review
---
Review the following: $ARGUMENTS
```

`disable-model-invocation: true` prevents auto-invocation. Only explicit `/skill-name` works. Use this for destructive skills you don’t want firing accidentally.

`shell: bash` specifies which shell to use for execution.

Agent fields you won’t find in any docs
---------------------------------------

Custom agents in `.claude/agents/` support frontmatter fields the documentation doesn’t mention.

`color` sets the UI color: `red`, `orange`, `yellow`, `green`, `blue`, `purple`, `pink`, or `gray`. Helps visually distinguish agents when multiple are running.

`memory` is the big one. It gives the agent persistent memory across invocations:

* `user` - global, persists across all projects
* `project` - per-project persistence
* `local` - private per-project (gitignored)

This means you can build an agent that learns. A security reviewer that tracks past findings. A code reviewer that remembers your patterns across sessions. The memory uses the same frontmatter format as the auto-memory system.

```
---
name: codebase-guide
description: Answer questions about the codebase, learning more with each session
tools: [Read, Grep, Glob, Bash]
color: green
memory: project
---
You are a codebase guide with persistent memory. Check your memory first before exploring the code.

After answering a question, save useful context to memory:
- Architecture decisions (type: project)
- Code locations for common tasks (type: reference)
- Patterns and conventions (type: feedback)

Over time, you should answer faster because you remember where things are.
```

After a few sessions, this agent builds a knowledge base about your codebase and starts answering from memory before grepping.

`omitClaudeMd: true` skips loading the CLAUDE.md instruction hierarchy. Useful for a “fresh eyes” reviewer that applies industry standards rather than your project’s conventions:

```
---
name: fresh-eyes
description: Review code without project-specific biases
tools: [Read, Grep, Glob]
omitClaudeMd: true
effort: high
color: blue
---
Review this code purely from first principles. You have no project context. Focus on correctness, security, performance, and readability by industry standards.
```

`criticalSystemReminder_EXPERIMENTAL` is a short message re-injected at every turn as a system reminder. Even after conversation compaction, this stays in context:

```
---
name: prod-deployer
description: Manages production deployments with strict safety checks
tools: [Bash, Read, Grep]
color: red
criticalSystemReminder_EXPERIMENTAL: "Always run migrations with --dry-run first. Never skip the staging verification step."
---
```

Warning: This field has EXPERIMENTAL in its actual name in the source code. Anthropic’s engineers consider it unstable. It works right now, but it could be removed or renamed in any release. Use it for nice-to-have safety reminders, don’t build critical infrastructure on it.

`requiredMcpServers` lists MCP server name patterns that must be configured. If the servers aren’t available, the agent won’t appear. Prevents agents from loading when their dependencies aren’t set up.

The auto-mode classifier accepts plain English
----------------------------------------------

The `autoMode` field in `settings.json` configures what Anthropic internally calls the “YOLO Classifier.” This controls what gets auto-approved in auto mode:

```
{
  "autoMode": {
    "allow": [
      "Bash(npm test)",
      "Bash(npm run *)",
      "Bash(git status)",
      "Bash(git diff *)",
      "Bash(git log *)",
      "Read",
      "Grep",
      "Glob"
    ],
    "soft_deny": [
      "Bash(git push *)",
      "Bash(rm *)",
      "Write(.env*)"
    ],
    "environment": [
      "NODE_ENV=development",
      "This is a local dev machine with no production database access",
      "All Docker containers use isolated networks",
      "The test suite is safe to run repeatedly, it uses a dedicated test database"
    ]
  }
}
```

`allow` patterns get auto-approved. `soft_deny` patterns always require confirmation. The `environment` array is the interesting one, it’s not patterns at all. These are plain English context strings the classifier reads to understand your setup. You can write “This project uses Docker, all commands run in containers” and the classifier factors that into its safety decisions for ambiguous commands.

Think of it like giving the classifier a briefing about your environment. The more specific you are, the better it makes decisions. “No production access” tells it to be less paranoid about destructive operations. “Test database is isolated” tells it running tests is always safe.

The learning loop toggles nobody documented
-------------------------------------------

Two `settings.json` fields activate Claude Code’s self-improvement system:

```
{
  "autoMemoryEnabled": true,
  "autoDreamEnabled": true
}
```

`autoMemoryEnabled` makes Claude Code automatically extract durable memories from your sessions. After each conversation, a background agent pulls out things worth remembering, your preferences, your codebase patterns, decisions you made, and writes them to `~/.claude/projects/<path>/memory/` using the standard memory frontmatter format.

`autoDreamEnabled` activates background “dream” consolidation. Every 24 hours, if 5 or more sessions have accumulated, a background agent reviews past session transcripts and consolidates memories. It merges duplicates, resolves contradictions, converts relative dates to absolute, and prunes stale entries.

Together these create a compound learning loop: sessions produce memories, dreams consolidate memories, consolidated memories inform future sessions. Turn both on and after a few weeks you’ll notice Claude Code remembering your preferences, conventions, and common patterns without being told. It’s genuine learning from experience without any model retraining.

Magic Docs: the exact format
----------------------------

The source reveals the regex: `/^#\s*MAGIC\s+DOC:\s*(.+)$/im`. It must be an H1 heading, it’s case insensitive, and the next line can be italicized instructions (wrapped in `_underscores_` or `*asterisks*`) that scope what the update agent focuses on:

```
# MAGIC DOC: API Endpoint Reference
_Only document public REST endpoints. Include method, path, request body, response schema, and auth requirements._

## Endpoints

(content auto-maintained by Claude Code)
```

Without the instruction line, the agent tries to update everything. With it, you tell it “only track public endpoints” or “focus on breaking changes” and it respects that. The update agent runs in the background and is restricted to editing only that specific file. Deleting the header stops tracking automatically.

The full permission rule syntax
-------------------------------

The docs show basic examples like `Bash(git *)`. The source reveals the complete pattern language:

```
Bash(npm *)              # wildcard after "npm "
Bash(git commit *)       # specific subcommand
Read(*.ts)               # file extension
Read(src/**/*.ts)        # recursive directory with extension
Write(src/**)            # recursive, all files
mcp__slack               # all tools on slack server
mcp__slack__*            # explicit wildcard (same effect)
mcp__slack__post_message # specific tool
Bash(npm:*)              # legacy colon prefix (word boundary)
```

`*` matches within boundaries like shell globbing. `**` matches recursively through directories. MCP tool permissions use double underscores: `mcp__<server>__<tool>`. The `if` field in hooks uses this exact same syntax. No regex, just globs.

```
{
  "permissions": {
    "allow": [
      "Bash(npm *)", "Bash(git status)", "Bash(git diff *)",
      "Read(src/**)", "Read(tests/**)", "Grep", "Glob",
      "mcp__database__query"
    ],
    "deny": [
      "Bash(rm -rf *)", "Write(/etc/**)", "Write(.env*)",
      "mcp__slack__delete_*"
    ],
    "ask": [
      "Bash(git push *)", "Write(*.json)", "Write(*.lock)",
      "mcp__slack__post_message"
    ]
  }
}
```

context: fork and why your model choice matters
-----------------------------------------------

When you set `context: fork` on a skill, it runs as a background forked subagent. The source reveals that forks share the parent’s prompt cache through a typed contract called `CacheSafeParams`. All forks produce byte-identical API request prefixes to maximize cache hits.

The practical implication: if you set a different model on a forked skill, you break the cache. The parent conversation is on Opus, the fork is on Haiku, the prefixes diverge, cache miss, you pay full price. Either omit the model field or use `model: inherit` on forked skills to keep the cache working.

Use `context: fork` for heavy work: security scans, dependency analysis, documentation generation, test suite runs. The fork runs in the background and notifies you when done, keeping your main conversation responsive.

```
---
name: full-audit
description: Comprehensive codebase audit running in the background
context: fork
allowed-tools: Bash, Read, Grep, Glob, WebSearch
effort: high
---
Run a comprehensive audit:
- Security scan (grep for dangerous patterns, check dependencies for CVEs)
- Code quality (duplicated logic, dead code, missing error handling)
- Test coverage (untested critical paths)
- Dependency health (outdated packages, unused deps, license issues)

Write a detailed report to /tmp/audit-report.md when complete.
```

Putting it all together
-----------------------

A self-improving code reviewer with persistent memory and scoped hooks:

`.claude/agents/reviewer.md`:

```
---
name: reviewer
description: Code reviewer that learns your codebase patterns over time
tools: [Read, Grep, Glob, Bash]
effort: high
color: yellow
memory: project
hooks:
  PostToolUse:
    - matcher: "Bash"
      hooks:
        - type: command
          command: "~/.claude/hooks/log-review.sh"
          async: true
---
Before reviewing, read your memory for past findings on this codebase.

Review git diff HEAD~1 for:
- Patterns you've flagged before (check memory)
- New issues worth flagging
- Resolved issues from past reviews

After review, save to memory:
- New patterns found (type: feedback)
- Recurring issues (type: project)

End with VERDICT: PASS, FAIL, or NEEDS_REVIEW.
```

This agent remembers what it found last time. It knows which patterns keep recurring. After a few reviews, it starts catching project-specific issues that a generic reviewer would miss.

A SessionStart hook with file watching plus an asyncRewake safety net:

`settings.json`:

```
{
  "hooks": {
    "SessionStart": [{
      "hooks": [{
        "type": "command",
        "command": "~/.claude/hooks/session-context.sh",
        "statusMessage": "Loading project context..."
      }]
    }],
    "PreToolUse": [{
      "matcher": "Bash",
      "hooks": [{
        "type": "command",
        "command": "~/.claude/hooks/auto-approve-readonly.sh"
      }, {
        "type": "command",
        "command": "~/.claude/hooks/block-dangerous.sh",
        "asyncRewake": true,
        "statusMessage": "Safety check..."
      }]
    }]
  }
}
```

`~/.claude/hooks/block-dangerous.sh`:

```
#!/bin/bash
CMD=$(jq -r '.tool_input.command' < /dev/stdin)
echo "$CMD" | grep -qE '(rm -rf /|sudo rm|chmod 777|> /dev/)' && exit 2 || exit 0
```

Read-only commands get auto-approved instantly. Dangerous commands get blocked. Everything in between goes through normal permission flow. The safety scanner runs async so it doesn’t slow anything down on the happy path.

A skill with model override, effort control, and agent delegation:

```
---
name: architecture-review
description: Deep architecture review using max effort, delegated to fresh-eyes agent
agent: fresh-eyes
effort: max
---
Review the architecture of this project. Ignore existing conventions (the agent has omitClaudeMd: true).
Focus on: $ARGUMENTS

Evaluate structural decisions, dependency graph health, separation of concerns, and scalability characteristics.
```

This chains three undocumented features: `effort: max` for deep thinking, agent delegation to a specific agent, and that agent uses `omitClaudeMd: true` for unbiased analysis.

---

These undocumented features reveal the gap between what Claude Code is today and what Anthropic is building it to become. The hooks system with event-specific response fields is a programmable middleware layer for AI tool use, more flexible than most CI/CD pipelines. Persistent agent memory creates AI specialists that accumulate genuine expertise across sessions. The dream consolidation system is learning from experience without model retraining. The auto-mode classifier accepts natural language descriptions of your environment to make safety decisions.

These aren’t hidden settings or easter eggs. They’re the scaffolding for persistent, learning, autonomous AI development environments, and they’re already functional in the npm package on your machine. The docs will probably catch up eventually, but if you want to build on the cutting edge of what Claude Code can actually do, the source code is where the real documentation lives.

12

2

Share

PreviousNext
