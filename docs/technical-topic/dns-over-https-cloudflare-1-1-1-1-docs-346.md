---
id: 346
url: https://developers.cloudflare.com/1.1.1.1/encryption/dns-over-https/
title: DNS over HTTPS · Cloudflare 1.1.1.1 docs
domain: developers.cloudflare.com
source_date: '2025-07-16'
tags:
- security
- web-dev
- cli-tool
summary: DNS over HTTPS (DoH) is an encryption protocol that protects DNS queries
  and responses by transmitting them through HTTPS on port 443, preventing attackers
  from forging or altering DNS traffic. By camouflaging DNS queries within standard
  HTTPS traffic, DoH enhances privacy and security while maintaining compatibility
  with existing internet infrastructure. Cloudflare's 1.1.1.1 service offers DoH implementation
  options for browsers, clients, and API requests.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# DNS over HTTPS · Cloudflare 1.1.1.1 docs

DNS over HTTPS
==============

DNS over HTTPS (DoH) encrypts DNS queries by wrapping them inside regular HTTPS requests. This prevents attackers from forging or altering your DNS traffic.

DoH sends DNS traffic over port `443` — the default port for HTTPS web traffic. Because DoH queries use the same port and protocol as normal web browsing, they are difficult to distinguish from other HTTPS traffic on the network.

DoH supports the HTTP, HTTP/2, and HTTP/3 protocols.

* [Configure DoH on your browser](/1.1.1.1/encryption/dns-over-https/encrypted-dns-browsers/)
* [Connect to 1.1.1.1 using DoH clients](/1.1.1.1/encryption/dns-over-https/dns-over-https-client/)
* [Make API requests to 1.1.1.1](/1.1.1.1/encryption/dns-over-https/make-api-requests/)
