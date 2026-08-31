---
id: 1303
url: https://github.com/astral-sh/uv/pull/21327
title: 'Deduplicate all files in the wheel cache by charliermarsh · Pull Request #21327
  · astral-sh/uv · GitHub'
domain: github.com
source_date: '2026-08-31'
tags:
- github-repo
- python
- devops
summary: This pull request introduces file-level deduplication to the uv package manager's
  wheel cache, storing every file under its BLAKE3 hash and using hardlinks to reference
  them from their original locations. The optimization achieves approximately 545.2
  MiB of cache savings (about 10% of total cache size) with a minimal performance
  tradeoff of less than 4% slowdown for cold installs and no impact on warm installs.
  The implementation passes comprehensive testing and benchmarks across multiple packages,
  confirming the deduplication works correctly without significant performance degradation.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# Deduplicate all files in the wheel cache by charliermarsh · Pull Request #21327 · astral-sh/uv · GitHub

### Uh oh!

There was an error while loading. Please reload this page.

[astral-sh](/astral-sh) 
/
**[uv](/astral-sh/uv)**
Public

* [Notifications](/login?return_to=%2Fastral-sh%2Fuv) You must be signed in to change notification settings
* [Fork
  3.5k](/login?return_to=%2Fastral-sh%2Fuv)
* [Star
   89.3k](/login?return_to=%2Fastral-sh%2Fuv)

Conversation
------------

