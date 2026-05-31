---
id: 975
url: https://github.com/yannick-cw/korb
title: 'GitHub - yannick-cw/korb: REWE delivery CLI · GitHub'
domain: github.com
source_date: '2026-04-01'
tags:
- github-repo
- cli-tool
- haskell
- ai
summary: Korb is a CLI tool written in Haskell that enables programmatic interaction
  with REWE's grocery delivery APIs to create and order shopping baskets for pickup
  at local markets. The tool outputs all results in JSON format and is designed to
  be used by AI agents to automate grocery shopping workflows, supporting features
  like product search, basket management, timeslot selection, and order history tracking.
  Installation is straightforward via pre-built binaries for macOS and Linux, and
  the project includes formal verification of its suggestion engine using Lean 4 proofs.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# GitHub - yannick-cw/korb: REWE delivery CLI · GitHub

// Update: Rewe not yet ready for agentic commerce
--------------------------------------------------

Rewe seems to not like independent agentic commerce and is actively blocking this CLI, fair choice, less shopping from me, but understandable at the same time. Unfortunately this means the CLI might or might not work depending on their cloudflare tls fingerprinting rules.

// korb
-------

The `korb` CLI allows using the REWE APIs programmatically to create baskets and order them for pickup to your local REWE market.

The CLI is handwritten in Haskell, but designed to be a CLI mostly used by agents to organise your REWE shopping on your behalf. All output is JSON.

korb\_demo.mp4

