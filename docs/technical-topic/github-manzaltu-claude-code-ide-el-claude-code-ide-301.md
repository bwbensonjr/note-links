---
id: 301
url: https://github.com/manzaltu/claude-code-ide.el
title: 'GitHub - manzaltu/claude-code-ide.el: Claude Code IDE integration for Emacs'
domain: github.com
source_date: '2025-08-07'
tags:
- github-repo
- llm
- cli-tool
summary: '**claude-code-ide.el** is an Emacs package that provides native integration
  with Claude Code CLI through the Model Context Protocol (MCP), enabling Claude to
  function as an Emacs-aware AI assistant. The package creates a bidirectional bridge
  between Claude and Emacs, allowing Claude to leverage Emacs'' powerful features
  like LSP, project management, tree-sitter, and custom Elisp functions for more intelligent
  code assistance. Key features include automatic project detection, terminal integration
  with color support, advanced diff viewing with ediff, diagnostic integration, and
  the ability to expose any Emacs command as an MCP tool for context-aware operations.'
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# GitHub - manzaltu/claude-code-ide.el: Claude Code IDE integration for Emacs

Claude Code IDE for Emacs
=========================

[![https://github.com/manzaltu/claude-code-ide.el/workflows/CI/badge.svg](https://github.com/manzaltu/claude-code-ide.el/workflows/CI/badge.svg)](https://github.com/manzaltu/claude-code-ide.el/actions/workflows/test.yml)
[![https://img.shields.io/badge/GNU%20Emacs-28--30-blueviolet.svg](https://camo.githubusercontent.com/8762af5d276e97f37ff86bfa21ad441c9ca45adb05f2840918630adbb16050fe/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f474e55253230456d6163732d32382d2d33302d626c756576696f6c65742e737667)](https://www.gnu.org/software/emacs/)
[![https://img.shields.io/badge/License-GPL%20v3-blue.svg](https://camo.githubusercontent.com/1b0c7e4911720d0444c16a1ffd145a039f14a1a7305362ab51184f757a4dd6bc/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4c6963656e73652d47504c25323076332d626c75652e737667)](https://www.gnu.org/licenses/gpl-3.0)

Overview
========

Claude Code IDE for Emacs provides native integration with Claude Code CLI through the Model Context Protocol (MCP). Unlike simple terminal wrappers, this package creates a bidirectional bridge between Claude and Emacs, enabling Claude to understand and leverage Emacs’ powerful features—from LSP and project management to custom Elisp functions. This transforms Claude into a true Emacs-aware AI assistant that works within your existing workflow and can interact with your entire Emacs ecosystem.

Features
--------

* Automatic project detection and session management
* Terminal integration with full color support using `vterm` or `eat`
* MCP protocol implementation for IDE integration
* Tool support for file operations, editor state, and workspace info
* Extensible MCP tools server for accessing Emacs commands (xrefs, tree-sitter, project info, e.g.)
* Diagnostic integration with Flycheck and Flymake
* Advanced diff view with ediff integration (modify suggestions before applying)
* Tab-bar support for proper context switching
* Selection and buffer tracking for better context awareness

Emacs Tool Integration
----------------------

This package enables Claude Code to leverage the full power of Emacs through MCP tools integration. Claude can directly access and utilize Emacs capabilities including:

* **Language Server Protocol (LSP)** integration through xref commands for intelligent code navigation (eglot, lsp-mode and others)
* **Tree-sitter** for syntax tree analysis and understanding code structure at the AST level
* **Imenu** for structured symbol listing and navigation within files
* **Project** integration for project-aware operations
* **Any Emacs command or function** can be exposed as an MCP tool, allowing Claude to:
  + Perform project-wide searches and refactoring
  + Access specialized modes and their features
  + Execute custom Elisp functions tailored to your workflow

This deep integration means Claude Code understands your project context and can leverage Emacs’ extensive ecosystem to provide more intelligent and context-aware assistance.

Screenshots
-----------

### Active File Awareness

[![](https://github.com/manzaltu/claude-code-ide.el/raw/fb517ac3700f92f8d5481f0bcf9fe4a3c26c91ab/screenshots/file.png)](https://github.com/manzaltu/claude-code-ide.el/blob/fb517ac3700f92f8d5481f0bcf9fe4a3c26c91ab/screenshots/file.png)

*Claude Code automatically knows which file you’re currently viewing in Emacs*

### Code Selection Context

[![](https://github.com/manzaltu/claude-code-ide.el/raw/fb517ac3700f92f8d5481f0bcf9fe4a3c26c91ab/screenshots/selection.png)](https://github.com/manzaltu/claude-code-ide.el/blob/fb517ac3700f92f8d5481f0bcf9fe4a3c26c91ab/screenshots/selection.png)

*Claude Code can access and work with selected text in your buffers*

### Advanced Diff View with Diagnostics

[![](https://github.com/manzaltu/claude-code-ide.el/raw/fb517ac3700f92f8d5481f0bcf9fe4a3c26c91ab/screenshots/ediff_diag.png)](https://github.com/manzaltu/claude-code-ide.el/blob/fb517ac3700f92f8d5481f0bcf9fe4a3c26c91ab/screenshots/ediff_diag.png)

*Integrated ediff view for code changes, with Claude Code able to directly access diagnostic data (errors, warnings, etc.) from opened files*

### Automatic Text Mentions

[![](https://github.com/manzaltu/claude-code-ide.el/raw/fb517ac3700f92f8d5481f0bcf9fe4a3c26c91ab/screenshots/mentions.png)](https://github.com/manzaltu/claude-code-ide.el/blob/fb517ac3700f92f8d5481f0bcf9fe4a3c26c91ab/screenshots/mentions.png)

*Automatically mention and reference selected text in Claude conversations*

### Session Restoration

[![](https://github.com/manzaltu/claude-code-ide.el/raw/fb517ac3700f92f8d5481f0bcf9fe4a3c26c91ab/screenshots/restore.png)](https://github.com/manzaltu/claude-code-ide.el/blob/fb517ac3700f92f8d5481f0bcf9fe4a3c26c91ab/screenshots/restore.png)

*Resume previous Claude Code conversations with the –resume flag*

Installation
============

Prerequisites
-------------

* Emacs 28.1 or higher
* Claude Code CLI installed and available in PATH
* `vterm` or `eat` package (for terminal support)

Installing Claude Code CLI
--------------------------

Follow the installation instructions at [Claude Code Documentation](https://docs.anthropic.com/en/docs/claude-code).

Installing the Emacs Package
----------------------------

Currently, this package is in early development.

To install using `emacs-version` >= 30 and `use-package` with the `vc` binding:

```
(use-package claude-code-ide
  :vc (:url "https://github.com/manzaltu/claude-code-ide.el" :rev :newest)
  :bind ("C-c C-'" . claude-code-ide-menu) ; Set your favorite keybinding
  :config
  (claude-code-ide-emacs-tools-setup)) ; Optionally enable Emacs MCP tools
```

To install using `use-package` and [straight.el](https://github.com/raxod502/straight.el):

```
(use-package claude-code-ide
  :straight (:type git :host github :repo "manzaltu/claude-code-ide.el")
  :bind ("C-c C-'" . claude-code-ide-menu) ; Set your favorite keybinding
  :config
  (claude-code-ide-emacs-tools-setup)) ; Optionally enable Emacs MCP tools
```

### Doom Emacs

In `packages.el`:

```
(package! claude-code-ide
  :recipe (:host github :repo "manzaltu/claude-code-ide.el"))
```

In `config.el`:

```
(use-package! claude-code-ide
  :bind ("C-c C-'" . claude-code-ide-menu) ; Set your favorite keybinding
  :config
  (claude-code-ide-emacs-tools-setup)) ; Optionally enable Emacs MCP tools
```

After saving the above, run: `doom sync` in the terminal.

Usage
=====

Basic Commands
--------------

The easiest way to interact with Claude Code IDE is through the transient menu interface, which provides visual access to all available commands. Simply run `M-x claude-code-ide-menu` to open the interactive menu.

| Command | Description |
| --- | --- |
| `M-x claude-code-ide-menu` | Open transient menu with all Claude Code commands |
| `M-x claude-code-ide-emacs-tools-setup` | Set up built-in MCP tools (e.g. xref, project) |
| `M-x claude-code-ide` | Start Claude Code for the current project |
| `M-x claude-code-ide-send-prompt` | Send prompt to Claude from minibuffer input |
| `M-x claude-code-ide-continue` | Continue most recent conversation in directory |
| `M-x claude-code-ide-resume` | Resume Claude Code with previous conversation |
| `M-x claude-code-ide-stop` | Stop Claude Code for the current project |
| `M-x claude-code-ide-switch-to-buffer` | Switch to project’s Claude buffer |
| `M-x claude-code-ide-list-sessions` | List all active Claude Code sessions and switch |
| `M-x claude-code-ide-check-status` | Check if Claude Code CLI is installed and working |
| `M-x claude-code-ide-insert-at-mentioned` | Send selected text to Claude prompt |
| `M-x claude-code-ide-send-escape` | Send escape key to Claude terminal |
| `M-x claude-code-ide-insert-newline` | Insert newline in Claude prompt (sends \ + Enter) |
| `M-x claude-code-ide-toggle` | Toggle visibility of Claude Code window |
| `M-x claude-code-ide-toggle-recent` | Toggle most recent Claude window globally |
| `M-x claude-code-ide-show-debug` | Show the debug buffer with WebSocket messages |
| `M-x claude-code-ide-clear-debug` | Clear the debug buffer |

Multi-Project Support
---------------------

Claude Code IDE automatically detects your project using Emacs’ built-in `project.el`. Each project gets its own Claude Code instance with a unique buffer name like `*claude-code[project-name]*`.

You can run multiple Claude Code instances simultaneously for different projects. Use `claude-code-ide-list-sessions` to see all active sessions and switch between them.

Window Management
-----------------

* Running `claude-code-ide` when a session is already active will toggle the window visibility
* The window can be closed with standard Emacs window commands (`C-x 0`) without stopping Claude
* Use `claude-code-ide-toggle-recent` to toggle the most recent Claude window from anywhere, regardless of your current project context. This is useful when you’re outside a project directory but want to quickly hide/show Claude

Diff Viewing with Ediff
-----------------------

When `claude-code-ide-use-ide-diff` is enabled (default), Claude’s code suggestions are displayed using Emacs’ powerful `ediff` interface. This provides two key advantages:

1. **Visual diff comparison** - See exactly what Claude wants to change with side-by-side or unified diff views
2. **Interactive editing** - You can modify Claude’s suggestions before applying them

### How to use ediff:

1. When Claude suggests code changes, `ediff` opens automatically
2. The ediff control buffer becomes active (a small window with ediff commands)
3. Buffer A shows the current code, Buffer B shows Claude’s suggestion
4. You can modify Buffer B to refine Claude’s proposed changes
5. Press `q` in the ediff control buffer to quit
6. When prompted, choose whether to accept the changes (`y` or `n`)
7. If you accept (`y`), any changes from Buffer B will be sent back to Claude to be applied on the original file

This allows you to refine Claude’s suggestions before they’re applied, ensuring the final code meets your exact requirements.

Configuration
-------------

### Configuration Variables

| Variable | Description | Default |
| --- | --- | --- |
| `claude-code-ide-cli-path` | Path to Claude Code CLI | `"claude"` |
| `claude-code-ide-buffer-name-function` | Function for buffer naming | `claude-code-ide--default-buffer-name` |
| `claude-code-ide-cli-debug` | Enable CLI debug mode (-d flag) | `nil` |
| `claude-code-ide-cli-extra-flags` | Additional CLI flags (e.g. “–model”) | `""` |
| `claude-code-ide-debug` | Enable debug logging | `nil` |
| `claude-code-ide-terminal-backend` | Terminal backend (vterm or eat) | `'vterm` |
| `claude-code-ide-vterm-anti-flicker` | Enable vterm flicker reduction | `t` |
| `claude-code-ide-vterm-render-delay` | vterm render batching delay (seconds) | `0.005` |
| `claude-code-ide-terminal-initialization-delay` | Initialization delay for terminals | `0.1` |
| `claude-code-ide-log-with-context` | Include session context in log messages | `t` |
| `claude-code-ide-debug-buffer` | Buffer name for debug output | `"*claude-code-ide-debug*"` |
| `claude-code-ide-use-side-window` | Use side window vs regular buffer | `t` |
| `claude-code-ide-window-side` | Side for Claude window | `'right` |
| `claude-code-ide-window-width` | Body width for side windows (left/right) | `100` |
| `claude-code-ide-window-height` | Height for side windows (top/bottom) | `20` |
| `claude-code-ide-focus-on-open` | Focus Claude window when opened | `t` |
| `claude-code-ide-focus-claude-after-ediff` | Focus Claude window after opening ediff | `t` |
| `claude-code-ide-show-claude-window-in-ediff` | Show Claude window during ediff | `t` |
| `claude-code-ide-use-ide-diff` | Use IDE diff viewer instead of terminal | `t` |
| `claude-code-ide-switch-tab-on-ediff` | Switch to Claude’s tab when opening ediff | `t` |
| `claude-code-ide-system-prompt` | Custom system prompt to append | `nil` |
| `claude-code-ide-enable-mcp-server` | Enable MCP tools server | `nil` |
| `claude-code-ide-mcp-server-port` | Port for MCP tools server | `nil` (auto-select) |
| `claude-code-ide-mcp-server-tools` | Alist of exposed Emacs functions | `nil` |
| `claude-code-ide-diagnostics-backend` | Diagnostics backend (auto/flycheck/flymake) | `'auto` |
| `claude-code-ide-no-flicker` | Enable flicker-free terminal renderer | `nil` |
| `claude-code-ide-prevent-reflow-glitch` | Prevent terminal reflow glitch (bug #1422) | `t` |
| `claude-code-ide-enable-execute-code` | Allow model to evaluate Elisp in Emacs | `t` |

### Side Window Configuration

Claude Code buffers open in a side window by default. You can customize the placement:

```
;; Open Claude on the left side
(setq claude-code-ide-window-side 'left)

;; Open Claude at the bottom with custom height
(setq claude-code-ide-window-side 'bottom
      claude-code-ide-window-height 30)

;; Open Claude on the right with custom width
(setq claude-code-ide-window-side 'right
      claude-code-ide-window-width 100)

;; Don't automatically focus the Claude window
(setq claude-code-ide-focus-on-open nil)

;; Keep focus on ediff control window when opening diffs
(setq claude-code-ide-focus-claude-after-ediff nil)

;; Hide Claude window during ediff for more screen space
(setq claude-code-ide-show-claude-window-in-ediff nil)

;; Disable IDE diff viewer to show diffs in terminal instead
(setq claude-code-ide-use-ide-diff nil)
```

Or, if you’d prefer to use a regular window:

```
;; Use regular window instead of side window
(setq claude-code-ide-use-side-window nil)
```

### Terminal Backend Configuration

Claude Code IDE supports both `vterm` and `eat` as terminal backends. By default, it uses `vterm`, but you can switch to `eat` if preferred:

```
;; Use eat instead of vterm
(setq claude-code-ide-terminal-backend 'eat)

;; Or switch back to vterm (default)
(setq claude-code-ide-terminal-backend 'vterm)
```

The `eat` backend is a pure Elisp terminal emulator that may work better in some environments where `vterm` compilation is problematic. Both backends provide full terminal functionality including color support and special key handling.

#### Flicker-Free Renderer (Experimental)

Claude Code includes an experimental alternative terminal renderer that eliminates flickering. To enable it:

```
(setq claude-code-ide-no-flicker t)
```

Note that with this renderer, normal Emacs buffer scrolling and search (`C-s`, `C-r`) will not work in the terminal buffer. Instead, use Claude Code’s built-in keybindings:

* `C-o j` / `C-o k` - Scroll up/down through the transcript
* `C-o /` - Search the transcript

#### vterm Rendering Optimization

Claude Code IDE includes intelligent flicker reduction for vterm terminals to provide smoother visual output:

```
;; Enable/disable vterm anti-flicker optimization (enabled by default)
(setq claude-code-ide-vterm-anti-flicker t)

;; Adjust the render delay for batching updates (default is 0.005 seconds)
(setq claude-code-ide-vterm-render-delay 0.01)  ; Increase for smoother but less responsive
```

This optimization detects rapid terminal redraw sequences (like when Claude expands text areas) and batches them for smoother rendering. The 5ms default delay provides optimal visual quality with imperceptible latency.

#### Terminal Initialization Delay

Claude Code IDE includes a brief initialization delay when launching terminals to ensure proper layout rendering:

```
;; Adjust the terminal initialization delay (default is 0.1 seconds)
(setq claude-code-ide-terminal-initialization-delay 0.15)

;; Or disable it entirely (may cause visual glitches)
(setq claude-code-ide-terminal-initialization-delay 0)
```

This delay prevents display artifacts such as misaligned prompts and incorrect cursor positioning that can occur when terminal emulation is initializing. The default 100ms delay is imperceptible but ensures reliable terminal startup.

#### Terminal Keybindings

Claude Code IDE adds custom keybindings to the terminal for easier interaction:

| Keybinding | Command | Description |
| --- | --- | --- |
| `M-RET` | `claude-code-ide-insert-newline` | Insert a newline in the prompt |
| `C-<escape>` | `claude-code-ide-send-escape` | Send escape key to cancel operations |

These keybindings are automatically set up for both `vterm` and `eat` backends and only apply within Claude Code terminal buffers.

#### Terminal Reflow Glitch Prevention (Temporary)

Claude Code IDE includes a temporary workaround for a known Claude Code bug ([#1422](https://github.com/anthropics/claude-code/issues/1422)) where terminal reflows during window resizes can cause uncontrollable scrolling. This workaround is enabled by default but can be disabled if needed:

```
;; Disable the terminal reflow glitch prevention (not recommended until bug is fixed)
(setq claude-code-ide-prevent-reflow-glitch nil)
```

The workaround will be removed once the upstream bug is fixed.

### Diagnostics Configuration

Claude Code IDE supports both Flycheck and Flymake for code diagnostics. By default, it will automatically detect which one is active:

```
;; Let Claude Code automatically detect the active diagnostics backend
(setq claude-code-ide-diagnostics-backend 'auto) ; default

;; Or force a specific backend
(setq claude-code-ide-diagnostics-backend 'flycheck)
(setq claude-code-ide-diagnostics-backend 'flymake)
```

### Elisp Code Execution

Claude Code can evaluate Elisp expressions directly in your running Emacs session via the `executeCode` MCP tool. This is enabled by default.

To disable it:

```
(setq claude-code-ide-enable-execute-code nil)
```

### Custom Buffer Naming

You can customize how Claude Code buffers are named:

```
(setq claude-code-ide-buffer-name-function
      (lambda (directory)
        (if directory
            (format "*Claude:%s*" (file-name-nondirectory (directory-file-name directory)))
          "*Claude:Global*")))
```

### Custom CLI Flags

You can pass additional flags to the Claude Code CLI:

```
;; Use a specific model
(setq claude-code-ide-cli-extra-flags "--model opus")

;; Pass multiple flags
(setq claude-code-ide-cli-extra-flags "--model opus --no-cache")

;; Flags are added to all Claude Code sessions
```

Note: These flags are appended to the Claude command after any built-in flags like `-d` (debug) or `-r` (resume).

### Custom System Prompt

You can append a custom system prompt to Claude’s default prompt, allowing you to customize Claude’s behavior for specific projects or contexts:

```
;; Set a custom system prompt
(setq claude-code-ide-system-prompt "You are an expert in Elisp and Emacs development.")

;; Or configure it per-project using dir-locals.el
;; In .dir-locals.el:
((nil . ((claude-code-ide-system-prompt . "Focus on functional programming patterns and avoid mutations."))))

;; Set via the transient menu: M-x claude-code-ide-menu → Configuration → Set system prompt
```

When set, this adds the `--append-system-prompt` flag to the Claude command. Set to `nil` to disable (default).

### Debugging

#### Claude CLI Debug Mode

To enable debug mode for Claude Code CLI (passes the `-d` flag):

```
(setq claude-code-ide-cli-debug t)
```

#### Emacs Debug Logging

To enable debug logging within Emacs (logs WebSocket messages and JSON-RPC communication):

```
(setq claude-code-ide-debug t)
```

Then view debug logs with:

* `M-x claude-code-ide-show-debug` - Show the debug buffer
* `M-x claude-code-ide-clear-debug` - Clear the debug buffer

The debug buffer shows:

* WebSocket connection events
* All JSON-RPC messages (requests/responses)
* Error messages and diagnostics
* General debug information with session context

Multiple Claude Code Instances on One Project
---------------------------------------------

Using git worktrees is the recommended way for running multiple Claude Code instances on different branches of the same project. This allows you to develop features or fix bugs in parallel:

```
# Create a new worktree for a feature branch
git worktree add ../myproject-worktree feature-branch
```

```
;; Start Claude Code in the main project
find-file /path/to/myproject
M-x claude-code-ide

;; Start another Claude Code instance in the worktree
find-file /path/to/myproject-worktree
M-x claude-code-ide
```

Each worktree is treated as a separate project by `project.el`, allowing you to have independent Claude Code sessions with their own buffers (e.g., `*claude-code[myproject]*` and `*claude-code[myproject-worktree]*`).

Emacs MCP Tools
---------------

Claude Code IDE includes built-in MCP tools that expose Emacs functionality to Claude, enabling powerful code navigation and analysis capabilities:

### Built-in Tools

* `xref-find-references` - Find all references to a symbol throughout the project
* `xref-find-apropos` - Find symbols matching a pattern across the entire project
* `treesit-info` - Get tree-sitter syntax tree information for deep code structure analysis
* `imenu-list-symbols` - List all symbols (functions, classes, variables) in a file using imenu
* `project-info` - Get information about the current project (directory, files, etc.)

### Enabling MCP Tools

To enable these tools, add to your configuration:

```
;; Set up the built-in Emacs tools
(claude-code-ide-emacs-tools-setup)
```

Once enabled, Claude can use these tools to navigate your codebase. For example:

* “Find the definition of function foo”
* “Show me all places where this variable is used”
* “What type of AST node is under the cursor?”
* “Analyze the parse tree of this entire file”
* “List all functions and variables in this file”
* “How many files are in this project?”

Creating Custom MCP Tools
-------------------------

You can expose your own Emacs functions to Claude through the MCP tools system. This allows Claude to interact with specialized Emacs features, custom commands, or domain-specific functionality.

### Tool Definition Format

Define tools using the `claude-code-ide-make-tool` function:

```
(claude-code-ide-make-tool
 :function #'function-name     ; The Emacs function to call
 :name "tool_name"             ; Name for Claude to use (snake_case recommended)
 :description "..."            ; Human-readable description
 :args '((:name "param1"       ; List of argument specifications
          :type string         ; Type: string, number, integer, boolean, etc.
          :description "..."   ; What this parameter does
          :optional t)))       ; Optional parameters marked with :optional t
```

Available argument types: `string`, `number`, `integer`, `boolean`, `array`, `object`, `null`

### Context-Aware Tool Example

```
;; Define a context-aware function that operates in the session's project
(defun my-project-grep (pattern)
  "Search for PATTERN in the current session's project."
  (claude-code-ide-mcp-server-with-session-context nil
    ;; This executes with the session's project directory as default-directory
    (let* ((project-dir default-directory)
           (results (shell-command-to-string
                    (format "rg -n '%s' %s" pattern project-dir))))
      results)))

;; Define and register the tool (automatically added to claude-code-ide-mcp-server-tools)
(claude-code-ide-make-tool
 :function #'my-project-grep
 :name "my_project_grep"
 :description "Search for pattern in project files"
 :args '((:name "pattern"
          :type string
          :description "Pattern to search for")))

;; Enable Emacs tool MCP server
(claude-code-ide-emacs-tools-setup)
```

The `claude-code-ide-mcp-server-with-session-context` macro ensures your tool executes in the correct project context.

License
=======

This project is licensed under the GNU General Public License v3.0 or later. See the LICENSE file for details.

Trademark Notice
================

Claude® is a registered trademark of Anthropic, PBC. Claude Code is an application developed by Anthropic, PBC.

Related Projects
================

* [Claude Code CLI](https://docs.anthropic.com/en/docs/claude-code)
* [Claude Code VS Code Extension](https://github.com/anthropics/claude-code)
* [claudecode.nvim](https://github.com/coder/claudecode.nvim) - Neovim integration
