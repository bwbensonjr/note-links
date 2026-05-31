---
id: 139
url: https://github.com/rowboatlabs/rowboat
title: 'GitHub - rowboatlabs/rowboat: Local-first, open-source tools for automating
  everyday work.'
domain: github.com
source_date: '2025-11-19'
tags:
- github-repo
- cli-tool
- ai
- python
summary: RowboatX is a local-first, open-source CLI tool that enables users to create
  and manage background AI agents with shell access for automating everyday tasks
  like meeting research, podcast summarization, and Slack message triage. The tool
  supports integration with multiple AI models (OpenAI, Anthropic, Google, Ollama,
  etc.) and Model Context Protocol (MCP) servers to extend agent capabilities. Users
  can build, schedule, monitor, and run agents through simple commands, with an optional
  web UI (Rowboat Studio) available for those preferring a graphical interface.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# GitHub - rowboatlabs/rowboat: Local-first, open-source tools for automating everyday work.

RowboatX - Claude Code for Everyday Automations RowboatX is a local-first CLI for creating background AI agents with full shell access. Example agents you can create: Research every person before your meetings (Exa search MCP + Google Calendar MCP) Daily podcast summarizing your saved articles (ElevenLabs MCP + ffmpeg) Auto-triage Slack DMs and draft responses while you sleep (Slack MCP) Quick start npx @rowboatlabs/rowboatx@latest Demo Examples Add and Manage MCP servers $ rowboatx Add MCP: 'Add this MCP server config: <config> ' Explore tools: 'What tools are there in <server-name> ' Create background agents $ rowboatx 'Create agent to do X.' '... Attach the correct tools from <mcp-server-name> to the agent' '... Allow the agent to run shell commands including ffmpeg' Schedule and monitor agents $ rowboatx 'Make agent <background-agent-name> run every day at 10 AM' 'What agents do I have scheduled to run and at what times' 'When was <background-agent-name> last run' 'Are any agents waiting for my input or confirmation' Run background agents manually rowboatx --agent= < agent-name > --input= " xyz " --no-interactive=true rowboatx --agent= < agent-name > --run_id= < run_id > # resume from a previous run Models support You can configure your models using: rowboatx model-config Alternatively, you can directly edit ~/.rowboat/config/models.json { "providers" : { "openai" : { "flavor" : " openai " }, "lm-studio" : { "flavor" : " openai-compatible " , "baseURL" : " http://localhost:2000/... " , "apiKey" : " ... " , "headers" : { "foo" : " bar " } }, "anthropic" : { "flavor" : " anthropic " }, "google" : { "flavor" : " google " }, "ollama" : { "flavor" : " ollama " } }, "defaults" : { "provider" : " lm-studio " , "model" : " gpt-5 " } } Contributing We want help with: Agent templates - Pre-built agents others can use (podcast generator, meeting prep, etc.) MCP server integrations - Add support for new tools Platform support - Windows improvements, Linux edge cases git clone git@github.com:rowboatlabs/rowboat.git cd rowboat npm install npm run build npm link rowboatx Ping us on Discord if you want to discuss before building. Prefer a Web UI: Rowboat Studio Cursor for Multi-agent Workflows ⚡ Build AI agents instantly with natural language | 🔌 Connect tools with one-click integrations | 📂 Power with knowledge by adding documents for RAG | 🔄 Automate workflows by setting up triggers and actions | 🚀 Deploy anywhere via API or SDK Quick start Set your OpenAI key export OPENAI_API_KEY=your-openai-api-key Clone the repository and start Rowboat (requires Docker) ./start.sh Access the app at http://localhost:3000 . Create a multi-agent assistant with MCP tools by chatting with Rowboat See Docs for more details. Made with ❤️ by the Rowboat team Discord · Twitter
