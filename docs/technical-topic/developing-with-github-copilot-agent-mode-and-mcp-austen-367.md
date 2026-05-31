---
id: 367
url: https://austen.info/blog/github-copilot-agent-mcp/
title: Developing with GitHub Copilot Agent Mode and MCP | Austen Stone
domain: austen.info
source_date: '2025-07-04'
tags:
- llm
- web-dev
- tutorial
- cli-tool
summary: GitHub Copilot Agent Mode combined with Model Context Protocol (MCP) significantly
  enhances development efficiency by allowing developers to customize AI responses
  through VS Code settings, custom instructions, and specialized chat modes. The author
  configures Copilot with auto-approval features, language-specific context, and integrates
  multiple MCP servers (like Playwright, SearXNG, and GitHub) to extend the agent's
  capabilities beyond code generation. This setup enables structured workflows such
  as a "research mode" that leverages web search, sequential thinking, and repository
  management tools to automate complex development tasks.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# Developing with GitHub Copilot Agent Mode and MCP | Austen Stone

I'm always looking for ways to work more efficiently and deliver better code faster. Recently, The [GitHub Copilot Agent Mode](https://code.visualstudio.com/blogs/2025/04/07/agentMode) in combination with [Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction) has transformed my development workflow.

Customizing Copilot[​](#Customizing-Copilot "Direct link to Customizing Copilot")
---------------------------------------------------------------------------------

The magic starts with [Customizing AI responses in VS Code](https://code.visualstudio.com/docs/copilot/copilot-customization). Instead of repeatedly explaining my preferences to the AI, I can now define:

* **Custom instructions** for consistent coding practices
* **Custom prompts** for reusable task templates
* **Custom chat modes** with specific tool configurations

This foundation allows me to create specialized AI assistants for different phases of development.

### VS Code Settings[​](#VS-Code-Settings "Direct link to VS Code Settings")

Here are [my VS Code settings](https://github.com/austenstone/.vscode). I have enabled experimental features and changed some settings to allow the agent to run without my intervention.

Details

VS Code Settings
View the most recent settings in [my VS Code settings](https://github.com/austenstone/.vscode)

settings.json

```
{  
  "github.copilot.nextEditSuggestions.enabled": true,  
  "github.copilot.enable": {  
    "*": true  
  },  
  "github.copilot.renameSuggestions.triggerAutomatically": true,  
  "github.copilot.editor.enableCodeActions": true,  
  "github.copilot.chat.startDebugging.enabled": true,  
  "github.copilot.chat.codeGeneration.instructions": [  
    {  
      "file": ".copilot-instructions.md"  
    },  
    {  
      "text": "Prefer to use TypeScript over Javascript"  
    },  
    {  
      "text": "My github username is austenstone."  
    }  
  ],  
  "github.copilot.chat.testGeneration.instructions": [],  
  "github.copilot.chat.reviewSelection.instructions": [],  
  "github.copilot.chat.commitMessageGeneration.instructions": [  
    {  
      "file": ".copilot-commit-message-instructions.md"  
    },  
    {  
      "text": "Keep the commit message short and concise. Use imperative mood and avoid unnecessary details."  
    }  
  ],  
  "github.copilot.chat.reviewSelection.enabled": true,  
  "github.copilot.chat.setupTests.enabled": true,  
  "github.copilot.chat.useProjectTemplates": true,  
  "github.copilot.chat.generateTests.codeLens": true,  
  "github.copilot.chat.edits.temporalContext.enabled": true,  
  "github.copilot.chat.languageContext.typescript.enabled": true,  
  "github.copilot.chat.completionContext.typescript.mode": "sidecar",  
  "github.copilot.chat.editor.temporalContext.enabled": true,  
  "github.copilot.chat.codesearch.enabled": true,  
  "github.copilot.chat.newWorkspaceCreation.enabled": true,  
  "github.copilot.chat.agent.thinkingTool": true,  
  "github.copilot.nextEditSuggestions.fixes": true,  
  "github.copilot.chat.languageContext.fix.typescript.enabled": true,  
  "github.copilot.chat.languageContext.inline.typescript.enabled": true,  
  "github.copilot.chat.notebook.followCellExecution.enabled": true,  
  "chat.editing.autoAcceptDelay": 5, // Delay in seconds before automatically accepting edits  
  "chat.tools.autoApprove": true, // Automatically approve run commands and tool requests  
  "chat.agent.maxRequests": 100, // Maximum iterations before asking to continue  
  "chat.renderRelatedFiles": true,  
  "chat.setup.continueLaterIndicator": true,  
  "inlineChat.enableV2": true,  
  "inlineChat.hideOnRequest": true,  
  "inlineChat.finishOnType": true,  
  "inlineChat.lineEmptyHint": true,  
  "mcp": {  
    "servers": {  
      "playwright": { // Useful for operating browser  
        "command": "npx",  
        "args": [  
          "@playwright/mcp@latest"  
        ]  
      },  
      "serena": { // An entirely separate coding assistant than copilot  
        "command": "uvx",  
        "args": [  
          "--from",  
          "git+https://github.com/oraios/serena",  
          "serena-mcp-server.exe"  
        ]  
      },  
      "time": { // Get the current time  
        "command": "uvx",  
        "args": [  
          "mcp-server-time",  
          "--local-timezone",  
          "America/New_York"  
        ]  
      },  
      "searxng": { // Search the web using SearxNG  
        "command": "npx",  
        "args": [  
          "-y",  
          "mcp-searxng"  
        ],  
        "env": {  
          "SEARXNG_URL": "http://localhost/"  
        }  
      },  
      "sequential-thinking": { // Sequential thinking tool for reasoning  
        "command": "npx",  
        "args": [  
          "-y",  
          "@modelcontextprotocol/server-sequential-thinking"  
        ]  
      },  
      "supabase": { // Supabase tool for database operations  
        "command": "npx",  
        "args": [  
          "-y",  
          "@supabase/mcp-server-supabase@latest",  
          "--read-only"  
        ],  
        "env": {  
          "SUPABASE_ACCESS_TOKEN": "${env:SUPABASE_ACCESS_TOKEN}"  
        }  
      },  
      "github": { // Interact with the GitHub platform  
        "url": "https://api.githubcopilot.com/mcp/",  
        "headers": {  
          "Authorization": "Bearer ${input:github_mcp_pat}"  
        }  
      }  
    },  
    "inputs": [  
      {  
        "type": "promptString",  
        "id": "github_mcp_pat",  
        "description": "GitHub Personal Access Token",  
        "password": true  
      }  
    ]  
  }  
}
```

* `github.copilot.chat.codeGeneration.instructions` - I have custom instructions personal to me
* `chat.agent.maxRequests` - Let's me allow the agent to run longer without asking for permission
* `chat.tools.autoApprove` - Automatically approves run commands and tool requests from the agent

[GitHub Copilot in VS Code settings reference](https://code.visualstudio.com/docs/copilot/reference/copilot-settings#_chat-settings)

### MCP Tools[​](#MCP-Tools "Direct link to MCP Tools")

The [Using Model Context Protocol (MCP) in VS Code](https://code.visualstudio.com/docs/copilot/chat/mcp-servers) allows me to provide the agent with access to external tools and data sources.

Some of the MCP servers I use include:

* [Sequential Thinking](https://github.com/modelcontextprotocol/servers/blob/main/src/sequentialthinking) - Dynamic and reflective problem-solving through thought sequences
* [SearXNG](https://github.com/ihor-sokoliuk/mcp-searxng) - Integrates the SearXNG API, providing web search capabilities.
* [Playwright](https://github.com/executeautomation/mcp-playwright) - This MCP Server will help you run browser automation and webscraping using Playwright
* [GitHub](https://github.com/modelcontextprotocol/servers-archived/tree/main/src/github) - Repository management, file operations, and GitHub API integration
* [time](https://github.com/modelcontextprotocol/servers/blob/main/src/time) - For getting the current time and date
* [Fetch](https://code.visualstudio.com/docs/copilot/chat/mcp-servers#fetch) - Web content fetching and conversion for efficient LLM usage

The repo [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) contains a list of available MCP servers.

Development Workflow[​](#Development-Workflow "Direct link to Development Workflow")
------------------------------------------------------------------------------------

### Research[​](#Research "Direct link to Research")

Before diving into coding, I often need to research new concepts or technologies. For this, I use a custom chat mode called `research` that includes tools like web search, and sequential thinking.

Research Chat Mode

research.chatmode.md

```
---  
description: 'Research mode for gathering information and analyzing topics in depth.'  
tools: ['changes', 'codebase', 'extensions', 'fetch', 'findTestFiles', 'githubRepo', 'new', 'openSimpleBrowser', 'problems', 'runCommands', 'runNotebooks', 'runTasks', 'search', 'searchResults', 'terminalLastCommand', 'terminalSelection', 'testFailure', 'usages', 'vscodeAPI', 'playwright', 'time', 'get_current_time', 'searxng', 'searxng_web_search', 'web_url_read', 'sequential-thinking', 'supabase', 'list_branches', 'github', 'list_branches', 'list_code_scanning_alerts', 'list_commits', 'list_issues', 'list_notifications', 'list_pull_requests', 'list_secret_scanning_alerts', 'list_tags', 'search_code', 'search_issues', 'search_repositories', 'search_users', 'sequentialthinking']  
---  
  
Activate research mode.  
  
Your task is to research and gather information about a specific topic.  
  
# Tools  
Use tools to gather information and do research. Use the `sequential-thinking` tool for complex problems requiring deep analysis and multi-step reasoning.  
- Use the `sequentialthinking` tool for complex problems requiring deep analysis and multi-step reasoning.  
- Use search tools  
  - Use `searxng_web_search` to search the web for broad, initial keyword-based web searches to discover relevant URLs.  
  - Use the `web_url_read` tool when you have a direct URL and need to quickly extract the raw text or content of a page.  
  - Use the `fetch` tool as an alternative to web_url_read, potentially for more complex requests.  
- Use the `playwright` tool to interact with web pages and gather information from the browser. Use to get CSS and style information.  
  
# 1. Strategic Planning (DO THIS FIRST)  
Use the sequential-thinking `sequentialthinking` tool to outline your research strategy. Identify keywords, potential information sources, and the steps you will take.  
  
# 2. Information Gathering & Analysis (THINGS YOU MUST DO)  
- When you don't understand a term or topic search the web using tools like `searxng_web_search` or `web_url_read` to gather more information.  
- Use all available tools to gather information and do research.  
- Continue using tools to gather information until you've fully researched the topic or problem.  
- Synthesize and summarize findings at key intervals. After gathering information from multiple sources, take a moment to synthesize what you've learned before proceeding.  
- When you're done use `sequentialthinking` to ask yourself if you've gathered enough information to answer the question or solve the problem.  
  
# 3. Concluding the Research (DO THIS LAST)  
- Use sequential-thinking to ask yourself: "Have I gathered sufficient, well-verified information to thoroughly address the user's request?"  
- Provide a final, structured response that includes:  
  - A direct answer to the core question.  
  - A summary of key findings with linked sources.  
  
# DO NOT (THINGS YOU MUST NOT DO)  
- Do not write actual code!  
- Do not make assumptions without verifying them through research or analysis.  
- Do not skip steps in the analysis process; always think step by step.  
- Do not rush to conclusions; take the time to explore different angles and gather sufficient information.  
- Do not stop until you have a comprehensive understanding of the topic or problem.
```

### Planning[​](#Planning "Direct link to Planning")

I start every project in a [custom chat mode](https://code.visualstudio.com/docs/copilot/chat/chat-modes) called `plan` that I have in my user space. The tools I want for are already selected and copilot can't edit my code even if it wanted to because I took away that tool. I find `Gemini 2.5 Pro` to be the best model for planning.

Plan Chat Mode

plan.chatmode.md

```
---  
description: 'Generate comprehensive implementation plans for features, refactoring, and bug fixes without making code changes.'  
tools: ['changes', 'codebase', 'editFiles', 'extensions', 'fetch', 'findTestFiles', 'githubRepo', 'problems', 'runCommands', 'search', 'searchResults', 'usages', 'vscodeAPI', 'time', 'get_current_time', 'searxng', 'sequential-thinking']  
---  
  
Activate planning mode.  
  
Your task is to think about and generate an implementation plan for a new feature or for refactoring existing code.  
  
# Planning mode instructions  
Don't make any code edits, just generate a plan.  
  
# Instructions  
1. **Gather Context**: Use the `codebase` tool to analyze the current codebase, including existing features, architecture, and dependencies. Use the `changes` tool to identify recent changes that may impact the new feature or refactoring task.  
2. **Research**: Use the `searxng_web_search` and `web_url_read` tools to gather information about best practices, design patterns, and similar implementations. This will help you understand how to approach the new feature or refactoring task effectively.  
3. **Plan Structure**: Create a structured plan.  
4. Repeat the process iteratively, refining your understanding and plan as you gather more information.  
  
# Output  
The plan consists of a Markdown document that describes the implementation plan, including the following sections:  
* Overview: A brief description of the feature or refactoring task.  
* Requirements: A list of requirements for the feature or refactoring task.  
* Implementation Steps: A detailed list of steps to implement the feature or refactoring task.  
* Testing: A list of tests that need to be implemented to verify the feature or refactoring task.  
  
# What You MUST Do:  
- Use tools to gather information and analyze the codebase before planning.  
- Use existing context and information from previous conversations to inform your planning.  
- Always gather comprehensive context before planning  
- Think through edge cases and potential complications  
- Plan for comprehensive testing at each phase  
- Document assumptions and decision rationale  
- Structure plans for easy team comprehension and execution  
- Consider backward compatibility and migration paths  
  
# What You MUST NOT Do:  
- Never write actual code or implementation details  
- Never modify files or make changes to the codebase  
- Never provide large code snippets or complete implementations  
- Never skip the analysis phase and jump directly to solutions  
- Never assume requirements without clarification  
  
# 3. Tool Usage Guidelines  
Use tools to help create implementation plan. Use the `sequential-thinking` tool for complex problems requiring deep analysis and multi-step reasoning.  
- Use the `sequentialthinking` tool for complex problems requiring deep analysis and multi-step reasoning.  
- Use search tools  
  - Use `searxng_web_search` to search the web for broad, initial keyword-based web searches to discover relevant URLs.  
  - Use the `web_url_read` tool when you have a direct URL and need to quickly extract the raw text or content of a page.  
  - Use the `fetch` tool as an alternative to web_url_read, potentially for more complex requests.  
- Use the `playwright` tool to interact with web pages and gather information from the browser. Use to get CSS and style information.  
- Use the `editFiles` tool to create prompt files in `.github/prompts` directory with the name `<name>.prompt.md` for planning and implementation. ONLY USE THIS TOOL TO CREATE PROMPT FILES.  
  
Think step by step through each planning phase, and always prioritize thorough analysis over speed. For complex problems that require deep reasoning, evolving understanding, or exploration of multiple approaches, utilize the sequential-thinking tool to maintain context and generate well-reasoned solutions. A well-researched plan prevents costly implementation mistakes and ensures successful project outcomes.
```

Prompt Creation Prompt

copilot-prompt.prompt.md

```
---  
mode: agent  
description: "Prompt files are standalone prompts that you can run directly in chat. They describe the task to be performed (what should be done)."  
---  
  
Create a prompt file in the `.github/prompts` directory that implements all previous conversation and context.  
  
Add as much context and information as possible.  
  
# Information  
  
## Prompt files  
Define reusable prompts for common tasks like generating code or performing a code review. Prompt files are standalone prompts that you can run directly in chat. They describe the task to be performed (what should be done). Optionally, you can include tasks-specific guidelines about how the task should be performed, or you can reference custom instructions in the prompt file.  
  
## Prompt file structure  
  
A prompt file is a Markdown file with the .prompt.md file suffix. It has the following two main sections:  
  
- (Optional) Header with metadata (Front Matter syntax)  
  - mode: The chat mode to use when running the prompt: ask, edit, or agent (default).  
  - description: A short description of the prompt.  
- Body with the prompt content  
  - Prompt files mimic the format of writing prompts in chat. This allows blending natural language instructions, additional context, and even linking to other prompt files as dependencies. You can use Markdown formatting to structure the prompt content, including headings, lists, and code blocks.  
  
You can reference other workspace files, prompt files, or instructions files by using Markdown links. Use relative paths to reference these files, and ensure that the paths are correct based on the location of the prompt file.  
  
Within a prompt file, you can reference variables by using the ${variableName} syntax. You can reference the following variables:  
  
- Workspace variables - ${workspaceFolder}, ${workspaceFolderBasename}  
- Selection variables - ${selection}, ${selectedText}  
- File context variables - ${file}, ${fileBasename}, ${fileDirname}, ${fileBasenameNoExtension}  
- Input variables - ${input:variableName}, ${input:variableName:placeholder} (pass values to the prompt from the chat input field)  
  
# Example  
  
```  
---  
mode: 'agent'  
description: ''  
---  
<content goes here>  
```
```

The goal of this phase is to generate a comprehensive `.prompt.md` file in `.github/prompts/` that serves as a detailed blueprint for the implementation.

tip

You can use the Command Palette (`ctrl+shift+p`) in VS Code to quickly create new chat modes and prompts.

### Implementation[​](#Implementation "Direct link to Implementation")

Once I have my planning prompt ready, I switch to regular agent mode with Claude Sonnet 4 and simply run `/prompt-name`. The beauty of this approach is that the AI has all the context it needs to execute the plan methodically.

The prompt file acts as a contract between the planning phase and implementation phase, ensuring consistency and reducing the need for back-and-forth clarification.

#### Course Correction[​](#Course-Correction "Direct link to Course Correction")

If the agent is close I will sometimes pause it and ask it to look at a specific resource or document to help it understand the problem better.

When the agent deviates from the desired behavior (which occasionally happens), I have a simple recovery process:

1. Clear my git diff to reset the changes
2. Modify the prompt file based on what I learned
3. Restart the implementation from scratch

This iterative refinement of prompts means I'm constantly improving my templates for future use.

### Validation[​](#Validation "Direct link to Validation")

Finally (or maybe first if we're following TDD) I want to ensure the implementation works as expected. Ideally our output is testable but sometimes this is hard.

For browser interactions, I use the `playwright` MCP tool to automate testing. This is really cool because the agent can use a browser just like I can! This lets it understand how the UI works and what it looks like.

Example[​](#Example "Direct link to Example")
---------------------------------------------

Let's walk though a real-world example. I want to add comments to my blog you're viewing right now.

### 1. Research[​](#1-Research "Direct link to 1. Research")

I start by in [`research`](#Research) mode using Gemini 2.5 Pro with a question:

```
How would I add comments to my blog posts in this Docusaurus site?
```

Copilot starts by using `sequentialthinking` think about how to perform research

sequentialthinking

```
{  
  "nextThoughtNeeded": true,  
  "thought": "I need to research how to add comments to a Docusaurus blog. I will start by searching for \"Docusaurus blog comments\" and analyze the results. I will look for official documentation and popular third-party solutions like Giscus, Disqus, or Utterances. Finally, I will synthesize the findings to provide a clear recommendation.",  
  "thoughtNumber": 1,  
  "totalThoughts": 2  
}
```

Then Copilot starts searching the web using `searxng_web_search` and `web_url_read` tools.

searxng\_web\_search

```
{  
  "query": "Docusaurus blog comments"  
}
```

It comes up with the idea to use Giscus as a commenting service.

> To add comments to your Docusaurus blog, you'll need to use a third-party commenting service because Docusaurus generates a static site. A highly recommended option that integrates perfectly with your existing GitHub-based project is Giscus.

[Full chat export](https://github.com/austenstone/portfolio/blob/main/blog/2025-06-30-github-copilot-agent-mcp/_prompts/chat1.json)

### 2. Planning[​](#2-Planning "Direct link to 2. Planning")

Now I switch to [`plan`](#Planning) chat mode.

```
Create a plan based on your research
```

Copilot comes up with a structured plan for me.

### 3. Implementation[​](#3-Implementation "Direct link to 3. Implementation")

Now I switch to regular `agent` mode.

We're going to reuse our prompt file from earlier to write the plan as a `.prompt.md` file.

```
/copilot-prompt
```

Copilot creates the `.github/prompts/implement-giscus.prompt.md` file.

Now I can switch to Claude Sonnet 4 and run the generated prompt file.

```
/implement-giscus
```

[Full chat export](https://github.com/austenstone/portfolio/blob/main/blog/2025-06-30-github-copilot-agent-mcp/_prompts/chat1.json)

#### Course Correction[​](#Course-Correction-1 "Direct link to Course Correction")

I'm watching the agent work and it got hung up on how to pass front matter metadata to the Giscus component.

I paused and asked it to look at document on the topic

```
look at how blog posts can do front matter  
https://docusaurus.io/docs/api/plugins/@docusaurus/plugin-content-blog#markdown-front-matter
```

Copilot looked at my resource and found even more resources to help it understand how to access blog post metadata.

> I'll examine how to properly access blog post front matter in Docusaurus by checking the documentation and updating the implementation accordingly.
>
> > Fetched <https://docusaurus.io/docs/api/plugins/@docusaurus/plugin-content-blog#markdown-front-matter>
>
> Now let me check the Docusaurus documentation about how to access blog post metadata in components:
>
> > Fetched <https://docusaurus.io/docs/blog#accessing-blog-post-information>
>
> Let me search for Docusaurus documentation specifically about the useBlogPost hook:
>
> ...

Copilot figured out that the ideal solution was the reactHook [`useBlogPost()`](https://github.com/austenstone/portfolio/pull/36/files#diff-6324df17a3dc2a08f453a5faaa507164572fb47b545db0c902dfa9386e9b7a43R11) which I totally agree with.

### 4. Validation[​](#4-Validation "Direct link to 4. Validation")

I want to ensure the Giscus comments are working correctly so I ask Copilot to browse to a link knowing it will use the `playwright` MCP tool.

```
check that the giscus comments are working  
browse to http://localhost:3000/blog/github-copilot-agent-mcp  
test functionality  
#changes
```

This tested the comments were working but I wanted it to actually make a comment on the blog post.

```
Test the comments by making comments on this blog post  
http://localhost:3000/blog/github-copilot-agent-mcp  
  
Make the comment about the blog post and say that it's coming from github copilot using playwright
```

The [comment](https://github.com/austenstone/portfolio/discussions/35#discussioncomment-13621611) on this blog post was actually the output of this prompt.

### Real Example[​](#Real-Example "Direct link to Real Example")

Copilot did complete my feature completely.

The full PR can be found at [austenstone/portfolio/pull/36](https://github.com/austenstone/portfolio/pull/36).

Benefits[​](#Benefits "Direct link to Benefits")
------------------------------------------------

This workflow has transformed how I approach development:

1. **Consistency**: Custom instructions ensure all generated code follows my patterns
2. **Efficiency**: Pre-planned prompts eliminate repetitive explanations
3. **Quality**: Structured thinking leads to better architectural decisions
4. **Testability**: UI-aware testing tools create more comprehensive test suites
5. **Reproducibility**: Documented prompts make complex tasks repeatable

Ultimately I can spend more time on high-level design and less on low-level implementation details. The AI handles the grunt work, allowing me to focus on delivering value.

The Future[​](#The-Future "Direct link to The Future")
------------------------------------------------------

This combination of Agent Mode and MCP represents a fundamental shift in how we can work with AI. Instead of treating AI as a simple code completion tool, we can create sophisticated, context-aware development partners that understand our specific needs and workflows.

The key insight is that the AI becomes more valuable when it has more context about our intentions, constraints, and environment. MCP provides that context, while custom prompts ensure consistent, high-quality outputs.

---

*Have you experimented with Agent Mode and MCP in your development workflow? I'd love to hear about your experiences and any creative tool combinations you've discovered. Connect with me on [GitHub](https://github.com/austenstone) or [LinkedIn](https://www.linkedin.com/in/austenstone/) to continue the conversation.*
