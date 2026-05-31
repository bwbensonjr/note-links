---
id: 229
url: https://www.abs-lang.org/
title: The ABS programming language
domain: www.abs-lang.org
source_date: '2025-09-30'
tags:
- cli-tool
- python
- javascript
- ruby
summary: ABS is a shell scripting programming language that combines familiar syntax
  from popular languages like Ruby, Python, and JavaScript with deep integration of
  system commands for easy scripting. The language is designed to be beginner-friendly,
  allowing developers to run scripts easily across Mac, Windows, and Linux platforms
  with minimal setup required.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# The ABS programming language

A familiar syntax ABS should look familiar to most of us, as its elements are borrowed from popular programming languages such as Ruby, Python or JavaScript: obj = { } for n in 1. .10 { if n % 2 == 0 { obj [ n.str() ] = rand ( 6 * * 2 ) } } echo ( "We have %s" , obj ) # We have { "10" : 79 , . . . } Scripting made easy System commands are deeply integrated (and encouraged); they make ABS ideal to work with in the context of shell scripting: ip = ` curl icanhazip.com ` ip . ok // true ip // 1.2.3.4 echo ( "type something..." ) input = stdin ( ) echo ( "you typed %s", input ) Easy to run Grab the latest release, run abs your_script.abs and see the magic happening. ABS works on Mac, Windows and Linux: $ abs test.abs 1.2.3.4 type something... Hello world! you typed Hello world! $ ©️ 2025 -- No developers were harmed in the making of this language
