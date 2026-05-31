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

Copy page DNS over HTTPS With DNS over HTTPS (DoH), DNS queries and responses are encrypted and sent via the HTTP, HTTP/2 and HTTP/3 protocols. DoH ensures that attackers cannot forge or alter DNS traffic. DoH uses port 443, which is the standard HTTPS traffic port, to wrap the DNS query in an HTTPS request. DNS queries and responses are camouflaged within other HTTPS traffic, since it all comes and goes from the same port. Configure DoH on your browser Connect to 1.1.1.1 using DoH clients Make API requests to 1.1.1.1 Was this helpful? Resources API New to Cloudflare? Directory Sponsorships Open Source Support Help Center System Status Compliance GDPR Company cloudflare.com Our team Careers Tools Cloudflare Radar Speed Test Is BGP Safe Yet? RPKI Toolkit Certificate Transparency Community X Discord YouTube GitHub © 2026 Cloudflare, Inc. Privacy Policy Terms of Use Report Security Issues Trademark Cookie Settings
