---
id: 1259
url: https://techascent.com/blog/just-ducking-around.html
title: TechAscent - DuckDB - Data power tools for your laptop, now in Clojure
domain: techascent.com
source_date: '2026-08-05'
tags:
- clojure
- database
- tutorial
summary: DuckDB integrated with Clojure's tech.ml.dataset provides a powerful solution
  for processing large datasets locally without distributed computing complexity.
  The article demonstrates practical examples of loading a 50GB CSV file into an 18GB
  DuckDB database and performing complex operations like joining 1.4 billion rows
  in under 2.5 seconds on a laptop. By leveraging DuckDB's vectorized SQL engine through
  Clojure, developers can handle out-of-memory data while maintaining functional programming
  benefits and efficient batched processing capabilities.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# TechAscent - DuckDB - Data power tools for your laptop, now in Clojure

[![Link Button Icon](/img/button-back.svg)Blog Home](/blog/)[![TechAscent - Delightful Software Solutions](/img/ta-mark-red.svg)](/)

[Contact](/contact.html)

2023-09-02

DuckDB - Data power tools for your laptop, now in Clojure
---------------------------------------------------------

#### Establishing the Need

Our in-memory column-major data processing platform, [tech.ml.dataset](https://github.com/techascent/tech.ml.dataset) (TMD), drives the future of functional data science. When data gets large enough not to fit in memory, one can continue with TMD by operating on samples of data, or otherwise filtering to relevant subsets to fit in bounds imposed by the working environment. Moreover, one can accomplish persistence, for data small and large, with nippy, arrow, or [parquet](/blog/clojure-csv-parquet.html).

When data becomes large enough, for example sets of .csv files on the order of ~100GB with relational aspects to them, the tools in their current state can become unwieldy. One is tempted to get involved in nonfunctional sparky cluster snafus. Of course, maintaining some level of transactional interaction and a simple disk IO model is still super-desirable. Local disks are big enough, and local chips are fast enough, no need to do anything rash.

Relational databases are well adapted for out-of-memory storage and fast relational queries - but, how to leverage this without giving up the advantages of functional programming, and TMD's column-major processing model? JDBC, along with Postgres, provide a good first answer to this question, but it's irritating to perform a full row-to-column conversion through an inefficient, non-batched API in order to get the data through JDBC and into TMD.

#### A New Challenger Appears

DuckDB showed up via a [github issue](https://github.com/techascent/tech.ml.dataset/issues/241) in May of 2021 and [tmducken](https://github.com/techascent/tmducken) was minimally integrated with their C bindings by December of that year. In that version, all query results were returned at once, and so needed to fit in memory. Also, in those early days of DuckDB there was not a specific high performance append or insert system, so IO was limiting potential performance, and Postgres persisted as the adjunct processing system to TMD. Much has changed since then.

In the last two years, DuckDB improved a lot. Importantly, the C interface now provides a batched system for both inserts and querying, which enables processing very large joins - more on that later. These improved capabilities can now be leveraged in Clojure, through TMD, to access DuckDB's state of the art vectorized SQL execution engine, and it's good.

#### Actual Use

Building on our [previous post](/blog/clojure-csv-parquet.html), there is a 50 gigabyte .csv file with 3 years of transaction data, totaling 400,000,000 rows:

```
$ ll -h data.csv
-rw-rw-r-- 1 harold harold 50G Aug  8 09:49 data.csv
```

Loading that into DuckDB is surprisingly easy - though, you do have to wait 2 minutes:

```
$ time duckdb data.ddb 'CREATE TABLE data AS FROM "data.csv";'
100% ▕████████████████████████████████████████████████████████████▏

real	1m50.091s
user	21m42.693s
sys	0m57.887s
$ ll -h data.ddb
-rw-rw-r-- 1 harold harold 18G Sep  6 10:57 data.ddb
```

So, that reduced the file to 18GB, which includes all of the indexes (!) created automatically by DuckDB.

The data is in there:

```
$ duckdb data.ddb
v0.8.1 6536a77232
Enter ".help" for usage hints.
D SELECT COUNT(*) AS n FROM data;
┌───────────┐
│     n     │
│   int64   │
├───────────┤
│ 400000000 │
└───────────┘
D DESCRIBE TABLE data;
┌────────────────┬─────────────┬─────────┬─────────┬─────────┬─────────┐
│  column_name   │ column_type │  null   │   key   │ default │  extra  │
│    varchar     │   varchar   │ varchar │ varchar │ varchar │ varchar │
├────────────────┼─────────────┼─────────┼─────────┼─────────┼─────────┤
│ customer-id    │ VARCHAR     │ YES     │         │         │         │
│ day            │ BIGINT      │ YES     │         │         │         │
│ inst           │ TIMESTAMP   │ YES     │         │         │         │
│ month          │ BIGINT      │ YES     │         │         │         │
│ brand          │ VARCHAR     │ YES     │         │         │         │
│ style          │ VARCHAR     │ YES     │         │         │         │
│ sku            │ VARCHAR     │ YES     │         │         │         │
│ year           │ BIGINT      │ YES     │         │         │         │
│ transaction-id │ VARCHAR     │ YES     │         │         │         │
│ quantity       │ BIGINT      │ YES     │         │         │         │
│ price          │ DOUBLE      │ YES     │         │         │         │
├────────────────┴─────────────┴─────────┴─────────┴─────────┴─────────┤
│ 11 rows                                                    6 columns │
└──────────────────────────────────────────────────────────────────────┘
```

Accessing this from Clojure, through TMD, is also easy:

```
user> (require '[tmducken.duckdb :as duckdb])
nil
user> (require '[tech.v3.dataset :as ds])
nil
user> (duckdb/initialize!)
Sep 06, 2023 11:00:12 AM clojure.tools.logging$eval7454$fn__7457 invoke
INFO: Attempting to load duckdb from "./binaries/libduckdb.so"
true
user> (def db (duckdb/open-db "data.ddb"))
#'user/db
user> (def conn (duckdb/connect db))
#'user/conn
user> (time (duckdb/sql->dataset conn "SELECT COUNT(*) AS n FROM data"))
"Elapsed time: 10.305756 msecs"
:_unnamed [1 1]:

|         n |
|----------:|
| 400000000 |
```

Now, imagine management lets us know that there is another dataset, that captures information for each sku about what colors the product is. That needs to be in the database as well:

```
user> (-> (let [colors ["red" "green" "blue" "yellow" "purple" "black" "white"]]
            (->> (for [brand (range 100)
                       style (range 10)
                       item (range 10)]
                   (let [sku (format "sku-%s-%s-%s" brand style item)
                         n (rand-int 8)]
                     (for [color (take n (shuffle colors))]
                       {"sku" sku
                        "color" color})))
                 (apply concat)))
          (ds/->dataset {:dataset-name "colors"}))
colors [35179 2]:

|        sku |  color |
|------------|--------|
|  sku-0-0-0 |    red |
|  sku-0-0-0 |   blue |
|  sku-0-0-0 |  white |
|  sku-0-0-0 | yellow |
|  sku-0-0-0 |  black |
|  sku-0-0-0 |  green |
|  sku-0-0-1 |  black |
|  sku-0-0-1 | yellow |
|  sku-0-0-1 |   blue |
|  sku-0-0-1 | purple |
|        ... |    ... |
| sku-99-9-8 | yellow |
| sku-99-9-8 | purple |
| sku-99-9-8 |  black |
| sku-99-9-8 |    red |
| sku-99-9-8 |  white |
| sku-99-9-8 |   blue |
| sku-99-9-8 |  green |
| sku-99-9-9 | purple |
| sku-99-9-9 |   blue |
| sku-99-9-9 |  black |
| sku-99-9-9 |  green |
user> (duckdb/create-table! conn *1)
"colors"
user> (duckdb/insert-dataset! conn *2)
35179
```

You know where this is going. We need to join the 400M transactions, each with a sku, with this data that implies each sku has about 3.51 colors.

Luckily, their first request is relatively simple. "How many items of each color were sold in March of 2021?", and "When can we know?" they ask.

```
;; First, because you can, join 1.4 billion rows on your laptop in 2.5s...
user> (time (duckdb/sql->dataset conn "SELECT COUNT(*) FROM data INNER JOIN colors ON data.sku = colors.sku;"))
"Elapsed time: 2486.620275 msecs"
:_unnamed [1 1]:

| count_star() |
|-------------:|
|   1416737859 |

;; Then, answer their question...
user> (time (duckdb/sql->dataset conn "SELECT color, COUNT(*) FROM data INNER JOIN colors ON data.sku = colors.sku WHERE data.year='2021' AND data.month='3' GROUP BY color;"))
"Elapsed time: 1077.723309 msecs"
:_unnamed [7 2]:

|  color | count_star() |
|--------|-------------:|
|    red |      5714223 |
| yellow |      5652010 |
|  black |      5720753 |
|   blue |      5750846 |
|  white |      5689916 |
|  green |      5816652 |
| purple |      5671959 |
```

We can know 1s from now. Here are the answers.

Maybe the next question is not well suited to SQL, and doing the processing in Clojure, with TMD, would be better. This example reduces over *every* transaction of the boss' favorite sku, sorted chronologically (in 1s):

```
user> (time
       (reduce (fn [eax ds]
                 (conj eax (ds/row-count ds)))
               []
               (duckdb/sql->datasets conn "SELECT * FROM data WHERE sku='sku-50-5-5' ORDER BY inst")))
"Elapsed time: 1067.480751 msecs"
[2048 576 2048 576 2048 576 2048 576 2048 576 2048 576 2048 576 2048 576 2048 576 2048 576 2048 576 2048 576 2048 576 2048 576 2048 576 733]
```

Of course, this reduction function is trivial, but it proves the point - realized datasets are available for arbitrary processing, through reduction, by a mechanism that will never run out of memory.

DuckDB also supports a [zero copy query pathway](https://duckdb.org/2021/12/03/duck-arrow.html). If no chunk of the query result needs to escape the reducing function, then the machine can possibly do less work. In the example below this is turned on and accessed by passing the `{:reduce-type :zero-copy-imm}` option.

When processing can be expressed in this manner, this is theoretically the lowest memory pathway available.

```
user> (time (let [sql "SELECT * FROM data WHERE sku='sku-50-5-5' ORDER BY inst"
                  options {:reduce-type :zero-copy-imm}]
              (reduce (fn [eax zc-ds]
                        (conj eax (ds/row-count zc-ds)))
                      []
                      (duckdb/sql->datasets conn sql options))))
"Elapsed time: 1037.480113 msecs"
[2048 531 2048 531 2048 531 2048 531 2048 531 2048 531 2048 531 2048 531 2048 531 2048 531 2048 531 2048 531 2048 531 2048 531 2048 531 1408]
```

---

Hopefully that gives a sense of the power afforded by this system, now.

#### Some Interesting DuckDB TidBits

DuckDB automatically stores all numeric data in [minmax indexes](https://duckdb.org/docs/sql/indexes.html) - also called BRIN indexes. These do not add significantly to the original data size but do dramatically increase query performance. It will also automatically create ART indexes in the case of unique or primary key columns. Finally, users can optionally create indexes for categorical columns but the drawback is increased disk storage size and potentially slower transactions.

DuckDB is written in standard C++11 and is thus fairly portable - they had a variant built for the mac m-1 quickly and if you had another platform and wanted some special sauce we would feel comfortable compiling and modifying the database for that platform. The src directory of their codebase, as of this writing (September 2023) clocks in at about 100,000 LOC of C++ code:

```
(base) chrisn@chrisn-lp2:~/dev/cnuernber/duckdb$ cloc src
    1612 text files.
    1612 unique files.
       0 files ignored.

github.com/AlDanial/cloc v 1.90  T=0.83 s (1936.0 files/s, 203773.8 lines/s)
-------------------------------------------------------------------------------
Language                     files          blank        comment           code
-------------------------------------------------------------------------------
C++                            831          13749           8912          99454
C/C++ Header                   679           7754           9903          28287
CMake                          101             49              0           1541
Markdown                         1              7              0             15
-------------------------------------------------------------------------------
SUM:                          1612          21559          18815         129297
-------------------------------------------------------------------------------
```

DuckDB is MIT licensed, has an open github development model, and their community is quick to answer questions. Developing such a high quality power tool in such an open manner is honorable.

#### Wrapping Up

Try out our [duckdb integration](https://github.com/techascent/tmducken), or to hire us to do it for you. DuckDB complements TMD well and greatly increases a small team's ability to efficiently manage and process large datasets without needing to resort to expensive distributed solutions. This integration supports and represents the value of high quality and efficient compute tools to truly democratize data processing by enabling functional solutions on laptops that others with duller tools will reach for a cluster to manage.

---

TechAscent: Getting our ducks in a row.

[Contact us](/contact.html)

Make software work for you.
---------------------------

[Get In Touch](/contact.html)
