---
id: 998
url: https://substack.com/home/post/p-193415720
title: PGLite evangelism - Bill Jackson
domain: substack.com
source_date: '2026-04-10'
tags:
- database
- cli-tool
summary: I don't have access to external web pages or the ability to browse URLs.
  To provide an accurate summary of the Bill Jackson article about PGLite evangelism,
  I would need you to either share the article text directly with me or provide the
  main content from the page. If you can paste the article content, I'd be happy to
  summarize it in 2-3 sentences.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# PGLite evangelism - Bill Jackson

PGLite evangelism
=================

[![Bill Jackson's avatar](https://substackcdn.com/image/fetch/$s_!_DaF!,w_36,h_36,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1b68bbaa-3391-470b-b515-eabf50528ecb_512x512.png)](https://substack.com/@billjackson7)

[Bill Jackson](https://substack.com/@billjackson7)

Apr 07, 2026

2

Share

Everyone[1](#footnote-1) loves SQLite, because it’s simple, fast, and in-process, meaning you don’t need a long-lived service running or, \*shudders\*, Docker Desktop. It’s common for ORMs to work out-of-the-box with SQLite, so you can start fiddling around before getting a proper database set up. It’s also *somewhat* common/encouraged to use it in tests, where a “real” database isn’t available.

However, this inevitably runs into problems. Production apps generally use Postgres, and subtle differences in the dialect mean that you have to use Postgres in development too, and try to use it in tests as well. Back in the day, this way lay pain, heartache, special poorly-maintained “testing” databases, a workflow for running tests that required two terminal tabs, or indeed the dreaded Docker Desktop.

Thanks for reading! Subscribe for free to receive new posts.

Thankfully, these days are now behind us because we now have [PGLite](https://pglite.dev/). PGLite! It’s like SQLite but Postgres! (but only in javascript/WASM, not as a standalone binary like SQLite).

What does that mean exactly? Postgres normally needs a database service permanently running. In development, you will also need two services, either both on your laptop or (more common) the Postgres instance running on a remote server. PGLite is an in-process version of Postgres, meaning you don’t need this second service, you just `import ‘pglite’` in code, and you will have a fully-fledged Postgres instance writing to a local file, rather than a separate docker container

Why is this incredibly useful? Primarily for testing! It means you can easily set up tests that read and write to a dummy database, and the point is that it’s exactly the same as the production behaviour. PGLite is literally a standalone build of the same codebase behind proper-Postgres. Example in a Typescript app with Drizzle ORM:

```
import { PGlite } from ‘@electric-sql/pglite’;

import { drizzle } from ‘drizzle-orm/pglite’;

import { beforeAll, beforeEach, test, expect } from ‘vitest’;

const client = new PGlite();

const db = drizzle(client);

beforeAll(async () => {

  // Create your tables, or use drizzle-kit’s pushSchema to do this automatically. In practice this would be in a setup file, not every test file.

  await db.execute(`CREATE TABLE users (id SERIAL PRIMARY KEY, name TEXT NOT NULL)`);

});

beforeEach(async () => {

  await db.execute(`TRUNCATE users CASCADE`);

});

test(’can insert and query a user’, async () => {

  await db.execute(`INSERT INTO users (name) VALUES (’Alice’)`);

  const result = await db.execute(`SELECT * FROM users`);

  expect(result.rows).toHaveLength(1);

  expect(result.rows[0].name).toBe(’Alice’);

});
```

What else is it (potentially) useful for:

* As a go-to quick-setup database when starting a new project, similar to SQLite. It saves having to do any migration to Postgres later.

* As an in-browser database, for doing non-trivial data operations on the client. This is actually the use case it was developed for, to plug into the [ElectricSQL](https://github.com/electric-sql/electric) local-first[2](#footnote-2) framework.

* Not crazy, but haven’t tried it: As an actual production database for small apps. This would save a lot of round trips and the cost of hosting a permanent database.

[1](#footnote-anchor-1)

I mean \*everyone\*, there are [over a trillion SQLite databases in active use](https://sqlite.org/mostdeployed.html), making it likely “the second most widely deployed software library”, and one of the most widely deployed human-created artefacts of any kind.

[2](#footnote-anchor-2)

“local-first” == “do all data operations locally in the browser, sync them to the backend”, as opposed to the usual “send all data operations to the backend, sync back to the client (potentially with optimistic updates)”

2

Share
