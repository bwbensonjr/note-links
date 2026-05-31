---
id: 942
url: https://grafeo.dev/
title: Grafeo - High-Performance Graph Database - Grafeo
domain: grafeo.dev
source_date: '2026-03-22'
tags:
- database
- rust
- distributed-systems
summary: Grafeo is a high-performance graph database written in Rust that supports
  both Labeled Property Graphs and RDF data models, offering the fastest performance
  on industry benchmarks with minimal memory footprint. It provides flexibility through
  support for multiple query languages (GQL, Cypher, Gremlin, GraphQL, SPARQL, and
  SQL), can be embedded directly into applications or run as a standalone server,
  and includes features like vector search, ACID transactions, and bindings for multiple
  programming languages. The database is designed for production workloads with memory-safe
  Rust code, full concurrency support, and an ecosystem that integrates with AI tools
  like LangChain and LlamaIndex.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# Grafeo - High-Performance Graph Database - Grafeo

**Grafeo**[¶](#grafeo "Permanent link")
=======================================

### A fast, lean, embeddable graph database built in Rust[¶](#a-fast-lean-embeddable-graph-database-built-in-rust "Permanent link")

[Get Started](getting-started/) [View on GitHub](https://github.com/GrafeoDB/grafeo) [Join Discord](https://discord.gg/jrgMD2Zj3)

[![Grafeo Playground](assets/playground.png)](https://grafeo.ai)

---

Why Grafeo?[¶](#why-grafeo "Permanent link")
--------------------------------------------

* **High Performance**

  ---

  Fastest graph database in our [graph-bench](ecosystem/graph-bench/) suite (includes [LDBC-inspired](https://ldbcouncil.org/benchmarks/snb/) workloads), both embedded and as a server, with a lower memory footprint than other in-memory databases. Built in Rust with vectorized execution, adaptive chunking and SIMD-optimized operations.
* **Multi-Language Queries**

  ---

  GQL, Cypher, Gremlin, GraphQL, SPARQL and SQL/PGQ. Choose the query language that fits the project and expertise level.
* **LPG & RDF Support**

  ---

  Dual data model support for both Labeled Property Graphs and RDF triples. Choose the model that fits the domain.
* **Vector Search**

  ---

  HNSW-based similarity search with quantization (Scalar, Binary, Product). Combine graph traversal with semantic similarity.
* **Embedded or Standalone**

  ---

  Embed directly into applications with zero external dependencies, or run as a standalone server with REST API and web UI. From edge devices to production clusters.
* **Rust Core**

  ---

  Core database engine written in Rust with no required C dependencies. Optional allocators (jemalloc/mimalloc) and TLS use C libraries for performance. Memory-safe by design with fearless concurrency.
* **ACID Transactions**

  ---

  Full ACID compliance with MVCC-based snapshot isolation. Reliable transactions for production workloads.
* **Multi-Language Bindings**

  ---

  Python (PyO3), Node.js/TypeScript (napi-rs), Go (CGO), C (FFI), C# (.NET 8 P/Invoke), Dart (dart:ffi) and WebAssembly (wasm-bindgen). Use Grafeo from the language of choice.
* **Ecosystem**

  ---

  AI integrations (LangChain, LlamaIndex, MCP), interactive notebook widgets, browser-based graphs via WebAssembly, standalone server with web UI and benchmarking tools.

---

Quick Start[¶](#quick-start "Permanent link")
---------------------------------------------

PythonRust

```
uv add grafeo
```

```
import grafeo

# Create an in-memory database
db = grafeo.GrafeoDB()

# Create nodes and edges
db.execute("""
    INSERT (:Person {name: 'Alix', age: 30})
    INSERT (:Person {name: 'Gus', age: 25})
""")

db.execute("""
    MATCH (a:Person {name: 'Alix'}), (b:Person {name: 'Gus'})
    INSERT (a)-[:KNOWS {since: 2024}]->(b)
""")

# Query the graph
result = db.execute("""
    MATCH (p:Person)-[:KNOWS]->(friend)
    RETURN p.name, friend.name
""")

for row in result:
    print(f"{row['p.name']} knows {row['friend.name']}")
```

```
cargo add grafeo
```

```
use grafeo::GrafeoDB;

fn main() -> Result<(), grafeo::Error> {
    // Create an in-memory database
    let db = GrafeoDB::new_in_memory();

    // Create a session and execute queries
    let mut session = db.session();

    session.execute(r#"
        INSERT (:Person {name: 'Alix', age: 30})
        INSERT (:Person {name: 'Gus', age: 25})
    "#)?;

    session.execute(r#"
        MATCH (a:Person {name: 'Alix'}), (b:Person {name: 'Gus'})
        INSERT (a)-[:KNOWS {since: 2024}]->(b)
    "#)?;

    // Query the graph
    let result = session.execute(r#"
        MATCH (p:Person)-[:KNOWS]->(friend)
        RETURN p.name, friend.name
    "#)?;

    for row in result.rows() {
        println!("{:?}", row);
    }

    Ok(())
}
```

---

Features[¶](#features "Permanent link")
---------------------------------------

### Dual Data Model Support[¶](#dual-data-model-support "Permanent link")

Grafeo supports both major graph data models with optimized storage for each:

LPG (Labeled Property Graph)RDF (Resource Description Framework)

* **Nodes** with labels and properties
* **Edges** with types and properties
* **Properties** supporting rich data types
* Ideal for social networks, knowledge graphs, application data

* **Triples**: subject-predicate-object statements
* **SPO/POS/OSP indexes** for efficient querying
* W3C standard compliance
* Ideal for semantic web, linked data, ontologies

### Query Languages[¶](#query-languages "Permanent link")

Choose the query language that fits the project:

| Language | Data Model | Style |
| --- | --- | --- |
| **GQL** (default) | LPG | ISO standard, declarative pattern matching |
| **Cypher** | LPG | Neo4j-compatible, ASCII-art patterns |
| **Gremlin** | LPG | Apache TinkerPop, traversal-based |
| **GraphQL** | LPG, RDF | Schema-driven, familiar to web developers |
| **SPARQL** | RDF | W3C standard for RDF queries |
| **SQL/PGQ** | LPG | SQL:2023 GRAPH\_TABLE for SQL-native graph queries |

GQLCypherGremlinGraphQLSPARQL

```
MATCH (me:Person {name: 'Alix'})-[:KNOWS]->(friend)-[:KNOWS]->(fof)
WHERE fof <> me
RETURN DISTINCT fof.name
```

```
MATCH (me:Person {name: 'Alix'})-[:KNOWS]->(friend)-[:KNOWS]->(fof)
WHERE fof <> me
RETURN DISTINCT fof.name
```

```
g.V().has('name', 'Alix').out('KNOWS').out('KNOWS').
  where(neq('me')).values('name').dedup()
```

```
{
  Person(name: "Alix") {
    friends { friends { name } }
  }
}
```

```
SELECT DISTINCT ?fofName WHERE {
  ?me foaf:name "Alix" .
  ?me foaf:knows ?friend .
  ?friend foaf:knows ?fof .
  ?fof foaf:name ?fofName .
  FILTER(?fof != ?me)
}
```

### Architecture Highlights[¶](#architecture-highlights "Permanent link")

* **Push-based execution engine** with morsel-driven parallelism
* **Columnar storage** with type-specific compression
* **Cost-based query optimizer** with cardinality estimation
* **MVCC transactions** with snapshot isolation
* **Zone maps** for intelligent data skipping

---

Installation[¶](#installation "Permanent link")
-----------------------------------------------

PythonNode.jsGoRustC#DartWASM

```
uv add grafeo
```

```
npm install @grafeo-db/js
```

```
go get github.com/GrafeoDB/grafeo/crates/bindings/go
```

```
cargo add grafeo
```

```
dotnet add package GrafeoDB
```

```
# pubspec.yaml
dependencies:
  grafeo: ^0.5.42
```

```
npm install @grafeo-db/wasm
```

---

License[¶](#license "Permanent link")
-------------------------------------

Grafeo is licensed under the [Apache-2.0 License](https://github.com/GrafeoDB/grafeo/blob/main/LICENSE).
