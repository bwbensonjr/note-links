---
id: 1188
url: https://blog.cloudflare.com/oauth-for-all/
title: Unlocking the Cloudflare app ecosystem with OAuth for all
domain: blog.cloudflare.com
source_date: '2026-06-25'
tags:
- web-dev
- security
- devops
summary: Cloudflare has announced OAuth for all, making self-managed OAuth available
  to all customers rather than just a limited number of manually onboarded partners.
  This enables developers to build integrations, SaaS applications, and agentic tools
  with standard OAuth flows that give users clearer consent and easier access revocation.
  To support this expansion securely, Cloudflare undertook a major upgrade of its
  underlying OAuth engine from Hydra, implementing a blue-green deployment strategy
  with innovative solutions like refresh token coalescing and revocation replay queues
  to minimize user disruption during the migration.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# Unlocking the Cloudflare app ecosystem with OAuth for all

Unlocking the Cloudflare app ecosystem with OAuth for all
=========================================================

2026-06-24

* [![Sam Cabell](https://blog.cloudflare.com/cdn-cgi/image/format=auto,dpr=3,width=64,height=64,gravity=face,fit=crop,zoom=0.5/https://cf-assets.www.cloudflare.com/zkvhlag99gkb/7FurLu5stbIo9nxEABOZZh/76dddf6ae7b3a7eeb4893e61e1aeee4b/Sam_Cabell_.webp)](/author/sam-cabell/)

  [Sam Cabell](/author/sam-cabell/)
* [![Mike Escalante](https://blog.cloudflare.com/cdn-cgi/image/format=auto,dpr=3,width=64,height=64,gravity=face,fit=crop,zoom=0.5/https://cf-assets.www.cloudflare.com/zkvhlag99gkb/RsjU3Hd0wT6DyNaNEpJnG/0168aa2bda8d8bde855cd30046b2bcdb/mike-escalante.jpg)](/author/mike-escalante/)

  [Mike Escalante](/author/mike-escalante/)
* [![Adam Bouhmad](https://blog.cloudflare.com/cdn-cgi/image/format=auto,dpr=3,width=64,height=64,gravity=face,fit=crop,zoom=0.5/https://cf-assets.www.cloudflare.com/zkvhlag99gkb/4aseXY5rjB2mooBiPmcQ9P/77d7246cb53fadde4bbc892adb14759e/Adam_Bouhmad_.webp)](/author/adam-bouhmad/)

  [Adam Bouhmad](/author/adam-bouhmad/)
* [![Nick Comer](https://blog.cloudflare.com/cdn-cgi/image/format=auto,dpr=3,width=64,height=64,gravity=face,fit=crop,zoom=0.5/https://cf-assets.www.cloudflare.com/zkvhlag99gkb/4XX534TzaPzsiYEPzRCJto/f5c0a75889e27da0a645bb6c7fae02f1/Nick_Comer.webp)](/author/nick-comer/)

  [Nick Comer](/author/nick-comer/)

6 min read

![](https://cf-assets.www.cloudflare.com/zkvhlag99gkb/470YV3u8pJdiSjyhZl1Zro/12aaff16d7787082571eeee0d2b8217f/image1.png)

Cloudflare provides services that help run 20% of the web, but we don’t do it alone. Developers on our platform use a myriad of tools and services from other companies too. Cloudflare provides a rich API for our platform that enables developers to create automations, CI/CD, and integrations that glue together the various parts of their infrastructure. Earlier this month, we announced [self-managed OAuth](https://developers.cloudflare.com/changelog/post/2026-06-03-public-oauth-clients/), making it easier for customers to create and manage their own OAuth clients for delegated access to the Cloudflare API.

Cloudflare isn’t new to OAuth. If you’ve used Wrangler, or used integrations from partners like PlanetScale, then you’ve already used it. However, until now, third-party OAuth was only available through a small number of manually onboarded integrations, and was not available to developers more broadly. That meant developers building their own integrations had to rely on API tokens, which are harder to manage and a poor fit for many delegated application flows.

Over the last year, we onboarded a growing number of early partners while improving the consent, revocation, and security model behind Cloudflare OAuth. But as our Developer Platform grew and agentic tools drove demand for delegated access, it became clear that opening up OAuth to all customers was critical to the success of our platform.

With self-managed OAuth, developers can now offer a standard OAuth flow where customers grant scoped access directly, making it easier to build SaaS integrations, internal developer platforms, and agentic tools while giving users clearer consent, easier revocation, and more control over what an application can do.

Scaling the ecosystem securely
------------------------------

While our earlier OAuth solution was sufficient for a small number of carefully managed partners, we realized that our permissions model, our consent experience, and our ways of mitigating potential abuse vectors were not mature enough.

Earlier this year we [updated our consent experience](https://blog.cloudflare.com/improved-developer-security/#improving-the-oauth-consent-experience) to make it clearer which application is requesting access, and what permissions it will receive. We also added revocation to the dashboard so developers can easily control which applications have access to their data, and made app ownership more visible to prevent OAuth phishing attacks.

Opening self-managed OAuth to all customers also required major upgrades to our underlying OAuth engine. This process required a large amount of planning to do with minimal user interruption, while also ensuring data stability and security.

Planning the upgrade to our OAuth engine
----------------------------------------

Years ago, we deployed [Hydra](https://github.com/ory/hydra), an open-source OAuth engine, to power Cloudflare OAuth under the hood. That deployment served us well when usage was limited, but as the developer platform grew and agentic workflows became more common, it became clear that we needed a major upgrade to unlock new capabilities and improve performance.

As we planned the upgrade, we decided to do two smaller sequential upgrades rather than doing one large upgrade.  First, we would move to the latest 1.X release, evaluate any behavior or performance changes, and then proceed with the 2.X upgrade.

During our upgrade planning, it became clear that even the 1.X upgrade wouldstill impact customers because the Hydra database required extensive schema migrations that:

1. Created indexes in a manner that would claim an exclusive lock on critical tables, preventing active users from performing important OAuth operations
2. Added columns to critical tables, and moved other columns to new tables

There was also a quirk in the version of Hydra we were using in which the SDK would perform SELECT \* operations, causing deserialization issues with the schema changes.

To prevent user impact, we rewrote the SQL migrations to use features such as CREATE INDEX CONCURRENTLY, and built a custom version of Hydra which selected explicit columns rather than SELECT \*.

With the latest 1.X upgrade planned out, we now needed to create a plan for the even larger 2.X upgrade. We identified three potential options, and weighed the benefits and drawbacks of each one. Doing an in-place upgrade was not going to work for us, due to the sheer amount of schema changes the major version bump brought with it. We decided that a blue-green strategy would work, but there was more that needed to be done than simply flipping a switch to start using the new version. The upgrade and migration process would take multiple hours, and we needed the system to continue functioning correctly in that time window.

The first blue-green option would involve disabling writes to the database, preventing any new authorizations from occurring. This means they would not be lost in the transition, but it also meant that nobody would be able to use existing OAuth apps unless they already had a valid credential. It also presented another large problem: if users needed to revoke access from an application for any reason, it would not be possible while the upgrade was being performed.

To combat these issues, we came up with a way to leave writes to the database enabled, at the cost of losing some of them in the switch to the green version. The first thing to solve was minimizing the number of writes for new tokens. There was an operational lever we pulled: increasing the expiry time of tokens to multiple hours. This would allow apps that received new tokens before the upgrade to continue using them without needing to refresh.

With reducing writes solved, we needed to come up with a way to not lose any revocations our users performed during the upgrade window. To do this, we created a queue system (using [Cloudflare Queues](https://developers.cloudflare.com/queues/)!) which, after a revocation event, would have a record written into the queue with information about that revocation. This would allow us to drain the queue with the database flipped to the green version, replaying all revocation events that took place in the time window in which they would have been lost. This was critical to get right, otherwise applications that users had revoked would inadvertently have their access restored.

Executing the upgrade
---------------------

### Upgrading to 1.X

From an operational point of view, our first upgrade to the last 1.X release went off without any hitches. Our custom database migrations ran faster than we expected, with no user impact. We had to do a hard cutover to the new version because the old version was unable to introspect tokens that were created by the newer version.

After the cutover, we saw an increase in refresh token errors that we had not seen before. This ended up being due to stricter refresh invalidation behaviors in the new version; if a refresh token was reused, Hydra would invalidate the whole access and refresh token chain. This is problematic for Wrangler and MCP clients. These clients both have a high request volume, and a single reused refresh token would invalidate the entire session.

We mitigated this by adding refresh token coalescing behavior to our Worker which routes OAuth traffic to the correct destination. This allowed us to briefly cache the refresh token request before it reached Hydra, so that if we detected a retry we could short-circuit the request and respond without invalidating the tokens. Fortunately, 2.X versions of Hydra have a configurable “refresh token grace period”, which resolves this by allowing a refresh token to be retried for a period of time without invalidating the whole chain.

### Upgrading to 2.X

Since multiple hours of high user-facing impact would not be acceptable, we had our blue-green upgrade strategy set. At a high level, this sounds simple; the migrations would run on a copy of our production database, and then cut over along with the new Hydra version after they complete. In reality, there were a *lot* more moving parts:

* Enable revocation replay capture queue
* Copy and restore our database to the new target
* Targeted data cleanup — existing data violated some new constraints introduced in the newer versions, which could prevent migrations from succeeding
* Perform cutovers on the Hydra service along with two additional critical internal systems simultaneously to prevent any errors
* Post-cutover monitoring and validation



We chose an upgrade window when Hydra had the lowest request volume per second to minimize lost token writes. Other than some timeout tuning, our production migrations ran well against the new database: the net runtime in production was approximately three hours. After the migrations completed, we carefully rolled out the new version of the Hydra service, along with two additional system configs to flip our systems to use the new SDK version.

Shortly after cutting traffic over, we observed that a data cleanup job in our authorization service (which relies on the Hydra consent session API) was being overeager in its purging of OAuth policy data. After investigation, we discovered that there was an issue in one of the Hydra migrations that corrupted the state of certain valid OAuth sessions, which resulted in the migration marking them as invalid. The valid sessions being corrupted caused a disagreement between Hydra and our authorization service, manifesting as an increase in 403s. To mitigate this, we did data restorations and began work on improvements for OAuth authorization behaviors to remove reliance on static policy data.

Beyond the data cleanup issue, there were some additional small fixes more driven by specific client behaviors which we landed quickly.

With the Hydra version upgrade complete, OAuth traffic has remained stable with improved system performance and reliability for our customers. It also brought production onto the same foundation our newer OAuth APIs had already been validated against in staging, clearing the way for our [self-managed OAuth release on June 3](https://developers.cloudflare.com/changelog/post/2026-06-03-public-oauth-clients/).

Performance improvements
------------------------

After completing a large upgrade like this, it is always rewarding and illuminating to look at some broad metrics about the impact. We gathered additional metrics during the database migrations, and observed considerable performance improvements after the upgrade was complete.

### Database

| Metric | Approx. Value |
| --- | --- |
| Rows updated | 132.5M |
| Rows inserted | 114.7M |
| Temp bytes | 136.97GB |
| Transaction commits | 22.2k |

### Hydra performance

| Metric (avg) | Before | After | Change |
| --- | --- | --- | --- |
| API P95 | 185ms | 101ms | -45% |
| RSS memory | 888MB | 763MB | -14% |
| Go heap alloc | 449MB | 271MB | -40% |
| Goroutines | 4015 | 3076 | -23% |
| CPU | 1.07 cores | 0.67 cores | -37% |

Self-managed OAuth for all
--------------------------

Opening up OAuth to all customers is an important step toward a broader Cloudflare app ecosystem. Today, any Cloudflare customer can create their own OAuth applications and build integrations on top of Cloudflare. We’re extremely excited to launch Cloudflare self-managed OAuth for all.

To get started, take a look at our [documentation](https://developers.cloudflare.com/fundamentals/oauth/) or jump straight to the OAuth apps page in the [dashboard](https://dash.cloudflare.com/?to=/:account/oauth-clients) and create your first OAuth app.

  [Developers](/tag/developers/)[API](/tag/api/)[Security](/tag/security/)[OAuth](/tag/oauth/)[Developer Platform](/tag/developer-platform/)[Agents](/tag/agents/)[Product News](/tag/product-news/)[Cloudflare Media Platform](/tag/cloudflare-media-platform/)[Identity](/tag/identity/)
