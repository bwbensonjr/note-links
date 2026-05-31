---
id: 831
url: https://gwern.net/gwtar
title: 'Gwtar: a static efficient single-file HTML format · Gwern.net'
domain: gwern.net
source_date: '2026-02-16'
tags:
- web-dev
- cli-tool
- javascript
summary: Gwtar is a new HTML archival format that solves the traditional trade-off
  between being static (self-contained), single-file, and efficient by combining a
  JavaScript header with a compressed tarball of assets, allowing browsers to lazy-load
  only necessary content while maintaining full portability and no external dependencies.
  This approach enables large web pages—even those hundreds of megabytes in size—to
  be archived as single files that can be efficiently viewed without downloading all
  assets upfront, addressing the linkrot problem on long-term websites like Gwern.net.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# Gwtar: a static efficient single-file HTML format · Gwern.net

[compression](/doc/cs/algorithm/information/compression/index "Link to cs/algorithm/information/compression tag index"), [Internet archiving](/doc/cs/linkrot/archiving/index "Link to cs/linkrot/archiving tag index")

Gwtar is a new polyglot HTML archival format which provides a single, self-contained, HTML file which still can be efficiently lazy-loaded by a web browser. This is done by a header’s JavaScript making HTTP range requests. It is used on Gwern.net to serve large HTML archives.

