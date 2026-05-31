---
id: 104
url: https://github.com/stoolap/stoolap
title: 'GitHub - stoolap/stoolap: A Modern Embedded SQL Database written in Rust'
domain: github.com
source_date: '2025-12-12'
tags:
- database
- rust
- github-repo
- sql
summary: Stoolap is a modern embedded SQL database written in pure Rust that offers
  enterprise-grade features comparable to PostgreSQL and DuckDB with zero external
  dependencies. Key features include time-travel queries, MVCC transactions, cost-based
  query optimization, adaptive query execution, and semantic query caching, with benchmarks
  showing 81% win rate against SQLite and 92% against DuckDB. It supports standard
  SQL operations, 100+ built-in functions, and can be used as both an in-memory or
  persistent database library with a command-line interface.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# GitHub - stoolap/stoolap: A Modern Embedded SQL Database written in Rust

[![Stoolap Logo](/stoolap/stoolap/raw/main/logo.svg)](/stoolap/stoolap/blob/main/logo.svg)

### A Modern Embedded SQL Database in Pure Rust

[Documentation](https://stoolap.io/docs) •
[Playground](https://stoolap.io/playground) •
[Releases](https://github.com/stoolap/stoolap/releases) •
[Benchmarks](/stoolap/stoolap/blob/main/BENCHMARKS.md)

[![CI](https://github.com/stoolap/stoolap/actions/workflows/ci.yml/badge.svg)](https://github.com/stoolap/stoolap/actions/workflows/ci.yml)
[![codecov](https://camo.githubusercontent.com/31ab05b12f2ffd875cae0a27cf33383e7f0e9ae6e912190d06969b816bfc0402/68747470733a2f2f636f6465636f762e696f2f67682f73746f6f6c61702f73746f6f6c61702f6272616e63682f6d61696e2f67726170682f62616467652e737667)](https://codecov.io/gh/stoolap/stoolap)
[![Crates.io](https://camo.githubusercontent.com/63bc64a51ac649acdd8e671e9fae530c9a85a58adb4f988eb4774993ac89dfae/68747470733a2f2f696d672e736869656c64732e696f2f6372617465732f762f73746f6f6c61702e737667)](https://crates.io/crates/stoolap)
[![GitHub release](https://camo.githubusercontent.com/bfc5aa6bd654da952349d063220d5b6c5ef19eba0f89918faf8d02fc3ef175fd/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f762f72656c656173652f73746f6f6c61702f73746f6f6c6170)](https://github.com/stoolap/stoolap/releases)
[![License](https://camo.githubusercontent.com/b29de0acdfd19013f1f02689b15c933e4a6c145be9efa718288f88ba3280b1c5/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6c6963656e73652d417061636865253230322e302d626c75652e737667)](/stoolap/stoolap/blob/main/LICENSE)

---

Stoolap is a feature-rich embedded SQL database built in pure Rust.
It targets low-latency transactional workloads and real-time analytical queries, with modern SQL features and no external server process.

Why Stoolap?
------------

Stoolap is designed around practical embedded database needs:

* **ACID + MVCC**: concurrent reads and writes with transaction isolation
* **Cost-based optimization**: statistics-aware planning with adaptive execution
* **Rich SQL surface**: joins, subqueries, CTEs, window functions, advanced aggregations
* **Multiple index types**: B-tree, Hash, Bitmap, multi-column, and HNSW for vectors
* **Pure Rust runtime**: memory-safe implementation, no C/C++ dependency chain

### Feature Snapshot

| Feature | Stoolap | SQLite | DuckDB | PostgreSQL |
| --- | --- | --- | --- | --- |
| AS OF Time-Travel Queries | ✅ | ❌ | ❌ | ❌\* |
| MVCC Transactions | ✅ | ❌ | ✅ | ✅ |
| Hot/Cold Columnar Storage | ✅ | ❌ | ✅ | ❌ |
| Cost-Based Optimizer | ✅ | ❌ | ✅ | ✅ |
| Adaptive Query Execution | ✅ | ❌ | ❌ | ❌ |
| Semantic Query Caching | ✅ | ❌ | ❌ | ❌ |
| Parallel Query Execution | ✅ | ❌ | ✅ | ✅ |
| Native Vector / HNSW Search | ✅ | ❌ | ❌ | ❌ |
| Pure Rust (Memory Safe) | ✅ | ❌ | ❌ | ❌ |

\*PostgreSQL typically needs extensions for temporal query workflows.

Quick Start
-----------

### Installation

```
[dependencies]
stoolap = "0.4"
```

Build from source:

```
git clone https://github.com/stoolap/stoolap.git
cd stoolap
cargo build --release
```

### Rust API

```
use stoolap::Database;

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let db = Database::open_in_memory()?;

    db.execute(
        "CREATE TABLE users (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT UNIQUE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )",
        (),
    )?;

    db.execute(
        "INSERT INTO users (id, name, email) VALUES ($1, $2, $3)",
        (1, "Alice", "alice@example.com"),
    )?;

    for row in db.query("SELECT id, name, email FROM users WHERE id = $1", (1,))? {
        let row = row?;
        println!(
            "id={} name={} email={}",
            row.get::<i64>(0)?,
            row.get::<String>(1)?,
            row.get::<String>(2)?
        );
    }

    Ok(())
}
```

### CLI

```
# Interactive REPL
./stoolap

# Execute a single query
./stoolap -e "SELECT version()"

# Persistent database
./stoolap --db "file://./mydb"
```

Stoolap Studio
--------------

[Stoolap Studio](https://github.com/stoolap/stoolap-studio) is a web-based database management interface with a SQL editor, schema browser, interactive data grid, vector search, and backup/restore.

[![Stoolap Studio](/stoolap/stoolap/raw/main/docs/assets/img/studio/studio-light.png#gh-light-mode-only)](/stoolap/stoolap/blob/main/docs/assets/img/studio/studio-light.png#gh-light-mode-only)

[![Stoolap Studio](/stoolap/stoolap/raw/main/docs/assets/img/studio/studio-dark.png#gh-dark-mode-only)](/stoolap/stoolap/blob/main/docs/assets/img/studio/studio-dark.png#gh-dark-mode-only)

```
git clone https://github.com/stoolap/stoolap-studio.git
cd stoolap-studio && npm install && npm run dev
```

Core SQL Capabilities
---------------------

### Transactions and Time-Travel

```
BEGIN;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;
COMMIT;

SELECT * FROM accounts AS OF TIMESTAMP '2024-01-15 10:30:00';
SELECT * FROM inventory AS OF TRANSACTION 1234;
```

### Cost-Based Query Optimizer

```
ANALYZE orders;
ANALYZE customers;

EXPLAIN SELECT * FROM orders WHERE customer_id = 100;

EXPLAIN ANALYZE
SELECT o.*, c.name
FROM orders o
JOIN customers c ON o.customer_id = c.id
WHERE c.country = 'US';
```

### Indexing

```
-- Auto-selected by data type
CREATE INDEX idx_created_at ON orders(created_at);   -- B-tree
CREATE INDEX idx_email ON users(email);              -- Hash
CREATE INDEX idx_active ON users(is_active) USING BITMAP;

-- Multi-column
CREATE INDEX idx_lookup ON events(user_id, event_type);
```

### Advanced SQL

```
WITH ranked AS (
    SELECT
        customer_id,
        amount,
        ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY amount DESC) AS rn
    FROM orders
)
SELECT * FROM ranked WHERE rn = 1;
```

Vector and Semantic Search
--------------------------

Stoolap supports native vectors via `VECTOR(N)` and approximate nearest-neighbor search with HNSW.

```
CREATE TABLE embeddings (
    id INTEGER PRIMARY KEY,
    content TEXT,
    embedding VECTOR(384)
);

CREATE INDEX idx_emb ON embeddings(embedding)
USING HNSW WITH (metric = 'cosine', m = 32, ef_construction = 400, ef_search = 128);

SELECT id, content,
       VEC_DISTANCE_COSINE(embedding, '[0.1, 0.2, ...]') AS dist
FROM embeddings
ORDER BY dist
LIMIT 10;
```

For built-in semantic text embeddings, enable the `semantic` feature:

```
[dependencies]
stoolap = { version = "0.4", features = ["semantic"] }
```

```
SELECT EMBED('How to reset my password');
```

See [Vector Search](https://stoolap.io/docs/data-types/vector-search/) and [Semantic Search](https://stoolap.io/docs/data-types/semantic-search/) docs for full workflows.

Storage and Durability
----------------------

Stoolap uses a hot/cold volume storage architecture inspired by Apache Iceberg and Delta Lake:

* **Hot buffer**: in-memory MVCC store with WAL for active writes
* **Cold volumes**: immutable columnar files with zone maps, bloom filters, dictionary encoding, and LZ4 compression
* **Adaptive compaction**: background thread merges cold volumes with size-aware, fully dynamic merge strategy
* **Crash recovery**: atomic manifest writes, fsync-before-rename, WAL replay from checkpoint LSN
* **Column pruning**: cold scans materialize only columns referenced by filters and projections

```
file://./mydb?sync_mode=normal&compression=on&checkpoint_interval=60
```

| DSN Parameter | Default | Description |
| --- | --- | --- |
| `sync_mode` | `normal` | `none` (no fsync, data durable at checkpoint), `normal` (fsync every 1s), `full` (fsync every write) |
| `compression` | `on` | LZ4 for both WAL and volumes |
| `wal_compression` | `on` | LZ4 for WAL entries only |
| `volume_compression` | `on` | LZ4 for cold volume files only |
| `checkpoint_interval` | `60` | Seconds between checkpoint cycles |
| `compact_threshold` | `4` | Sub-target volumes per table before merging |
| `target_volume_rows` | `1048576` | Target rows per cold volume |

Performance
-----------

Detailed benchmark results are in [BENCHMARKS.md](/stoolap/stoolap/blob/main/BENCHMARKS.md).

Benchmark figures are point-in-time and workload-dependent. Validate on your own hardware, data distribution, and query patterns.

Documentation
-------------

* Installation: <https://stoolap.io/docs/getting-started/installation/>
* SQL commands: <https://stoolap.io/docs/sql-commands/sql-commands/>
* Data types: <https://stoolap.io/docs/data-types/data-types/>
* Functions: <https://stoolap.io/docs/functions/sql-functions-reference/>
* Architecture: <https://stoolap.io/docs/architecture/architecture/>
* Drivers: [Node.js](https://stoolap.io/docs/drivers/nodejs/) | [Python](https://stoolap.io/docs/drivers/python/) | [PHP](https://stoolap.io/docs/drivers/php/) | [WASM](https://stoolap.io/docs/drivers/wasm/) | [C](https://stoolap.io/docs/drivers/c/)

Development
-----------

```
cargo build
cargo nextest run
cargo clippy --all-targets --all-features -- -D warnings
cargo fmt --check
```

Contributing
------------

See [CONTRIBUTING.md](/stoolap/stoolap/blob/main/CONTRIBUTING.md).

License
-------

Apache License 2.0. See [LICENSE](/stoolap/stoolap/blob/main/LICENSE).
