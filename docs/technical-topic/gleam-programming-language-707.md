---
id: 707
url: https://gleam.run/
title: Gleam programming language
domain: gleam.run
source_date: '2026-01-14'
tags:
- compilers
- web-dev
- distributed-systems
summary: Gleam is a modern programming language that combines a strong type system
  with functional programming capabilities, running on the battle-tested Erlang virtual
  machine to enable reliable, scalable systems that can handle millions of concurrent
  operations. It comes with comprehensive built-in tools including a compiler, formatter,
  and package manager, and can interoperate with thousands of libraries from the BEAM
  ecosystem written in Gleam, Erlang, or Elixir, while also compiling to JavaScript
  for browser compatibility. The language prioritizes developer experience through
  clear error messages, no null values or exceptions, and a welcoming community committed
  to inclusivity and respect.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# Gleam programming language

The power of a type system, the expressiveness of functional programming, and the reliability of the highly concurrent, fault tolerant Erlang runtime, with a familiar and modern syntax. import gleam/io pub fn main () { io . println ( "hello, friend!" ) } Kindly supported by and sponsors like you! Reliable and scalable Running on the battle-tested Erlang virtual machine that powers planet-scale systems such as WhatsApp and Ericsson, Gleam is ready for workloads of any size. Thanks to its multi-core actor based concurrency system that can run millions of concurrent green threads, fast immutable data structures, and a concurrent garbage collector that never stops the world, your service can scale and stay lightning fast with ease. pub fn main () -> Nil { // Run loads of green threads, no problem list . range ( 0 , 200_000 ) |> list . each (spawn_greeter) } fn spawn_greeter (i: Int ) { process . spawn ( fn () { let n = int . to_string (i) io . println ( "Hello from " <> n) }) } Ready when you are Gleam comes with compiler, build tool, formatter, editor integrations, and package manager all built in, so creating a Gleam project is just running gleam new As part of the wider BEAM ecosystem, Gleam programs can use thousands of published packages, whether they are written in Gleam, Erlang, or Elixir. ➜ (main) gleam add gleam_json Resolving versions Downloading packages Downloaded 2 packages in 0.01s Added gleam_json v0.5.0 ➜ (main) gleam test Compiling thoas Compiling gleam_json Compiling app Compiled in 1.67s Running app_test.main . 1 tests, 0 failures Here to help No null values, no exceptions, clear error messages, and a practical type system. Whether you're writing new code or maintaining old code, Gleam is designed to make your job as fun and stress-free as possible. error: Unknown record field ┌─ ./src/app.gleam:8:16 │ 8 │ user.alias │ ^^^^^^ Did you mean `name`? The value being accessed has this type: User It has these fields: .name Multilingual Gleam makes it easy to use code written in other BEAM languages such as Erlang and Elixir, so there's a rich ecosystem of thousands of open source libraries for Gleam users to make use of. Gleam can additionally compile to JavaScript, enabling you to use your code in the browser, or anywhere else JavaScript can run. It also generates TypeScript definitions, so you can interact with your Gleam code confidently, even from the outside. @external (erlang, "Elixir.HPAX" , "new" ) pub fn new (size: Int ) -> Table pub fn register_event_handler () { let el = document . query_selector ( "a" ) element . add_event_listener (el, fn () { io . println ( "Clicked!" ) }) } Friendly 💜 As a community, we want to be friendly too. People from around the world, of all backgrounds, genders, and experience levels are welcome and respected equally. See our community code of conduct for more. Black lives matter. Trans rights are human rights. No nazi bullsh*t. Lovely people If you enjoy Gleam consider becoming a sponsor (or tell your boss to) You're still here? Well, that's all this page has to say. Maybe you should go read the language tour! Let's go! Wanna keep in touch? Subscribe to the Gleam newsletter We send emails at most a few times a year, and we'll never share your email with anyone else. This site is protected by reCAPTCHA and the Google Privacy Policy and Terms of Service apply.
