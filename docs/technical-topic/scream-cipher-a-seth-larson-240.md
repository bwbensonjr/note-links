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

Blog : About : RSS : Blogroll SCREAM CIPHER (“ǠĂȦẶAẦ ĂǍÄẴẶȦ”) Seth Larson @ 2025-09-13 You've probably heard of stream ciphers , but what about a scream cipher 😱? Today I learned there are more “ Latin capital letter A ” Unicode characters than there are letters in the English alphabet. You know what that means, it's time to scream: CIPHER = { "A" : "A" , # Round-trip! "B" : "Á" , "G" : "Ẳ" , "L" : "Ậ" , "Q" : "Ǟ" , "V" : "À" , "C" : "Ă" , "H" : "Ẵ" , "M" : "Ầ" , "R" : "Ȧ" , "W" : "Ả" , "D" : "Ắ" , "I" : "Ǎ" , "N" : "Ẩ" , "S" : "Ǡ" , "X" : "Ȃ" , "E" : "Ặ" , "J" : "Â" , "O" : "Ẫ" , "T" : "Ạ" , "Y" : "Ā" , "F" : "Ằ" , "K" : "Ấ" , "P" : "Ä" , "U" : "Ȁ" , "Z" : "Ą" , } CIPHER . update ({ map ( str . lower , kv ) for kv in CIPHER . items ()}) UNCIPHER = { v : k for k , v in CIPHER . items ()} def SCREAM ( text : str ) -> str : return "" . join ( CIPHER . get ( ch , ch ) for ch in text ) def unscream ( scream : str ) -> str : return "" . join ( UNCIPHER . get ( ch , ch ) for ch in scream ) print ( s := SCREAM ( "SCREAM CIPHER" )) # ǠĂȦẶAẦ ĂǍÄẴẶȦ print ( unscream ( s )) # SCREAM CIPHER Wow, you made it to the end! Share your thoughts with me on Mastodon , email , or Bluesky . Browse this blog’s archive of 160 entries. Check out this list of cool stuff I found on the internet. Follow this blog on RSS or the email newsletter . Go outside (best option)
