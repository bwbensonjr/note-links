---
id: 957
url: https://cc.storyfox.cz/
title: Claude Code Cheat Sheet
domain: cc.storyfox.cz
source_date: '2026-03-23'
tags:
- cli-tool
- tutorial
- ai
summary: This cheat sheet provides a comprehensive reference guide for Claude Code,
  covering keyboard shortcuts, slash commands, configuration options, and advanced
  features. Key takeaways include quick access commands for common tasks (Ctrl+C to
  cancel, Ctrl+L to clear), slash commands for session management and model switching
  (/clear, /model, /effort), and configuration through CLAUDE.md files for project-specific
  settings and memory. The guide also highlights advanced features like MCP servers
  for extensibility, agent workflows, voice mode support, and various CLI flags for
  headless and scripted usage.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# Claude Code Cheat Sheet

⌨️ Keyboard Shortcuts

General Controls

CtrlC Cancel input/generation

CtrlD Exit session

CtrlL Clear prompt input + force full screen redraw

CtrlO Toggle transcript viewer (verbose tool usage); cycles focus view in fullscreenNEW

CtrlU Clear entire input buffer

CtrlY Restore cleared input buffer

CtrlG Open in editor (same as Ctrl+X Ctrl+E)

CtrlR Reverse search history

CtrlX CtrlK Kill all background agents (press twice to confirm)

CtrlB Background running tasks

CtrlT Toggle task list

EscEsc Rewind or summarize

Mode Switching

ShiftTab Cycle permission modes (default → acceptEdits → plan → …)

Mac Option Keys (configure Option as Meta)

⌥P Switch model

⌥T Toggle extended thinking

⌥O Toggle fast mode

Input

\Enter Newline

v Vim visual mode (char selection + operators)NEW

V Vim visual-line modeNEW

Prefixes

/ Slash command

! Direct bash

@ File mention + autocomplete

🔌 MCP Servers

Add Servers

--transport http Remote HTTP (recommended)

--transport stdio Local process

--transport sse Remote SSE

Scopes

Local ~/.claude.json (you only)

Project .mcp.json (shared/VCS)

User ~/.claude.json (global)

Manage

/mcp Interactive UI

claude mcp list List all servers

alwaysLoad: true Keep server connected across all sessions (server config)NEW

maxResultSizeChars `_meta["anthropic/maxResultSizeChars"]` raises per-tool text threshold (up to 500K chars)NEW



⚡ Slash Commands

Session

/clear Clear conversation

/compact [focus] Compact context

/branch [name] Branch conversation (/fork alias)

/usage Token usage, cost and cache breakdown (replaces `/cost`/`/stats`)NEW

/context Visualize context (grid)

/diff Interactive diff viewer

/copy [N] Copy last (or Nth) response

/recap Summarize session context when returningNEW

/undo Alias for /rewindNEW

/rewind Rewind conv / code checkpoint

/export Export conversation

/plan [desc] Enter plan mode directly

/resume [session] Resume by ID/name

/focus Toggle focus view (fullscreen only)NEW

/goal [desc] Set completion goal; Claude works until met with live progress overlayNEW

Config

/config [key [value]] View/set settings (persists to `~/.claude/settings.json`)NEW

/model [model] Switch model (←→ effort)NEW

/fast [on|off] Toggle fast mode

/theme [name] Create and switch named custom themes; includes "Auto (match terminal)" dark/lightNEW

/permissions View/update permissions

/effort [level] Set effort (low/medium/high/xhigh/max); opens interactive slider with arrow keys when called without args

/color [color] Set prompt-bar color

/keybindings Customize keyboard shortcuts

/scroll-speed [speed] Adjust output scroll speedNEW

/terminal-setup Configure terminal keybindings

Tools

/init Create CLAUDE.md

/memory Edit CLAUDE.md files, toggle auto memory, view entries

/mcp Manage MCP servers

/hooks Manage hooks

/skills List available skills

/reload-skills Reload skills without restartingNEW

/agents Manage agent configurationsNEW

/workflows View and manage background multi-agent workflow runsNEW

/review [PR] Review PR locally