[![@charliermarsh](https://avatars.githubusercontent.com/u/1309177?s=80&v=4)](/charliermarsh)

### @charliermarsh **[charliermarsh](/charliermarsh)** commented [Aug 27, 2026](#issue-5271456937) • edited Loading Uh oh! There was an error while loading. Please reload this page.

Copy link
 

Copy Markdown

Member

Summary
-------

On main, we support content-addressed caching, but only at the wheel-level. That is, if you download the same wheel twice from different sources, they share a cache entry. But files *within* or *across* wheels are not deduplicated at all.

This PR adds deduplication at the file level: every file is now stored under its BLAKE3 hash in a `files-v0` bucket. We hardlink these objects into their original locations in `archive-v0`, so the installation step doesn't change at all -- we're just deduping *within* the cache (and cache cleanup removes file objects when their hardlink count drops to one).

In the prior proposal ([#19694](https://github.com/astral-sh/uv/pull/19694)), we included the following table:

| File selection | Additional savings | Files hardlinked | Distinct `files-v0` objects |
| --- | --- | --- | --- |
| Executables and native libraries | 275.7 MiB | 3,336 | 3,088 |
| Any payload file ≥ 10 MiB | 235.0 MiB | 80 | 78 |
| Any payload file ≥ 1 MiB | 279.7 MiB | 373 | 349 |
| Any payload file ≥ 100 KiB | 353.4 MiB | 2,830 | 2,458 |
| Any payload file ≥ 10 KiB | 475.7 MiB | 23,767 | 18,722 |
| Any payload file ≥ 1 KiB | 537.4 MiB | 95,156 | 66,422 |
| All payload files | 545.2 MiB | 134,222 | 87,129 |

So we're saving 545.2 MiB on my local machine, or about 10% of the cache.

In return, the net effect seems to be something like a <4% slowdown for cold installs (and no effect on warm installs), which I think is *probably* worthwhile here.

[![@charliermarsh](https://avatars.githubusercontent.com/u/1309177?s=40&u=6328c998d93a48eba87c6b039783b8a7644c62c3&v=4)](/charliermarsh)

[charliermarsh](/charliermarsh)
[temporarily deployed](https://github.com/astral-sh/uv/actions/runs/33109528930/job/98648403110)
to
automations
[August 27, 2026 19:40](#event-30126623090) — with ![](https://avatars.githubusercontent.com/in/15368?s=40&u=167a342ed94d2a713daf64a8b476ead2cebe1852&v=4)
[GitHub Actions](https://github.com/apps/github-actions)

Inactive

[![@astral-automations-bot](https://avatars.githubusercontent.com/in/4307167?s=40&v=4)](/apps/astral-automations-bot)
[astral-automations-bot](/apps/astral-automations-bot)
Bot
mentioned this pull request
[Aug 27, 2026](#ref-issue-5271688833)

[Linux cargo-test setup fails when Depot runners lack Minix support
astral-sh/uv-dev#896](/astral-sh/uv-dev/issues/896)

Open

[![@charliermarsh](https://avatars.githubusercontent.com/u/1309177?s=40&u=6328c998d93a48eba87c6b039783b8a7644c62c3&v=4)](/charliermarsh)

[charliermarsh](/charliermarsh)
[temporarily deployed](https://github.com/astral-sh/uv/actions/runs/33120732611/job/98686840556)
to
automations
[August 27, 2026 22:01](#event-30132854801) — with ![](https://avatars.githubusercontent.com/in/15368?s=40&u=167a342ed94d2a713daf64a8b476ead2cebe1852&v=4)
[GitHub Actions](https://github.com/apps/github-actions)

Inactive

[![@charliemarsh-oai](https://avatars.githubusercontent.com/u/282065134?s=80&u=bdb0ab25cf17a57513b5e77a5db213b15a60cc6a&v=4)](/charliemarsh-oai)

### **[charliemarsh-oai](/charliemarsh-oai)** commented [Aug 27, 2026](#issuecomment-5445746459) • edited by charliermarsh Loading Uh oh! There was an error while loading. Please reload this page.

Copy link
 

Copy Markdown

Contributor

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| *N.B. Slop comment for benchmark data.*  We benchmarked the optimization in [85c3f7485](https://github.com/astral-sh/uv/commit/85c3f748502f1372af29c020c4b31f860550b0c7) against the binary-only cache at [a3f977ece](https://github.com/astral-sh/uv/commit/a3f977ece0370cc0663bb578b1d0d51600228042), with `--preview-features content-addressed-cache` enabled on both. These are medians for the complete `uv pip install` process; positive changes mean slower.   | Wheel | Cache | Parent median | Optimized median | Change (95% CI) | | --- | --- | --- | --- | --- | | AnyIO 4.9.0 | cold | 90.4 ms | 93.4 ms | +3.39% (+2.87% to +3.86%) | | AnyIO 4.9.0 | warm | 29.9 ms | 30.3 ms | +1.14% (-1.08% to +3.85%) | | SymPy 1.14.0 | cold | 367.1 ms | 381.6 ms | +3.95% (+3.49% to +4.46%) | | SymPy 1.14.0 | warm | 84.6 ms | 84.0 ms | -0.64% (-1.04% to -0.11%) | | NumPy 2.2.6 | cold | 314.1 ms | 326.5 ms | +3.95% (+3.24% to +4.82%) | | NumPy 2.2.6 | warm | 62.5 ms | 62.7 ms | +0.28% (-0.55% to +1.25%) | | PyTorch 2.7.1+cpu | cold | 2982.6 ms | 3072.9 ms | +3.03% (+0.98% to +5.18%) | | PyTorch 2.7.1+cpu | warm | 404.0 ms | 403.1 ms | -0.21% (-0.72% to +0.11%) |   Before this optimization, the measured cold regressions were +4.02% for AnyIO 4.9.0, +19.41% for SymPy 1.14.0, +12.75% for NumPy 2.2.6, +15.30% for PyTorch 2.7.1+cpu.  **All eight median regressions are below 5%.** The PyTorch cold 95% interval still reaches 5.18%, so its upper bound is not below 5%. Every other upper bound is below 5%.  We retained all 1,860 measured installs, including outliers, and combined every confirmation run for this candidate. Cold measurements have 360 paired rounds for AnyIO, 120 each for SymPy and NumPy, and 90 for PyTorch; warm measurements have 60 paired rounds per wheel. Baseline/candidate order alternates, with three warmups per case. Intervals use a paired percentile bootstrap of the ratio of medians with 10,000 resamples.  These measurements ran on Linux/ext4, an AMD EPYC-Milan VM pinned to eight CPUs, with Python 3.12.13. Both binaries use Rust 1.98.0 and the same `profiling` profile (optimized, no LTO). Each sample installs one pinned local wheel offline, without dependencies or bytecode compilation, using hardlinks into a fresh virtual environment. Cold removes the entire uv cache; warm retains a primed cache. Setup and cleanup are untimed, and the wheel OS page cache is warm. No compilation ran during the benchmarks. These results do not cover other platforms or network-inclusive installs.  All-file deduplication, content/executable identities, the cache layout, complete archives, and copy fallbacks are preserved. Inode checks confirmed that every archived file shares its file-store object for all four wheels. The five targeted integration tests passed ten stress iterations (50 executions), including local and streamed wheels with one and four workers, RECORD handling, cache cleanup, and cross-filesystem installation. Formatting and Clippy with warnings denied also passed. |

[![@charliermarsh](https://avatars.githubusercontent.com/u/1309177?s=40&u=6328c998d93a48eba87c6b039783b8a7644c62c3&v=4)](/charliermarsh)

[charliermarsh](/charliermarsh)
[temporarily deployed](https://github.com/astral-sh/uv/actions/runs/33126779314/job/98706849532)
to
automations
[August 27, 2026 23:35](#event-30136024269) — with ![](https://avatars.githubusercontent.com/in/15368?s=40&u=167a342ed94d2a713daf64a8b476ead2cebe1852&v=4)
[GitHub Actions](https://github.com/apps/github-actions)

Inactive

[![@codspeed-hq](https://avatars.githubusercontent.com/in/257293?s=80&v=4)](/apps/codspeed-hq)

### **[codspeed-hq](/apps/codspeed-hq) Bot** commented [Aug 27, 2026](#issuecomment-5446639271) • edited Loading Uh oh! There was an error while loading. Please reload this page.

Copy link
 

Copy Markdown

|  |
| --- |
| Merging this PR will **not alter performance** `✅ 25` untouched benchmarks  `⏩ 12` skipped benchmarks[1](#user-content-fn-skipped-01f518c4a19ea1b4e91666bff13d0fba)   ---   Comparing `charlie/dirhash-all-files` ([d12d2ad](https://github.com/astral-sh/uv/commit/d12d2ad2b909621e1151d62e4d7dada645227edd)) with `main` ([7c1d80e](https://github.com/astral-sh/uv/commit/7c1d80ed02eb434f8228f42b32fa6c157bab7f3c)) [Open in CodSpeed](https://app.codspeed.io/astral-sh/uv/branches/charlie%2Fdirhash-all-files?utm_source=github&utm_medium=comment-v2&utm_content=button) Footnotes  1. 12 benchmarks were skipped, so the baseline results were used instead. If they were deleted from the codebase, [click here and archive them to remove them from the performance reports](https://app.codspeed.io/astral-sh/uv/branches/charlie%2Fdirhash-all-files?q=is%3Askipped&utm_source=github&utm_medium=comment-v2&utm_content=archive). [↩](#user-content-fnref-skipped-01f518c4a19ea1b4e91666bff13d0fba) |

[![@charliermarsh](https://avatars.githubusercontent.com/u/1309177?s=40&u=6328c998d93a48eba87c6b039783b8a7644c62c3&v=4)](/charliermarsh)

[charliermarsh](/charliermarsh)
marked this pull request as ready for review
[August 28, 2026 00:03](#event-30136831499)

[![@charliermarsh](https://avatars.githubusercontent.com/u/1309177?s=40&u=6328c998d93a48eba87c6b039783b8a7644c62c3&v=4)](/charliermarsh)

[charliermarsh](/charliermarsh)
[force-pushed](/astral-sh/uv/compare/a3f977ece0370cc0663bb578b1d0d51600228042..1f28fd5f49873c1cb8993d94c07b48046443d989)
the

charlie/dirhash-binaries
branch
from
[`a3f977e`](/astral-sh/uv/commit/a3f977ece0370cc0663bb578b1d0d51600228042) to
[`1f28fd5`](/astral-sh/uv/commit/1f28fd5f49873c1cb8993d94c07b48046443d989)  [Compare](/astral-sh/uv/compare/a3f977ece0370cc0663bb578b1d0d51600228042..1f28fd5f49873c1cb8993d94c07b48046443d989)
[August 28, 2026 00:08](#event-30136997361)

[![@charliermarsh](https://avatars.githubusercontent.com/u/1309177?s=40&u=6328c998d93a48eba87c6b039783b8a7644c62c3&v=4)](/charliermarsh)

[charliermarsh](/charliermarsh)
[force-pushed](/astral-sh/uv/compare/0a8edc0249bcbb4964812cb2ad14bb1eec4110cc..a108fab82108ad09a373913f95c6d9c5313a4ab1)
the

charlie/dirhash-all-files
branch
from
[`0a8edc0`](/astral-sh/uv/commit/0a8edc0249bcbb4964812cb2ad14bb1eec4110cc) to
[`a108fab`](/astral-sh/uv/commit/a108fab82108ad09a373913f95c6d9c5313a4ab1)  [Compare](/astral-sh/uv/compare/0a8edc0249bcbb4964812cb2ad14bb1eec4110cc..a108fab82108ad09a373913f95c6d9c5313a4ab1)
[August 28, 2026 00:08](#event-30136997714)

[![@charliermarsh](https://avatars.githubusercontent.com/u/1309177?s=40&u=6328c998d93a48eba87c6b039783b8a7644c62c3&v=4)](/charliermarsh)

[charliermarsh](/charliermarsh)
[temporarily deployed](https://github.com/astral-sh/uv/actions/runs/33128769751/job/98713261012)
to
automations
[August 28, 2026 00:09](#event-30137026573) — with ![](https://avatars.githubusercontent.com/in/15368?s=40&u=167a342ed94d2a713daf64a8b476ead2cebe1852&v=4)
[GitHub Actions](https://github.com/apps/github-actions)

Inactive

[![@charliermarsh](https://avatars.githubusercontent.com/u/1309177?s=40&u=6328c998d93a48eba87c6b039783b8a7644c62c3&v=4)](/charliermarsh)

[charliermarsh](/charliermarsh)
changed the base branch from
charlie/dirhash-binaries
to
main
[August 28, 2026 00:09](#event-30137027402)

[![@charliermarsh](https://avatars.githubusercontent.com/u/1309177?s=40&u=6328c998d93a48eba87c6b039783b8a7644c62c3&v=4)](/charliermarsh)
[charliermarsh](/charliermarsh)
added
[enhancement](/astral-sh/uv/issues?q=state%3Aopen%20label%3Aenhancement)
New feature or improvement to existing functionality
[preview](/astral-sh/uv/issues?q=state%3Aopen%20label%3Apreview)
Experimental behavior
labels
[Aug 28, 2026](#event-30137125456)

[![@charliermarsh](https://avatars.githubusercontent.com/u/1309177?s=40&u=6328c998d93a48eba87c6b039783b8a7644c62c3&v=4)](/charliermarsh)

[charliermarsh](/charliermarsh)
requested review from
[woodruffw](/woodruffw) and
[zanieb](/zanieb)
[August 28, 2026 00:13](#event-30137129060)

[![@charliermarsh](https://avatars.githubusercontent.com/u/1309177?s=40&u=6328c998d93a48eba87c6b039783b8a7644c62c3&v=4)](/charliermarsh)

[charliermarsh](/charliermarsh)
[temporarily deployed](https://github.com/astral-sh/uv/actions/runs/33129526181/job/98715666341)
to
automations
[August 28, 2026 00:23](#event-30137439553) — with ![](https://avatars.githubusercontent.com/in/15368?s=40&u=167a342ed94d2a713daf64a8b476ead2cebe1852&v=4)
[GitHub Actions](https://github.com/apps/github-actions)

Inactive

[![@charliermarsh](https://avatars.githubusercontent.com/u/1309177?s=40&u=6328c998d93a48eba87c6b039783b8a7644c62c3&v=4)](/charliermarsh)
[charliermarsh](/charliermarsh)
mentioned this pull request
[Aug 28, 2026](#ref-pullrequest-5273564008)

[Pipeline file cache publication for streamed wheels
#21333](/astral-sh/uv/pull/21333)

Draft

[![@astral-sh-bot](https://avatars.githubusercontent.com/in/2242089?s=80&v=4)](/apps/astral-sh-bot)

### **[astral-sh-bot](/apps/astral-sh-bot) Bot** commented [Aug 28, 2026](#issuecomment-5447209293)

Copy link
 

Copy Markdown

|  |
| --- |
| uv test inventory changes This PR changes the tests when compared with the `main` base revision.   * Added tests: **5** * Removed tests: **0** * Changed suites: **2**  `uv-extract`: +1 / -0   **Added:**   * `uv-extract::dirhash::archive::tests::extracted_file_executable_status`   **Removed:** none   `uv::pip_install`: +4 / -0   **Added:**   * `uv::pip_install::pip_install::all_files_except_record_use_archive_file_store` * `uv::pip_install::pip_install::binary_payload_copy_fallback_uses_archive_file_store` * `uv::pip_install::pip_install::binary_payloads_stay_in_archive_without_preview` * `uv::pip_install::pip_install::binary_payloads_use_archive_file_store`   **Removed:** none |

[![@charliermarsh](https://avatars.githubusercontent.com/u/1309177?s=40&u=6328c998d93a48eba87c6b039783b8a7644c62c3&v=4)](/charliermarsh)
[charliermarsh](/charliermarsh)
mentioned this pull request
[Aug 28, 2026](#ref-pullrequest-5273732810)

[Store cached wheel permissions in archive manifests
#21334](/astral-sh/uv/pull/21334)

Draft

[![@zsol](https://avatars.githubusercontent.com/u/66740?s=40&u=ecd19aa2e680ad56fb921430e8edab1dcc7c7285&v=4)](/zsol)

[zsol](/zsol)
self-requested a review
[August 28, 2026 09:53](#event-30157903937)

This was referenced Aug 28, 2026

[Prefetch wheel central directories for streamed file publication
#21338](/astral-sh/uv/pull/21338)

Draft

[Pipeline wheel file publication with executable deferral
#21339](/astral-sh/uv/pull/21339)

Draft

[![@charliemarsh-oai](https://avatars.githubusercontent.com/u/282065134?s=40&u=bdb0ab25cf17a57513b5e77a5db213b15a60cc6a&v=4)](/charliemarsh-oai)
[charliemarsh-oai](/charliemarsh-oai)
mentioned this pull request
[Aug 28, 2026](#ref-pullrequest-5279860936)

[Reuse the hashing buffer across streamed wheel files
#21340](/astral-sh/uv/pull/21340)

Merged

[charliermarsh](/charliermarsh)
added a commit
that referenced
this pull request
[Aug 28, 2026](#ref-commit-dd85179)

[![@charliemarsh-oai](https://avatars.githubusercontent.com/u/282065134?s=40&u=bdb0ab25cf17a57513b5e77a5db213b15a60cc6a&v=4)](/charliemarsh-oai) [![@charliermarsh](https://avatars.githubusercontent.com/u/1309177?s=40&u=6328c998d93a48eba87c6b039783b8a7644c62c3&v=4)](/charliermarsh)

`Reuse the hashing buffer across streamed wheel files (#21340)`

…

`dd85179`

```
## Summary

When content hashing is enabled, we currently allocate and zero a new 64
KiB buffer for every file we copy and hash during streaming extraction.
This PR reuses one buffer across the wheel instead. For the PyTorch
wheel used in the benchmarks, that reduces buffer allocations for
hashing from 11,120 to one, while keeping the buffer size at 64 KiB per
active wheel.

The following measurements compare #21327 at
`a188b8e833aef3c3b4b60a32ed9fafe6ac74186a` with this optimization
applied on top, before moving the change onto `main`. They are not
measurements against `main`. The Linux benchmarks alternate base and
candidate, using pinned wheels served over local HTTP with
content-addressed caching enabled:

| Cold install | #21327 | #21327 + buffer reuse | Change |
| --- | ---: | ---: | ---: |
| AnyIO | 110 ms | 107 ms | -2.6% |
| SymPy | 845 ms | 775 ms | -8.3% |
| NumPy | 627 ms | 567 ms | -9.5% |
| PyTorch CPU | 6.50 s | 5.99 s | -7.8% |
| 14-package environment, concurrency 4 | 6.95 s | 6.47 s | -7.0% |

The individual results above use 16 paired rounds; the full environment
uses 12. AnyIO, SymPy, and NumPy were repeated after an initial 20-pair
run: the initial AnyIO timings were noisy, while the initial SymPy and
NumPy improvements were 7.8% and 6.9%. All original samples were
retained. Cached installs and local-wheel controls showed no consistent
change. Across the initial runs, repeats, and controls, we measured 672
installs, excluding warmups and cache priming.

Co-authored-by: Charlie Marsh <charlie.r.marsh@gmail.com>
```

[![@charliermarsh](https://avatars.githubusercontent.com/u/1309177?s=40&u=6328c998d93a48eba87c6b039783b8a7644c62c3&v=4)](/charliermarsh)

[charliermarsh](/charliermarsh)
[force-pushed](/astral-sh/uv/compare/a188b8e833aef3c3b4b60a32ed9fafe6ac74186a..694af801fd59e78e1654254899f1db68a15c1f9d)
the

charlie/dirhash-all-files
branch
from
[`a188b8e`](/astral-sh/uv/commit/a188b8e833aef3c3b4b60a32ed9fafe6ac74186a) to
[`694af80`](/astral-sh/uv/commit/694af801fd59e78e1654254899f1db68a15c1f9d)  [Compare](/astral-sh/uv/compare/a188b8e833aef3c3b4b60a32ed9fafe6ac74186a..694af801fd59e78e1654254899f1db68a15c1f9d)
[August 28, 2026 16:56](#event-30177339582)

[![@charliermarsh](https://avatars.githubusercontent.com/u/1309177?s=40&u=6328c998d93a48eba87c6b039783b8a7644c62c3&v=4)](/charliermarsh)

[charliermarsh](/charliermarsh)
[had a problem deploying](https://github.com/astral-sh/uv/actions/runs/33192356891/job/98920916076)
to
automations
[August 28, 2026 16:57](#event-30177366419) — with ![](https://avatars.githubusercontent.com/in/15368?s=40&u=167a342ed94d2a713daf64a8b476ead2cebe1852&v=4)
[GitHub Actions](https://github.com/apps/github-actions)

Error

[![@charliermarsh](https://avatars.githubusercontent.com/u/1309177?s=80&u=6328c998d93a48eba87c6b039783b8a7644c62c3&v=4)](/charliermarsh)

### **[charliermarsh](/charliermarsh)** commented [Aug 28, 2026](#issuecomment-5455416974)

Copy link
 

Copy Markdown

Member

Author

|  |
| --- |
| Okay, I experimented with a bunch of alternatives to try and make this more performant:   * Store all files as non-executable, and then apply executable flags at install-time ([Store cached wheel permissions in archive manifests #21334](https://github.com/astral-sh/uv/pull/21334), [Pipeline file cache publication for streamed wheels #21333](https://github.com/astral-sh/uv/pull/21333)). This would allow us to hardlink into `files-v0` while we unzip. Unfortunately, it also means we have to *copy* every executable that we want to install, since hardlinks share a mode. Ultimately, this was a bit tradeoff -- it was slower! * Pre-fetching the central directory so that we can determine whether a given file is executable at extraction-time. (As-is, we only get the central directory *after* we've unzipped, so we don't know if a file is executable until *after* it's been extracted.) This also turned out to be slower because we have additional overhead from making more HTTP requests.   I also considered something like "guess whether a file is executable" during extraction (and then, if we're wrong, copy it and change the mode after unzipping). I guess this could end up being more performant, but I wasn't very happy with the heuristics.  Ultimately, I think what we have here is good. |

[![@charliermarsh](https://avatars.githubusercontent.com/u/1309177?s=80&u=6328c998d93a48eba87c6b039783b8a7644c62c3&v=4)](/charliermarsh)

### **[charliermarsh](/charliermarsh)** commented [Aug 28, 2026](#issuecomment-5455451126)

Copy link
 

Copy Markdown

Member

Author

|  |
| --- |
| If you bundle in [#21340](https://github.com/astral-sh/uv/pull/21340), I believe this is also *faster* than before (i.e., gains from [#21340](https://github.com/astral-sh/uv/pull/21340) outweigh the extra cost in this PR). |

[![@charliermarsh](https://avatars.githubusercontent.com/u/1309177?s=40&u=6328c998d93a48eba87c6b039783b8a7644c62c3&v=4)](/charliermarsh)

[charliermarsh](/charliermarsh)
[temporarily deployed](https://github.com/astral-sh/uv/actions/runs/33193464134/job/98924777184)
to
automations
[August 28, 2026 17:11](#event-30178001758) — with ![](https://avatars.githubusercontent.com/in/15368?s=40&u=167a342ed94d2a713daf64a8b476ead2cebe1852&v=4)
[GitHub Actions](https://github.com/apps/github-actions)

Inactive

[![@charliermarsh](https://avatars.githubusercontent.com/u/1309177?s=40&u=6328c998d93a48eba87c6b039783b8a7644c62c3&v=4)](/charliermarsh)

[charliermarsh](/charliermarsh)
[temporarily deployed](https://github.com/astral-sh/uv/actions/runs/33194774256/job/98929233620)
to
automations
[August 28, 2026 17:28](#event-30178764890) — with ![](https://avatars.githubusercontent.com/in/15368?s=40&u=167a342ed94d2a713daf64a8b476ead2cebe1852&v=4)
[GitHub Actions](https://github.com/apps/github-actions)

Inactive

[charliermarsh](/charliermarsh)
and others
added 22 commits
[August 31, 2026 08:56](#commits-pushed-1ba014d)

[![@charliermarsh](https://avatars.githubusercontent.com/u/1309177?s=40&v=4)](/charliermarsh)

`Narrow archive manifest and hardlink helper visibility`

`1ba014d`

[![@charliermarsh](https://avatars.githubusercontent.com/u/1309177?s=40&v=4)](/charliermarsh)

`Simplify binary archive object identities`

`1b4b1d8`

[![@charliermarsh](https://avatars.githubusercontent.com/u/1309177?s=40&v=4)](/charliermarsh)

`Finalize binary archive manifests before publishing`

`a89ce5e`

[![@charliermarsh](https://avatars.githubusercontent.com/u/1309177?s=40&v=4)](/charliermarsh)

`Simplify and document binary archive deduplication`

`4e7d0dc`

[![@charliermarsh](https://avatars.githubusercontent.com/u/1309177?s=40&v=4)](/charliermarsh)

`Gate binary archive deduplication behind preview`

`5c29fbc`

[![@charliermarsh](https://avatars.githubusercontent.com/u/1309177?s=40&v=4)](/charliermarsh)

`Simplify archive extraction and manifest validation`

`7b483f1`

[![@charliermarsh](https://avatars.githubusercontent.com/u/1309177?s=40&v=4)](/charliermarsh)

`Share executable and large files with complete archives`

`412eb87`

[![@charliermarsh](https://avatars.githubusercontent.com/u/1309177?s=40&v=4)](/charliermarsh)

`Expose the archive file size cutoff environment variable`

`fc6e334`

[![@charliermarsh](https://avatars.githubusercontent.com/u/1309177?s=40&v=4)](/charliermarsh)

`Share executables and native libraries regardless of size`

`aed81af`

[![@charliermarsh](https://avatars.githubusercontent.com/u/1309177?s=40&v=4)](/charliermarsh)

`Rename shared file and manifest cache buckets`

`7e944ef`

[![@charliermarsh](https://avatars.githubusercontent.com/u/1309177?s=40&v=4)](/charliermarsh)

`Separate file-cache deduplication from installation`

`65f6c62`

[![@charliermarsh](https://avatars.githubusercontent.com/u/1309177?s=40&v=4)](/charliermarsh)

`Keep cache-only callers and generated schema consistent`

`d0682a4`

[![@charliermarsh](https://avatars.githubusercontent.com/u/1309177?s=40&v=4)](/charliermarsh)

`Model hashed and unhashed extraction explicitly`

`b6cdda1`

[![@charliermarsh](https://avatars.githubusercontent.com/u/1309177?s=40&v=4)](/charliermarsh)

`Bundle hashed wheel metadata and trim helper tests`

`8acb8c8`

[![@charliermarsh](https://avatars.githubusercontent.com/u/1309177?s=40&v=4)](/charliermarsh)

`Remove archive publication comment`

`7c10407`

[![@charliermarsh](https://avatars.githubusercontent.com/u/1309177?s=40&v=4)](/charliermarsh)

`Avoid duplicate extracted wheel file records`

`390db4e`

[![@charliermarsh](https://avatars.githubusercontent.com/u/1309177?s=40&v=4)](/charliermarsh)

`Deduplicate all files in the wheel cache`

`7818a02`

[![@charliemarsh-oai](https://avatars.githubusercontent.com/u/282065134?s=40&v=4)](/charliemarsh-oai) [![@charliermarsh](https://avatars.githubusercontent.com/u/1309177?s=40&v=4)](/charliermarsh)

`Optimize wheel file cache publication`

`ef2a9b7`

[![@charliemarsh-oai](https://avatars.githubusercontent.com/u/282065134?s=40&v=4)](/charliemarsh-oai) [![@charliermarsh](https://avatars.githubusercontent.com/u/1309177?s=40&v=4)](/charliermarsh)

`Exclude RECORD from wheel file deduplication`

`d2e340c`

[![@charliermarsh](https://avatars.githubusercontent.com/u/1309177?s=40&v=4)](/charliermarsh)

`Include executable status in file cache hashes`

`b37fdee`

[![@charliermarsh](https://avatars.githubusercontent.com/u/1309177?s=40&v=4)](/charliermarsh)

`Prune orphaned file objects when cleaning an unreferenced cache`

`af30c8c`

[![@charliermarsh](https://avatars.githubusercontent.com/u/1309177?s=40&v=4)](/charliermarsh)

`Prune file objects once per cache clean`

`87bd56f`

[![@charliermarsh](https://avatars.githubusercontent.com/u/1309177?s=40&u=6328c998d93a48eba87c6b039783b8a7644c62c3&v=4)](/charliermarsh)

[charliermarsh](/charliermarsh)
[force-pushed](/astral-sh/uv/compare/73c621b5ebdb43d8d79d780f3f2c6470ea2260a1..87bd56fc8f9742b064878ce3b1c13f51faf84eab)
the

charlie/dirhash-all-files
branch
from
[`73c621b`](/astral-sh/uv/commit/73c621b5ebdb43d8d79d780f3f2c6470ea2260a1) to
[`87bd56f`](/astral-sh/uv/commit/87bd56fc8f9742b064878ce3b1c13f51faf84eab)  [Compare](/astral-sh/uv/compare/73c621b5ebdb43d8d79d780f3f2c6470ea2260a1..87bd56fc8f9742b064878ce3b1c13f51faf84eab)
[August 31, 2026 12:59](#event-30279753833)

[![@charliermarsh](https://avatars.githubusercontent.com/u/1309177?s=40&u=6328c998d93a48eba87c6b039783b8a7644c62c3&v=4)](/charliermarsh)

[charliermarsh](/charliermarsh)
[temporarily deployed](https://github.com/astral-sh/uv/actions/runs/33394555764/job/99496026011)
to
automations
[August 31, 2026 13:00](#event-30279787033) — with ![](https://avatars.githubusercontent.com/in/15368?s=40&u=167a342ed94d2a713daf64a8b476ead2cebe1852&v=4)
[GitHub Actions](https://github.com/apps/github-actions)

Inactive

[![@charliermarsh](https://avatars.githubusercontent.com/u/1309177?s=40&v=4)](/charliermarsh)

`Address wheel cache review feedback`

`d12d2ad`

[![@charliermarsh](https://avatars.githubusercontent.com/u/1309177?s=40&u=6328c998d93a48eba87c6b039783b8a7644c62c3&v=4)](/charliermarsh)

[charliermarsh](/charliermarsh)
[temporarily deployed](https://github.com/astral-sh/uv/actions/runs/33396067873/job/99501013487)
to
automations
[August 31, 2026 13:17](#event-30280789749) — with ![](https://avatars.githubusercontent.com/in/15368?s=40&u=167a342ed94d2a713daf64a8b476ead2cebe1852&v=4)
[GitHub Actions](https://github.com/apps/github-actions)

Inactive

[![@charliermarsh](https://avatars.githubusercontent.com/u/1309177?s=40&u=6328c998d93a48eba87c6b039783b8a7644c62c3&v=4)](/charliermarsh)
[charliermarsh](/charliermarsh)
mentioned this pull request
[Aug 31, 2026](#ref-pullrequest-5300654742)

[Reuse cached small files during wheel extraction
#21375](/astral-sh/uv/pull/21375)

Draft

Hide details
View details

[![@charliermarsh](https://avatars.githubusercontent.com/u/1309177?s=40&u=6328c998d93a48eba87c6b039783b8a7644c62c3&v=4)](/charliermarsh)

[charliermarsh](/charliermarsh)
merged commit [`15bf04f`](/astral-sh/uv/commit/15bf04f7d69fc84aa194d8ea55721dc15addfb6f)
into

main
[Aug 31, 2026](https://github.com/astral-sh/uv/pull/21327#event-30281433190)

82 checks passed

### Uh oh!

There was an error while loading. Please reload this page.

[![@charliermarsh](https://avatars.githubusercontent.com/u/1309177?s=40&u=6328c998d93a48eba87c6b039783b8a7644c62c3&v=4)](/charliermarsh)

[charliermarsh](/charliermarsh)
deleted the

charlie/dirhash-all-files
 
branch
[August 31, 2026 13:28](#event-30281439674)

[charliermarsh](/charliermarsh)
added a commit
that referenced
this pull request
[Aug 31, 2026](#ref-commit-2577582)

[![@charliermarsh](https://avatars.githubusercontent.com/u/1309177?s=40&u=6328c998d93a48eba87c6b039783b8a7644c62c3&v=4)](/charliermarsh) [![@zanieb](https://avatars.githubusercontent.com/u/2586601?s=40&u=e5c86f7ff3b859e7e183187ac2b17fd6ee32b3ab&v=4)](/zanieb)

`Read file-cache link counts in bulk on macOS (#21344)`

…

`2577582`

```
## Summary

Follow-up to #21327.

Cache cleanup currently reads the hardlink count of every `files-v0`
object separately. On macOS, we can request names, file types, and link
counts in batches with `getattrlistbulk`, allocating paths only for
files with a single link.

Use this fast path for flat cache shards. We keep the existing walk on
other platforms, when bulk reads or required attributes aren't
available, and for nested directories. We don't follow symlinks, and
file removal still uses the existing storage accounting.

On macOS, with 87,129 distinct empty file objects across 256 shards and
two hardlinks per object, median full-command times across eight paired
warm-cache runs were:

| Command                        | Before |  After |
| ------------------------------ | -----: | -----: |
| `uv cache clean <package>`     | 386 ms | 105 ms |
| `uv cache clean <10 packages>` | 389 ms | 104 ms |
| `uv cache prune`               | 386 ms | 101 ms |

These runs retain every object, so they measure scan cost rather than
deletion throughput. The scan is still single-threaded.

---------

Co-authored-by: Zanie Blue <contact@zanie.dev>
```

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters]({{ revealButtonHref }})

[Sign up for free](/join?source=comment-repo)
**to join this conversation on GitHub**.
Already have an account?
[Sign in to comment](/login?return_to=https%3A%2F%2Fgithub.com%2Fastral-sh%2Fuv%2Fpull%2F21327)

### Labels

[enhancement](/astral-sh/uv/issues?q=state%3Aopen%20label%3Aenhancement)
New feature or improvement to existing functionality
[preview](/astral-sh/uv/issues?q=state%3Aopen%20label%3Apreview)
Experimental behavior

### 4 participants

[![@charliermarsh](https://avatars.githubusercontent.com/u/1309177?s=52&v=4)](/charliermarsh) [![@charliemarsh-oai](https://avatars.githubusercontent.com/u/282065134?s=52&v=4)](/charliemarsh-oai) [![@akx](https://avatars.githubusercontent.com/u/58669?s=52&v=4)](/akx) [![@zanieb](https://avatars.githubusercontent.com/u/2586601?s=52&v=4)](/zanieb)

Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.
