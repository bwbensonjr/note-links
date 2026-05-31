---
id: 240
url: https://sethmlarson.dev/scream-cipher
title: SCREAM CIPHER (“ǠĂȦẶAẦ ĂǍÄẴẶȦ”) — Seth Larson
domain: sethmlarson.dev
source_date: '2025-09-20'
tags:
- security
- tutorial
summary: Seth Larson presents the "scream cipher," a humorous encryption method that
  exploits the abundance of Unicode variations of the Latin letter "A" to create a
  substitution cipher. The cipher maps each English letter to a visually similar accented
  or modified "A" character, allowing text like "SCREAM CIPHER" to be encoded as "ǠĂȦẶAẦ
  ĂǍÄẴẶȦ" and vice versa. It's a playful exploration of Unicode's extensive character
  set rather than a serious cryptographic tool.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# SCREAM CIPHER (“ǠĂȦẶAẦ ĂǍÄẴẶȦ”) — Seth Larson

[Blog](/) :
[About](/about) :
[RSS](/feed) :
[Blogroll](/blogroll)

SCREAM CIPHER (“ǠĂȦẶAẦ ĂǍÄẴẶȦ”)
===============================

Seth Larson @ 2025-09-13

You've probably heard of [stream ciphers](https://en.wikipedia.org/wiki/Stream_cipher), but what about a *scream cipher* 😱?
Today I learned there are more “[Latin capital letter A](https://utf8.xyz/latin-capital-letter-a-)”
Unicode characters than there are letters in the English alphabet. You know what that means, it's time to scream:

```
CIPHER = {
"A":"A",  # Round-trip!
"B":"Á","G":"Ẳ","L":"Ậ","Q":"Ǟ","V":"À",
"C":"Ă","H":"Ẵ","M":"Ầ","R":"Ȧ","W":"Ả",
"D":"Ắ","I":"Ǎ","N":"Ẩ","S":"Ǡ","X":"Ȃ",
"E":"Ặ","J":"Â","O":"Ẫ","T":"Ạ","Y":"Ā",
"F":"Ằ","K":"Ấ","P":"Ä","U":"Ȁ","Z":"Ą",
}
CIPHER.update({map(str.lower, kv) for kv in CIPHER.items()})
UNCIPHER = {v: k for k, v in CIPHER.items()}

def SCREAM(text: str) -> str:
    return "".join(CIPHER.get(ch, ch) for ch in text)

def unscream(scream: str) -> str:
    return "".join(UNCIPHER.get(ch, ch) for ch in scream)


print(s := SCREAM("SCREAM CIPHER"))
# ǠĂȦẶAẦ ĂǍÄẴẶȦ

print(unscream(s))
# SCREAM CIPHER
```

> ***Wow, you made it to the end!***
>   
>
> * Share your thoughts with me on [Mastodon](https://mastodon.social/@sethmlarson), [email](mailto:sethmichaellarson@gmail.com), or [Bluesky](https://bsky.app/profile/sethmlarson.dev).
> * Browse this [blog’s archive](/) of 181 entries.
> * Check out this [list of cool stuff](/blogroll) I found on the internet.
> * Follow this blog on [RSS](/feed) or the [email newsletter](https://buttondown.email/sethmlarson).
> * Go outside (best option)