2026-01-20–2026-01-27
*finished*
[certainty](/about#confidence-tags "Explanation of 'confidence' metadata: probability of overall being meaningfully correct, expressed as Kesselman Estimative Words (ranging 0–100%: 'certain'/'highly likely'/'likely'/'possible'/'unlikely'/'highly unlikely'/'remote'/'impossible')"): *certain*
[importance](/about#importance-tags "Explanation of 'importance' metadata: rating 1–10 about how much a topic matters to the world."): *4*
[similar](#similars "Similar links for this link (by text embedding).")
[bibliography](#link-bibliography "Bibliography of links cited in this page (forward citations).")

* [Background](#background)
* [HTML Trilemma](#html-trilemma)
* [Trisecting](#trisecting)
  + [Download Stopping Mechanisms](#download-stopping-mechanisms)
* [Concatenated Archive Design](#concatenated-archive-design)
  + [Creation](#creation)
  + [Implementation](#implementation)
    - [Header](#header)
    - [Details](#details)
  + [Fallback](#fallback)
  + [Compression](#compression)
  + [Limitations](#limitations)
    - [Local Viewing](#local-viewing)
    - [Range Request Support](#range-request-support)
      * [Cloudflare Is Broken](#cloudflare-is-broken)
  + [Accessing Binary Assets](#accessing-binary-assets)
  + [Optional Trailing Data](#optional-trailing-data)
    - [FEC](#fec)
    - [Signing](#signing)
* [Metadata](#metadata)
* [IP](#ip)
* [Further Work](#further-work)
* [External Links](#external-links)

> Archiving HTML files faces a trilemma: it is easy to create an archival format which is any two of “static” (self-contained ie. all assets included, no special software or server support), “single-file” (when stored on disk, zero additional files or modifications), and “efficient” (lazy-loads assets only as necessary to display to a user), but no known format allows all 3 simultaneously. One must trade off, usually achieving “static”+“efficient” or “static”+“single-file”.
>
> We introduce an experimental new format, **Gwtar** ([logo](/doc/cs/algorithm/information/compression/2026-01-23-dbohdan-gpt5imagemini-gwtarlogo-guitar.svg "Bohdan 2026"); pronounced “guitar”, `.gw⁠tar.html` extension), which achieves all 3 properties simultaneously using what we call the “`window.stop` trick”.
>
> A Gwtar is a classic fully-inlined HTML file, which is then processed into a self-extracting concatenated file of an HTML + JavaScript header followed by a tarball of the original HTML and assets. The HTML header’s JS stops web browsers from loading the rest of the file, loads just the original HTML, and then hooks requests and turns them into range requests into the tarball part of the file.
>
> Thus, a regular web browser loads what seems to be a normal HTML file, and all assets download only when they need to. In this way, a static HTML page can inline anything—such as gigabyte-size media files—but those will not be downloaded until necessary, even while the server sees just a single large HTML file it serves as normal. And because it is self-contained in this way, it is forwards-compatible: no future user or host of a Gwtar file needs to treat it specially, as all functionality required is old standardized web browser/server functionality.
>
> Gwtar allows us to easily and reliably archive even the largest HTML pages, while still being user-friendly to read.
>
> Example page: [“The Secret of Psalm 46”](/doc/philosophy/religion/2010-02-brianmoriarty-thesecretofpsalm46.gwtar.html), vs [original SingleFile archive](/doc/philosophy/religion/2010-02-brianmoriarty-thesecretofpsalm46.html "‘The Secret of Psalm 46’, Moriarty 2010") (the audio files are large and may take a while to download; second link is a 286MB download).

[Background](#background "Link to section: § 'Background'")
===========================================================

[Linkrot](https://en.wikipedia.org/wiki/Linkrot "Linkrot") is one of the biggest challenges for long-term websites. Gwern.net makes [heavy use of web page archiving](/archiving "‘Archiving URLs’, Gwern 2011") to solve this; and due to quality problems and [long-term reliability concerns](/archiving#why-not-internet-archive "‘Archiving URLs § Why Not Internet Archive?’, Gwern 2011"), simply linking to the [Internet Archive](https://en.wikipedia.org/wiki/Internet_Archive "Internet Archive") is not enough, so I try to create & host my own web page archives of everything I link.

There are 3 major properties we would like of an HTML archive format, beyond the basics of actually capturing a page in the first place:

1. it should be **static**, ie. not dynamic and should not depend in any way on the original web page, because then it is not an archive and will *inevitably* break;
2. it should be easy to manage and store, so you can scalably create them and store them for the long run (ideally, requiring users to know no more about than they do a PDF), preferably a simple standalone **single-file**;
3. and it should be **efficient**, which for HTML largely means that readers should be able to download only the parts they need in order to view the current page (critical as web pages get ever larger and more media-heavy, increasing the cost of static archives).

[HTML Trilemma](#html-trilemma "Link to section: § 'HTML Trilemma'")
====================================================================

No current format achieves all 3. The built-in web browser save-as-HTML format achieves single and efficient, but not static; save-as-HTML-with-directory achieves static partially and efficient, but not single; [MHTML](https://en.wikipedia.org/wiki/MHTML "MHTML"), [MAFF](https://en.wikipedia.org/wiki/Mozilla_Archive_Format "Mozilla Archive Format"), [SingleFile](https://github.com/gildas-lormeau/SingleFile/ "'SingleFile', Lormeau 2026"), & [SingleFileZ](/doc/www/gildas-lormeau.github.io/dcdf119444ce9a4c490438c44fe153e03c7bb772.html "How to Create HTML/ZIP/PNG Polyglot Files") (a [ZIP](https://en.wikipedia.org/wiki/ZIP "ZIP")-compressed variant) achieve static, single, but not efficiency; [WARCs](https://en.wikipedia.org/wiki/WARC_(file_format) "WARC (file format)")/[WACZs](/doc/www/specs.webrecorder.net/ff89b4b8b9c4be57fb7763bfb1aa72efe9a60dea.html "Web Archive Collection Zipped (WACZ)") achieve static and efficient, but not single (because while the WARC is a single file, it relies on a complex software installation like [WebRecorder](/doc/www/webrecorder.net/82689b025a750b04cef057df3f4fc757aa4cba5c.html "Webrecorder: Web Archiving for All")/[Replay Webpage](/doc/www/replayweb.page/4f0b451c235dfd9685fa00ddf0ba492bc8554dad.html "ReplayWeb.page") to display).

An ordinary ‘save as page HTML’ browser command doesn’t work because “Web Page, HTML Only” leaves out most of a web page; even “Web Page, Complete” is inadequate because a lot of assets are dynamic and only appear when you interact with the page—especially images. If you want a **static** HTML archive, one which has no dependency on the original web page or domain, you have to use a tool specifically designed for this. I usually use SingleFile. SingleFile produces a static snapshot of the live web page, while making sure that [lazy-loaded](https://en.wikipedia.org/wiki/Lazy_loading "Lazy loading") images are first loaded, so they are included in the snapshot.

SingleFile often produces a useful static snapshot. It also achieves another nice property: the snapshot is a **single file**, just a simple single `.html` file, which makes life so much easier in terms of organizing and hosting. Want to mirror a web page? SingleFile it, and upload the resulting single file to a convenient directory somewhere, boom—done forever. Being a single file is important on Gwern.net, where I must host so many files, and I run so many lints and checks and automated tools and track metadata etc. and where other people may rehost my archives.

However, a user of SingleFile quickly runs into a nasty drawback: snapshots can be surprisingly large. In fact, some snapshots on Gwern.net are over half a gigabyte! For example, the homepage for the research project [“PaintsUndo: A Base Model of Drawing Behaviors in Digital Paintings”](/doc/www/lllyasviel.github.io/96def0bcd8813bb1389665c487366a2ac61eaf4e.html "PaintsUndo: A Base Model of Drawing Behaviors in Digital Paintings") is 485MB *after* size optimization, while the raw HTML is 0.6MB. It is common for an ordinary somewhat-fancy Web 2.0 blog post like a [Medium.com](https://en.wikipedia.org/wiki/Medium.com "Medium.com") post to be >20MB once fully archived. This is because such web pages wind up importing a lot of [fonts](https://en.wikipedia.org/wiki/Web_Fonts "Web Fonts"), JS, widgets and icons etc., all of which assets must be saved to ensure it is fully static; and then there is additional wasted space overhead due to [converting](https://en.wikipedia.org/wiki/Binary-to-text_encoding "Binary-to-text encoding") assets from their original binary encoding into [Base64](https://en.wikipedia.org/wiki/Base64 "Base64") text which can be [interleaved with the original HTML](https://en.wikipedia.org/wiki/Data_URI_scheme "Data URI scheme").

This is especially bad because, unlike the original web page, anyone viewing a snapshot *must* download the *entire thing*. That 500MB web page is possibly OK because a reader only downloads the images that they are looking at; but the archived version must download everything. A web browser has to download the entire page, after all, to display it properly; and there is no lazy-loading or ability to optionally load ‘other’ files—there are no other files ‘elsewhere’, that was the whole point of using SingleFile!

Hence, a SingleFile archive is static, and a single file, but it is not **efficient**: viewing it requires downloading unnecessary assets.

So, for some archives, we ‘split’ or ‘deconstruct’ the static snapshot back into a normal HTML file and a directory of asset files, using [`deconstruct_singlefile.php`](/static/build/deconstruct_singlefile.php) (which incidentally makes it easy to re-compress all the images, which produces large savings as many websites are surprisingly bad at basic stuff like PNG/JPG/GIF compression); then we are back to a static, efficient, but not single file, archive.

This is fine for our [auto-generated local archives](/archiving#preemptive-local-archiving "‘Archiving URLs § Preemptive Local Archiving’, Gwern 2011") because they are stored in their own directory tree which is off-limits to most Gwern.net infrastructure (and off-limits to search engines & agents or off-site hotlinking), and it doesn’t matter too much if they litter tens of thousands of directories and files. It is not fine for HTML archives I would like to host as first-class citizens, and expose to Google, and hope people will rehost someday when Gwern.net inevitably dies.

So, we could either host a regular SingleFile archive, which is static, single, and inefficient; or a deconstructed archive, which is static, multiple, and efficient, but not all 3 properties.

This issue came to a head in January 2026 when I was archiving the Internet Archive snapshots of Brian Moriarty’s famous lectures [“Who Buried Paul?”](/doc/philosophy/religion/1999-03-17-brianmoriarty-whoburiedpaul.html "'Who Buried Paul?', Moriarty 1999") and [“The Secret of Psalm 46”](/doc/philosophy/religion/2010-02-brianmoriarty-thesecretofpsalm46.html "‘The Secret of Psalm 46’, Moriarty 2010"), since I noticed while writing [an essay drawing on them](/video-game-art "‘Video Games as Art’, Gwern 2025") that his whole website had sadly gone down. I admire them and wanted to host them properly so people could easily find my fast reliable mirrors (unlike the slow, hard-to-find, unreliable IA versions), but realized I was running into our long-standing dilemma: they would be efficient in the local archive system after being split, but unfindable; or if findable, inefficiently large and reader-unfriendly. Specifically, the video of “Who Buried Paul?” was not a problem because it had been linked as a separate file, so I simply [converted it to MP4](/doc/philosophy/religion/1999-03-17-brianmoriarty-whoburiedpaul-videolecture.mp4) and edited the link; but “The Secret of Psalm 46” turned out to inline the OGG/MP3 recordings of the lecture and abruptly increased from <1MB to *286MB*.

I discussed it with [Said Achmiz](https://wiki.obormot.net/ "Welcome to OborWiki"), and he began developing a fix.

[Trisecting](#trisecting "Link to section: § 'Trisecting'")
===========================================================

To achieve all 3, we need some way to download only part of a file, and selectively download the rest. This lets us have a single static archive of potentially arbitrarily large size, which can safely store every asset which might be required.

HTTP already easily supports selective downloading via the ancient [HTTP Range query feature](https://en.wikipedia.org/wiki/Byte_serving "Byte serving"), which allows one to query for a precise range of bytes inside a URL. This is mostly used to do things like resume downloads, but you can also [do interesting things](/design-graveyard#range-queries) like run databases in reverse: a web browser client can run a database application locally which reads a database file stored on a server, because Range queries let the client download only the exact parts of the database file it needs at any given moment, as opposed to the entire thing (which might be terabytes in size).

This is how formats like WARC can render efficiently: host a WARC as a normal file, and then simply range-query the parts displayed at any moment.

The challenge is the first part: how do we download *only* the original HTML and subsequently only the displayed assets? If we have a single HTML file and then a separate giant archive file, we could easily just rewrite the HTML using JS to point to the equivalent ranges in the archive file (or do something server-side), but that would achieve only static and efficiency, not single file. If we combine them, like SingleFile, we are back to static and single file, but not efficiency.

The simplest solution here would be to decide to complicate the server itself and do the equivalent of `deconstruct_singlefile.php` on the fly. HTML requests, perhaps detecting some magic string in the URL like `.singlefile.html`, is handed to a [CGI](https://en.wikipedia.org/wiki/Common_Gateway_Interface "Common Gateway Interface") proxy process, which splits the original single HTML file into a normal HTML file with lazy-loaded references. The client browser sees a normal multiple efficient HTML, while everything on server sees a static single inefficient HTML. (A possible example is [WWZ](/doc/www/github.com/ff0072519026bd8a7f72adcf3f86a25a1932e14d.html "oils-for-unix/wwz: A WSGI program that serves content out of a zip file (.wwz file). Deploy as CGI or FastCGI").)

While this solves the immediate Gwern.net problem, it does so at the permanent cost of server complexity, and does not do much to help anyone else. (It is unrealistic to expect more than a handful of people to modify their servers this invasively.) I also considered taking the WARC red pill and going full WebRecorder, but quailed.

[Download Stopping Mechanisms](#download-stopping-mechanisms "Link to section: § 'Download Stopping Mechanisms'")
-----------------------------------------------------------------------------------------------------------------

How can we trick an HTML file into acting like a [tarball](https://en.wikipedia.org/wiki/Tar_(computing) "Tar (computing)") or ZIP file, with partial random access?

Our initial approach was to ship an HTML + JS header with an appended archive, where the JS would do HTTP Range queries into the appended binary archive; the challenge, however, was to *stop* the file from downloading past the header. To do this, we considered some approaches ‘outside’ the page, like encoding the archive index into the filename/URL itself (ie. `foo.gwtar-$N.html`) and requiring the server to parse `$N` out and slice the archive down to just the header, which then handled the range requests; this minimized how much special handling the server did, while being backwards/forwards-compatible with non-compliant servers (who would ignore the index and simply return the entire file, and be no worse than before). This worked in our prototypes, but required at least some server-side support and also required that the header be fixed-length (because any changes would in length would invalidate the index).

Eventually, Achmiz realized that you *can* stop downloading from *within* an HTML page, using the JS command `window.stop()`! [MDN](/doc/www/developer.mozilla.org/eb69f87617159b3c35da467410d978000623cabd.html "'Window: <code>stop()</code> method—Web APIs', MDN 2026") ([>96% support](https://caniuse.com/mdn-api_window_stop "Window API: <code>stop</code>"), [spec](/doc/www/html.spec.whatwg.org/eec44fc1e9facbc02385059984f186cfd5690346.html#dom-window-stop "HTML Standard")):

> The `window.stop()` stops further resource loading in the current browsing context, equivalent to the stop button in the browser.
>
> Because of how scripts are executed, this method cannot interrupt its parent document’s loading, but it will stop its images, new windows, and other still-loading objects.

This is precisely what we need, and the design falls into place.

[Concatenated Archive Design](#concatenated-archive-design "Link to section: § 'Concatenated Archive Design'")
==============================================================================================================

A Gwtar is an HTML file with a HTML + JS + JSON header followed by a tarball and [possibly further assets](#optional-trailing-data). (A Gwtar could be seen as *almost* a [polyglot file](https://en.wikipedia.org/wiki/Polyglot_(computing) "Polyglot (computing)") is a file valid as more than one format—in this case, a `.html` file that is also a `.tar` archive, and possibly `.par2`. But strictly speaking, it is not.)

[Creation](#creation "Link to section: § 'Creation'")
-----------------------------------------------------

We provide a reference PHP script, [`deconstruct_singlefile.php`](/static/build/deconstruct_singlefile.php), which creates Gwtars from SingleFile HTML snapshots.

It additionally tries to recompress JPG/PNG/GIFs before storing in the Gwtar, and then appends [PAR2 FEC](#fec).

Example command to replace the original [`2010-02-brianmoriarty-thesecretofpsalm46.html`](/doc/philosophy/religion/2010-02-brianmoriarty-thesecretofpsalm46.html "‘The Secret of Psalm 46’, Moriarty 2010") by [`2010-02-brianmoriarty-thesecretofpsalm46.gwtar.html`](/doc/philosophy/religion/2010-02-brianmoriarty-thesecretofpsalm46.gwtar.html) with PAR2 FEC:

```
php ./static/build/deconstruct_singlefile.php --create-gwtar --add-fec-data \
    2010-02-brianmoriarty-thesecretofpsalm46.html
```

[Implementation](#implementation "Link to section: § 'Implementation'")
-----------------------------------------------------------------------

### [Header](#header "Link to section: § 'Header'")

The first line of the header is the magic HTML string `<html> <!-- Gwtar self-extracting HTML archive, v1 -->`, and the final line is the magic HTML string `<!-- GWTAR END`. (Additional metadata like the original input filename/hash/date may be included in comments.)

The header stores a JSON dictionary of files/sizes/types/[SHA-256](https://en.wikipedia.org/wiki/SHA-2 "SHA-2")-hashes[1](#fn1) of the real HTML (always first, with the name `0`), followed by all of its assets (`basename-asset-N.ext`). There is always a HTML file and at least one asset. All of these assets are stored in the tarball immediately following the header (but which does not necessarily contain *only* these assets) Example (with whitespace added for readability):

```
<script>
let assets = {
    "0": {
        "size": 130673,
        "content-type": "text/html",
        "basename": "1999-03-17-brianmoriarty-whoburiedpaul",
        "hash": "79111815b482504d79428f5cea329741348060fd2d943da933288595e2c9e969"
    },
    "1999-03-17-brianmoriarty-whoburiedpaul-asset-1.js": {
        "size": 15127,
        "content-type": "application/x-javascript",
        "hash": "d739d46b0f3b188cd409c97ab47964ea3a009cce9d08a50b763fdb958e39b822"
    },
    "1999-03-17-brianmoriarty-whoburiedpaul-asset-2.js": {
        "size": 27146,
        "content-type": "text/javascript",
        "hash": "dd29affcde5ff55d96613aa7ac55fa56cc8eeda20d6aef90185b75332e2c3cde"
    },
    ...
}
</script>
```

(Unfortunately, the assets are not necessarily valid for their mime-type—SingleFile passes through invalid or mismatched images and doesn’t guarantee much about the validity of its generated HTML. So Gwtar cannot require or guarantee much about the input or output HTML and is best-effort.)

[The header JS](/static/build/gwtar.js) is attached to the window once it stops loading and does nothing initially.

Finally, `window.stop()` is called at the end, before the appended tarball begins. This stops the web browser from loading any more data; then the main JS is free to run.

The main header JS starts using range requests to first load the real HTML, and then it watches requests for resources; the resources have been rewritten to be deliberately broken 404 errors (requesting from localhost, specifically, `0.0.0.0`, to avoid polluting any server logs), so when they fail, the JS then rewrites them into working range requests into the tarball, and repeats them.

### [Details](#details "Link to section: § 'Details'")

The simple approach is to download the binary assets, encode them into Base64 text, and inject them into the HTML DOM. This is inefficient in both compute and RAM because the web browser must immediately reverse this to get a binary to work with. So we actually use the browser optimization of [blobs](/doc/www/developer.mozilla.org/6e7c2e7b2ee5ccbc06d56751793dc191e7fdd3d1.html "Blob—Web APIs") to just pass the binary asset straight to the browser.

A tricky bit is that inline JS can depend on “previously loaded” JS files, which may not have actually loaded *yet* because the first attempt failed (of course) and the real Range request is still racing. We currently solve this by just downloading all JS before rendering the HTML, at some cost to responsiveness.

So, a web browser will load a normal web page; the JS will halt its loading; a new page loads, and all of its requests initially fail but get repeated immediately and work the second time; the entire archive never gets downloaded unless required. All assets are provided, there is a single Gwtar file, it is efficient; it doesn’t require JS for archival integrity, as just the entire archive downloads if the JS is not executed; and it is cross-platform and standards-compliant, requires no server-side support or future users/hosts to do anything whatsoever, and is a transparent, self-documenting file format which can be easily converted back to a ‘normal’ multiple-file HTML (`cat foo.gwtar.html | perl -ne'print $_ if $x; $x=1 if /<!-- GWTAR END/' | tar xf -`) *or* a user can just re-archive it normally with tools like SingleFile.

[Fallback](#fallback "Link to section: § 'Fallback'")
-----------------------------------------------------

In the event of JS problems, [a `<noscript>` message](/static/build/gwtar_noscript.html) explains what the Gwtar format is and why it requires JS, and links to this page for more details.

It also detects whether range requests are supported or downgraded to requesting the entire file. If the latter, it will start rendering it.

This is not as slow as it seems because we can benefit from connection level compression like [gzip](https://en.wikipedia.org/wiki/Gzip "Gzip") or [Brotli compression](https://en.wikipedia.org/wiki/Brotli_compression "Brotli compression"). And because our preprocessing linearize the assets in dependency order, we receive the bytes in order of page appearance, and so in this mode, the “above the fold” images and stuff will still load first and quickly. (This in comparison to the usual SingleFile, where you have to receive every single asset before you’re done, and which may be slower.)

[Compression](#compression "Link to section: § 'Compression'")
--------------------------------------------------------------

Gwtar does not directly support deduplication or compression.

Gwtars may overlap and have redundant copies of assets, but because they will be stored bit-identical inside the tarballs, a [de-duplicating](https://en.wikipedia.org/wiki/Data_deduplication "Data deduplication") filesystem can transparently remove most of that redundancy.

Media assets like MP3 or JPEG are already compressed, and can be compressed during the build phase by a gwtar implementation.

The HTML text itself could be compressed; it is currently unclear to me how Gwtar’s range requests interact with transparent negotiated compression like Brotli compression (which for Gwern.net was as easy as enabling one option in [Cloudflare](https://en.wikipedia.org/wiki/Cloudflare "Cloudflare")). [RFC 7233](/doc/www/datatracker.ietf.org/07d457e632f14e2352ad8c8dff57057805885036.html "RFC 7233—Hypertext Transfer Protocol (HTTP/1.1): Range Requests") doesn’t seem to give a clear answer about this, and the [cursory and unhelpful discussion here](/doc/www/github.com/65ab1543899bde87417bd885a63424a25af38b89.html "Ranges and Content and Transfer Encoding · Issue #11 · httpwg/http-core") *seems* to indicate that the range requests would have to be interpreted relative to the compressed version rather than the original, which is useful for the core use-case of resuming downloads but not for our use-case. So I suspect that probably Cloudflare would either disable Brotli, or downgrade to sending the entire file instead. It is possible that [“transfer-encoding”](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Transfer-Encoding "Transfer-Encoding header—HTTP") solves this, but [as of 2018, Cloudflare didn’t support it](/doc/www/stackoverflow.com/18071621a0b975f4baf10eba55e91480b4dc641f.html "Is it possible to send HTTP response using GZIP and byte ranges at the same time?"), making it useless for us and suggesting little support in the wild.

If this is a serious problem, it may be possible to compress the HTML during the Gwtar generation phase and adjust the JS.

[Limitations](#limitations "Link to section: § 'Limitations'")
--------------------------------------------------------------

### [Local Viewing](#local-viewing "Link to section: § 'Local Viewing'")

Strangely, the biggest drawback of Gwtar turns out to be *local* viewing of HTML archives. SingleFileZ encounters the same issue: in the name of security ([origin](https://en.wikipedia.org/wiki/Same-origin_policy "Same-origin policy")/[CORS](https://en.wikipedia.org/wiki/CORS "CORS")/sandboxing), browsers will not execute certain requests in local HTML pages, so it will break, as it is no longer able to request from itself.

We regard this as unfortunate, but an acceptable tradeoff, as for local browsing, the file can be easily converted back to the non-JS dependent multiple/single-file HTML formats.

### [Range Request Support](#range-request-support "Link to section: § 'Range Request Support'")

Range requests are old, standardized, and important for resuming downloads or viewing large media files like video, and every web server should, in theory, support it by default. In practice, there may be glitches, and one should check.

An example curl command which should return a HTTP 206 (not 200) request if range requests are correctly working:

```
curl --head --header "Range: bytes=0-99" 'https://gwern.net/doc/philosophy/religion/1999-03-17-brianmoriarty-whoburiedpaul.gwtar.html'
# HTTP/2 206
# date: Sun, 25 Jan 2026 22:20:57 GMT
# content-type: x-gwtar
# content-length: 100
# server: cloudflare
# last-modified: Sun, 25 Jan 2026 07:08:33 GMT
# etag: "6975c171-7aeb5c"
# age: 733
# cache-control: max-age=77760000, public, immutable
# content-disposition: inline
# content-range: bytes 0-99/8055644
# cf-cache-status: HIT
# ...
```

Servers *should* serve Gwtar files as `text/html` if possible. This may require some configuration (eg. [in nginx](/doc/www/blog.nginx.org/cae9ac005b843b501c6626a67d100044d77e076d.html "Smart and Efficient Byte-Range Caching with NGINX")[2](#fn2)), but should be straightforward.

#### [Cloudflare Is Broken](#cloudflare-is-broken "Link to section: § 'Cloudflare Is Broken'")

However, Cloudflare has an undocumented, inclement behavior: its proxy (not cache) will strip Range request headers for `text/html` responses regardless of cache settings. This does not break Gwtar rendering, of course, but it does break efficiency and defeats the point of Gwtar for Gwern.net

As a workaround, we serve Gwtars with the MIME type `x-gwtar`—web browsers like Firefox & Chromium will content-sniff the opening `<html>` tag and render correctly, while Cloudflare passes Range requests through for unrecognized types. (This is not ideal, but a more conventional MIME type like `application/...` results in web browsers downloading the file without trying to render it at all; and using a MIME type trick is better than alternatives like trying to serve Gwtars as MP4s, using a special-case subdomain just to bypass Cloudflare completely, using complex tools like Service Workers to try to undo the removal, etc.)

[Accessing Binary Assets](#accessing-binary-assets "Link to section: § 'Accessing Binary Assets'")
--------------------------------------------------------------------------------------------------

Because a Gwtar can store large binary assets without burdening the viewer and is an archive format, it may be useful for reproducible science/statistics: include datasets, such as [Sqlite3 databases](/doc/www/sqlite.org/2871ae9cc332fe667da6d47e7e27a21ba40ee6a7.html "sqlite3 WebAssembly &amp; JavaScript Documentation Index"), and do computation on them like visualization or analysis. The question is, how do we ensure that assets get referenced in a way that SingleFile can “see” them and include them inline (to be stored in the final Gwtar as split-out objects), and then addressed and loaded by simple user JS, in a way which still works *without* Gwtar?

A potential approach in Gwtar v1 would be to reference all such assets using the [`<object>` tag](/doc/www/developer.mozilla.org/f55cf6cc432633d16437c94d52922c45bf99c9b2.html "‘<object>’, element—HTML MDN")[3](#fn3), and then the user JS adds a simple listener hook to the `load` event, which will fire either when the browser loads the asset normally (multi-file) or when Gwtar completes its range-fetch rewrite, and then kicks off the actual userland work. This does not require any unusual or contorted user JS, appears to be backwards/forwards compatible, and to satisfy all our desiderata.

Untested pseudo-code:

```
<object id="dataset" data="dataset.sqlite3" type="application/x-sqlite3" width="0" height="0"></object>

<script>
document.getElementById('dataset').addEventListener('load', function () {
    fetch(this.data)
        .then(function (r) { return r.arrayBuffer(); })
        .then(function (buf) {
            // `buf` is the raw .sqlite3 bytes.
            // Hand off to whatever SQL-in-JS library you're using.
        });
});
</script>
```

[Optional Trailing Data](#optional-trailing-data "Link to section: § 'Optional Trailing Data'")
-----------------------------------------------------------------------------------------------

The appended tarball can itself be followed by additional arbitrary binary assets, which can be large since they will usually not be downloaded. (While the exact format of each appended file is up to the users, it’s a good idea to wrap them in tarballs if you can.)

This flexibility is intended primarily for allowing ad hoc metadata extensions like [cryptographic signatures](https://en.wikipedia.org/wiki/Cryptographic_signatures "Cryptographic signatures") or forward error correction ([FEC](https://en.wikipedia.org/wiki/Error_correction_code "Error correction code § Forward error correction")).

### [FEC](#fec "Link to section: § 'FEC'")

The Gwern.net generation script uses this feature to add [par2](https://en.wikipedia.org/wiki/Par2 "Par2") FEC in an additional tarball.[4](#fn4) This allows recovery of the original Gwtar if it has been partially corrupted or lost. (It cannot recover loss of the file as a whole, which is why FEC is ideally done over large corpuses, and not individual files, but this is better than nothing, and gives us free integrity checking as well.)

PAR2 can find its FEC data even in corrupted files by scanning for FEC data (“packets”) it recognizes, while tar ignores appended data; so adding, say, 25% par2 FEC is as simple as running `par2create -r25 -n1 foo.gwtar.html && tar cf. - foo.gwtar.html.par2 foo.gwtar.html.vol*.par2 >> foo.gwtar.html && rm foo.gwtar.html*.par2`, and repairing a corrupted file is as simple as `ln --symbolic broken.gwtar.html broken.gwtar.html.par2 && par2repair broken.gwtar.html.par2 broken.gwtar.html`.[5](#fn5)

This yields the original `foo.gwtar.html` without any FEC. A repaired Gwtar file can then have fresh FEC added to be just like the old Gwtar + FEC archive, or be integrated in some broader system which achieves long-term protection some other way.

### [Signing](#signing "Link to section: § 'Signing'")

A simple form of cryptographic signing would be to use GPG to sign it as a normal, separate, signature file (creates `foo.gwtar.html.sig`): `gpg --detach-sign --armor foo.gwtar.html`.

And we could also append an ASCII ‘armored’ GPG signature, as it won’t confuse tar, like `gpg --detach-sign --armor foo.gwtar.html >> foo.gwtar.html`. Since GPG won’t munge a file like PAR2 will, an adhoc format would be to wrap it in tar to assist extracting:

```
gpg --detach-sign --armor foo.gwtar.html
tar cf. - foo.gwtar.html.sig >> foo.gwtar.html
rm foo.gwtar.html.sig
```

or in magic text, like a HTML comment:

```
# sign and append
FILE="foo.gwtar.html"
gpg --detach-sign --armor -o "$FILE".asc "$FILE"
echo '<!-- GWTAR-GPG-SIG' >> "$FILE"
cat "$FILE".asc >> "$FILE"
echo '-->' >> "$FILE"
rm "$FILE".asc

# Extract and verify:
SIG=$(mktemp XXXXXX.asc)
CONTENT=$(mktemp)
sed --quiet '/<!-- GWTAR-GPG-SIG/,/-->$/p' "$FILE" |
    grep -Ev 'GWTAR-GPG-SIG|-->' > "$SIG"
sed '/<!-- GWTAR-GPG-SIG/,$d' "$FILE" > "$CONTENT"
gpg --verify "$SIG" "$CONTENT"
rm "$SIG" "$CONTENT"
```

[Metadata](#metadata "Link to section: § 'Metadata'")
=====================================================

A Gwtar is served with a `text/html` mime-type. If necessary to [work around broken services like Cloudflare](#cloudflare-is-broken), its mime-type is `x-gwtar`.

[IP](#ip "Link to section: § 'IP'")
===================================

This documentation and the Gwtar code is licensed under the [CC-0](https://creativecommons.org/public-domain/cc0/ "‘CC-0: Creative Commons public domain license’, Commons 2002") public domain copyright license. We are unaware of any software patents.

[Further Work](#further-work "Link to section: § 'Further Work'")
=================================================================

Gwtar v1 could be improved with:

1. Validation tool
2. Checking of hashsums when rendering (possibly async or deferred)
3. More aggressive prefetching of assets
4. Integration into SingleFile (possibly as a “SingleFileZ2” forma?)
5. Testing: corpus of edge-case test files (inline SVG, `srcset`, CSS `@import` chains, web fonts, data URIs in CSS…)

A Gwtar v2 could add breaking changes like:

1. format provides more rigorous validation/checking of HTML & assets; require HTML & asset validity, assets all decode successfully, etc.
2. standardize appending formats
3. require FEC
4. built-in compression with Brotli/gzip for formats not already compressed
5. multi-page support

   One would try to replace MAFF’s capability of creating sets of documents which are convenient to link/archive and can automatically share assets for de-duplication (eg. page selected by a built-in widget, or perhaps by a hash-anchor like `archive.gwtar.html#page=foo.html`? Can an initial web page open new tabs of all the other web pages in the archive?)
6. Better de-duplication, eg. content-addressed asset names (hash-based) enabling deduplication across multiple gwtars

[External Links](#external-links "Link to section: § 'External Links'")
=======================================================================

* Discussion: [HN](/doc/www/news.ycombinator.com/9623fc5666282318255110ae91a783247c3dfacf.html "Gwtar: A static efficient single-file HTML format")

---

1. Gwtar may at some point try to check hash integrity during viewing; they are currently provided for forwards-compatibility and offline integrity-checking. We use SHA-256 specifically because it is familiar, easy to use on the commandline or in JavaScript, my default hash, provides long-term security, and is fast enough to never plausibly be a bottleneck in the Gwtar context.[↩︎](#fnref1)
2. A server I increasingly regret using on Gwern.net rather than Apache, as it seems nothing is ever simple or sane in it.[↩︎](#fnref2)
3. Or if that doesn’t work, perhaps a `<img>` tag combined with a zero width/height size so readers don’t see a broken image placeholder. (Use of `display: none` risks browsers/SingleFile deciding that it can be omitted entirely.)[↩︎](#fnref3)
4. Strictly speaking, the tarball wrapper is unnecessary because par2 can scan & repair inside arbitrary bitstreams (see [example command](#par2-repair)), but it’s tidier and friendlier.[↩︎](#fnref4)
5. A longer demonstration of using PAR2:

   ```
   mkdir -p ./tmp && cd ./tmp

   wget 'https://gwern.net/doc/philosophy/religion/1999-03-17-brianmoriarty-whoburiedpaul.gwtar.html'
   cp 1999-03-17-brianmoriarty-whoburiedpaul.gwtar.html archive.gwtar

   ## record size + hash of the protected payload
   ORIGSIZE=$(stat -c %s archive.gwtar)
   sha256sum archive.gwtar > archive.gwtar.sha256

   ## create 25% redundancy for 'archive.gwtar'
   par2create -r25 archive.gwtar
   tar cf. archive.gwtar.par2 archive.gwtar.vol*.par2

   ## build one-file carrier (payload + tarball of par2 packets)
   cat archive.gwtar archive.gwtar.par2 > archive.withfec.html

   ## simulate "only the one-file carrier survived"
   rm -f archive.gwtar archive.gwtar.par2 archive.gwtar.vol*.par2

   ## corrupt some bytes in the protected region only (0..ORIGSIZE−1)
   cp archive.withfec.html broken.html
   for i in {1..32}; do
     OFFSET=$(( (RANDOM << 15 | RANDOM) % ORIGSIZE ))
     printf '\x00' | dd of=broken.html bs=1 seek="$OFFSET" count=1 conv=notrunc status=none
   done

   ## IMPORTANT: give par2repair (1) a .par2 filename, (2) an extra file to scan
   ln -sf broken.html broken.html.par2
   par2repair broken.html.par2 broken.html

   # Loading "broken.html.par2".
   # Loaded 503 new packets including 499 recovery blocks
   # Loading "broken.html.par2".
   # No new packets found
   #
   # There are 1 recoverable files and 0 other files.
   # The block size used was 2472 bytes.
   # There are a total of 1997 data blocks.
   # The total size of the data files is 4936480 bytes.
   #
   # Verifying source files:
   #
   # Target: "archive.gwtar" - missing.
   #
   # Scanning extra files:
   #
   # Opening: "broken.html"
   # File: "broken.html" - found 1968 of 1997 data blocks from "archive.gwtar".
   #
   # Repair is required.
   # 1 file(s) are missing.
   # You have 1968 out of 1997 data blocks available.
   # You have 499 recovery blocks available.
   # Repair is possible.
   # You have an excess of 470 recovery blocks.
   # 29 recovery blocks will be used to repair.
   #
   # Computing Reed Solomon matrix.
   # Constructing: done.
   # Solving: done.
   #
   # Wrote 4936480 bytes to disk
   #
   # Verifying repaired files:
   #
   # Opening: "archive.gwtar"
   # Target: "archive.gwtar" - found.
   #
   # Repair complete.

   ## verify reconstructed file
   sha256sum -c archive.gwtar.sha256
   # archive.gwtar: OK
   ```

   [↩︎](#fnref5)

[Similar Links](#similars-section "Link to section: § 'Similar Links'")
=======================================================================

[[Similar links by topic]](/metadata/annotation/similar/%252Fgwtar.html "Similar links for this link (by text embedding). Lazily-transcluded version at footer of page for easier scrolling.")

[Bibliography](#link-bibliography-section "Link to section: § 'Bibliography'")
==============================================================================

[[Bibliography of links/references used in page]](/metadata/annotation/link-bibliography/%252Fgwtar.html "Bibliography of links cited in this page (forward citations). Lazily-transcluded version at footer of page for easier scrolling.")