/ultrareview [PR#] Cloud code review — parallel multi-agent analysis

/security-review Scan diff for vulnerabilities

/loop [interval] [prompt] Recurring task (/proactive alias)NEW

/ide IDE integrations status

/add-dir <path> Add working directory

Special

/btw <question> Ask a side question without adding to the conversation

/extra-usage Extra usage when rate limited

/voice Toggle push-to-talk voice dictation

/doctor Diagnose installation

/insights Analyze sessions report

/desktop Continue in Desktop app

/rename [name] Rename current session

/help Show help + commands

/feedback Submit feedback (alias: /bug)

📁 Memory & Files

CLAUDE.md Locations

./CLAUDE.md or ./.claude/CLAUDE.md Project (team-shared)

./CLAUDE.local.md Local personal project notes (gitignored)

~/.claude/CLAUDE.md Personal (all projects)

/etc/claude-code/CLAUDE.md Managed policy (Linux/WSL, org-wide)

Rules & Import

.claude/rules/\*.md Project rules

~/.claude/rules/\*.md User rules

paths: frontmatter Path-specific rules

@path/to/file Import in CLAUDE.md

Auto Memory

~/.claude/projects/<proj>/memory/

`MEMORY.md` auto-loads at startup (first 25KB or 200 lines); topic files load on demand



🧠 Workflows & Tips

Plan Mode

ShiftTab Normal → Auto-Accept → Plan

--permission-mode plan Start in plan mode

Plan file naming Files named after your prompt (e.g. `fix-auth-race-snug-otter.md`)

Thinking & Effort

AltT Toggle thinking on/off

"ultrathink" Max effort for turn

CtrlO See thinking (verbose)

/effort ○ low · ◐ medium · ● high · ★ xhigh · ★★ max

Auto Mode Denied

/permissions → Recent Retry denied with RNEW

Git Worktrees

--worktree name Isolated branch per feature

isolation: worktree Agent in own worktree

sparsePaths Checkout only needed dirs

workspace.git\_worktree Status line JSON: linked worktree pathNEW

/batch Auto-creates worktrees

Voice Mode

/voice Enable push-to-talk

Space (hold) Record, release to send

20 languages EN, ES, FR, DE, CZ, PL…

Context Management

/context Usage + optimization tips

/compact [focus] Compress with focus

1M context Opus 4.6 (Max/Team/Ent)

Session Power Moves

claude -c Continue last conv

claude -r "name" Resume by name

/btw question Side Q, no context cost

SDK / Headless

claude -p "query" Non-interactive

--output-format json Structured output

--max-budget-usd 5 Cost cap

cat file | claude -p Pipe input

Scheduling & Remote

/loop 5m msg Recurring task

--remote Web session on claude.ai

! <cmd> Run shell cmd as background sessionNEW

⚙️ Config & Env

Config Files

~/.claude/settings.json User settings

.claude/settings.json Project (shared)

.claude/settings.local.json Local only

~/.claude.json OAuth, MCP, state

.mcp.json Project MCP servers

managed-settings.d/ Drop-in policy fragments

Key Settings

modelOverrides Map model picker → custom IDs

autoMode.hard\_deny Unconditional auto-mode classifier deny rulesNEW

hooks: if Conditional hooks (permission rule syntax)

DISABLE\_PROMPT\_CACHING\* Startup warning when prompt caching is disabledNEW

Monitor tool Stream events from background scriptsNEW

PermissionDenied Hook: auto-mode denialNEW

showThinkingSummaries Opt-in (off by default now)NEW

hooks: "defer" Pause headless → resume later

type: "mcp\_tool" Hook step invokes an MCP tool directlyNEW

continueOnBlock Hook config: keep running after a blocked tool callNEW

disableSkillShellExec Block !`cmd`NEW

refreshInterval Re-run custom status line every N secNEW

Key Env Vars

ANTHROPIC\_API\_KEY

ANTHROPIC\_MODEL

ANTHROPIC\_BASE\_URL Proxy/gateway override

ANTHROPIC\_BETAS Additional beta headers

ANTHROPIC\_CUSTOM\_MODEL\_OPTION Custom /model entry

MAX\_THINKING\_TOKENS 0=off

ENABLE\_PROMPT\_CACHING\_1H Opt into 1h prompt cache TTLNEW

CLAUDE\_CODE\_ENABLE\_AWAY\_SUMMARY Force recap when telemetry disabledNEW

CLAUDECODE Detect CC shell (=1)

CLAUDE\_CODE\_DISABLE\_CRON Disable scheduled tasks

CLAUDE\_CODE\_FORK\_SUBAGENT Enable forked subagents on external builds (=1)NEW

DISABLE\_UPDATES Block all update pathsNEW

API\_TIMEOUT\_MS API timeout (default: 600000ms)

MCP\_TIMEOUT MCP server startup timeout (ms)

CLAUDE\_CODE\_SESSION\_ID Unique session ID for hooks and CI tracingNEW

CLAUDE\_CODE\_DISABLE\_ALTERNATE\_SCREEN Opt out of fullscreen rendering (=1)NEW

CLAUDE\_CODE\_DISABLE\_AUTO\_MEMORY

CLAUDE\_CODE\_DISABLE\_1M\_CONTEXT

CLAUDE\_CODE\_PACKAGE\_MANAGER\_AUTO\_UPDATE Auto-upgrade via Homebrew/WinGetNEW

CLAUDE\_CODE\_ENABLE\_AUTO\_MODE Enable auto mode on Bedrock/Vertex/Foundry (=1)NEW



🔧 Skills & Agents

Built-in Skills

Skill tool Discovers built-in slash commands (/init, /review, /security-review…)NEW

/code-review [effort] Code review; `--fix` flag applies findings to working treeNEW

/batch Large parallel changes (5-30 worktrees)

/debug [desc] Troubleshoot from debug log

/loop [interval] Recurring scheduled task

/claude-api Load API + SDK reference

Custom Skill Locations

.claude/skills/<name>/ Project skills

~/.claude/skills/<name>/ Personal skills

Skill Frontmatter

description Auto-invocation trigger

allowed-tools Skip permission prompts

disallowed-tools Block specific tools from skillNEW

model Override model for skill

effort Override effort level

paths: [globs] Path-specific (YAML list)NEW

context: fork Run in subagent

$ARGUMENTS User input placeholder

${CLAUDE\_SKILL\_DIR} Skill's own directory

${CLAUDE\_EFFORT} Current effort level (skill variable)NEW

!`cmd` Dynamic context injection

plugin bin/ Ship executables for Bash toolNEW

Built-in Agents

Explore Fast read-only (Haiku)

Plan Research for plan mode

General Full tools, complex tasks

Bash Terminal separate context

Agent Frontmatter

permissionMode default/acceptEdits/plan/dontAsk/bypassPermissions

isolation: worktree Run in git worktree

memory: user|project|local Persistent memory

background: true Background task

maxTurns Limit agentic turns

initialPrompt Auto-submit first turn

SendMessage Resume agents (replaces resume)

@agent-name Mention named subagentsNEW

🖥️ CLI & Flags

Core Commands

claude Interactive

claude "q" With prompt

claude -p "q" Headless (SDK)

claude -c Continue last

claude -r "n" Resume by ID/name

claude update Update

claude auth login Sign in (--sso, --console)

claude agents List agents

claude mcp MCP config

claude plugin Plugin management

claude plugin init <name> Scaffold new pluginNEW

claude project purge [path] Delete all Claude Code project stateNEW

claude ultrareview [target] Non-interactive code review (PR / branch / path)NEW

Key Flags

--model Set model

-n / --name Session name

--resume, -r Resume session

--continue, -c Continue most recent

--add-dir Add working dir

--agent Use agent

--allowedTools Pre-approve tools

--disallowedTools Remove tools

--allow-danger… Add bypassPerms to ⇧Tab cycle

--output-format text/json/stream-json

--max-budget-usd Cost cap

--remote Web session on claude.ai

--effort low/medium/high/xhigh/max

--permission-mode default/acceptEdits/plan/auto/dontAsk/bypassPermissions

--dangerously-skip-permissions Skip all prompts ⚠️

--debug [filter] Debug logging

--settings <file> Load settings JSON

--from-pr Load PR context (GitHub / GitLab / Bitbucket / GHE)NEW
