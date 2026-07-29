---
id: 1227
url: https://www.networkworld.com/article/4192827/meta-reuses-old-ram-in-new-servers-with-custom-bridge-chip.html
title: Meta reuses old RAM in new servers with custom bridge chip  | Network World
domain: www.networkworld.com
source_date: '2026-07-09'
tags:
- news
- devops
- database
summary: Meta has developed a custom Computer Express Link (CXL) chip called Vistara
  that allows the company to reuse older RAM from decommissioned servers in newer
  machines, addressing both cost concerns and the fact that memory chips last longer
  than other server components. About 40% of Meta's servers are memory-constrained,
  and with RAM prices expected to soar, this solution enables the integration of older
  DIMMs alongside new memory without significant performance degradation. The technology
  represents a practical approach to managing hardware costs during a period of widespread
  memory shortage and price increases expected to last until 2027.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# Meta reuses old RAM in new servers with custom bridge chip  | Network World

With the cost of new RAM soaring, Meta has found a thrifty way to reuse older memory in newer servers.

The performance of about 40% of Meta’s millions of servers is limited by a lack of memory, the company said — but it has a surplus of older DIMMs from decommissioned servers, because RAM chips can last about twice as long as the rest of the machine.

To profit from this imbalance, it developed a custom Computer Express Link (CXL) chip it calls Vistara, and associated software, to decouple older memory from server memory channels, enabling its reuse in new machines alongside their native memory. Using the older RAM with the CXL interface doesn’t significantly affect performance — although it would have done if the older DIMMs were plugged straight into newer servers.

Kudos to tech site [The Register](https://www.theregister.com/systems/2026/06/29/zuck-saves-meta-bucks-by-reusing-memory-from-old-servers-with-a-custom-cxl-asic/5263483) for noticing the development, which Meta described in a technical paper: [Vistara: Making CXL Real — Full Path from ASIC Design and OS Support to Hyperscale Deployment,” setting out how the new technology works](https://aisystemcodesign.github.io/papers/isca26/vistara_camera_ready.pdf).

There is a particular need to be thrifty right now, given the current state of the market. Last year, [users were warned that memory prices could double](https://www.networkworld.com/article/4093752/server-memory-prices-could-double-by-2026-as-ai-demand-strains-supply.html) by the end of 2026, while [the RAM shortage could last until 2027](https://www.computerworld.com/article/4161043/the-memory-shortage-appears-set-to-continue-through-2027.html). This week, [Apple suggested using cheap Chinese chips](https://www.networkworld.com/article/4192382/cheap-chinese-chips-could-offer-way-out-of-ram-price-crisis-apple-suggests.html), a move that may well be frowned on by the Trump administration. The Meta development may prove to be an efficient way forward.

[Servers](https://www.networkworld.com/servers/)[Data Center](https://www.networkworld.com/data-center/)[Cloud Computing](https://www.networkworld.com/cloud-computing/)

SUBSCRIBE TO OUR NEWSLETTER

### From our editors straight to your inbox

Get started by entering your email address below.
