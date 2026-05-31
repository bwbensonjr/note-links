---
id: 952
url: https://github.com/GrafeoDB/grafeo-langchain
title: 'GitHub - GrafeoDB/grafeo-langchain: LangChain integration for the Grafeo graph/vector
  database.  Provides GrafeoGraphStore and GrafeoGraphVectorStore for knowledge-graph
  storage and hybrid graph+vector retrieval inside LangChain pipelines. · GitHub'
domain: github.com
source_date: '2026-03-22'
tags:
- github-repo
- llm
- database
- python
summary: 'Grafeo-langchain is a LangChain integration for GrafeoDB, an embedded graph
  database with native vector search capabilities that requires no server setup or
  configuration. It provides two main components: GrafeoGraphStore for storing and
  querying LLM-extracted knowledge graphs using GQL/Cypher, and GrafeoGraphVectorStore
  for hybrid retrieval combining vector similarity search with graph traversal for
  Graph RAG applications. Unlike Neo4j, Grafeo operates as a lightweight, serverless
  solution deployable as a single .db file with built-in graph algorithms and support
  for offline/edge use cases.'
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# GitHub - GrafeoDB/grafeo-langchain: LangChain integration for the Grafeo graph/vector database.  Provides GrafeoGraphStore and GrafeoGraphVectorStore for knowledge-graph storage and hybrid graph+vector retrieval inside LangChain pipelines. · GitHub

grafeo-langchain LangChain graph store and vector store backed by GrafeoDB — an embedded graph database with native vector search. No servers, no Docker, no configuration. Just pip install and go. Install pip install grafeo-langchain Quick Start Knowledge Graph (GraphStore) Store LLM-extracted triples and query them with GQL/Cypher: from langchain_openai import ChatOpenAI from langchain_experimental . graph_transformers import LLMGraphTransformer from langchain_core . documents import Document from grafeo_langchain import GrafeoGraphStore llm = ChatOpenAI ( model = "gpt-4o-mini" , temperature = 0 ) transformer = LLMGraphTransformer ( llm = llm ) documents = [ Document ( page_content = "Alice works at Microsoft. Bob works at Google. Alice knows Bob." ), ] graph_documents = transformer . convert_to_graph_documents ( documents ) store = GrafeoGraphStore ( db_path = "./knowledge.db" ) store . add_graph_documents ( graph_documents , include_source = True ) results = store . query ( "MATCH (p:Person)-[:WORKS_AT]->(c) RETURN p.node_id, c.node_id" ) print ( store . get_schema ) Vector + Graph Retrieval (GraphVectorStore) Combine vector similarity search with graph traversal for Graph RAG: from langchain_openai import OpenAIEmbeddings from grafeo_langchain import GrafeoGraphVectorStore embeddings = OpenAIEmbeddings ( model = "text-embedding-3-small" ) store = GrafeoGraphVectorStore ( embedding = embeddings , db_path = "./doc_graph.db" , embedding_dimensions = 1536 , ) store . add_texts ( texts = [ "Python is a programming language..." , "Guido van Rossum..." , "ABC influenced..." ], metadatas = [ { "id" : "python" , "__graph_links__" : [{ "target_id" : "abc" , "type" : "INFLUENCED_BY" }]}, { "id" : "guido" }, { "id" : "abc" , "__graph_links__" : [{ "target_id" : "python" , "type" : "INFLUENCED" }]}, ], ids = [ "python" , "guido" , "abc" ], ) # Standard vector search docs = store . similarity_search ( "What programming languages exist?" , k = 2 ) # Vector search + graph traversal docs = store . traversal_search ( "What programming languages exist?" , k = 4 , depth = 2 ) # MMR-diversified graph traversal docs = store . mmr_traversal_search ( "programming history" , k = 4 , depth = 2 , lambda_mult = 0.7 ) Why Grafeo? Feature Neo4j Grafeo Requires server Yes (Docker/Cloud) No (embedded, pip install) GraphStore Yes Yes GraphVectorStore Community package Built-in (native HNSW) Query language Cypher GQL + Cypher + Gremlin Graph algorithms GDS plugin ($$$) Built-in (PageRank, Louvain, ...) Deployment Docker container Single .db file Offline/edge No Yes API Reference GrafeoGraphStore GrafeoGraphStore(db_path=None) — in-memory or persistent graph store .add_graph_documents(docs, include_source=False) — ingest LLM-extracted graph documents .query(query, params=None) — execute GQL/Cypher queries .get_schema / .get_structured_schema — inspect the graph schema .refresh_schema() — refresh the cached schema .client — access the underlying GrafeoDB instance GrafeoGraphVectorStore GrafeoGraphVectorStore(embedding, db_path=None, embedding_dimensions=1536) — vector store with graph links .add_texts(texts, metadatas=None, ids=None) — add documents with embeddings and optional graph links .similarity_search(query, k=4) — standard vector similarity search .traversal_search(query, k=4, depth=1) — vector search + graph traversal .mmr_traversal_search(query, k=4, depth=2, fetch_k=100, lambda_mult=0.5) — MMR-diversified traversal .from_texts(...) / .from_documents(...) — factory methods Requirements Python 3.12+ License Apache-2.0
