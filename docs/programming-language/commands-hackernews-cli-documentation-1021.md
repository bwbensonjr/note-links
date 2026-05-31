---
id: 1021
url: https://pythonhosted.org/hackernews-cli/commands.html
title: Commands — HackerNews CLI  documentation
domain: pythonhosted.org
source_date: '2026-04-15'
tags:
- python
- cli-tool
- tutorial
summary: The HackerNews CLI is a command-line tool that allows users to interact with
  Hacker News directly from the terminal using the `hn` command. It provides several
  key commands including `stories` to list top stories with sorting and limit options,
  `go` to navigate to a specific story, `comments` to view story comments, and `comment`
  to post comments. The tool offers a streamlined interface for hackers to browse
  and engage with Hacker News content without leaving the command line.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# Commands — HackerNews CLI  documentation

### Navigation

* [index](genindex.html "General Index")
* [next](changelog.html "Changelog") |
* [previous](index.html "Welcome to HackerNews CLI") |
* [HackerNews CLI documentation](index.html) »

Commands[¶](#commands "Permalink to this headline")
===================================================

Start hacking with hn command:

```
$ hn --help
Usage: hn [OPTIONS] COMMAND [ARGS]...

  HackerNews CLI - for hackers

Options:
  --version  Show the version and exit.
  --help     Show this message and exit.

Commands:
  comment   comment story on HackerNews
  comments  show comments for the story
  go        go to the story on HackerNews
  stories   list stories
```

```
$ hn stories --help
Usage: hn stories [OPTIONS]

  list stories

Options:
  -s, --sort_by [newest|best]  sort type
  -l, --limit INTEGER          number of top stories to show
  --help                       Show this message and exit.
```

```
$ hn go --help
Usage: hn go [OPTIONS] STORY_ID

  go to the story on HackerNews

Options:
  --help  Show this message and exit.
```

```
$ hn comments --help
Usage: hn comments [OPTIONS] STORY_ID

  show comments for the story

Options:
  --help  Show this message and exit.
```

```
$ hn comment --help
Usage: hn comment [OPTIONS] STORY_ID

  comment story on HackerNews

Options:
  --help  Show this message and exit.
```

[![Logo](_static/hn_hat.png)

HackerNews CLI
==============](index.html)

### Navigation

* Commands
* [Changelog](changelog.html)

### Quick search

Enter search terms or a module, class or function name.

©2014 Kamil Chmielewski.
|
Powered by [Sphinx 1.2.3](http://sphinx-doc.org/)
& [Alabaster 0.6.1](https://github.com/bitprophet/alabaster)
|
[Page source](_sources/commands.txt)
