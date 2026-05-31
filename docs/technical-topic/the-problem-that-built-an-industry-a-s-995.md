---
id: 995
url: https://ajitem.com/blog/iron-core-part-1-the-problem-that-built-an-industry/
title: The Problem That Built an Industry // a.s
domain: ajitem.com
source_date: '2026-04-12'
tags:
- distributed-systems
- database
- academic-paper
summary: Airline reservation systems trace their origins to the 1960s when American
  Airlines partnered with IBM to create SABRE, a system designed to replace manual
  index card booking methods that took up to 90 minutes per reservation. The infrastructure
  that powers modern flight bookings today is built on decades-old data models, protocols,
  and transaction semantics—particularly IBM's Transaction Processing Facility (TPF)—which
  persist because they excel at processing massive volumes of small transactions with
  sub-millisecond response times that modern systems still struggle to match. Despite
  replacing hardware and adding cloud-native layers, airlines maintain these 60-year-old
  cores because they reliably handle thousands of transactions per second and continue
  to fly the 4.5 billion people who travel annually.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# The Problem That Built an Industry // a.s

SeriesPart 1 of 6 // Iron Core

![](/optimized/images/blog/iron-core-part-1-the-problem-that-built-an-industry-hero.webp)

The Problem That Built an Industry
==================================

*Part 1 of 6 in the Iron Core series: the 60-year-old infrastructure that flies 4.5 billion people a year.*

---

In December 2025, someone at Technogise opened MakeMyTrip's corporate platform, typed in a destination, and booked me two flights to London. The whole thing took under a minute. A confirmation email landed in my inbox. Six-character booking references appeared: **DDTCIV** and **DHB4AL**.

I was going to speak at ContainerDays 2026. A conference about containers, orchestration, and cloud-native infrastructure: the kind of modern, ephemeral, stateless systems I spend my working life thinking about.

The irony only hit me on the flight over.

The infrastructure that booked those flights traces its design to the 1960s. It still runs on lineages that predate Unix and speaks command languages built for teletypes. The implementations, hardware, and surrounding software have been replaced and upgraded many times. What persists is the data model, the protocols, and the transaction semantics. None of that happened in a single rewrite: it accumulated while the system kept flying, and at peak it still handles on the order of 10,000 transactions per second.

I build distributed systems. I thought I understood complex infrastructure. Then I looked at my own boarding pass and pulled the thread.

This is a six-part series about what I found.

---

The World Before SABRE
----------------------

To understand why this infrastructure exists, you need to understand the problem it was built to solve.

By the mid-1950s, American Airlines was managing reservations on index cards. A booking required a phone call to an agent, who would search physical card racks across multiple city offices, confirm availability verbally, and call the passenger back. A transatlantic reservation could take 90 minutes to confirm. The airline was processing roughly 85,000 reservation requests a day across 50-plus cities. The system was collapsing.

The origin story of what would become the GDS (Global Distribution System) is well-documented, though it has acquired a degree of mythology in retelling. In 1953, C.R. Smith, president of American Airlines, was seated next to R. Blair Smith, an IBM salesman, on a cross-country flight. IBM and American Airlines entered a formal development partnership in 1959, six years later.

The result was **SABRE** (Semi-Automated Business Research Environment). It went live in 1964: five years after the 1959 contract, and eleven years after the 1953 conversation.

That is the scale of lead time for infrastructure of this kind. The same year SABRE launched, IBM announced the System/360. Three years before the first ATM. Five years before the moon landing. Fifteen years before VisiCalc.

Within a decade, every major airline followed suit:

| GDS | Founded | Original Owner | Tech Foundation |
| --- | --- | --- | --- |
| SABRE | 1964 | American Airlines + IBM | IBM ACP / TPF |
| Apollo | 1971 | United Airlines | IBM TPF |
| Galileo | 1987 | United + BA + KLM + Swissair | IBM TPF |
| Worldspan | 1990 | Delta + Northwest + TWA | IBM TPF |
| Amadeus | 1987 | Air France + Lufthansa + Iberia + SAS | Bull mainframe, then Unix |