[
](https://private-user-images.githubusercontent.com/2485755/571005616-308041f4-4b1f-4db4-9040-0e157247efea.mp4?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3ODAyNDcyMDYsIm5iZiI6MTc4MDI0NjkwNiwicGF0aCI6Ii8yNDg1NzU1LzU3MTAwNTYxNi0zMDgwNDFmNC00YjFmLTRkYjQtOTA0MC0wZTE1NzI0N2VmZWEubXA0P1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQVZDT0RZTFNBNTNQUUs0WkElMkYyMDI2MDUzMSUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyNjA1MzFUMTcwMTQ2WiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9ZjgwMzYxMmYzZTBhYzQ3ZWZjOTZmZjQ0N2YwNzhmNjUyNjAwZmVmY2Q4OWFkNWNkMDk2ZWRhZGQyYzkwMDNlNSZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QmcmVzcG9uc2UtY29udGVudC10eXBlPXZpZGVvJTJGbXA0In0.o8Hg51asbr7mitFa6gHKLrOX6PslJJqLTl-MwQkPmd0)

// agentic workflow with UI
---------------------------

[![agentic_order](https://private-user-images.githubusercontent.com/2485755/573826327-ff0d7b91-2572-4ba0-9609-0dac313306b2.gif?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3ODAyNDcyMDYsIm5iZiI6MTc4MDI0NjkwNiwicGF0aCI6Ii8yNDg1NzU1LzU3MzgyNjMyNy1mZjBkN2I5MS0yNTcyLTRiYTAtOTYwOS0wZGFjMzEzMzA2YjIuZ2lmP1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQVZDT0RZTFNBNTNQUUs0WkElMkYyMDI2MDUzMSUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyNjA1MzFUMTcwMTQ2WiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9MTNmNWE5YmJmMGQ4OTUzOWRjNjQwMGYzYmE5YjA2NTc2YWFkNTM0NzExZWU4MmZhOGJjZmNhMmNiZmFjMDI1YSZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QmcmVzcG9uc2UtY29udGVudC10eXBlPWltYWdlJTJGZ2lmIn0.7lKKZ1yktElXdray4-aKhcd1v7rcbf02oOprUvjqN_M)](https://private-user-images.githubusercontent.com/2485755/573826327-ff0d7b91-2572-4ba0-9609-0dac313306b2.gif?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3ODAyNDcyMDYsIm5iZiI6MTc4MDI0NjkwNiwicGF0aCI6Ii8yNDg1NzU1LzU3MzgyNjMyNy1mZjBkN2I5MS0yNTcyLTRiYTAtOTYwOS0wZGFjMzEzMzA2YjIuZ2lmP1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQVZDT0RZTFNBNTNQUUs0WkElMkYyMDI2MDUzMSUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyNjA1MzFUMTcwMTQ2WiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9MTNmNWE5YmJmMGQ4OTUzOWRjNjQwMGYzYmE5YjA2NTc2YWFkNTM0NzExZWU4MmZhOGJjZmNhMmNiZmFjMDI1YSZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QmcmVzcG9uc2UtY29udGVudC10eXBlPWltYWdlJTJGZ2lmIn0.7lKKZ1yktElXdray4-aKhcd1v7rcbf02oOprUvjqN_M)

// My e2e flow
--------------

My current E2E flow (I use claude to run korb) is as follows:

1. **Add grocery when I think of it** A Siri shortcut appends items to a shared markdown file. I say *"Add oat milk to the shopping list"* in the kitchen and it's on the list.
2. **Weekly Order** Tell the agent "use korb to buy groceries, I need X,Y,Z". It begins from a default template (my usual items and quantities, created with `korb orders history`) and checks the shopping list file and my input for anything extra.
3. **Adjust template suggestion** I tell the agent what to skip, change, or add. It searches products via `korb search` / `korb favorites search` and adds them with `korb basket add`.
4. **Review & confirm** The agent prints the full basket and a selected timeslot. After I confirm, it runs `korb checkout order`.
5. **Clean shopping list** Ordered items get ticked off in the shopping list.

In the directory that store the shopping list file I also have a claude.md explaining this process.
The **magic** is the generated template of what I always order. Just tell an agent to use `korb orders history` to identify commonly ordered items.

// Installation
---------------

**DON'T: as of right now krob does not work - rewe does not want it to work**

### Dependencies

Currently it needs `curl` installed.

### Binary (recommended)

Download the latest release from [GitHub Releases](https://github.com/yannick-cw/korb/releases):

```
# macOS (Apple Silicon)
curl -L https://github.com/yannick-cw/korb/releases/latest/download/korb-aarch64-macos -o korb

# macOS (Intel)
curl -L https://github.com/yannick-cw/korb/releases/latest/download/korb-x86_64-macos -o korb

# Linux (x86_64)
curl -L https://github.com/yannick-cw/korb/releases/latest/download/korb-x86_64-linux -o korb
```

Then:

```
chmod +x korb
mv korb /usr/local/bin/   # or sudo mv on Linux
```

### From source

Requires GHC 9.12+ and Cabal. You also need the REWE mTLS client certificates.

```
git clone https://github.com/yannick-cw/korb.git
cd korb

# Extract mTLS certificates from the REWE app
# See: https://github.com/ByteSizedMarius/rewerse-engineering/tree/main/docs
# Place them at:
#   certs/mobile-clients-api.rewe.de/private.pem
#   certs/mobile-clients-api.rewe.de/private.key

cabal install --install-method=copy
```

// Getting started
------------------

```
# 1. Authenticate with your REWE account (one-time, use Chrome to get the link, firefox does not work for this)
korb login --pretty

# 2. Find and set your pickup store - stored locally, needs to be done just once
korb store search 80336 # returns market identifier for zip code
korb store set 420240 80336

# 3. Search for products by name or EAN barcode
korb search "milch" --pretty
korb search "milch" --organic --pretty
korb search "4305615100005" --pretty  # search by EAN barcode
# Or browse your favorites
korb favorites
korb favorites search "avo"

# 4. Add items to basket
korb basket add 8-6AJQ3RLX-bd7c2a1e-f1c1-3464-8250-900b12c90f70

# 5. Check your basket
korb basket --pretty

# 6. Pick a timeslot and checkout
korb timeslots # lists available timeslots for pickup
korb checkout create <TIMESLOT_ID>  # create checkout - not ordered yet
korb checkout order # order it with selected timeslot and payment in market

# 7. Cancel an order if needed
korb orders
korb orders delete <ORDER_ID>
```

// Usage
--------

```
Usage: korb COMMAND [-p|--pretty] [-v|--version]
  REWE Pickup CLI

Available options:
  -p,--pretty              Pretty JSON output
  -h,--help                Show this help text
  -v,--version             Show version

Commands:

  korb store                       Show currently selected store
  korb store search <ZIP>          Find pickup stores near ZIP code
  korb store set <ID> <ZIP>        Set active store by market ID and ZIP

  korb search <QUERY|EAN>          Search products by name or EAN barcode (use * to browse all)
  korb search <Q> --organic        Filter by attribute (--organic, --regional, --vegan, --vegetarian)
  korb search <Q> --category <SLUG> Filter by category slug (repeatable, from korb categories)

  korb favorites                   Show all favorite products across all lists
  korb favorites search <QUERY>    Filter favorites by name (case-insensitive, substring match)
  korb favorites add <LID> <PID>   Add product to default favorites list (listing ID + product ID)
  korb favorites delete <ITEM_ID>  Remove item from default favorites list (item ID from favorites)

  korb basket                      Show current basket with items, totals, and free pickup status
  korb basket add <LISTING_ID>     Set item quantity by listing ID. Overwrites existing quantity.
                                   --qty N sets absolute quantity. Default 1. Use --qty 0 to remove.

  korb timeslots                   List available pickup timeslots

  korb checkout                    Show the checkout for current basket. Payment is always in market.
  korb checkout create <TIMESLOT_ID> Create a checkout for a given timeslot id
  korb checkout order              Place the order. Timeslot must be attached first.

  korb orders                      Show open orders.
  korb orders history              Show all orders.
  korb orders get <ORDER_ID>       Get an order (with details) by id.
  korb orders delete <ORDER_ID>    Cancel an order by order ID - will give 200 on successive calls.

  korb suggestion threshold <N>    Suggest N items to add to reach free pickup threshold.
                                   Ranks by purchase frequency, excludes items already in basket.

  korb categories                   List all product categories (with subcategories).

  korb ebons                       List digital receipts (eBons).
  korb ebons download <EBON_ID>    Download eBon PDF. --output FILE (default: ebon.pdf)

  korb login                       Authenticate via REWE PKCE browser flow.

All commands support --pretty for formatted JSON output.
Output is JSON for agent consumption.
```

// API documentation
--------------------

Reverse-engineered OpenAPI specs for the REWE mobile API:

* [REWE Product & Checkout API](/yannick-cw/korb/blob/main/api/rewe.openapi.yaml)
* [REWE Account / Keycloak API](/yannick-cw/korb/blob/main/api/account-rewe.yaml)

// Platform support
-------------------

Currently macOS and linux.

// Formal verification with Lean 4
----------------------------------

The suggestion engine (`korb suggestion threshold`) is re-implemented in [Lean 4](/yannick-cw/korb/blob/main/leanKorb) with five mathematically proven properties: suggestions have positive frequency, are sorted descending, come from ordered and available products, exclude basket items, and respect the count limit.
A Differential Random Testing bridge in the Haskell test suite generates random inputs, runs both implementations, and asserts identical output.
If the Lean proofs compile and the DRT passes, the Haskell production code behaves like the proven spec.
Inspired by how [AWS Cedar](https://github.com/cedar-policy/cedar-spec) verifies their authorization engine.

I also summarised the approach in a [Blog post](https://www.dev-log.me/formal_verification_in_any_language_for_everybody/).

Oh and yes, this is complete overkill here and just for fun.

// Prior work & attribution
---------------------------

* <https://github.com/ByteSizedMarius/rewerse-engineering>
* <https://github.com/foo-git/rewe-discounts>
* <https://github.com/torbenpfohl/rewe-discounts>

// Disclaimer
-------------

This project is unofficial and not affiliated with REWE. It uses reverse-engineered APIs that may change without notice. Use at your own risk.
