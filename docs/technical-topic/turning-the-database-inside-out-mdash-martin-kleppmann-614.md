---
id: 614
url: https://martin.kleppmann.com/2015/11/05/database-inside-out-at-oredev.html
title: Turning the database inside-out &mdash; Martin Kleppmann&rsquo;s talks
domain: martin.kleppmann.com
source_date: '2025-01-28'
tags:
- database
- distributed-systems
- academic-paper
summary: Martin Kleppmann's talk challenges the traditional database model—which treats
  databases as mutable, shared global state since the 1960s—by proposing an alternative
  "inside-out" architecture based on immutable facts and stream processing. Using
  Apache Samza (a distributed stream processing framework built on Apache Kafka),
  this approach processes incoming data streams in real-time functionally rather than
  imperatively, offering benefits like simpler code, better scalability, improved
  robustness, lower latency, and greater flexibility. The talk presents a fundamentally
  different way to think about application architecture that moves away from conventional
  database design.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# Turning the database inside-out &mdash; Martin Kleppmann&rsquo;s talks

Skip to content Martin Kleppmann Student Projects About/Contact Supporters Turning the database inside-out A talk at Øredev , Malmö, Sweden, 05 Nov 2015 Transcript Slides Video This was a repeat of my talk at Strange Loop 2014 . Abstract Databases are global, shared, mutable state. That’s the way it has been since the 1960s, and no amount of NoSQL has changed that. However, most self-respecting developers have got rid of mutable global variables in their code long ago. So why do we tolerate databases as they are? A more promising model, used in some systems, is to think of a database as an always-growing collection of immutable facts. You can query it at some point in time — but that’s still old, imperative style thinking. A more fruitful approach is to take the streams of facts as they come in, and functionally process them in real-time. This talk introduces Apache Samza, a distributed stream processing framework developed at LinkedIn. At first it looks like yet another tool for computing real-time analytics, but it’s more than that. Really it’s a surreptitious attempt to take the database architecture we know, and turn it inside out. At its core is a distributed, durable commit log, implemented by Apache Kafka. Layered on top are simple but powerful tools for joining streams and managing large amounts of data reliably. What we have to gain from turning the database inside out? Simpler code, better scalability, better robustness, lower latency, and more flexibility for doing interesting things with data. After this talk, you’ll see the architecture of your own applications in a completely new light. Subscribe Site RSS feed To find out when I write something new, sign up to receive an email notification , follow me on Bluesky or Mastodon , or subscribe to the RSS feed . I won't give your email address to anyone else, won't send you any spam, and you can unsubscribe at any time. My book My book, Designing Data-Intensive Applications , has received thousands of five-star reviews. I am an Associate Professor working on local-first software and security protocols at the University of Cambridge . If you find my work useful, please support me on Patreon . Recent posts 08 Dec 2025: Prediction: AI will make formal verification go mainstream 05 Jul 2024: Pudding: user discovery for anonymity networks 04 Jan 2024: 2023 year in review 12 Oct 2022: Verifying distributed systems with Isabelle/HOL 03 Jan 2022: Book Review: The Future of Fusion Energy Full archive Conference talks 02 Apr 2025 at 20th European Conference on Computer Systems (EuroSys) 31 Mar 2025 at 12th Workshop on Principles and Practice of Consistency for Distributed Data (PaPoC) 30 May 2024 at Local-First Conference 27 Feb 2024 at Local First (LoFi) meetup 06 Nov 2023 at IETF-118 Decentralization of the Internet Research Group Full archive Unless otherwise specified, all content on this site is licensed under a Creative Commons Attribution 3.0 Unported License . Theme borrowed from Carrington , ported to Jekyll by Martin Kleppmann.
