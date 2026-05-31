---
id: 651
url: http://www.wilfred.me.uk/blog/2019/03/24/the-siren-song-of-little-languages/
title: The Siren Song of Little Languages &#8211; Wilfred Hughes::Blog
domain: www.wilfred.me.uk
source_date: '2025-01-13'
tags:
- scheme
- clojure
- compilers
- academic-paper
summary: Programming languages with small, elegant specifications—like Shen, Scheme,
  BF, and Forth—often attract developers who find them fun to implement rather than
  actually use, resulting in numerous implementations but few practical applications.
  The author argues that while clean design is valuable, languages need sufficient
  complexity and features to encourage users to write code in them rather than build
  alternative implementations. Languages like Clojure and Racket have achieved a better
  balance by being large enough to attract a user community before spawning multiple
  implementations.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# The Siren Song of Little Languages &#8211; Wilfred Hughes::Blog

Some programming languages languish due to obscurity. They lack breathless blog posts exclaiming how much nicer they are to use. Other languages are too ambitious. They aspire to support so many features that the original implementers struggle to get a first version working. For example, the type system in Fortress required constraint solving which took exponential time . Sometimes a usable language struggles simply because it’s too much fun to write your own . Developers end up building their own implementation rather than actually using the language. The most obvious implementation-focused language is BF . Despite having many implementations , BF programmers have to encourage the implementers to actually try using the language ! Scheme is also susceptible to this. Wikipedia lists 31 different Scheme implementations , not to mention the many toy implementations. Writing a Scheme is a great introduction to interpreters, especially once you get beyond the minimal lisp featureset . I’ve certainly written more implementation code than Scheme code. The problem seems to be languages with a small, well written specification. Shen is a multiparadigm lisp defined in terms of an elegant base language with only 46 system functions. This has resulted in a remarkable 15 third-party implementations , but only a small number of libraries implemented in the language . This phenomenon is not limited to lisps. Forth is also a language that developers often prefer to implement rather than use. Jones Forth is both a Forth tutorial and a discussion of how to build a Forth compiler. There are even stories of people spending years working on implementations without learning much of the language . Designing a language with a straightforward implementation is not a bad thing. It’s just a pitfall that language designers need to be aware of. Some crypto systems have this problem too . It seems that we need languages to be big enough that new users write hello world in the language, not write a tool for others to write hello world. In the Lisp family, Clojure and Racket seem to have reached a size threshold where newcomers are happy downloading the canonical implementation. This doesn’t mean multiple implementations are bad. It’s a great sign of language health. We just don’t need these until there’s a community of users and there is a need for implementations with different qualities. A language can be too small and elegant.
