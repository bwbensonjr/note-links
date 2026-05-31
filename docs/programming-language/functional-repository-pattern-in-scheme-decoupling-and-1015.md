---
id: 1015
url: https://jointhefreeworld.org/blog/articles/lisps/functional-repository-pattern-in-scheme-with-macros/index.html
title: Functional repository pattern in Scheme? Decoupling and abstracting the data
  layer in Lisp - jointhefreeworld
domain: jointhefreeworld.org
source_date: '2026-04-14'
tags:
- scheme
- lisp
- tutorial
- database
summary: The author presents a functional implementation of the Repository Pattern
  in Scheme using hygienic macros to decouple the data layer from application logic
  in MVC architecture. Two key macros—`define-record-with-kw` for ergonomic keyword-argument
  constructors and `define-repo-method` for flexible method definitions—create a clean
  embedded domain-specific language that abstracts SQLite implementation details away
  from business logic. This approach enables better separation of concerns, easier
  testing, and cleaner code organization across the author's Scheme projects.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# Functional repository pattern in Scheme? Decoupling and abstracting the data layer in Lisp - jointhefreeworld

*Implementing the Repository Pattern with Hygienic Macros in Scheme*

**Hi everyone!**

I’ve been working on a new approach for the data layer of my projects
lately, and I’d love to poke your brains and get some feedback.

Coming from a background in Scala, Java and other OOP languages and a
fascination for FP languages and Lisps (as well as Rust and Haskell),
I’ve seen a lot of patterns come and go.

Recently, I noticed a common anti-pattern in my own Scheme projects: a
tight coupling between my controller layer and the SQLite
implementation. It wasn’t ideal, and I really missed the clean
separation of the **Repository Pattern**.

So, I set out to decouple my data layer from my controller layer in the
MVC architecture I love. I wanted to do this using pure functional
programming, and I ended up building something really fun using
**Scheme’s hygienic macros**.

(If you want to see this implemented in a real project, check out my
example repo here:
[lucidplan](https://codeberg.org/jjba23/lucidplan))

I am working on adding it to
[byggsteg](https://codeberg.org/jjba23/byggsteg) too.

I plan to bring this pattern to all my projects to reap the benefits of
the eDSL, better decoupling, and easier testing. Here is how I built it.

The Macros [#](#the-macros)
---------------------------

I created two main macros. `define-record-with-kw` magically defines a
keyword-argument constructor, bypassing the need for strict parameter
ordering. It’s highly ergonomic.

`define-repo-method` is the real
superpower. It accepts any arity, plus optional or `#:keyword`
arguments. This saves a ton of work, reduces tedious parameter passing,
and gives you a very clean eDSL definition.

```
(define-module (lucidplan domain repo)
  #:declarative? #t
  #:use-module (srfi srfi-9)
  #:export (define-repo-method define-record-with-kw))

(define-syntax define-repo-method
  (syntax-rules ()
                ((_ method-name accessor docstring)
                 (define* (method-name repo . args)
                   docstring
                   (apply (accessor repo) args)))))

(define-syntax define-record-with-kw
  (syntax-rules ()
                ((_ (type-name constructor-name pred) kw-constructor-name
                    (field-name accessor-name) ...)
                 (begin
                   ;; Define the standard SRFI-9 record
                   (define-record-type type-name
                     (constructor-name field-name ...) pred
                     (field-name accessor-name) ...)

                   ;; Define the keyword-argument constructor
                   (define* (kw-constructor-name #:key field-name ...)
                     (constructor-name field-name ...))

                   ;; Auto-export members
                   (export type-name pred kw-constructor-name accessor-name
                           ...)))))
```

Defining the Domain eDSL [#](#defining-the-domain-edsl)
-------------------------------------------------------

Here is how I use those macros to define my DSL for a “projects” entity:

```
(define-module (lucidplan domain project)
  #:declarative? #t
  #:use-module (srfi srfi-9)
  #:use-module (lucidplan domain repo)
  #:export (get-projects))

;; -- Record definition ---

(define-record-with-kw (<project-repository> %make-project-repository
                                             project-repository?)
                       mk-project-repository
                       (get-projects-proc repo-get-projects))

;; --- eDSL: Embedded Domain Specific Language ---

(define-repo-method get-projects repo-get-projects
 "Retrieves a list of all active projects from the given REPO.")
```

The SQLite Implementation [#](#the-sqlite-implementation)
---------------------------------------------------------

Finally, here is the concrete SQLite implementation using Artanis. this
is completely decoupled from the rest of the application logic.

```
(define-module (lucidplan sqlite project)
               #:declarative? #t
               #:use-module (srfi srfi-9)
               #:use-module (kracht prelude)
               #:use-module (artanis db)
               #:use-module (lucidplan sqlite util)
               #:use-module (lucidplan domain project)
               #:export (make-sqlite-project-repository))

;; --- Artanis + SQLite implementation ---
(define (make-sqlite-project-repository rc)
        (define columns
                '(id human-id
                     title
                     url
                     vcs-url
                     description
                     created-at
                     updated-at
                     deleted-at))

        (define (get-projects)
                (let* ((query (format #f
                                      "SELECT ~a
                   FROM project WHERE deleted_at IS NULL
                   ORDER BY human_id ASC"
                                      (symbols->sql-columns-list columns)))
                       (_ (log-info "get-projects query:\n\t~a\n" query))
                       (rows (map sql-row->scheme-alist
                                  (DB-get-all-rows (DB-query (DB-open rc) query))))
                       (_ (log-info "get-projects rows: ~a\n"
                                    (length rows))))
                  rows))

        (mk-project-repository #:get-projects-proc get-projects))
```

A condensed example with keyword arguments:

```
;; The DSL (notice how arity is clean)
(define-repo-method get-jobs repo-get-jobs
                  "Retrieves a list of active jobs from the given REPO.")

;; SQLite implementation
(define* (get-jobs #:key limit offset)
  (let* ((query (format #f
                 "SELECT ~a FROM job
                 ORDER BY created_at DESC LIMIT ~a OFFSET ~a"
                 (symbols->sql-columns-list columns) limit offset))
         (_ (log-info "get-jobs query:\n\t~a\n" query))
         (rows (map sql-row->scheme-alist
                    (DB-get-all-rows (DB-query (DB-open rc) query))))
         (_ (log-info "get-jobs rows: ~a\n"
                      (length rows))))
    rows))
```

Using it can look like

```
(let*
  (job-repo (make-sqlite-job-repository rc))
  (jobs (get-jobs job-repo #:limit 50 #:offset 0))
.......)
```

I believe I have something really powerful cooking here, but I know
there is always room for improvement.

**What do you all think?** How would you go about improving this? I’m
entirely open to criticism, feedback, and brainstorming!

Thanks for reading this :)