Four of the five North American-originated stacks in that table were built on IBM TPF (or its ACP lineage). Amadeus is the exception: Bull, then Unix. They did not all land on the same executable runtime, but they had to solve the same problem shape: huge volume of small, latency-bounded transactions over shared inventory and settlement rules, in an industry where IATA practice and interlining economics made divergence expensive.

That convergence was not an accident of engineering taste. IATA's messaging standards, interlining settlement rules, and the economic penalties of non-interoperable systems pushed carriers toward compatible shapes. When you see similar stacks in one industry, regulatory standards and switching costs are usually doing more work than independent discovery.

---

TPF: The OS That Refuses to Die
-------------------------------

**Transaction Processing Facility** (TPF) is an IBM mainframe operating system descended from ACP, American Airlines' original Airline Control Program. It was designed for one purpose: processing enormous volumes of simple transactions with sub-millisecond response times.

It is not Unix. It does not share Unix's lineage, its philosophy, or its abstractions. It predates Unix by a decade.

Understanding TPF requires setting aside almost everything you know about modern operating systems:

| Property | TPF | Modern OS |
| --- | --- | --- |
| Process model | No processes. No threads. Short-lived "programs" that execute and exit. | Processes, threads, coroutines |
| Memory model | Fixed memory "cells" per transaction. No heap. No dynamic allocation. | Virtual memory, heap, GC |
| I/O model | Extremely fast synchronous I/O to DASD (Direct Access Storage) | Async I/O, block storage, NVMe |
| Scheduling | Preemptive, priority-based, microsecond granularity | Typically millisecond granularity |
| Failure model | Transaction-level rollback. The system does not crash; the transaction does. | Depends on application |
| Primary language | Assembler. C was added later. | Everything |

TPF is not really an OS in the way you think of one. It is closer to what we would now call a **transaction runtime**: a system purpose-built to receive a unit of work, execute a short program against it, commit state changes, and immediately move on. The application-facing transaction path is deliberately minimal: no long-lived per-client worker holding connection state in memory between units of work, and no Unix-style thread-per-request model for that path. System-level scheduling, I/O, and housekeeping still exist; this is not a claim that the machine does nothing between transactions.

This design was made for one workload. It is exceptionally good at that workload.

Modern TPF-based systems handle around 10,000 transactions per second under normal conditions. During a fare sale, when millions of customers simultaneously discover that flights are cheap, that number can reach 50,000 TPS. End-to-end message round-trip: roughly 100 milliseconds. Those numbers reflect a tight transaction model and sixty years of operational hardening.

In the 1990s, when every other industry was migrating off mainframes to Unix, airlines looked at the performance numbers and stayed put. The replacements could not match the throughput for this specific workload. Many still cannot. The IBM Z-series mainframes running z/TPF today are not running it out of nostalgia.

Sabre (the company) today also sells cloud-native layers and API-first products around the same domain. The industry runs old cores and new surfaces in parallel more often than headlines suggest.

---

Where My Flights Fit Into This
------------------------------

When Technogise booked my ContainerDays travel through myBiz, the booking touched a specific layer of this ecosystem. MakeMyTrip uses **Amadeus** as its GDS: the system born from a 1987 partnership between Air France, Lufthansa, Iberia, and SAS, and now the dominant GDS across Europe, India, and much of Asia-Pacific.

Amadeus is not running on the original 1987 Bull mainframe. It migrated to Unix in the 1990s and has since moved progressively toward a more modern architecture. But the data model, the protocol, and the command language that agents use (cryptic mode) remain continuous with the original 1960s design. The format of my PNR, the structure of my e-ticket, the way the fare is calculated: all of it follows conventions established before I was born.

My outbound was entirely Air India (**DDTCIV**, NAG→DEL→LHR). Air India runs on **Amadeus Altéa**, a modern PSS (Passenger Service System) built on top of the Amadeus infrastructure. They migrated to it in 2023, replacing a legacy SITA system. That migration is one of the largest airline PSS migrations in Asian aviation history, and its cost and complexity are worth understanding on their own terms. I come back to it in Part 4.

The return (**DHB4AL**, MAN→LHR→DEL→NAG) mixed British Airways (also on Amadeus Altéa) and Air India. Because both carriers on that routing sit on the same Amadeus stack, a single PNR could span both airlines without a hand-built bridge between unrelated PSSs. That consistency is what made the booking work, and what made re-accommodation possible when things went wrong.

