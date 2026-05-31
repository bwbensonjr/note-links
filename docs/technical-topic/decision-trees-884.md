---
id: 884
url: https://mlu-explain.github.io/decision-tree/
title: Decision Trees
domain: mlu-explain.github.io
source_date: '2026-03-01'
tags:
- ai
- tutorial
summary: Decision Trees are machine learning models that classify data by recursively
  splitting it into regions based on feature values. The algorithm creates nested
  decision rules by partitioning data to separate different classes, but must balance
  accuracy with generalization by avoiding overfitting through excessive splitting.
  Once trained, a Decision Tree can quickly classify new data points by passing them
  through the learned sequence of decisions.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# Decision Trees

MLU-explAIn
-----------

Decision Trees
==============

The unreasonable power of nested decision rules.

By [Jared Wilber](https://twitter.com/jdwlbr) & [Lucía Santamaría](https://twitter.com/lusantala)

Let's Build a Decision Tree
---------------------------

Let's pretend we're farmers with a new plot of land. Given only the Diameter and Height of a tree trunk, we must determine if it's an Apple, Cherry, or Oak tree. To do this, we'll use a Decision Tree.

Start Splitting
---------------

Almost every tree with a Diameter ≥ 0.45 is an Oak tree! Thus, we can probably assume that any other trees we find in that region will also be one.   
  
This first decision node will act as our root node. We'll draw a vertical line at this Diameter and classify everything above it as Oak (our first leaf node), and continue to partition our remaining data on the left.

Split Some More
---------------

We continue along, hoping to split our plot of land in the most favorable manner. We see that creating a new decision node at Height ≤ 4.88 leads to a nice section of Cherry trees, so we partition our data there.   
  
 Our Decision Tree updates accordingly, adding a new leaf node for Cherry.

And Some More
-------------

After this second split we're left with an area containing many Apple and some Cherry trees. No problem: a vertical division can be drawn to separate the Apple trees a bit better.   
  
Once again, our Decision Tree updates accordingly.

And Yet Some More
-----------------

The remaining region just needs a further horizontal division and boom - our job is done! We've obtained an optimal set of nested decisions.   
  
 That said, some regions still enclose a few misclassified points. Should we continue splitting, partitioning into smaller sections?   
  
 Hmm...

Don't Go Too Deep!
------------------

If we do, the resulting regions would start becoming increasingly complex, and our tree would become unreasonably deep. Such a Decision Tree would learn too much from the noise of the training examples and not enough generalizable rules.   
  
 Does this ring familiar? It is the well known tradeoff that we have explored in our explainer on [The Bias Variance Tradeoff](https://mlu-explain.github.io/bias-variance/)! In this case, going too deep results in a tree that overfits our data, so we'll stop here.   
  
 We're done! We can simply pass any new data point's Height and Diameter values through the newly created Decision Tree to classify them as either an Apple, Cherry, or Oak tree!
