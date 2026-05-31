---
id: 462
url: https://urtext.co/
title: Introduction - Urtext /ˈʊrtekst/
domain: urtext.co
source_date: '2025-05-19'
tags:
- python
- cli-tool
- github-repo
summary: Urtext is an open-source, text-based markup language for creating programmable
  notebooks in plain text files using Python. It features a flexible, freeform syntax
  that combines content, structure, and instructions directly in the text buffer,
  along with capabilities for linking between nodes, executing Python code, and managing
  metadata—all while remaining local-first, future-proof, and free from proprietary
  formats. The tool is currently available as implementations for Sublime Text and
  Pythonista (iOS), with its core library designed to be language-agnostic for future
  expansion.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# Introduction - Urtext /ˈʊrtekst/

Urtext /ˈʊrtekst/ is a markup language for programmable notebooks in text files on top of the Python language. It is open source , text-based , local first , and future proof . There are implementations in NeoVim , Sublime Text , and Pythonista (for iOS) . Everything in Text Buffers The syntax combines content, structure and instructions together; there is no additional code or markup “behind” the syntax. Everything can be accomplished without leaving the text buffer. Freeform, Flexible Syntax Syntax Overview _ (the single underscore character denotes the node title) Most of the syntax is freeform. { This is a bracket node. It has its own identity within the project. { Bracket nodes can be nested to arbitrary depth. An optional linter indents and formats the syntax as you write. } } | Link > | Pointer >> Timestamp: < T hu., May. 08, 2025, 09:20 PM CEST > Metadata_Key ::Metadata value – another metadata value – etc. #hash_metadata_value (a shorthand) Metadata User-definable metadata syntax permits unlimited tagging. { type ::book title ::The Beautiful and Damned author ::| Scott Fitzgerald > } { Scott Fitzgerald _ Inside this node may be more metadata, including more nodes as metadata: birthday :: < 1900 > nationality ::United States short_description :: { Short description here inside another node } } Links A project encompass up to thousands of files , within which nodes may be linked in wiki-link fashion. Links can also run actions or arbitrary Python code. Link Examples _ Link to another node: | Other node id here > Links to a character position in the destination node | Destination node id here >:30 Link to a file (absolute or relative): | / README.md > Trigger Link – on click, executes the Python code block in the linked node | ! Open Urtext Website > Action Link – runs an Action, such as Random Node | : Random Node > Cross-Project Link – link to a node in another active projeg =>”Name or Path of the other project” | destination node ID > Python Block Execution It execute self-modifying or arbitrary Python code . It can be extended to add or modify functionality, to the extent of the Python language. { Code Example _ [[ . > ( | Python Output > ) . EXEC (@self) ]] %%Python # text in here is not parsed as Urtext # code must respect Python indentation def times_ten ( i ) : return i * 10 print ( times_ten ( 8 ) ) %% } { ~ Python Output _ 80 } Local First Operates on files locally present. It is not dependent on any cloud or other subscription service. Third-party services may be used to sync projects across devices, but we have found robust version control tools such as Git to be the best solution. No Need to Touch Files Direct interaction with file system is mostly unnecessary. Creating, naming, saving, and organizing files is handled for you . Future Proof No binary or propriety file format is used. The .urtext file extension denotes the syntax only, which is held in Unicode. Plaintext is fast, human-readable, flexible, cross-platform, device-portable, and future-proof. It can be easily diffed and version-controlled. Because the storage format is plain text, an interpreter, compiler, and editor could be implemented in any sufficiently capable language, current, past or future. Implementations The core library is headless and requires a implementation in an editor. Implementations are currently available for Sublime Text for desktop and Pythonista for iOS. Sublime Text (Mac/Windows/Linux) Pythonista for iOS (iPhone, iPad)
