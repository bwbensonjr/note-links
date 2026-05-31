---
id: 35
url: https://www.cs.cmu.edu/~pavlo/blog/2026/01/2025-databases-retrospective.html
title: 'Databases in 2025: A Year in Review // Blog // Andy Pavlo - Carnegie Mellon
  University'
domain: www.cs.cmu.edu
source_date: '2026-01-05'
tags:
- database
- academic-paper
- distributed-systems
summary: In 2025, PostgreSQL continued its dominance in the database world, with major
  acquisitions and new initiatives from tech giants like Databricks, Snowflake, and
  Microsoft investing billions in PostgreSQL-based services and DBaaS offerings. The
  year saw significant developments including PostgreSQL v18's new asynchronous I/O
  storage subsystem and growing momentum around distributed PostgreSQL projects (Multigres,
  Neki, and PgDog) that aim to add horizontal scaling capabilities similar to existing
  MySQL sharding solutions. Key takeaways include the consolidation of the PostgreSQL
  ecosystem through M&A activity, the emergence of competing open-source sharding
  middleware projects, and the establishment of PostgreSQL offerings across all major
  cloud vendors, solidifying its position as the dominant database platform.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# Databases in 2025: A Year in Review // Blog // Andy Pavlo - Carnegie Mellon University

Another year passes. I was hoping to write more articles instead of just these end-of-the-year screeds, but I almost [died](https://bsky.app/profile/andypavlo.bsky.social/post/3lsvwhx2ixk2v) in the spring semester, and it sucked up my time. Nevertheless, I will go through what I think are the major trends and happenings in databases over the last year.

There were many exciting and unprecedented developments in the world of databases. [Vibe coding](https://twitter.com/karpathy/status/1886192184808149383) entered the vernacular. The Wu-Tang Clan announced their [time capsule project](https://www.youtube.com/watch?v=4u-bttzVubs). Rather than raising one massive funding round this year instead of going public, Databricks raised [two massive rounds](#random-fundings) instead of going public.

Meanwhile, other events were expected and less surprising. Redis Ltd. [switched their license back](https://antirez.com/news/151) one year after their [rugpull](https://redis.io/blog/redis-adopts-dual-source-available-licensing/) (I called this shot [last year](https://www.cs.cmu.edu/~pavlo/blog/2025/01/2024-databases-retrospective.html#licenses)). SurrealDB reported great benchmark numbers because they [weren't flushing writes to disk and lost data](https://blog.cf8.gg/surrealdbs-ch/). And Coldplay can [break up your marriage](https://www.reddit.com/r/WatchPeopleDieInside/comments/1m239rb/astronomer_ceo_and_cpo_caught_having_an_affair_on/). Astronomer did make some pretty good [lemonade](https://www.youtube.com/watch?v=vich2C-Tl7Q) on that last one though.

Before I begin, I want to address the question I get every year in the comments about these articles. People always ask why I don't mention a particular [system](https://www.reddit.com/r/programming/comments/1hr3xor/databases_in_2024_a_year_in_review/m4vone0/), [database](https://news.ycombinator.com/item?id=42566660), or [company](https://news.ycombinator.com/item?id=34225377) in my analysis. I can only write about so many things, and unless something interesting/notable happened in the past year, then there is nothing to discuss. But not all notable database events are appropriate for me to opine about. For example, the recent attempt to [unmask the AvgDatabase CEO](https://twitter.com/CeolinWill/status/2005601763051856293) is fair game, but the [MongoDB suicide lawsuit](https://news.ycombinator.com/item?id=46403128) is decidedly not.

With that out of the way, let's do this. These articles are getting longer each year, so I apologize in advance.

Previous entries:

* [Databases in 2024: A Year in Review](https://www.cs.cmu.edu/~pavlo/blog/2025/01/2024-databases-retrospective.html)
* [Databases in 2023: A Year in Review](https://www.cs.cmu.edu/~pavlo/blog/2024/01/2023-databases-retrospective.html)
* [Databases in 2022: A Year in Review](https://www.cs.cmu.edu/~pavlo/blog/2022/12/2022-databases-retrospective.html)
* [Databases in 2021: A Year in Review](https://www.cs.cmu.edu/~pavlo/blog/2021/12/2021-databases-retrospective.html)

The Dominance of PostgreSQL Continues
-------------------------------------

I first wrote about how PostgreSQL was [eating the database world](https://www.cs.cmu.edu/~pavlo/blog/2021/12/2021-databases-retrospective.html#dominance-of-postgresql) in 2021. That trend continues unabated as most of the most interesting developments in the database world are happening once again with PostgreSQL. The DBMS's latest version ([v18](https://www.postgresql.org/about/news/postgresql-18-released-3142/)) dropped in November 2025. The most prominent feature is the new [asynchronous I/O storage subsystem](https://www.cybertec-postgresql.com/en/postgresql-18-and-beyond-from-aio-to-direct-io/), which will finally put PostgreSQL on the path to dropping its reliance on the OS page cache. It also [added support](https://www.postgresql.org/message-id/CAH2-Wzmn1YsLzOGgjAQZdn1STSG_y8qP__vggTaPAYXJP%2BG4bw%40mail.gmail.com) for [skip scans](https://www.pgedge.com/blog/postgres-18-skip-scan-breaking-free-from-the-left-most-index-limitation); queries can still use multi-key B+Tree indexes even if they are missing the leading keys (i.e., prefix). There are some additional improvements to the query optimizer (e.g., removing [superfluous self-joins](https://betterstack.com/community/guides/databases/postgresql-18-new-features/#optimizer-and-query-planning-improvements)).

Savvy database connoisseurs will be quick to point out that these are not groundbreaking features and that other DBMSs have had them for years. PostgreSQL is the only major DBMS still relying on the OS page cache. And Oracle has supported [skip scans since 2002](https://richardfoote.wordpress.com/2008/03/10/index-skip-scan-does-index-column-order-matter-any-more-warning-sign/) (v9i)! You may wonder, therefore, why I am claiming that the hottest action in databases for 2025 happened with PostgreSQL?

The reason is that most of the database energy and activity is going into PostgreSQL companies, offerings, projects, and derivative systems.

#### Acquisitions + Releases:

In the last year, the hottest data start-up ([Databricks](https://www.databricks.com/)) paid [$1b for a PostgreSQL DBaaS company](https://www.wsj.com/articles/databricks-to-buy-startup-neon-for-1-billion-fdded971) ([Neon](https://neon.com/)). Next, one of the biggest database companies in the world ([Snowflake](https://www.snowflake.com/en/)) paid [$250m for another PostgreSQL DBaaS company](https://www.wsj.com/articles/snowflake-to-buy-crunchy-data-for-250-million-233543ab) ([CrunchyData](https://www.crunchydata.com/)). Then, one of the biggest tech companies on the planet (Microsoft) launched [a new PostgreSQL DBaaS](https://techcommunity.microsoft.com/blog/adforpostgresql/announcing-azure-horizondb/4469710) ([HorizonDB](https://azure.microsoft.com/en-us/products/horizondb)). Neon and HorizonDB follow Amazon Aurora's [original high-level architecture](https://doi.org/10.1145/3035918.3056101) from the 2010s, with a single primary node separating compute and storage. For now, Snowflake's PostgreSQL DBaaS uses the same core architecture as standard PostgreSQL because they built on [Crunchy Bridge](https://www.crunchydata.com/products/crunchy-bridge).

#### Distributed PostgreSQL:

All of the services I listed above are single-primary node architectures. That is, applications send writes to a primary node, which then sends those changes to secondary replicas. But in 2025, there were two announcements on new projects to create scale-out (i.e., horizontal partitioning) services for PostgreSQL. In June 2025, Supabase announced that it had hired [Sugu](https://www.linkedin.com/in/sougou/), the Vitess co-creator and former PlanetScale co-founder/CTO, to lead the [Multigres](https://multigres.com/) project to create sharding middleware for PostgreSQL, similar to how Vitess shards MySQL. Sugu left PlanetScale in 2023 and had to lie back in the cut for two years. He is now likely clear of any legal issues and can make things happen at Supabase. You know it is a [big deal](https://simonwillison.net/2025/Jul/1/planetscale-for-postgres/) when a database engineer joins a company, and the [announcement](https://supabase.com/blog/multigres-vitess-for-postgres) focuses more on the person than the system. The [co-founder/CTO of SingleStore](https://www.linkedin.com/in/adam-prout-0b347630/) joined Microsoft in 2024 to [lead HorizonDB](https://www.linkedin.com/posts/adam-prout-0b347630_im-happy-to-share-that-im-starting-a-new-activity-7167922823800324096-v1OD), but Microsoft (incorrectly) did not make a big deal about it. Sugu joining Supabase is like [Ol' Dirty Bastard](https://en.wikipedia.org/wiki/Ol%27_Dirty_Bastard) (RIP) getting out on [parole after two years](https://youtu.be/TDXKvYQ3Xb4) and then [announcing a new record deal](https://www.nme.com/news/music/odb-3-1383866) on the first day of his release.

One month after the Multigres news dropped, PlanetScale [announced](https://planetscale.com/blog/planetscale-for-postgres#neki-vitess-for-postgres) its own Vitess-for-PostgreSQL project, [Neki](https://www.neki.dev/). PlanetScale launched its initial [PostgreSQL DBaaS](https://planetscale.com/blog/announcing-metal) in March 2025, but the core architecture is single-node stock [PostgreSQL with pgBouncer](https://planetscale.com/blog/planetscale-for-postgres#performance-and-reliability).

#### Commercial Landscape:

With Microsoft's introduction of HorizonDB in 2025, all major cloud vendors now have serious projects for their own PostgreSQL offerings. Amazon has offered [Aurora PostgreSQL](https://aws.amazon.com/about-aws/whats-new/2017/04/announcing-open-preview-of-amazon-aurora-with-postgresql-compatibility/) since 2017. Google put out [AlloyDB](https://venturebeat.com/data-infrastructure/google-announces-alloydb-a-faster-hosted-version-of-postgresql) in 2022. ServiceNow launched its [RaptorDB service in 2024](https://www.investing.com/news/company-news/servicenow-unveils-raptordb-pro-and-future-knowledge-graph-93CH-3609528), based on its 2021 [acquisition](https://www.zdnet.com/article/servicenow-acquires-database-performance-company-swarm64/) of Swarm64. Even the old flip-phone IBM has had its [cloud version of PostgreSQL](https://cloud.ibm.com/docs/databases-for-postgresql?topic=databases-for-postgresql-postgresql-relnotes) since 2018. Oracle released its [PostgreSQL service in 2023](https://docs.oracle.com/en-us/iaas/releasenotes/changes/9a4b73b5-d4d6-4c89-bd31-b1fa2098fa34/index.htm), though there is a rumor that its in-house PostgreSQL team was collateral damage in its [MySQL OCI layoffs](https://www.theregister.com/2025/09/11/oracle_slammed_for_mysql_job/) in September 2025.

There are still a few independent (ISV) PostgreSQL DBaaS companies. [Supabase](https://supabase.com/) is likely the largest of these by the number of instances. Others include [YugabyteDB](https://www.yugabyte.com/), [TigerData](https://www.tigerdata.com/) (née TimeScale), [PlanetScale](https://planetscale.com/), [Xata](https://xata.io/), [PgEdge](https://www.pgedge.com/), and [Nile](https://www.thenile.dev/). Xata built its original architecture on [Amazon Aurora](https://xata.io/blog/serverless-postgres-platform#:~:text=AWS%20Aurora%20under%20the%20hood), but this year, it announced it is [switching to its own infrastructure](https://xata.io/blog/xata-postgres-with-data-branching-and-pii-anonymization). [ParadeDB](https://www.paradedb.com/) has yet to announce its hosted service. [Tembo](https://www.tembo.io/) dropped its [hosted PostgreSQL offering](https://tembo-io.notion.site/Tembo-Cloud-Migration-Guide-1de7c9367d6a80349570e7469ba7f17b) in 2025 to pivot to a coding agent that can do some database tuning. [Hydra](https://www.hydra.so/) and [PostgresML](https://postgresml.org/) went bust in 2025 (see [Deaths](#random-deaths) section), so they're out of the game. Other systems provide a Postgres-compatible front-end, but the back-end systems are not derived from PostgreSQL (e.g., [CockroachDB](https://www.cockroachlabs.com/docs/stable/postgresql-compatibility), [CedarDB](https://cedardb.com/docs/compatibility/), [Google Spanner](https://docs.cloud.google.com/spanner/docs/postgresql-interface)). There are also hosting companies that offer PostgreSQL DBaaS alongside other systems, such as [Aiven](https://aiven.io/) and [Tessel](https://www.tessell.com/).

**Update 2026-01-05:** I was reminded via private email that [PgDog](https://pgdog.dev/) is also another open-source middleware system that seeks to support horizontal sharding in PostgreSQL. I had mentally compartmentalized PgDog in the same category as a connection pooling proxy ([PgBouncer](https://www.pgbouncer.org/)), but it is actually a competitor to Multigres and Neki.

**Update 2026-01-05:** I was reminded via private email that [PgDog](https://pgdog.dev/) is also another open-source middleware system that seeks to support horizontal sharding in PostgreSQL. I had mentally compartmentalized PgDog in the same category as a connection pooling proxy ([PgBouncer](https://www.pgbouncer.org/)), but it is actually a competitor to Multigres and Neki.

**Update 2026-01-18:** I was asked to include a link to the [commit](https://www.postgresql.org/message-id/CAH2-Wzmn1YsLzOGgjAQZdn1STSG_y8qP__vggTaPAYXJP%2BG4bw%40mail.gmail.com) that added PostgreSQL's skip scan feature.

### Andy's HeadAndy's Take:

It is not clear who the next major buyer will be after Databricks and Snowflake bought PostgreSQL companies. Again, every major tech company already has a Postgres offering. EnterpriseDB is the oldest PostgreSQL ISV, but missed out on the two most significant PostgreSQL acquisitions in the last five years. But they can ride Bain Capital's jock for a while, or hope that HPE buys them even though that [partnership](https://community.hpe.com/t5/oem-solutions/recap-hpe-greenlake-launch-discover-2017-madrid/ba-p/6991195) is from eight years ago. The PostgreSQL M&A playfield is reminiscent of OLAP acquisitions in the late 2000s, when [Vertica](https://investor.hp.com/news-events/news/news-details/2011/HP-to-Acquire-Vertica-Customers-Can-Analyze-Massive-Amounts-of-Big-Data---at-Speed-and-Scale/default.aspx) was the last one waiting at the bus stop after [AsterData](https://techcrunch.com/2011/03/03/teradata-buys-aster-data-263-million/), [Greenplum](https://techcrunch.com/2010/07/06/emc-acquires-data-warehousing-and-analytics-company-greenplum/), and [DATAllegro](https://news.microsoft.com/source/2008/07/24/microsoft-to-acquire-datallegro/) were acquired.

The development of the ~~two~~ three competing distributed PostgreSQL projects ([Multigres](https://multigres.com/), [Neki](https://planetscale.com/neki), [PgDog](https://pgdog.dev/)) is welcome news. These projects are not the first time somebody has attempted this: [Greenplum](https://www.vmware.com/products/app-platform/tanzu-greenplum), [ParAccel](https://en.wikipedia.org/wiki/ParAccel), and [Citus](https://www.citusdata.com/) have been around for two decades for OLAP workloads. Citus supports OLTP workloads, but they started in 2010 focused on [analytics](https://www.citusdata.com/blog/2018/06/07/what-is-citus-good-for/#:~:text=we%20focused%20on%20building%20a%20fast%20database%20to%20power%20analytics). For OLTP, 15 years ago, the NTT RiTaDB project joined forces with [GridSQL](https://wiki.postgresql.org/wiki/GridSQL) to create [Postgres-XC](https://wiki.postgresql.org/wiki/Postgres-XC). Developers from Postgres-XC founded [StormDB](https://dbdb.io/db/stormdb), which [Translattice](https://translattice.com/pr/TransLattice_Acquires_StormDB_to_Enhance_TransLattice_Elastic_Database.shtml) later acquired in 2013. [Postgres-X2](https://postgres-x2.github.io/) was an attempt to modernize XC, but the developers abandoned that effort. Translattice open-sourced StormDB as [Postgres-XL](https://en.wikipedia.org/wiki/Postgres-XL), but the project has been dormant since 2018. [YugabyteDB](https://www.yugabyte.com/) came out in [2016](https://www.yugabyte.com/blog/yugabyte-has-arrived/) and is probably the most widely deployed sharded PostgreSQL system (and remains [open-source](https://github.com/yugabyte/yugabyte-db)!), but it is a hard fork, so it is only compatible with [PostgreSQL v15](https://docs.yugabyte.com/stable/api/ysql/). Amazon announced its own sharded PostgreSQL ([Aurora Limitless](https://aws.amazon.com/blogs/aws/amazon-aurora-postgresql-limitless-database-is-now-generally-available/)) in 2024, but it is closed source.

I know Microsoft bought Citus in 2019 but it is hard to keep track of what they were doing before HorizonDB because of their confusing product names. Citus was rebranded as [Azure Database for PostgreSQL Hyperscale](https://techcommunity.microsoft.com/blog/adforpostgresql/azure-database-for-postgresql---hyperscale-citus-now-generally-available/1014865) in 2019 and was then renamed to [Azure Cosmos DB for PostgreSQL](https://devblogs.microsoft.com/cosmosdb/distributed-postgresql-comes-to-azure-cosmos-db/) in 2022. But then there is [Azure Database for PostgreSQL with Elastic Clusters](https://learn.microsoft.com/en-us/azure/postgresql/elastic-clusters/concepts-elastic-clusters) that also uses Citus, but it is not the same as the Citus-powered Azure Cosmos DB for PostgreSQL. Microsoft discontinued [Azure PostgreSQL Single Server](https://techcommunity.microsoft.com/discussions/azuredatabaseforpostgresql/announcement---retiring-azure-postgresql-single-server-in-march-2025-and-introdu/3820887) in 2023, but kept Azure PostgreSQL Flexible Server. That is a lot of Azure this and Azure that. It is sort of like how Amazon could not resist adding "Aurora" to [DSQL's](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/what-is-aurora-dsql.html) name. Either way, at least Microsoft was smart enough to keep the name for their new system to just "Azure HorizonDB" (for now).

The PlanetScale squad has [no love for the other side](https://youtu.be/CvgIRHhyRQE?t=143) and is known to throw hands at [Neon](https://blog.alexoglou.com/posts/database-decisions/) and [Timescale](https://twitter.com/samlambert/status/1984010289348780137). Database companies popping off at each other is nothing new (see [Yugabyte vs. CockroachDB](https://www.linkedin.com/posts/bobdoyleyugabyte_cockroach-labs-activity-7311530387271237634-xR78/) or [Databricks vs. Snowflake](https://www.cs.cmu.edu/~pavlo/blog/2025/01/2024-databases-retrospective.html#gangwar)). I suspect we will see more of this in the future as the PostgreSQL wars heat up. I suggest that these smaller companies [call out the big cloud vendors](https://twitter.com/samlambert/status/1996035931057652125) and keep each other's name [out of their mouths](https://youtu.be/0dT9siTP70Y).



MCP For Every Database!
-----------------------

If 2023 was the year [every DBMS added a vector index](https://www.cs.cmu.edu/~pavlo/blog/2024/01/2023-databases-retrospective.html#vector), then 2025 was the year that every DBMS added support for Anthropic's [Model Context Protocol](https://en.wikipedia.org/wiki/Model_Context_Protocol) (MCP). MCP is a standardized client-server JSON-RPC interface that lets LLMS interact with external tools and data sources without requiring custom glue code. An MCP server acts as middleware in front of a DBMS and exposes a listing of tools, data, and actions it provides. An MCP client (e.g., an LLM host such as Claude or ChatGPT) discovers and uses these tools to extend its models' capabilities by sending requests to the server. In the case of databases, the MCP server converts these queries into the appropriate database query (e.g., SQL) or administrative command. In other words, MCP is the middleman who keeps [the bricks counted and the cream straight](https://youtu.be/VXuwljCWZMU), so the database and LLMs trust each other enough to do business.

Anthropic [announced](https://www.theverge.com/2024/11/25/24305774/anthropic-model-context-protocol-data-sources) MCP in November 2024, but it really took off in March 2025 when OpenAI announced it would [support MCP in its ecosystem](https://techcrunch.com/2025/03/26/openai-adopts-rival-anthropics-standard-for-connecting-ai-models-to-data/). Over the next few months, every DBMS vendor released MCP servers for all system categories: OLAP (e.g., [ClickHouse](https://github.com/ClickHouse/mcp-clickhouse), [Snowflake](https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-agents-mcp), [Firebolt](https://github.com/firebolt-db/mcp-server), [Yellowbrick](https://yellowbrick.com/blog/application-development/yellowbrick-mcp-server-llms-cutting-code-time-and-speeding-up-etl-development/)), SQL (e.g., [YugabyteDB](https://www.yugabyte.com/blog/yugabytedb-mcp-server/), [Oracle](https://blogs.oracle.com/database/introducing-mcp-server-for-oracle-database), [PlanetScale](https://planetscale.com/docs/vitess/connecting/mcp)), and NoSQL (e.g., [MongoDB](https://www.mongodb.com/company/blog/announcing-mongodb-mcp-server), [Neo4j](https://github.com/neo4j-contrib/mcp-neo4j), [Redis](https://github.com/redis/mcp-redis)). Since there is no official Postgres MCP server, every Postgres DBaaS has released its own (e.g., [Timescale](https://github.com/timescale/pg-aiguide), [Supabase](https://github.com/supabase-community/supabase-mcp), [Xata](https://xata.io/blog/built-xata-mcp-server)). The cloud vendors released multi-database MCP servers that can talk to any of their managed database services (e.g., [Amazon](https://aws.amazon.com/blogs/database/supercharging-aws-database-development-with-aws-mcp-servers/), [Microsoft](https://learn.microsoft.com/en-us/azure/developer/azure-mcp-server/tools/azure-sql), [Google](https://cloud.google.com/blog/products/ai-machine-learning/mcp-toolbox-for-databases-now-supports-model-context-protocol)). Allowing a single gateway to talk to heterogeneous databases is almost, but not quite, a holy-grail [federated database](https://en.wikipedia.org/wiki/Federated_database_system). As far as I know, each request in these MCP servers targets only a single database at a time, so the application is responsible for performing joins across sources.

Beyond the official vendor MCP implementations, there are [hundreds](https://github.com/TensorBlock/awesome-mcp-servers/blob/main/docs/databases.md) of rando MCP server implementations for nearly every DBMS. Some of them attempt to support multiple systems (e.g., [DBHub](https://dbhub.ai/), [DB MCP Server](https://github.com/FreePeak/db-mcp-server)). DBHub put out a [good overview](https://dbhub.ai/blog/state-of-postgres-mcp-servers-2025) of PostgreSQL MCP servers.

An interesting feature that has proven helpful for agents is database branching. Although not specific to MCP servers, branching allows agents to test database changes quickly without affecting production applications. Neon reported in July 2025 that agents [create 80% of their databases](https://www.linkedin.com/posts/amitkumarvsingh_ai-agents-are-creating-more-databases-on-activity-7336398117862371328-Q6pO/). Neon was designed from the beginning to support [branching](https://dev.to/semaphore/a-first-look-at-neon-a-postgres-database-that-branches-10e6) (Nikita showed me an early demo when the system was still called "[Zenith](https://dbdb.io/db/neon#history)"), whereas other systems have added branching support later. See Xata's recent [comparison article](https://xata.io/blog/neon-vs-supabase-vs-xata-postgres-branching-part-1) on database branching.

### Andy's HeadAndy's Take:

On one hand, I'm happy that there is now a standard for exposing databases to more applications. But nobody should trust an application with unfettered database access, whether it is via MCP or the system's regular API. And it remains good practice only to grant minimal privileges to accounts. Restricting accounts is especially important with unmonitored agents that may start going wild all up in your database. This means that lazy practices like giving admin privileges to every account or using the same account for every service are going to get wrecked when the LLM starts popping off. Of course, if your company leaves its database [open to the world](https://www.theregister.com/2025/01/30/deepseek_database_left_open/) while you cause the stock price of one of the wealthiest companies to [drop by $600b](https://www.theregister.com/2025/01/30/deepseek_database_left_open/), then rogue MCP requests are not your top concern.

From my cursory examination of a few MCP server implementations, they are simple proxies that translate the MCP JSON requests into database queries. There is no deep introspection to understand what the request aims to do and whether it is appropriate. Somebody is going to try to [order 18,000 water cups](https://www.youtube.com/watch?v=DF8Pny3VTg8) in your application, and you need to make sure it doesn't crash your database. Some MCP servers have basic protection mechanisms (e.g., ClickHouse only allows [read-only queries](https://clickhouse.com/docs/use-cases/AI/MCP#clickhouse-mcp-server)). DBHub provides a few additional [protections](https://dbhub.ai/#why-dbhub), such as capping the number of returned records per request and implementing query timeouts. Supabase's documentation offers [best-practice guidelines](https://supabase.com/docs/guides/getting-started/mcp#recommendations) for MCP agents, but they rely on humans to follow them. And of course, if you rely on humans to do the right thing, [bad things will happen](https://www.generalanalysis.com/blog/supabase-mcp-blog).

Enterprise DBMSs already have automated guardrails and other safety mechanisms that open-source systems lack, and thus, they are better prepared for an agentic ecosystem. For example, [IBM Guardium](https://www.ibm.com/docs/en/gdp/12.x?topic=overview-guardium) and [Oracle Database Firewall](https://www.oracle.com/security/database-security/audit-vault-database-firewall/) identify and block anomalous queries. I am not trying to shill for these big tech companies. I know we will see more examples in the future of agents ruining lives, like [accidentally dropping databases](https://twitter.com/emil_priver/status/1783399265366052877). Combining MCP servers with proxies (e.g., connection pooling) is an excellent opportunity to introduce automated protection mechanisms.



MongoDB, Inc. v. FerretDB Inc.
------------------------------

MongoDB has been the NoSQL stalwart for two decades now. FerretDB was launched in 2021 by Percona's top brass to provide a middleware proxy that converts MongoDB queries into SQL for a PostgreSQL backend. This proxy allows MongoDB applications to switch over to PostgreSQL without rewriting queries.

They coexisted for a few years before MongoDB sent FerretDB a [cease-and-desist letter](https://blocksandfiles.com/wp-content/uploads/2025/04/Letter-from-MongoDB-to-FerretDB_3-Nov-2023-signed.pdf) in 2023, alleging that FerretDB infringes MongoDB's patents, copyrights, and trademarks, and that it violates MongoDB's license for its documentation and wire protocol specification.
This letter became public in May 2025 when MongoDB went [nuclear](https://youtu.be/11BlEYtj53Q) on FerretDB by filing a [federal lawsuit](https://dockets.justia.com/docket/delaware/dedce/1:2025cv00641/89247) over these issues.
Part of their beef is that FerretDB is out on the street, claiming they have a "[drop-in replacement](https://blog.ferretdb.io/ferretdb-1-0-ga-opensource-mongodb-alternative/)" for MongoDB without authorization. MongoDB's [court filing](https://storage.courtlistener.com/recap/gov.uscourts.ded.89247/gov.uscourts.ded.89247.1.0.pdf) has all the standard complaints about (1) misleading developers, (2) diluting trademarks, and (3) damaging their reputation.

The story is further complicated by Microsoft's announcement that it donated its MongoDB-compatible [DocumentDB](https://documentdb.io/) to the [Linux Foundation](https://www.linuxfoundation.org/press/linux-foundation-welcomes-documentdb-to-advance-open-developer-first-nosql-innovation). The project website mentions that DocumentDB is compatible with the MongoDB drivers and that it aims to "[build a MongoDB compatible open source document database](https://documentdb.io/#:~:text=our%20mission%20is%20to%20build%20a%20MongoDB%20compatible%20open%20source%20document%20database)". Other major database vendors, such as Amazon and Yugabyte, are also involved in the project. From a cursory glance, this language seems similar to what MongoDB is accusing FerretDB of doing.

### Andy's HeadAndy's Take:

I could not find an example of a database company suing another one for replicating their API. The closest is Oracle suing Google for using a clean-room copy of the Java API in Android. The Supreme Court ultimately [ruled in favor of Google](https://en.wikipedia.org/wiki/Google_LLC_v._Oracle_America%2C_Inc.) on fair use grounds, and the case affected how re-implementation is treated legally.

I don't know how the lawsuit will play out if it ever goes to trial. A jury of random people off the street may not be able to comprehend the specifics of MongoDB's wire protocol, but they are definitely going to understand that the original name of FerretDB was [MangoDB](https://www.reddit.com/r/programming/comments/qlyalj/mangodb_a_truly_open_source_mongodb_alternative/). It is going to be challenging to convince a jury that you were not trying to divert customers when you changed one letter in the other company's name. Never mind that it is not even an original name: there is already a parody DBMS called [MangoDB](https://dbdb.io/db/mangodb) that writes everything to `/dev/null` as a joke.

And while we are on the topic of database system naming, Microsoft's choice of "DocumentDB" is unfortunate. There are already [Amazon DocumentDB](https://aws.amazon.com/documentdb/) (which, by the way, is also [compatible](https://docs.aws.amazon.com/documentdb/latest/developerguide/compatibility.html#mongodb-80) with MongoDB, but Amazon probably pays for that), [InterSystems DocDB](https://docs.intersystems.com/irislatest/csp/docbook/DocBook.UI.Page.cls?KEY=GDOCDB_intro), and [Yugabyte DocDB](https://docs.yugabyte.com/stable/architecture/docdb/). Microsoft's original name for "Cosmos DB" was also [DocumentDB](https://auth0.com/blog/documentdb-with-aspnetcore/) back in 2016.

Lastly, MongoDB's court filing claims they "pioneered the development of 'non-relational' databases". This statement is incorrect. The first general-purpose DBMSs were non-relational because the relational model had not yet been invented. General Electric's [Integrated Data Store](https://en.wikipedia.org/wiki/Integrated_Data_Store) (1964) used a [network data model](https://en.wikipedia.org/wiki/Network_model), and IBM's [Information Management System](https://en.wikipedia.org/wiki/IBM_Information_Management_System) (1966) used a [hierarchical data model](https://en.wikipedia.org/wiki/Hierarchical_database_model). MongoDB is also not the first document DBMS. That title goes to the object-oriented DBMSs from the late 1980s (e.g., [Versant](http://www.versant.com/products/versant-object-database)) or the XML DBMSs from the 2000s (e.g., [MarkLogic](https://www.progress.com/marklogic)). MongoDB is the most successful of these approaches by a massive margin (except maybe IMS).



File Format Battleground
------------------------

File formats are an area of data systems that have been mostly dormant for the last decade. In 2011, Meta released a column-oriented format for Hadoop called [RCFile](https://en.wikipedia.org/wiki/RCFile). Two years later, Meta refined RCFile and announced the PAX-based [ORC](https://orc.apache.org/) (Optimized Record Columnar File) format. A month after ORC's release, Twitter and Cloudera released the first version of [Parquet](https://parquet.apache.org/). Nearly 15 years later, Parquet is the dominant file open-source format.

In 2025, there were five new open-source file formats released vying to dethrone Parquet:

* [CWI FastLanes](https://github.com/cwida/FastLanes)
* [CMU + Tsinghua F3](https://github.com/future-file-format/f3)
* [SpiralDB Vortex](https://vortex.dev)
* [The Germans' AnyBlox](https://github.com/AnyBlox)
* [Microsoft Amudai](https://web.archive.org/web/20250802074742/https://github.com/microsoft/amudai)

These new formats joined the other formats released in 2024:

* [Meta Nimble](https://github.com/facebookincubator/nimble)
* [LanceDB Lance](https://lancedb.com/blog/lance-v2/)
* [IoTDB TsFile](https://tsfile.apache.org/)

[SpiralDB](https://spiraldb.com/) made the biggest splash this year with their announcement of [donating Vortex to the Linux Foundation](https://www.linuxfoundation.org/press/lf-ai-data-foundation-hosts-vortex-project-to-power-high-performance-data-access-for-ai-and-analytics) and the establishment of their multi-organization steering committee. Microsoft quietly [killed off](https://github.com/microsoft/amudai) Amudai (or at least closed sourced it) at some point at the end of 2025. The other projects (FastLanes, F3, Anyblox) are academic prototypes. Anyblox won the [VLDB Best Paper](https://www.linkedin.com/posts/janagiceva_im-thrilled-and-honored-to-share-that-our-activity-7368909487023329281-mhDv/) award this year.

This fresh competition has lit a fire in the Parquet developer community to [modernize its features](https://docs.google.com/document/d/e/2PACX-1vSDHW7gvG8eO6aIxaIVPrZSqYYhtRDb5W1imnbpM4QRYNPsTwEO1fU5z7SEhVIFa4YqWJeSRJ9tcXYS/pub). See this [in-depth technical analysis](https://sympathetic.ink/2025/12/11/Column-Storage-for-the-AI-era.html) of the columnar file format landscape by Parquet PMC Chair ([Julien Le Dem](http://julien.ledem.net/)).

### Andy's HeadAndy's Take:

The main problem with Parquet is not inherent in the format itself. The specification can and has evolved. Nobody expected organizations to rewrite petabytes of legacy files to update them to the latest Parquet version. The problem is that there are so many implementations of reader/writer libraries in different languages, each supporting a distinct subset of the specification. Our [analysis](https://bsky.app/profile/andypavlo.bsky.social/post/3m256lckmec2z) of Parquet files in the wild found that 94% of them use only v1 features from 2013, even though their creation timestamps are after 2020. This lowest common denominator means that if someone creates a Parquet file using v2 features, it is unclear whether a system will have the correct version to read it.

I worked on the [F3](https://db.cs.cmu.edu/projects/future-file-formats/) file format with brilliant people at Tsinghua ([Xinyu Zeng](https://xinyuzeng.github.io/), [Ruijun Meng](https://dl.acm.org/profile/99661226655), [Huanchen Zhang](https://people.iiis.tsinghua.edu.cn/~huanchen/)), CMU ([Martin Prammer](https://www.cs.cmu.edu/~mprammer/), [Jignesh Patel](https://csd.cmu.edu/people/faculty/jignesh-patel)), and [Wes McKinney](https://wesmckinney.com/). Our focus is on solving this interoperability problem by providing both native decoders as shared objects (Rust crates) and embedded WASM versions of those decoders in the file. If somebody creates a new encoding and the DBMS does not have a native implementation, it can still read data using the WASM version by passing Arrow buffers. Each decoder targets a single column, allowing a DBMS to use a mix of native and WASM decoders for a single file. AnyBlox takes a different approach, generating a single WASM program to decode the entire file.

I don't know who will win the file format war. The next battle is likely to be over GPU support. SpiralDB seems to be making the right moves, but Parquet's ubiquity will be challenging to overcome. I also didn't even discuss how [DuckLake](https://ducklake.select/) seeks to upend Iceberg...

Of course, when this topic comes up, somebody always posts this [xkcd comic on competing standards](https://xkcd.com/927/). I've seen it before. You don't need to email it to me again.



Random Happenings
-----------------

Databases are big money. Let's go through them all!

#### Acquisitions:

Lots of movement on the block. Pinecone [replaced its CEO](https://venturebeat.com/data-infrastructure/pinecone-founder-edo-liberty-appoints-googler-ash-as-ceo) in September to [prepare for an acquisition](https://archive.is/N5h2a), but I have not heard anything else about it. Here are the ones that did happen:

* [DataStax → IBM](https://www.datastax.com/blog/ibm-plans-to-acquire-datastax)

  The Cassandra stalwart got picked up by IBM at the beginning of the year for an [estimated $3b](https://www.linkedin.com/posts/nathanlatka_saas-datastax-activity-7300252058274672640-OQx_/).
* [Quickwit → DataDog](https://quickwit.io/blog/quickwit-joins-datadog)

  The leading company behind the Lucene replacement, [Tantivy](https://github.com/quickwit-oss/tantivy), a full-text search engine, was acquired at the beginning of the year. The good news is that Tantivy development continues unabated.
* [SDF → dbt](https://www.getdbt.com/blog/dbt-labs-announces-sdf-labs-acquisition)

  This acquisition was a solid pick-up for dbt as part of their [Fusion](https://www.getdbt.com/product/fusion) announcement this year. It allows them to perform more rigorous SQL analysis in their DAGs.
* [Voyage.ai → MongoDB](https://www.mongodb.com/company/blog/news/redefining-database-ai-why-mongodb-acquired-voyage-ai)

  Mongo picked up an early-stage AI company to [expand](https://news.ycombinator.com/item?id=43160731) its RAG capabilities in its cloud offering. One of my [best students](https://www.linkedin.com/in/wangpatrick57/) joined Voyage one week before the announcement. He thought he was going against the "family" by not signing with a database company, only to end up at one.
* [Neon → Databricks](https://neon.tech/blog/neon-and-databricks)

  Apparently, there was a bidding war for this PostgreSQL company, but Databricks paid a [mouthwatering $1b](https://www.wsj.com/articles/databricks-to-buy-startup-neon-for-1-billion-fdded971) for it. Neon still exists today as a standalone service, but Databricks quickly rebranded it in its ecosystem as [Lakebase](https://www.databricks.com/product/lakebase).
* [CrunchyData → Snowflake](https://www.wsj.com/articles/snowflake-to-buy-crunchy-data-for-250-million-233543ab)

  You know Snowflake could not let Databricks get all the excitement during the summer, so they paid $250m for the 13-year-old PostgreSQL company CrunchyData. Crunchy had picked up top ex-Citus talent in recent years and was expanding its DBaaS offering before Snowflake wrote them a check. Snowflake announced the public preview of its [Postgres](https://www.snowflake.com/en/product/features/postgres/) service in December 2025.
* [Informatica → Salesforce](https://www.cnbc.com/amp/2025/05/27/salesforce-informatica-deal.html)

  The 1990s old-school ETL company Informatica got picked up by Salesforce for [$8b](https://finance.yahoo.com/news/salesforce-buys-informatica-8b-failed-150907984.html). This is after they went public in 1999, reverted to PE in 2015, and went public again in 2021.
* [Couchbase → Private Equity](https://investors.couchbase.com/news-releases/news-release-details/couchbase-be-acquired-haveli-investments-15-billion)

  To be honest, I never understood how Couchbase went public in 2021. I guess they were riding on MongoDB's coattails? Couchbase did interesting work a few years ago by incorporating components from the [AsterixDB project at UC Irvine](https://www.couchbase.com/press-releases/couchbase-announces-first-commercial-implementation-of-sql-with-n1ql-for-analytics/).
* [Tecton → Databricks](https://www.reuters.com/business/finance/databricks-buy-sequoia-backed-tecton-ai-agent-push-2025-08-22/)

  Tecton provides Databricks with additional tooling to build agents. Another one of my [former students](https://www.linkedin.com/in/agrawalrohit10/) was at the company and is now at Databricks.
* [Tobiko Data → Fivetran](https://www.fivetran.com/press/fivetran-acquires-tobiko-data-to-power-the-next-generation-of-advanced-ai-ready-data-transformation)

  This team is behind two useful tools: [SQLMesh](https://sqlmesh.readthedocs.io/) and [SQLglot](https://sqlglot.com/). The former is the only viable open-source contender to dbt (see [below](#random-mergers) for their pending merger with Fivetran). SQLglot is a handy SQL parser/deparser that supports a heuristic-based query optimizer. The combination of this in Fivetran and SDF with dbt makes for an interesting technology play in this space in the coming years.
* [SingleStore → Private Equity](https://www.businesswire.com/news/home/20250910856970/en/SingleStore-Announces-Growth-Buyout-Led-by-Vector-Capital)

  The PE firm buying SingleStore ([Vector Capital](https://www.vectorcapital.com/)) has prior experience in managing a database company. They previously purchased the [XML database company MarkLogic in 2020](https://www.businesswire.com/news/home/20201021005279/en/Vector-Capital-Completes-Acquisition-of-MarkLogic) and flipped it to [Progress in 2023](https://investors.progress.com/news-releases/news-release-details/progress-announces-plans-acquire-marklogic).
* [Codership → MariaDB](https://www.dbta.com/Editorial/News-Flashes/MariaDB-to-Acquire-Galera-Cluster-to-Enable-Deeper-Integration-of-Synchronous-Replication-Technology-169742.aspx)

  After getting bought by PE in 2024, the MariaDB Corporation went on a buying spree this year. The first up is the company behind the [Galera Cluster](https://mariadb.com/docs/galera-cluster) scale-out middleware for MariaDB. See my 2023 overview of the [MariaDB dumpster fire](https://www.cs.cmu.edu/~pavlo/blog/2024/01/2023-databases-retrospective.html#mariadb).
* [SkySQL → MariaDB](https://www.crn.com/news/cloud/2025/mariadb-buys-back-skysql-in-database-flexibility-push)

  And then we have the second MariaDB acquisition. Just so everyone is clear, the original commercial company backing MariaDB was called "SkySQL Corporation" in 2010, but it changed its name to "MariaDB Corporation" in 2014. Then in 2020, the MariaDB Corporation released a MariaDB DBaaS called SkySQL. But because they were hemorrhaging cash, the MariaDB Corporation spun SkySQL Inc. out as an [independent company in 2023](https://www.businesswire.com/news/home/20231214486927/en/MariaDB-Finalizes-Spinoff-of-SkySQL). And now, in 2025, MariaDB Corporation has come full circle by [buying back SkySQL Inc](https://medium.com/@arbaudie.it/personal-opinion-mariadb-re-acquires-skysql-125181507358). I did not have this move on my database bingo card this year.
* [Crystal DBA → Temporal](https://www.crystaldba.ai/blog/post/temporal-technologies-acquires-crystal-dba)

  The automated database optimization tool company heads off to Temporal to automatically optimize their databases! I'm happy to hear that Crystal's founder and Berkeley database group alumnus [Johann Schleier-Smith](https://www.linkedin.com/in/jssmith/) is doing well there.
* [HeavyDB → Nvidia](https://www.harvestmp.com/transactions)

  This system (formerly OmniSci, formerly MapD) was one of the first GPU-accelerated databases, launched in 2013. I couldn't find an official announcement of their closing, aside from an M&A firm listing the successful deal. And then we had a meeting with Nvidia to discuss potential database research collaborations, and some HeavyDB friends showed up.
* [DGraph → Istari Digital](https://www.prnewswire.com/news-releases/istari-digital-acquires-dgraph-to-strengthen-data-foundation-for-ai-and-engineering-302593246.html)

  Dgraph was previously acquired by [Hypermode in 2023](https://web.archive.org/web/20250806150448/https://hypermode.com/blog/the-future-of-dgraph-is-open-serverless-and-ai-ready). It looks like Istari just bought Dgraph and not the rest of Hypermode (or they ditched it). I still haven't met anybody who is actively using Dgraph.
* [DataChat → Mews](https://www.mews.com/en/press/mews-acquires-datachat)

  This was one of the first "chat with your database" out of the University of Wisconsin and now CMU-DB professor [Jignesh Patel](https://jigneshpatel.org/). But they were bought by a European hotel management SaaS. Take that to mean what you think it means.
* [Datometry → Snowflake](https://siliconangle.com/2025/11/10/snowflake-acquires-database-migration-startup-datometry/)

  Datometry has been working on the perilous problem of automatically converting legacy SQL dialects (e.g., Teradata) to newer OLAP systems for several years. Snowflake picked them up to expand their [migration tooling](https://www.snowflake.com/en/blog/accelerate-data-migration-datometry-technology/). See Datometry's 2020 [CMU-DB tech talk](https://www.youtube.com/watch?v=cL1-BIaQSYE&list=PLSE8ODhjZXjagqlf1NxuBQwaMkrHXi-iz&index=23) for more info.
* [LibreChat → ClickHouse](https://clickhouse.com/blog/librechat-open-source-agentic-data-stack)

  Like Snowflake buying Datometry, ClickHouse's acquisition here is a good example of improving the developer experience for high-performance commodity OLAP engines.
* [Mooncake → Databricks](https://www.databricks.com/blog/mooncake-labs-joins-databricks-accelerate-vision-lakebase)

  After buying Neon, Databricks bought Mooncake to enable PostgreSQL to read/write to Apache Iceberg data. See their November 2025 [CMU-DB talk](https://www.youtube.com/watch?v=VqFZyWHGQVM&list=PLSE8ODhjZXjbEeW_bOCZ8c_nx_Jhoz-GW&index=8) for more info.
* [Confluent → IBM](https://www.reuters.com/technology/ibm-nears-roughly-11-billion-deal-confluent-wsj-reports-2025-12-08/)

  This is the archetype of how to make a company out of a grassroots open-source project. Kafka was originally developed at Linkedin in 2011. Confluent was then spun out as a separate startup in 2014. They went IPO seven years later in 2021. Then IBM wrote a big check to take it over. Like with DataStax, it remains to be seen whether IBM will do to Confluent what IBM normally does with [acquired companies](https://news.ycombinator.com/item?id=43200706), or whether they will be able to remain autonomous like RedHat.
* [Gel → Vercel](https://www.geldata.com/blog/gel-joins-vercel)

  Formerly [EdgeDB](#random-naming), they provided DSL on top of PostgreSQL that got picked up by Verel at the end of the year.
* [Kuzu → ???](https://www.theregister.com/2025/10/14/kuzudb_abandoned/)

  The embedded graph DBMS out of the University of Waterloo was acquired by an unnamed company in 2025. The KuzuDB company then announced it was abandoning the open-source project. The [LadybugDB](https://ladybugdb.com/) project is an attempt at maintaining a fork of the Kuzu code.
* [Oxla → Redpanda](https://www.redpanda.com/press/redpanda-acquires-oxla-launches-new-agentic-data-plane-for-enterprise-data)

  The Kafka-compatible streaming company Redpanda bought a PostgreSQL-compatible distributed database company.

#### Mergers:

Unexpected news dropped in October 2025 when [Fivetran](https://www.fivetran.com/) and [dbt Labs](https://www.getdbt.com/) announced they were [merging](https://www.reuters.com/business/a16z-backed-data-firms-fivetran-dbt-labs-merge-all-stock-deal-2025-10-13) to form a single company.

The last merger I can think of in the database space was the 2019 merger between [Cloudera and Hortonworks](https://techcrunch.com/2018/10/03/cloudera-and-hortonworks-announce-5-2-billion-merger/). But that deal was just weak keys getting [stepped on in a kitchen](https://youtu.be/9qkOyiWJIXI): two companies that were struggling to find market relevance with Hadoop merged into a single company to try to find it (spoiler: they did not). The MariaDB Corporation merger with [Angel Pond Holdings Corporation](https://mariadb.com/newsroom/press-releases/mariadb-completes-merger-and-lands-on-nyse-as-mrdb/) in 2022 via a [SPAC](https://en.wikipedia.org/wiki/Special-purpose_acquisition_company) technically counts too, but that deal was so MariaDB could backdoor their way to IPO. And it didn't end well for [investors](https://www.bizjournals.com/sanjose/news/2022/12/19/mariadb-goes-public-in-spac-merger.html). The Fivetran + dbt merger is different (and better) than these two. They are two complementary technology companies combining to become an ETL juggernaut, preparing for a legit IPO in the near future.

#### Funding:

Unless I missed them or they weren't announced, there were not as many early-stage funding rounds for database startups. The buzz around vector databases has muted, and VCs are only writing checks for LLM companies.

* **Databricks** - [$4b Series L](https://www.databricks.com/company/newsroom/press-releases/databricks-surpasses-4-8b-revenue-run-rate-growing-55-year-over-year)
* **Databricks** - [$1b Series K](https://www.reuters.com/business/databricks-eyes-over-100-billion-valuation-investors-back-ai-growth-plans-2025-08-19/)
* **ClickHouse** - [$350m Series C](https://clickhouse.com/blog/clickhouse-raises-350-million-series-c-to-power-analytics-for-ai-era)
* **Supabase** - [$200m Series D](https://finance.yahoo.com/news/exclusive-supabase-raises-200-million-112154867.html)
* **Timescale** - [$110m Series C](https://www.tigerdata.com/blog/year-of-the-tiger-110-million-to-build-the-future-of-data-for-developers-worldwide)
* **Supabase** - [$100m Series E](https://supabase.com/blog/supabase-series-e)
* **Astronomer** - [$93m Series D](https://www.astronomer.io/press-releases/astronomer-secures-93-million-series-d-funding/)
* **Tessel** - [$60m Series B](https://www.tessell.com/press-releases/tessell-raises-60m-series-b-to-expand-ai-driven-multi-cloud-data-ecosystems)
* **LanceDB** - [$30m Series A](https://lancedb.com/blog/series-a-funding/)* **Convex** - [$24m Series B](https://news.convex.dev/convex-raises-24m/)* **SpiralDB** - [$22m Series A](https://www.axios.com/pro/enterprise-software-deals/2025/09/11/database-startup-spiral-22-million)
    * **ParadeDB** - [$12m Series A](https://techcrunch.com/2025/07/15/paradedb-takes-on-elasticsearch-as-interest-in-postgres-explodes-amid-ai-boom/)
    * **CedarDB** [$5.9m Seed](https://www.munich-startup.de/en/109750/cedardb-secures-53-million-euros/)
    * **TopK** - [$5.5m Seed](https://www.topk.io/blog/seed-round)
    * **Columnar** - [$4m Seed](https://columnar.tech/blog/announcing-columnar)
    * **SereneDB** - [$2.1m Pre-Seed](https://tech.eu/2025/12/03/serenedb-lands-21m-to-fuse-search-analytics-and-postgres-into-one-engine/)
    * **Starburst** - [Undisclosed?](https://www.prnewswire.com/news-releases/starburst-announces-strategic-investment-from-citi-302456950.html)
    * **TurboPuffer** - [Undisclosed?](https://tpuf.link/comms)

#### Name Changes:

A new category in my yearly write-up is database companies changing the name of their company or system.

* [HarperDB → Harper](https://www.dbta.com/Editorial/News-Flashes/HarperDBs-Rebrand-Reflects-its-Commitment-to-Delivering-a-Full-Stack-Application-Delivery-Platform-168390.aspx)

  The JSON database company dropped the "DB" suffix from its name to emphasize its positioning as a platform for database-backed applications, similar to [Convex](https://www.convex.dev/) and Heroku. I like the Harper people. Their 2021 [CMU-DB tech talk](https://www.youtube.com/watch?v=I5_xIs6xsJQ&list=PLSE8ODhjZXjbeqnfuvp30VrI7VXiFuOXS&index=7) presented the [worst](https://twitter.com/andy_pavlo/status/1372673306445365250) DBMS idea I have ever heard. Thankfully, they ditched that once they realized how bad it was and switched to LMDB.
* [EdgeDB → Gel](https://www.geldata.com/blog/edgedb-is-now-gel-and-postgres-is-the-future)

  This was a smart move because the name "Edge" conveys that it is a database for edge devices or services (e.g., [Fly.io](http://fly.io)). But I'm not sure "Gel" conveys the project's higher-level goals. See their 2025 [CMU-DB talk on Gel's query language](https://www.youtube.com/watch?v=RzLo-pdUJ7I&list=PLSE8ODhjZXjbpOIrZheFWxkYG8HD87xW1&index=10) (still called EdgeQL) from a CMU Ph.D. alum.
* [Timescale → TigerData](https://www.tigerdata.com/blog/timescale-becomes-tigerdata)

  This is a rare occurrence of a database company renaming itself to distinguish itself from its main database product. It is usually companies renaming themselves to be the name of the database (e.g., "Relational Software, Inc." to "Oracle Systems Corporation", "10gen, Inc." to "MongoDB, Inc."). But it makes sense for the company to try to shed the perception of being a specialized time-series DBMS instead of an improved version of PostgreSQL for general applications, since the former is a much smaller market segment than the latter.

#### Deaths:

In full disclosure, I was a technical advisor for two of these failed startups. My success rate as an advisor is terrible at this point. I was also an advisor for [Splice Machine](https://dbdb.io/db/splice-machine), but they closed shop in 2021. In my defense, I only talk with these companies about technical ideas, not business strategies. And I did tell Fauna they should add SQL support, but they did not take my advice.

* [Fauna](https://www.infoworld.com/article/3853569/fauna-to-shut-down-faunadb-service-in-may.html)

  An interesting distributed DBMS based on [Dan Abadi's](https://www.cs.umd.edu/~abadi/) research for [deterministic concurrency control](https://vldb.org/pvldb/vol3/R06.pdf). They provided strongly consistent transactions right when the NoSQL fade was waning, and Spanner made transactions cool again. But they had a [proprietary query language](https://faunadb-docs.netlify.app/fauna/current/learn/query/) and made big bets on GraphQL.
* [PostgresML](https://github.com/postgresml/postgresml/issues/1688#issuecomment-3041057338)

  The idea seemed obvious: enable people to run ML/AI operations inside of their PostgreSQL DBMS. The challenge was to convince people to migrate their existing databases to their hosted platform. They were pushing [pgCat](https://github.com/postgresml/pgcat) as a proxy to mirror database traffic. One of the co-founders joined Anthropic. The other co-founder created a new proxy project called [pgDog](https://pgdog.dev/).
* [Derby](https://issues.apache.org/jira/browse/DERBY-7177)

  This is one of the first DBMSs written in Java, dating back to 1997 (originally called "Java DB" or "JBMS"). IBM donated it to the Apache Foundation in the 2000s, and it was renamed as Derby. In October 2025, the project announced that the system would enter "read-only mode" because no one was actively maintaining it anymore.
* [Hydra](https://www.hydra.so/)

  Although there is no official announcement for the DuckDB-inside-Postgres startup, the co-founders and employees have scattered to other companies.
* [MyScaleDB](https://twitter.com/MyScaleDB/status/1917163010311037327)

  This was a fork of Clickhouse that adds vector search and full-text indexing using Tantivy. They announced they were closing in May 2025.
* [Voltron Data](https://www.linkedin.com/posts/aocsa_as-some-of-you-may-have-seen-voltron-data-activity-7395229870517022720-sGOP/)

  This was supposed to be the supergroup of database companies. Think of it like having [Run the Jewels](https://youtu.be/G-S9mtYowPY) team of heavy hitters. You had top engineers from Nvidia Rapids, the [inventor](https://en.wikipedia.org/wiki/Wes_McKinney) of Apache Arrow and Python Pandas, and the Peruvian GPU wizards from [BlazingSQL](https://github.com/BlazingDB/blazingsql). Then throw in [$110m in VC money](https://waldencatalyst.com/blog/founder-spotlight-voltron-data) from top firms that included the future CEO of Intel (and a [board of trustee member at CMU](https://en.wikipedia.org/wiki/Lip-Bu_Tan)). They built a GPU-accelerated database ([Theseus](https://arxiv.org/abs/2508.05029)), but failed to launch it in a timely manner.

Lastly, although not a business, I would be remiss not to mention the [closing](https://www.siliconvalley.com/2025/07/10/ibm-san-jose-tech-data-ai-internet-property-real-estate-economy-web/) of [IBM Research Almaden](https://en.wikipedia.org/wiki/IBM_Research#Almaden_in_Silicon_Valley). IBM built this site in 1986 and was the database research mecca for decades. I interviewed at [Almaden in 2013](https://twitter.com/andy_pavlo/status/306455280823177216) and found the scenery to be beautiful. The IBM Research Database Group is not what it [used to be](https://dl.acm.org/doi/10.1145/126482.126493). Still, the alum list of this hallowed database ground is impressive: [Rakesh Agrawal](https://en.wikipedia.org/wiki/Rakesh_Agrawal_(computer_scientist)), [Donald Chamberlin](https://en.wikipedia.org/wiki/Donald_D._Chamberlin), [Ronald Fagin](https://en.wikipedia.org/wiki/Ronald_Fagin), [Laura Haas](https://en.wikipedia.org/wiki/Laura_M._Haas), [Mohan](https://en.wikipedia.org/wiki/C._Mohan), [Pat Selinger](https://en.wikipedia.org/wiki/Patricia_Selinger), [Moshe Vardi](https://en.wikipedia.org/wiki/Moshe_Vardi), [Jennifer Widom](https://en.wikipedia.org/wiki/Jennifer_Widom), and [Guy Lohman](https://scholar.google.com/citations?user=wUkamYwAAAAJ&hl=en).

**Update 2026-01-05:** I missed that Gel was acquired by Vercel in December 2025. [[Credit]](https://www.geldata.com/blog/gel-joins-vercel)

**Update 2026-01-05:** I also missed that Supabase raised two funding rounds in 2025.

**Update 2026-01-05:** Although TurboPuffer has not made an official announcement for raising a round, their CEO mentions adding somebody from Thrive Capital to their team. [[Credit]](https://www.linkedin.com/in/julianlaneve)

**Update 2026-01-05:** Apparently I need a better way to track fundraises because I missed LanceDB's Series A round too! [[Credit]](https://twitter.com/brittwalker_/status/2008306941286904111)

**Update 2026-01-18:** I added that Redpanda bought Oxla in October 2025.

### Andy's HeadAndy's Take:

Somebody [claimed](https://news.ycombinator.com/item?id=42571405) that I judge the quality of a database based on how much funding the backing company raises for its development. This is obviously not true. I track these happenings because the database research game is crowded and high-energy. Not only am I "competing" against academics at other universities, but big tech companies and small start-ups are also putting out interesting systems I need to follow. The industry research labs are not what they used to be, except for Microsoft Research, which is still aggressively hiring top people and doing incredible work.

I [predicted in 2022](https://www.cs.cmu.edu/~pavlo/blog/2022/12/2022-databases-retrospective.html#:~:text=fate%20of%20database%20start%2Dups) that there would be a large number of database company closings in 2025. Yes, there were more closings this year than in previous years, but not at the scale I expected.

The death of Voltron and sort-of acquihire of HeavyDB seem to continue the trend of the inviability of GPU-accelerated databases. [Kinetica](https://twitter.com/KineticaHQ/status/1988983193870156171) has been milking government contracts for years, and [Sqream](https://sqream.com/) still appears to be kicking it. These companies are still niche, and nobody has been able to make a significant dent in the dominance of CPU-powered DBMSs. I can't say who or what, but you will hear some major GPU-accelerated database announcements by vendors in 2026. It also provides further evidence of the commoditization of OLAP engines; modern systems have gotten so fast that the performance between them is negligible for low-level operations (scans, joins), so the things that differentiate one system from another are user experience and the quality of the query plans their optimizers generate.

The Couchbase and SingleStore acquisitions by private equity (PE) firms might signal a future trend in the database industry. Of course, PE acquisitions have happened before, but they all seem to be in recent times: (1) [MarkLogic](https://www.vectorcapital.com/investments/case-study/marklogic) in 2020, (2) [Cloudera](https://techcrunch.com/2021/06/01/cloudera-to-go-private-as-kkr-cdr-grab-it-for-5-3b/) in 2021, and (3) [MariaDB](https://techcrunch.com/2024/09/10/mariadb-goes-private-with-new-ceo-as-k1-closes-acquisition/) in 2023. The only ones I can find before 2020 were [SolidDB](https://www.channelinsider.com/tech-companies/ibm-buys-database-software-firm/) in 2007 and [Informatica](https://www.aakashg.com/story-informatica-second-ipo/) in 2015. PE acquisitions might replace the trend of plateaued database companies being bought by holding companies that milk the maintenance fees until eternity (Actian, Rocket). Even Oracle is still making money off [RDB/VMS](https://www.oracle.com/database/technologies/related/rdb.html) after buying them 30 years ago!

Lastly, props to [Nikita Shamgunov](https://www.linkedin.com/in/nikitashamgunov). As far as I know, he is the only person to have co-founded two database companies ([SingleStore](https://hackernoon.com/founder-interviews-nikita-shamgunov-of-memsql-8a9ca8d33552) and [Neon](https://www.madrona.com/building-a-modern-database-neon-nikita-shamgunov-serverless-postgres/)) that were both acquired in a single year. Like when DMX (RIP) released two #1 albums in a single year ([It's Dark and Hell Is Hot](https://en.wikipedia.org/wiki/It%27s_Dark_and_Hell_Is_Hot), [Flesh of My Flesh](https://en.wikipedia.org/wiki/Flesh_of_My_Flesh,_Blood_of_My_Blood)), I don't think anybody is going to break Nikita's record any time soon.



Peak Male Performance
---------------------

Talk about a banner year for the database OG Larry Ellison. The man turned 81 and accomplished more in one year than most people do in their lifetime. I will cover it all in chronological order.

Larry started the year ranked third-richest in the world. The idea that he would be worth less than Mark Zuckerberg was keeping him up at night. Some were saying Larry's insomnia was due to a diet change after he [bought a famous British pub](https://www.bbc.com/news/uk-england-oxfordshire-67221202) and was eating more pies. But I assure you that Larry's "[veg-aquarian](https://tech.yahoo.com/science/articles/80-old-billionaire-larry-ellison-105236014.html)" diet has not changed in 30 years. Then, in April 2025, we got the news that Larry had become the [second-richest person in the world](https://www.msn.com/en-in/autos/photos/larry-ellison-becomes-second-richest-person-beats-zuckerberg-bezos-after-oracle-stock-soars/ar-AA1GKdbu). He started sleeping a little better, but it still wasn't good enough. There was also still a lot going on in his life that was stressing him out. For example, Larry finally decided to sell his rare, semi-road-legal [McLaren F1 supercar](https://www.forbes.com/sites/maryroeloffs/2025/08/05/larry-ellisons-old-mclaren-f1-could-break-a-sales-record/), complete with the original owner's manual in the glovebox.

In July 2025, Larry graced us with this [third tweet](https://twitter.com/larryellison/status/1945229587929337947) in 13 years (known as "#3" by Larry aficionados such as myself). This was an update about the [Ellison Institute of Technology](https://eit.org/) (EIT) that Larry established near the University of Oxford. With the name EIT and its association with Oxford, it sounds like it would be a pure research, non-profit institution, similar to Stanford's [SRI](https://en.wikipedia.org/wiki/SRI_International) or CMU's [SEI](https://en.wikipedia.org/wiki/Software_Engineering_Institute). But it turns out to be an umbrella organization for a series of for-profit companies owned by a California-based limited liability company. Of course, a bunch of weirdos replied to #3 with promises of [blockchain-powered cryogenic freezing](https://twitter.com/SFCryptoRounder/status/1946047224779030564) or [room-temperature superconductors](https://twitter.com/JackSarfatti/status/1975985052204101709). Larry told me he ignores those. Then there are people like [this guy](https://twitter.com/aseemchandra/status/1945509650201301304) who get it.

The biggest database news of the year (possibly the century) hit us on Wednesday, September 10th, at approximately 3:00pm EST. After waiting for his turn for decades, Larry Joseph Ellison was finally anointed the [richest person in the world](https://www.theguardian.com/technology/2025/sep/10/larry-ellison-dislodges-elon-musk-as-worlds-richest-person). [$ORCL](https://finance.yahoo.com/quote/ORCL/) shares rose by 40% that morning, and since Larry still owns 40% of the company, his estimated total worth is [$393b](https://www.bbc.com/news/articles/cx2rp992y88o). To put this in perspective, this not only made Larry the wealthiest person in the world, but also the richest person in the entire history of humanity. The peak net worths, adjusted for inflation, of [John D. Rockefeller](https://en.wikipedia.org/wiki/John_D._Rockefeller) and [Andrew Carnegie](https://en.wikipedia.org/wiki/Andrew_Carnegie) (yes, the 'C' in CMU) were only [$340b](https://www.buysidedigest.com/insights/the-top-10-wealthiest-historical-figures-adjusted-for-inflation/) and [$310b](https://www.celebritynetworth.com/richest-businessmen/richest-billionaires/andrew-carnegie-net-worth/), respectively.

On top of Larry's ascension to the top of the world, Oracle was also involved in the [acquisition of the U.S. company controlling TikTok](https://www.npr.org/2025/12/18/nx-s1-5648844/tiktok-deal-oracle-trump) and Larry [bankrolling Paramount](https://variety.com/2025/tv/news/paramount-skydance-larry-ellison-irrevocable-personal-guarantee-warner-bros-discovery-1236614728/) (controlled by his son from his fourth marriage) bid to [take over Warner Bros](https://www.nytimes.com/2025/12/24/business/media/larry-david-ellison-warner-bros-discovery-cbs.html). The U.S. president even chided Larry to [take control of CNN's news division](https://www.theguardian.com/us-news/2025/nov/20/warner-bros-discovery-takeover-paramount-skydance-larry-ellison) since Larry is the majority shareholder of Paramount.

### Andy's HeadAndy's Take:

I don't even know where to begin. Of course, when I found out that Larry Ellison had become the richest person in the world, all thanks to databases, I was [heartened](https://twitter.com/andy_pavlo/status/1965865919223312495) that something positive had finally happened in our lives. I don't care that Oracle's stock was artificially pumped up by [splashy deals](https://www.investors.com/news/technology/oracle-stock-orcl-ai-analyst-targets/) to build AI data centers instead of its traditional software business. I don't care that he dropped down the rankings after personally losing [$130b in two months](https://www.bloomberg.com/news/articles/2025-11-21/oracle-slump-sends-ellison-sliding-down-ranks-of-world-s-richest). That's like you and me [blowing a paycheck on FortuneCoins](https://www.reddit.com/r/gambling/comments/1j4xby2/blew_my_whole_paycheck/). It stings a little, and we had to eat rice and beans for two weeks mixed with expired hot sauce packets we took from Taco Bell, but we'll be alright.

Some people claim that Larry is [out of touch](https://news.ycombinator.com/item?id=45413203) with ordinary people. Or that he has lost his way because he is involved in things not directly related to databases. They point to things like his [Hawaiian robot farm](https://techcrunch.com/2025/02/23/the-lesson-of-larry-ellisons-misadventures-in-farming/) selling [lettuce at $24/pound](https://beatofhawaii.com/the-most-expensive-lettuce-in-hawaii-billionaire-larry-ellisons-24-lb-experiment/) (€41/kg). Or that 81-year-old men don't have [naturally blonde hair](https://assets.sfstandard.com/image/994911177489/image_cooaesgkll0v99j57e84lobk7k/-S3840x2560-FPNG).

The truth is that Larry Ellison has conquered the enterprise database world, [competitive sailing](https://sg.finance.yahoo.com/news/why-oracle-founder-larry-ellison-205016907.html), and [techbro wellness spas](https://www.businessinsider.com/larry-ellison-hawaii-wellness-spa-sensei-lanai-photos-2021-2). The obvious next step is to take over a cable TV channel watched by thousands of people waiting in airports every day. Every time I talk with Larry, he makes it clear that he does not care one bit what people say or think about him. He knows his [fans love him](https://twitter.com/HolgersenTobias/status/1945239198572712323). His (new) [wife loves him](https://www.financialexpress.com/life/lifestyle-who-is-jolin-zhu-worlds-richest-man-larry-ellisons-fifth-wife-47-years-younger-than-him-3974373/). And in the end, that's all that matters.



Conclusion
----------

Before we close, I want to give some quick shout outs and words of advice. First is to PT for keeping their [database game tight](https://turso.tech/blog/working-on-databases-from-prison) with Turso in lockdown (see you on the outside). Condolences to JT for [losing their job](https://twitter.com/canoozie/status/1952305339824574576) for trapping their [KevoDB](https://github.com/KevoDB/kevo) database sidepiece. And be sure to only put in fake data in your database for testing and not to [sell it for $175m only to end up getting a seven year bid](https://abcnews.go.com/Business/charlie-javice-founder-lied-175m-startup-faces-sentencing/story?id=126034577).

My Ph.D. students and I also have a new [start-up](https://sydht.ai/). I hope to say more on that soon. Word is bond.
