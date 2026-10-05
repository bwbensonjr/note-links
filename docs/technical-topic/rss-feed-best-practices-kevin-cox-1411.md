---
id: 1411
url: https://kevincox.ca/2022/05/06/rss-feed-best-practices/
title: RSS Feed Best Practices - Kevin Cox
domain: kevincox.ca
source_date: '2026-10-02'
tags:
- tutorial
- web-dev
- security
summary: This guide outlines essential technical practices for publishing RSS feeds,
  emphasizing standardized formats, proper metadata, and security. Key recommendations
  include using Atom or RSS 2 format with correct content-type headers, ensuring all
  URLs are absolute, implementing feed discovery through HTML link tags, and always
  serving feeds over HTTPS. The article also stresses providing full content in feeds,
  maintaining consistent entry IDs, and properly handling publication and update dates
  to ensure compatibility across feed readers and search engines.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# RSS Feed Best Practices - Kevin Cox

RSS Feed Best Practices
=======================

Posted on 2022-05-06

Last updated on 2024-03-13

These are some **technical** tips for publishing a blog. These have nothing to do with good content, just how to share that content. The recommendations are roughly in order of importance and have rationale for why they are that important.

[Formats](#formats)
-------------------

People generally call feeds “RSS Feeds” but usually they aren’t specifically talking about RSS. RSS isn’t the only, or even the best format. Using a standardized format is critical to your feed being understood by the widest variety of readers and search engines.

You should use [RSS 2](https://validator.w3.org/feed/docs/rss2.html) or [Atom](https://datatracker.ietf.org/doc/html/rfc4287). These formats are very widely supported. Other common formats are earlier RSS standards and [JSON Feed](https://www.jsonfeed.org/) or [Microformats h-feed](https://microformats.org/wiki/h-feed). I would avoid using these—or even less common formats—as they are less widely supported.

If you don’t have a feed yet I would highly recommend Atom. The specification has much less ambiguity, so you are less likely to have compatibility issues with the wide variety of clients in use. The specification is also simpler and more clear overall. If you already have an RSS 2 feed there is little reason to upgrade.

A minimal Atom template is below. For full details see [the spec](https://datatracker.ietf.org/doc/html/rfc5023). If you need an example you can look at [my feed](/feed.atom).

```
<?xml version="1.0" encoding="UTF-8"?>
<feed xmlns="http://www.w3.org/2005/Atom">
	<title>{{FEED_NAME}}</title>
	<id>{{HOMEPAGE_URL}}</id>
	<link rel="alternate" href="{{HOMEPAGE_URL}}"/>
	<link rel="self" href="{{FEED_URL}}"/>
	<updated>{{LAST_UPDATE_TIME in RFC3339 format}}</updated>
	<author>
		<name>{{AUTHOR_NAME}}</name>
	</author>
	<entry>
		<title>{{ENTRY.TITLE}}</title>
		<link rel="alternate" type="text/html" href="{{ENTRY.HTML_URL}}"/>
		<id>{{ENTRY.PERMALINK}}</id>
		<published>{{ENTRY.FIRST_POST_TIME in RFC3339 format}}</published>
		<updated>{{ENTRY.LAST_UPDATE_TIME in RFC3339 format}}</updated>
		<content type="html">{{ENTRY.HTML}}</content>
	</entry>
</feed>
```

There is very little reason to provide feeds in multiple formats. If you have an Atom feed you don’t need to provide an RSS feed as well.

Changing feed format is safe. Very few readers will be confused if a feed switches between Atom and RSS. This can be done either by changing the feed at the same URL or by redirecting new a new URL. (Just be sure to update the [content type](#content-type))

[Content Type](#content-type)
-----------------------------

Be sure to set the `Content-Type` header properly.

* Atom: `Content-Type: application/atom+xml`
* RSS: `Content-Type: application/rss+xml`
* JSON Feed: `Content-Type: application/feed+json`

You will see other values used in the wild, but these are the standard values and have the widest support.

[Absolute URLs](#absolute-urls)
-------------------------------

Every URL in your feed should be absolute. While Atom has clearly specified how to resolve relative URLs they are rarely implemented correctly. In order to ensure that your feed can be understood by all readers use only absolute URLs (starting with `https://`).

This includes all `<link>` elements and the summary and body of posts (including in the HTML).

[Discovery](#discovery)
-----------------------

On all of your blog pages and likely every page of your site you should include metadata to advertise you feed. This will allow readers and search engines to subscribe and become aware of your new content. This is as simple as providing the following in your HTML:

```
<link rel=alternate title="Blog Posts" type=application/atom+xml href="/feed.atom">
```

If you have multiple feeds you can advertise them all with appropriate titles.

```
<link rel=alternate title="All Posts" type=application/atom+xml href="/feed.atom">
<link rel=alternate title='Posts in the "Social" category' type=application/atom+xml href="/feeds/social.atom">
<link rel=alternate title="Comments on this Post" type=application/atom+xml href="/post/hello-world/comments.atom">
```

Make sure that you use the correct `type` for your feed. The examples provided are for Atom feeds.

Prefer to put the “most important” feed at the top. Many clients will preserve the order when presenting feeds to the user. This is subjective but typically would be a whole-site feed, then category feeds, then a comment feed for the specific page. If you offer your feeds in multiple formats I recommend only advertising one (either Atom or RSS 2). Including multiple links to the same content in multiple formats may confuse potential subscribers or leave them in analysis paralysis. (How do they know that the content is the same?)

You can validate that this is working correctly by putting your website URL into the [W3C Feed Validation Service](https://validator.w3.org/feed/). If your links are set up correctly it should detect and validate your feed. Try out a few different pages to make sure that you have discovery working everywhere. Try your homepage, post lists page and an individual post page.

If it is difficult to modify the HTML a `Link` header in the HTTP response can be used. However, this isn’t as widely supported. Using HTML `<link>` tags is preferred for wider compatibility.

```
Link: /feed.atom; rel="alternate"; type="application/atom+xml"
```

You should also include a link with an RSS logo [![rss logo](/a/87JpFA/rss.svg)](/a/87JpFA/rss.svg) for users without another feed indicator.

[HTTPS](#https)
---------------

[HTTPS](https://en.wikipedia.org/wiki/HTTPS) is key to security and privacy on the internet. Providing feeds over HTTPS ensures user privacy and ensures that your feed is not modified by a malicious actor.

1. Reference all embedded media (such as images) over HTTPS. Many readers will run in a secure context where HTTP requests are not allowed.
2. Provide the feed over HTTPS.
3. Ensure that your [self link](#self-link) is HTTPS.
4. Redirect HTTP requests to HTTPS.
5. Consider using [`Strict-Transport-Security`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Strict-Transport-Security).

[Full Content](#full-content)
-----------------------------

It is generally recommended to provide the full content of your posts in the feed. This is what most readers prefer. For RSS and Atom the [`<content>`](https://datatracker.ietf.org/doc/html/rfc4287#section-4.1.3) element should contain the full article. Atom also has a [`<summary>`](https://datatracker.ietf.org/doc/html/rfc4287#section-4.2.13) element in which to include a shorter summary for readers who prefer it.

Of course sharing full content in feeds is unacceptable to some publications due to the difficulty of monetizing these views. First, consider that some readers may leave if they can’t view the full content in their feed reader. Even if they don’t see your ads they may share your content with friends or on news aggregators. Likely it is still more valuable for you to have this reader than to lose them.

If your content is paid consider allowing users to generate private links by providing an auth token. For example `/feed.atom?user=peruserauthtoken`. You can also use [basic auth](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Authentication) like `https://fred:peruserauthtoken@blog.example/feed.atom` however this is supported by fewer readers than providing a token in the URL path or query string.

[Entry IDs](#entry-ids)
-----------------------

Entry IDs are the primary way to identify and differentiate entries in your feed. If your entry IDs change or repeat, readers will receive duplicates or miss entries.

1. Never change the ID of an existing article.
   * If you change your ID scheme, ensure that it only applies to new entries.
2. Never reuse Entry IDs for different articles.
3. Prefer to use article permalinks for Entry IDs.
4. Prefer to make your Entry IDs globally unique across all feeds in existence.
   * Some readers will merge feeds together, unique IDs help ensure there are no issues.
   * The easiest way to accomplish this is to use a URL on a domain that you control. If that isn’t possible you can use a [UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier) such as `urn:uuid:f4a3ca5b-5799-44e8-aaaa-e40728f037d3`.

[Dates](#dates)
---------------

Both Atom and RSS differentiate between time of publication (the time the entry first appeared in the feed) and the time of last update (the last time the entry was changed). Be sure to handle these correctly.

1. Include a publication time.
2. The publication time should never change. An entry can only be published once.
3. Prefer making the publication time roughly match when the entry appeared on the feed. Some readers will ignore entries that were published in the far past.
4. Strongly avoid having entries start appearing in the feed in a different order than their publication time suggests. (For example avoid having an item with a published time of 14:00 start appearing in the feed at 14:00 then have an item with the published time of 13:00 start appearing in the feed at 15:00. Some clients will be suspicious that they already know about the 14:00 item but don’t yet know about the “earlier” 13:00 item.) Another way of viewing this is that every new item that appears in a feed should have a published time that is later than all items previously in the feed. Some clients will ignore these “backdated” entries even if the published time is quite recent.
5. Avoid future publication times. If a publication time is too far in the future many readers will ignore it as a bug.
6. Update time should be greater than or equal to the publication time. New entries should have these two be the same.
7. Update time should only change on **significant** updates. Slight formatting changes or typo fixes probably shouldn’t change the last update time. Most readers ignore the update time, some will resurface your article as “updated”.

[Feed Title](#titles)
---------------------

The title of your feed is likely used by default in the user’s reader. Many readers have options to override the title, but it is extra work for the user and not universally supported. Try to pick a good title for your feed.

1. Include context. The title is likely one of many feeds in their reader. For example call it “Kevin Cox’s Blog” rather than “Blog Posts”.
2. Keep it succinct. The user is already subscribed, no need to advertise more. For example “John Smith” or “John Smith’s Photography Blog”. Not “John Smith — Ramblings on Photography every Tuesday and Friday, Cameras, Film and Development — Exclusive Content”.
3. Avoid HTML special characters such as `<` `>` and `&`. In RSS it isn’t completely clear if you can include styling like `<b>` tags in your feed title. Very few readers will parse HTML and will almost always treat the title literally.

You can update your feed title at any time, but it may be confusing to users if it changes too frequently.

[Styling](#styling)
-------------------

Feel free to use CSS in your feed! However, keep in mind that many feed readers don’t use modern browser engines and may be limited in what they can render. Additionally, many feed readers will sanitize your feed so uncommon elements and custom CSS may be partially or completely stripped. But don’t let that stop you! Using HTML and CSS can greatly improve the experience for users with good readers. Consider the following tips:

1. Consider what will happen if any CSS doesn’t apply. For example if you set `background: black; color: white` and one of the two rules is stripped you will have unreadable text. In general prefer to make small adjustments rather than relying on CSS for dramatic changes.
2. Prefer inline CSS `style` attributes to separate `<style>` blocks. They have wider compatibility.
3. Prefer semantic elements such as `<p>`, `<h1>`, `<pre>` and `<code>` over emulating their style on `<div>`s and `<span>`s.
4. Don’t rely on JavaScript, almost no readers support it.
5. Provide fallbacks for `<audio>`, `<video>` and `<iframe>` tags. Support isn’t common.
6. Avoid form and input elements. Support is rare and incompatible.

Unfortunately there is no substitute for testing in various readers to see what works.

[Self Link](#self-link)
-----------------------

Ensure that the self-link for your feed is accurate.

```
<link rel="self" href="https://kevincox.ca/feed.atom"/>
```

This provides the following benefits:

1. Allows you to move your feed. Some readers will update the feed URL if they get a permanent redirect and the redirect target contains a self link that points to itself.
2. Improve cache hits. It is common for users to find slight variations of your feed URL. For example `http:` instead of `https:`, `/feed` vs `/feed/`, `www.example.com` vs `example.com`, `feed.atom?tracker=lookatme` or `?category=rant&content=full` vs `?content=full&category=rant`. By providing a canonicalized self link you can merge these to reduce variance and increase you cache hit rate.
3. Required for [WebSub](#websub).
4. If the user has a copy of the feed file they can subscribe to it. For example some feed readers will act as file handlers for feeds. If the file contains a self link then they can use that URL to subscribe and fetch updates. If the file doesn’t have a self link it isn’t possible to do that.

[Caching](#caching)
-------------------

Feeds are followed by constant polling. This can create a decent amount of load on your server. Setting cache headers can help control the readers. If you don’t provide any guidance every client will pick their own value, which may be too fast or slow for your feed. If you make a suggestion some will follow it. Try to pick a reasonable value based on when you post. If your blog updates monthly then caching for an hour would make sense. However, if you are posting many times a day, a five minute cache may be more suitable.

Example cache headers:

* 5 min: `Cache-Control: max-age=300`
* 15 min: `Cache-Control: max-age=900`
* 1 h: `Cache-Control: max-age=3600`

If you use scheduled posts and want to get very fancy you can vary the cache time based on when the next post will go live. But a static cache time is sufficient.

[Conditional Requests](#conditional-requests)
---------------------------------------------

Support conditional requests on your feed. This makes polling more efficient for both you and your users.

Return an `ETag` and/or `Last-Modified` header. Then return a `304` response if the feed hasn’t changed. See [HTTP conditional requests on MDN](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Conditional_requests) for more details.

[WebSub](#websub)
-----------------

[WebSub](https://www.w3.org/TR/websub/) is a standard for real-time feed updates. Not only does it push your updates out faster, but it also reduces load on your server.

You can use a [public hub](https://pubsubhubbub.appspot.com/) or run your own. Note that a hub can modify or inject content into your feed, so be sure you trust the hub you pick.

I can’t find good generic setup instructions but the [Google hub](https://pubsubhubbub.appspot.com/) has basic instructions on their homepage. Maybe I’ll write a guide one day…

[Bot Access](#bot-access)
-------------------------

If you use any bot-blocking technology be sure to turn it off (or turn it way down) for your feeds. They are intended to be consumed by bots! Otherwise users will have trouble accessing your feed and will not know about your new content.

Many [popular](https://blog.cloudflare.com/) [sites](https://medium.com) have problems here. [I’ve written about this in the past](/2021/12/07/cloudflare-bot-block-failures/). Make sure that you aren’t hurt by defaults of various services.

[Categories](#categories)
-------------------------

Categories are a reliable way to filter items in feeds. It is far better to let someone subscribe for one category—or all categories but one—than to lose a subscriber because they were annoyed by a subset of your content.

For Atom feeds adding categories is as simple as one element. For example this post contains the following markup in my feed:

```
<category term="RSS"/>
<category term="Guide"/>
```

For RSS 2 the syntax is just slightly different:

```
<category>Rant</category>
```

Some readers don’t support categories, so you may wish to consider generating different feeds for different categories or providing a URL parameter to your feed to filter by category. Personally I wouldn’t worry about this.

[Changing URL](#changing-url)
-----------------------------

As much as possible you should avoid changing your feed’s URL. But if you need to do it here is how to do it without losing many subscribers.

1. Make the feed available at the new URL in addition to the old URL.
2. Make sure the self link of the new feed points at the new URL.
3. If you use WebSub, start pinging your hub for both URLs whenever you post.
4. Redirect the old URL to the new one with a [308 Permanent Redirect](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/308).
5. If you use WebSub you should continue pinging the old URL for at least 3 months or the max subscription lifetime of your hub (whichever is greater).

Remember that that some subscribers will not move. Try to keep the redirect alive as long as possible. After an extended period of time you may consider replacing the redirect with a feed that has an entry informing readers of the new location. But an ounce of prevention is worth a pound of cure, try picking a good URL (that you control) from the start.

[CORS](#cors)
-------------

CORS or [Cross-Origin Resource Sharing](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS) is a kludge to fix some holes in the original web security model. It adds restrictions to what requests web pages can make and controls what they can see about the response.

This is relevant for feeds as without opting-out of CORS browser-based readers that fetch feeds client side will not be able to access your feed.

For feeds the following headers are sufficient and secure for all feeds:

```
Access-Control-Allow-Origin: *
```

This means that your feed can be requested as a public resource (notably no cookies will be sent).

To test it out you can navigate to any third-party webpage (such as <https://example.com>) then run the following Javascript in [the developer console](https://www.digitalocean.com/community/tutorials/how-to-use-the-javascript-developer-console):

```
fetch("https://YOUR_FEED_HERE").then(r => r.text()).then(console.log, console.error)
```

If the content of your feed gets logged than you are all set. If you get an error then something has gone wrong.

[Performance](#performance)
---------------------------

While small and local feed readers tend to use simple poll rates many larger services use a variety of heuristics to determine when to check your feed. If you don’t support WebSub you should aim to respond to feed requests in less than 1s. If your feed is slower, especially if it is slower than 3 s polling will likely be slowed down and you readers will get updates slower.

---

The items below this point are relatively unimportant. They are a good idea if you are creating a product or feed generator but likely not worth the time if you are just making a feed for your own blog.

[Summaries](#summaries)
-----------------------

Some readers will display short snippets as an article preview. Providing a summary in your feed gives them high quality content for a good user experience. If you don’t provide an explicit summary they will likely use your first paragraph or first couple of sentences of your main content.

[Pagination](#pagination)
-------------------------

Pagination is a useful tool for keeping your feed archive available while keeping the size of your recent items small. It is specified in [RFC 5005: Feed Paging and Archiving](https://www.rfc-editor.org/rfc/rfc5005). Unfortunately, few clients have support. However, adding support in your feed doesn’t have any downsides, so it is still a good idea.

Pagination is very easy. Just add the following link to your feed.

```
<link href="https://kevincox.ca/feed/2022-03-05.atom" rel="next"/>
```

Then on subsequent pages also include a `prev` link. Of course the last page won’t have a `next` link.

```
<link href="https://kevincox.ca/feed.atom" rel="prev"/>
<link href="https://kevincox.ca/feed/2022-01-21.atom" rel="next"/>
```

When deciding how large to make your pages remember that not all clients will support pagination, so you don’t want to move new entries off your first page too quickly. I provide the following recommendations. Note that these are just general rules and should be applied judiciously. For example if you post 20 times a day you probably don’t need to keep 7 days of content in your feed. Similarly, if your posts are only a paragraph or two you can probably keep a few more on the first page.

1. Ensure your **newest** items are on the first page.
2. Try to keep items in the feed for at least a day. Some clients check quite infrequently. If reasonable, keep items for at least a week.
3. Avoid making the feed too large, well under a megabyte is recommended.

---
