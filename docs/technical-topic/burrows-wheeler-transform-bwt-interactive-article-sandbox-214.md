---
id: 214
url: https://sandbox.bio/concepts/bwt
title: Burrows-Wheeler Transform (BWT) - Interactive article - sandbox.bio
domain: sandbox.bio
source_date: '2025-10-10'
tags:
- tutorial
- compilers
- biology
summary: The Burrows-Wheeler Transform (BWT) is a data transformation algorithm that
  works by generating all rotations of a string, sorting them lexicographically, and
  extracting the last column of the sorted matrix. This technique is particularly
  useful for data compression and DNA sequence analysis because it rearranges characters
  in a way that groups similar characters together, making the data more compressible.
  The interactive example demonstrates how "banana$" is transformed through rotation
  and sorting to produce the BWT output.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# Burrows-Wheeler Transform (BWT) - Interactive article - sandbox.bio

Write down all rotations b a n a n a $ a n a n a $ b n a n a $ b a a n a $ b a n n a $ b a n a a $ b a n a n $ b a n a n a Sort strings (row-wise) $ b a n a n a a $ b a n a n a n a $ b a n a n a n a $ b b a n a n a $ n a $ b a n a n a n a $ b a The BWT is the last column a n n b $ a a
