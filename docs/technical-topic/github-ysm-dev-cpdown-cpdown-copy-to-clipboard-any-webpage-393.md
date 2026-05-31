---
id: 393
url: https://github.com/ysm-dev/cpdown
title: 'GitHub - ysm-dev/cpdown: 📥 cpdown - Copy to clipboard any webpage content/youtube
  subtitle as clean markdown with one click or shortcut'
domain: github.com
source_date: '2025-06-19'
tags:
- github-repo
- web-dev
- llm
- cli-tool
summary: '**cpdown** is a browser extension that converts any webpage content into
  clean, formatted markdown with a single click or keyboard shortcut. It also supports
  copying YouTube subtitles as markdown and provides token counting for LLM use. The
  extension uses advanced content extraction tools (Defuddle or Mozilla Readability)
  to remove unnecessary elements and offers customizable settings for markdown formatting,
  available for Chrome and Firefox.'
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# GitHub - ysm-dev/cpdown: 📥 cpdown - Copy to clipboard any webpage content/youtube subtitle as clean markdown with one click or shortcut

cpdown Copy any webpage as clean markdown. Overview cpdown is a browser extension that allows you to copy the content of any webpage as clean, formatted markdown. If you're on YouTube, you can also copy the subtitle as markdown. Demo Cap.2025-05-21.at.17.13.06.mp4 Features 📋 Copy any webpage content as clean markdown with one click (or keyboard shortcut) 📋 Copy YouTube subtitle as clean markdown with one click (or keyboard shortcut) 📖 Uses Defuddle or Mozilla's Readability to extract the main content 🔍 Removes unnecessary HTML elements (scripts, styles, iframes, etc.) 🔢 Shows token count for the copied content (for LLM) ⌨️ Keyboard shortcut support Installation Chrome: Chrome Web Store Firefox: Firefox Add-ons Options Go to chrome://extensions/?options=knnaflplggjdedobhbidojmmnocfbopf or click the "Options" link in the extension's details page to configure cpdown after installation. Manual Installation Clone this repository Install dependencies: bun i Build the extension: bun run build Load the unpacked extension: Open Chrome/Edge and navigate to chrome://extensions Enable "Developer mode" Click "Load unpacked" and select the .output/chrome-mv3 directory Usage Navigate to any webpage you want to copy Click the cpdown icon in your browser toolbar, or use the keyboard shortcut The page content will be copied to your clipboard as markdown Paste the markdown content anywhere you need it Settings cpdown offers several configuration options: Use Defuddle : Use Defuddle to clean up the markdown output Use Mozilla Readability : Parse webpage content using Readability for cleaner markdown output Wrap in Triple Backticks : Wrap the copied content in triple backticks for better readability Show Success Toast : Display a notification when content is successfully copied Show Raycast Confetti : Celebrate successful copying with a confetti animation (for Raycast users) Development This extension is built with: Cursor - For the vibe coding WXT - The Web Extension Toolkit React - For the options UI Shadcn UI - For the options UI Sonner - For the toast notifications Tailwind CSS - For styling Defuddle - For main content extraction & markdown cleanup Mozilla Readability - For main content extraction Turndown - For HTML to Markdown conversion tiktoken - For token counting Development Commands bun run dev Star History License MIT