---

IndiGo and the Budget Carrier Divergence
----------------------------------------

IndiGo (the largest airline in India by market share) does not use Amadeus. It uses **Navitaire**, a PSS built specifically for low-cost carriers, now owned by Amadeus but operated as a separate product. Navitaire's NewSkies platform is purpose-built for high-volume, low-margin, point-to-point flying: no interline, no complex fare construction, no legacy baggage.

This is a deliberate architectural choice. Navitaire is cheaper to operate, faster to configure, and optimised for the IndiGo model: high frequency, fixed pricing, minimal complexity. The trade-off is reduced interoperability. IndiGo distributes inventory into Amadeus for travel agent bookings (you can see 6E flights in a cryptic availability display), but the ticketing and check-in systems are entirely Navitaire.

The split matters when something goes wrong. An IndiGo delay affecting an Air India connection does not trigger automatic re-accommodation between systems. A human has to intervene.

| Airline | PSS | GDS Distribution |
| --- | --- | --- |
| Air India (AI) | Amadeus Altéa | Amadeus (primary) |
| IndiGo (6E) | Navitaire NewSkies | Amadeus / Sabre (via distribution layer) |
| Vistara (absorbed into AI) | Amadeus Altéa | Amadeus |
| Air India Express | Navitaire | Amadeus / Sabre |

---

What a 30-Second Booking Actually Triggers
------------------------------------------

When myBiz confirmed my booking in December 2025, the following sequence fired:

Each arrow is a system boundary. Each boundary has its own protocol, its own failure mode, and its own eventual consistency characteristics. The 30-second booking conceals a chain of synchronous and asynchronous calls across systems built in different decades by different companies in different countries.

The PNR at the end of that chain (six characters, DDTCIV) is the thread that holds it all together.

In the next part, I will decode exactly what those six characters are, what they contain, and why the fare calculation line on my e-ticket is one of the most information-dense strings in commercial aviation.

---

Takeaways
---------

**A narrow, well-tested design maintained by people who understand it deeply can be the hardest thing to displace for the workload it was built for.** TPF is not modern. It would fail most architectural reviews a contemporary engineering team would apply. What it has is a transaction model built for inventory and settlement, decades of operational tuning, and peak loads on the order of 50,000 TPS with end-to-end latency around 100 milliseconds. The numbers are a consequence of fit between design and workload, not a general property of mainframes.

**Similar stacks in one industry usually reflect shared constraints, not independent convergence.** The GDS world is not a clean story of unrelated companies discovering the same solution. Regulated-era economics, interlining, IATA messaging practice, and network effects pushed carriers toward interoperable shapes. Several majors bet on TPF for the core transaction engine; Amadeus bet elsewhere yet still speaks the same lineage of PNRs, fares, and cryptic at the edge. Asking what standards and settlement rules made divergence expensive is usually more productive than asking why engineers made similar choices.

**PSS migrations are years-long undertakings with visible scar tissue.** Air India's move to Amadeus Altéa in 2023 involved decades of booking history, interline agreements, loyalty programme integrations, and airport systems dependencies. The operational impact lasted months past go-live. Scale and data age are the variables that make airline migrations different from typical enterprise software replacements.

---

*Next: Part 2: Six Characters. What DDTCIV actually is, what it contains, and why it is less unique than you think.*

*The Iron Core is a six-part series by Ajitem Sahasrabuddhe. Ajitem is a software engineer at [Technogise](https://technogise.com) and spoke at ContainerDays 2026 in London.*

Series contents
---------------

01

The Problem That Built an Industry

Current

[02

Six Characters

Read](/blog/iron-core-part-2-six-characters/)[03

The Command Line That Never Died

Read](/blog/iron-core-part-3-the-command-line-that-never-died/)[04

From GDS to Gate

Read](/blog/iron-core-part-4-from-gds-to-gate/)[05

Bird Strike, Terminal 2

Read](/blog/iron-core-part-5-bird-strike-terminal-2/)[06

The Revolution That's Taking Forever

Read](/blog/iron-core-part-6-the-revolution-thats-taking-forever/)
