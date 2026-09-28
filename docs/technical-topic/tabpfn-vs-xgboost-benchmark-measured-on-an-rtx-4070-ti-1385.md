---
id: 1385
url: https://efraingaray.com/en/blog/tabpfn-vs-xgboost/
title: 'TabPFN vs XGBoost: benchmark measured on an RTX 4070 Ti'
domain: efraingaray.com
source_date: '2026-09-28'
tags:
- ai
- llm
- python
- tutorial
summary: TabPFN and TabICL, tabular foundation models that use in-context learning
  to make predictions without training on data, outperformed tuned XGBoost on 14 out
  of 14 benchmark datasets by making predictions in a single forward pass with only
  data copied to GPU rather than gradient descent optimization. The models reverse
  traditional machine learning economics by making fitting nearly free and prediction
  costly, though TabPFN showed weaknesses on high-dimensional tables with many columns.
  This benchmark challenges conventional practice by suggesting that hyperparameter
  tuning may no longer be necessary for competitive tabular prediction performance.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# TabPFN vs XGBoost: benchmark measured on an RTX 4070 Ti

![Portada del artículo: TabPFN and TabICL against tuned XGBoost: the model that does not train won on fourteen tables out of fourteen](/media/og/og-tablas.png)

ModelsBenchmarksGPUData

TabPFN and TabICL against tuned XGBoost: the model that does not train won on fourteen tables out of fourteen
=============================================================================================================

The claim behind TabPFN and TabICL is that they predict on a table without ever training on it and still beat tuned boosting. I measured it on fourteen datasets from the Grinsztajn benchmark, with the same split and the same clock for everyone. The one that does not train wins, the advantage holds up to 32,000 rows instead of breaking, and the most-cited model can no longer be downloaded without an account.

Efrain Garay 17 August 2026 18 August 2026

Listen to the summary0:00Playing summary

The claim has been going around for months and it is concrete enough to be measurable: a tabular foundation model predicts on a table **without ever having trained on it** and still beats tuned boosting.

If that is true, half a decade of practice changes shape. Searching hyperparameters stops being a mandatory step and becomes a luxury that sometimes does not pay off.

So I put it to the test on my own card, with fourteen datasets, four contenders and the same stopwatch for everyone.

[![Your browser does not support HTML5 video.](/media/tablas-reel-poster.jpg)](/media/tablas-reel-en.mp4)

In 33 seconds with narration: two bots compete over a table. The one-eyed one looks and answers; the geared one tries twenty-five combinations before replying. Every number is a measured one. Muted by default: turn it on in the controls.[Watch it in the reel viewer →](/en/reels/tabpfn-vs-xgboost/)

What exactly these models do
----------------------------

A tabular foundation model is pretrained on millions of synthetic tables generated on purpose. When a new table arrives, it does not adjust a single weight: it receives the training rows **as context** and produces the predictions in one forward pass.

It is the same in-context learning idea we already know from language models, moved from words to columns. That is why the verb “train” sits oddly: the code still calls it `fit`, but inside there is no gradient descent, there is a copy of data to the card.

That also explains why the cost shows up where you do not expect it. Fitting is nearly free and **prediction** is what pays, exactly the reverse of a tree.

Put that way it sounds abstract, so here is the full journey of one row: a request arrives with an empty cell, the model weighs it against everything that already happened, resolves it in one pass and returns a future. Pick any of the six cases I measured to see it with their real data:

Default riskSales campaignClinical readmissionRecidivismElectricity demandMolecular screening

?

The request

The context

A single pass

The prediction

A credit application arrives

2 100 applications already settled · 10 columns  
`clf_num/credit.csv`

TabICL · nothing tuned · **0.8 s**

Will they repay?

repaysdefaults

AUC **0.8528**  
credit

A contact enters the list

2 100 calls already made · 7 columns  
`clf_num/bank-marketing.csv`

TabICL · nothing tuned · **0.8 s**

Is it worth calling them?

signs updoes not

AUC **0.8699**  
bank-marketing

A patient is discharged

2 100 previous discharges · 7 columns  
`clf_num/Diabetes130US.csv`

TabICL · nothing tuned · **0.8 s**

Will they be readmitted?

returnsdoes not

AUC **0.6484**  
Diabetes130US

A case is assessed

2 100 cases already closed · 11 columns  
`clf_cat/compas-two-years.csv`

TabICL · nothing tuned · **0.6 s**

Will they reoffend?

reoffendsdoes not

AUC **0.7329**  
compas-two-years

A market period closes

2 100 previous periods · 7 columns  
`clf_num/electricity.csv`

TabICL · nothing tuned · **0.8 s**

Does the price go up or down?

updown

AUC **0.8873**  
electricity

A candidate molecule arrives

2 100 molecules already assayed · 419 columns  
`clf_num/Bioresponse.csv`

TabICL · nothing tuned · **6.0 s**

Does it trigger a biological response?

activeinert

AUC **0.8667**  
Bioresponse

?

The request

The context

A single pass

The prediction

A credit application arrives

2 100 applications already settled · 10 columns  
`clf_num/credit.csv`

TabICL · nothing tuned · **0.8 s**

Will they repay?

repaysdefaults

AUC **0.8528**  
credit

A contact enters the list

2 100 calls already made · 7 columns  
`clf_num/bank-marketing.csv`

TabICL · nothing tuned · **0.8 s**

Is it worth calling them?

signs updoes not

AUC **0.8699**  
bank-marketing

A patient is discharged

2 100 previous discharges · 7 columns  
`clf_num/Diabetes130US.csv`

TabICL · nothing tuned · **0.8 s**

Will they be readmitted?

returnsdoes not

AUC **0.6484**  
Diabetes130US

A case is assessed

2 100 cases already closed · 11 columns  
`clf_cat/compas-two-years.csv`

TabICL · nothing tuned · **0.6 s**

Will they reoffend?

reoffendsdoes not

AUC **0.7329**  
compas-two-years

A market period closes

2 100 previous periods · 7 columns  
`clf_num/electricity.csv`

TabICL · nothing tuned · **0.8 s**

Does the price go up or down?

updown

AUC **0.8873**  
electricity

A candidate molecule arrives

2 100 molecules already assayed · 419 columns  
`clf_num/Bioresponse.csv`

TabICL · nothing tuned · **6.0 s**

Does it trigger a biological response?

activeinert

AUC **0.8667**  
Bioresponse

Banking’s most repeated case: deciding who gets lent to.

| dataset | size | TabICL | TabPFN | tuned XGB |
| --- | --- | --- | --- | --- |
| credit | 3000 × 10 | 0.7667 | 0.7578 | 0.7533 |
| heloc | 3000 × 22 | 0.7222 | 0.7300 | 0.7078 |
| default-of-credit | 3000 × 20 | 0.6956 | 0.6967 | 0.6944 |

All three datasets go to the foundation model. On heloc TabPFN takes 0.022 and TabICL 0.014: in credit risk that is not decoration.

Context: [`clf_num/credit.csv`](https://huggingface.co/datasets/inria-soda/tabular-benchmark/resolve/main/clf_num/credit.csv) from the [inria-soda/tabular-benchmark](https://huggingface.co/datasets/inria-soda/tabular-benchmark/tree/main) suite, trimmed to 3,000 rows with seed 0 and split 70/30 with stratification.  
sha256 `22a759296600c39a56884dafd84eb346be018c537ff096adc8c2ae7e0520f2a9`

Who to call first when there are a thousand contacts and time for a hundred.

| dataset | size | TabICL | TabPFN | tuned XGB |
| --- | --- | --- | --- | --- |
| bank-marketing | 3000 × 7 | 0.7944 | 0.7967 | 0.7833 |

The only case where TabPFN ends up ahead of TabICL. Both beat tuned boosting.

Context: [`clf_num/bank-marketing.csv`](https://huggingface.co/datasets/inria-soda/tabular-benchmark/resolve/main/clf_num/bank-marketing.csv) from the [inria-soda/tabular-benchmark](https://huggingface.co/datasets/inria-soda/tabular-benchmark/tree/main) suite, trimmed to 3,000 rows with seed 0 and split 70/30 with stratification.  
sha256 `3433fecd416ce949692442882669881746e8a6b24b904a5f808cdcb196443e7e`

A real hospital record: which patient gets readmitted.

| dataset | size | TabICL | TabPFN | tuned XGB |
| --- | --- | --- | --- | --- |
| Diabetes130US | 3000 × 7 | 0.5911 | 0.5933 | 0.5900 |

On accuracy they nearly tie, but the area under the curve opens up sharply: 0.6484 against 0.6264. The risk ordering, which is what a triage uses, improves considerably more than accuracy suggests.

Context: [`clf_num/Diabetes130US.csv`](https://huggingface.co/datasets/inria-soda/tabular-benchmark/resolve/main/clf_num/Diabetes130US.csv) from the [inria-soda/tabular-benchmark](https://huggingface.co/datasets/inria-soda/tabular-benchmark/tree/main) suite, trimmed to 3,000 rows with seed 0 and split 70/30 with stratification.  
sha256 `9be384ad7edbb9a98b509adb9cc08578e63bd87545b05d97d5147aa15b71385a`

The dataset that opened the debate on algorithmic bias in the courts.

| dataset | size | TabICL | TabPFN | tuned XGB |
| --- | --- | --- | --- | --- |
| compas-two-years | 3000 × 11 | 0.6733 | 0.6767 | 0.6700 |

The foundation model wins, and it is worth saying that a better model here does not make the use legitimate: this dataset’s argument was never about accuracy.

Context: [`clf_cat/compas-two-years.csv`](https://huggingface.co/datasets/inria-soda/tabular-benchmark/resolve/main/clf_cat/compas-two-years.csv) from the [inria-soda/tabular-benchmark](https://huggingface.co/datasets/inria-soda/tabular-benchmark/tree/main) suite, trimmed to 3,000 rows with seed 0 and split 70/30 with stratification.  
sha256 `7e0bcef09ae633ad81e26b0a8f8f96dbc4ac3c29b9da0760d38ef2a75adde8d8`

Consumption and price series from an electricity market.

| dataset | size | TabICL | TabPFN | tuned XGB |
| --- | --- | --- | --- | --- |
| electricity | 3000 × 7 | 0.8178 | 0.8111 | 0.8178 |

The tie. TabICL matches tuned boosting to the fourth decimal and TabPFN falls below. It is one of the two cases where the advantage does not show up.

Context: [`clf_num/electricity.csv`](https://huggingface.co/datasets/inria-soda/tabular-benchmark/resolve/main/clf_num/electricity.csv) from the [inria-soda/tabular-benchmark](https://huggingface.co/datasets/inria-soda/tabular-benchmark/tree/main) suite, trimmed to 3,000 rows with seed 0 and split 70/30 with stratification.  
sha256 `d6005007c4b1f7ba88cf91cb1f231969cce3e49c98d445338c0ab0342ead5d7e`

419 columns of chemical descriptors: the wide table.

| dataset | size | TabICL | TabPFN | tuned XGB |
| --- | --- | --- | --- | --- |
| Bioresponse | 3000 × 419 | 0.7922 | 0.7567 | 0.7744 |

This is where TabPFN breaks: 0.7567 is worse than even untuned XGBoost, and it costs 18.1 seconds. TabICL holds up and comes first. The table’s width, not its length, is what squeezes.

Context: [`clf_num/Bioresponse.csv`](https://huggingface.co/datasets/inria-soda/tabular-benchmark/resolve/main/clf_num/Bioresponse.csv) from the [inria-soda/tabular-benchmark](https://huggingface.co/datasets/inria-soda/tabular-benchmark/tree/main) suite, trimmed to 3,000 rows with seed 0 and split 70/30 with stratification.  
sha256 `bd3d277821eb949df41219363f0386549019249776fccf7a9f08d3bec10b8727`

Pick a case above to follow one row’s journey. The context is the 2 100 training rows, the time is the one TabICL measured, and the orb’s arc draws that dataset’s area under the curve, from chance to a perfect score.

What this is for, concretely
----------------------------

The six cases in the diagram are not brochure examples: they are the datasets I measured with. But it is worth widening the map, because “tabular foundation model” sounds like a laboratory and the problem it solves is one of the most common there is.

A table is a spreadsheet: rows that are cases and columns that are attributes. And the task is always the same, **predict one column from the others**:

* A customer table with tenure, plan, usage and complaints, to estimate **which ones are going to leave next month**.
* A transaction log with amount, merchant, hour and country, to flag **which ones are fraud**.
* A history of credit applications with income, debt and payment behaviour, to estimate **who is not going to repay**. Three of the datasets I measured are exactly that: `credit`, `heloc` and `default-of-credit`.
* Sensor readings from a machine, to anticipate **when it is going to break**.
* Patient records with symptoms and lab results, to prioritize **who gets seen first**. `Diabetes130US`, another of the datasets, is a real hospital record.

That is half the data work done in any company. It is also the ground where deep learning had been losing for years: for tables, a good gradient-boosted tree ensemble was still the right answer, and the research that assembled these datasets was titled exactly that way, asking why trees still won.

### What changes if the promise holds

Today, solving any of those cases has a ritual: prepare the data, choose a model, **search hyperparameters**, validate, repeat. The search is the boring part and the one that eats machine and human hours. In this benchmark, XGBoost’s search took up to 50 seconds per dataset; on a real problem with more rows and more combinations, it is minutes or hours.

A tabular foundation model proposes skipping that ritual entirely. You hand it the table, it answers in a second, and that is that. No tree depth to choose, no learning rate, no cross-validation to decide among twenty-five candidates.

Put in concrete terms: instead of spending the afternoon tuning a churn model, you have an answer in the time it takes to make coffee, and only then do you decide whether anything is worth refining. For exploring a table that just arrived, or for having an honest baseline before investing time, it is hard to beat.

The question, then, is not whether the idea is attractive. It is whether the result holds up when measured.

The benchmark’s rules
---------------------

A badly built benchmark says whatever you want. These are the rules I imposed on myself before seeing a single number:

**The data is third-party and from the field where this argument is fought.** I used Grinsztajn’s tabular benchmark, the suite gathered for the work asking why trees still beat deep learning on tables. Choosing the datasets yourself is the easiest way to manufacture the result you like.

**XGBoost goes in tuned, not for decoration.** The claim says “tuned boosting”, so comparing against factory parameters would be a straw man. I ran two versions: one with fixed, reasonable parameters and another with a random search over twenty-five combinations and three-fold cross-validation.

**Same split, same seed, same columns for everyone.** Categoricals are integer-encoded. It is not the best possible treatment, but it is identical for all four, which is what makes the number comparable.

**Five seeds per dataset, and the median is reported.** A single split cannot tell signal from luck.

**Prediction time includes two inference passes**, the class one and the probability one, because the benchmark needs both to compute accuracy and area under the curve. That makes things more expensive precisely for the foundation models, which is where their cost lives, so the seconds I publish for them are inflated in nobody’s favour.

**Two cores are left free.** The machine has other work on it, and a benchmark that eats the whole CPU measures the fight with the scheduler, not the model.

Everything ran on a 16 GB RTX 4070 Ti SUPER, with fourteen cores for XGBoost.

Three stumbles before the first number
--------------------------------------

Publishing only the final table would be lying by omission. This is what it cost to get there.

### PyTorch turned the GPU off without saying so

I set up the environment, ran the benchmark, and the first line said `device: cpu`. The card was free and visible. The reason:

```
2.13.0+cu130   driver 570.144   torch.cuda.is_available() → False
```

PyTorch had resolved to a build for CUDA 13.0 while the machine’s driver exposes 12.8. Instead of failing, **it silently turns the GPU off** and carries on with the CPU. The warning only shows up if you inspect `torch.cuda.is_available()` by hand.

It is fixed by pinning the version to the right index:

```
pip install --no-cache-dir \
  --index-url https://download.pytorch.org/whl/cu128 torch==2.9.1+cu128
```

This is the second time this year the same trap has cost me a whole run. If a GPU benchmark gives suspiciously slow numbers, that is the first place to look.

### OpenML’s API returned 504 on every endpoint

The original plan was to take the datasets from OpenML, which is the canonical source for these comparisons. It failed completely during the run:

```
https://api.openml.org/api/v1/json/data/31          → 504 (16.9 s)
https://www.openml.org/api/v1/json/data/31          → 504 (15.7 s)
https://api.openml.org/api/v1/json/data/features/31 → 504 (16.5 s)
```

Four retries with growing backoff made no difference: it was not a rate problem, it was the gateway being down. I switched the source to the same benchmark’s CSVs hosted on HuggingFace, which resolved in 250 milliseconds. It is an uncomfortable reminder of how much reproducible research depends on a single service.

### The most-cited model no longer downloads without an account

This is the finding that interests me most, because it is not technical.

TabPFN is the name that appears in nearly all coverage of this topic. I installed the current version, 8.3.0, and on the first `fit`:

```
TabPFNLicenseError: TabPFN requires a one-time license acceptance
to download model weights for local inference, but no interactive
terminal is available.
```

To fetch the weights you have to open a browser, register, accept the license in a tab on the vendor’s site and export an account token. The best-known tabular foundation model stopped being something you install and run.

There are two ways out, and I tried both:

* **TabPFN’s 2.x series still downloads the weights without registering.** I installed 2.2.1 in a separate environment and it worked first try. That is the one in the tables below.
* **TabICL, from Inria’s Soda team, has a three-clause BSD license** and downloads with no barrier at all. It also turned out to be the better of the two.

![Illustration: a small lens-eyed robot facing a large geared machine, on a floor of spreadsheet cells.](/media/tablas/duelo.png)

The benchmark’s two contenders: on the left the one that just looks at the table and answers, on the right the one that spends half a minute trying combinations.

The numbers
-----------

Fourteen datasets, all trimmed to 3,000 rows so the comparison is homogeneous. Accuracy as the median of five seeds. The seconds column sums fitting and prediction, which is each one’s honest cost:

| dataset | rows × cols | TabICL | TabPFN 2.2.1 | XGBoost | Tuned XGB | s TabICL | s tuned XGB |
| --- | --- | --- | --- | --- | --- | --- | --- |
| bank-marketing | 3000 × 7 | 0.7944 | **0.7967** | 0.7711 | 0.7833 | 0.8 | 1.8 |
| credit | 3000 × 10 | **0.7667** | 0.7578 | 0.7478 | 0.7533 | 0.8 | 2.2 |
| heloc | 3000 × 22 | 0.7222 | **0.7300** | 0.7022 | 0.7078 | 0.8 | 1.6 |
| pol | 3000 × 26 | **0.9844** | 0.9833 | 0.9778 | 0.9756 | 0.8 | 1.0 |
| eye\_movements | 3000 × 20 | 0.6100 | **0.6111** | 0.5944 | 0.5833 | 0.8 | 3.0 |
| california | 3000 × 8 | 0.8967 | **0.8978** | 0.8833 | 0.8767 | 0.6 | 1.6 |
| house\_16H | 3000 × 16 | **0.8811** | 0.8744 | 0.8722 | 0.8711 | 1.1 | 3.0 |
| MagicTelescope | 3000 × 10 | **0.8778** | 0.8622 | 0.8489 | 0.8456 | 1.3 | 2.4 |
| electricity | 3000 × 7 | 0.8178 | 0.8111 | 0.8156 | **0.8178** | 0.8 | 2.4 |
| Diabetes130US | 3000 × 7 | 0.5911 | **0.5933** | 0.5644 | 0.5900 | 0.8 | 1.4 |
| default-of-credit | 3000 × 20 | 0.6956 | **0.6967** | 0.6878 | 0.6944 | 0.9 | 4.5 |
| compas-two-years | 3000 × 11 | 0.6733 | **0.6767** | 0.6444 | 0.6700 | 0.6 | 0.7 |
| Bioresponse | 3000 × 419 | **0.7922** | 0.7567 | 0.7844 | 0.7744 | 6.0 | 27.2 |
| albert | 3000 × 31 | 0.6500 | **0.6611** | 0.6511 | **0.6611** | 1.8 | 2.6 |

Against tuned XGBoost, by accuracy:

* **TabICL: twelve wins, one tie (electricity) and one loss (albert).** Mean difference +0.0106.
* **TabPFN 2.2.1: eleven wins, one tie (albert) and two losses** (electricity and Bioresponse). Mean difference +0.0075.

Accuracy, however, is a coarse metric: it depends on the threshold and punishes differently depending on how the classes are balanced. Area under the curve is more informative, and there the result gets sharper:

| model | AUC wins | mean difference |
| --- | --- | --- |
| TabICL | **14 of 14** | +0.0114 |
| TabPFN 2.2.1 | 13 of 14 | +0.0089 |

TabICL beats tuned XGBoost **on every dataset without exception**. Even on albert, where it loses on accuracy, it has a better AUC (0.7101 against 0.7094). That detail is exactly why both metrics are worth looking at: accuracy said “loss” where the probability ordering said “win by a hair”.

That said, the enthusiasm needs calibrating. Winning fourteen of fourteen is a strong signal of **consistency**, not of crushing superiority: the mean difference is one hundredth. Nobody is going to notice that on a dashboard. What does get noticed is the other thing.

The cost is the reverse of what you expect
------------------------------------------

Look again at the table’s last two columns. TabICL resolves a dataset in under a second **without tuning anything**. Tuned XGBoost takes between 0.7 and 27.2 seconds searching hyperparameters, and still comes out below.

That is the real argument, and it is not accuracy. It is that the expensive part of the work, the one that consumes human and machine time, simply disappears.

The surprise: the advantage does not break with size
----------------------------------------------------

This is where I expected to dismantle the promise. The standard objection to these models is that they only work on toy tables, because the training rows have to fit inside the transformer’s context.

I took jannis, which has 57,580 rows, and trimmed it to growing sizes. Three seeds per size:

| rows | TabICL | XGBoost | Tuned XGB | s TabICL | s tuned XGB |
| --- | --- | --- | --- | --- | --- |
| 500 | 0.7533 | **0.7733** | 0.7533 | 0.7 | 3.2 |
| 1,000 | **0.7733** | 0.7467 | 0.7533 | 0.9 | 4.9 |
| 2,000 | **0.7800** | 0.7583 | 0.7667 | 1.1 | 9.4 |
| 4,000 | **0.7817** | 0.7692 | 0.7725 | 1.8 | 21.1 |
| 8,000 | **0.7958** | 0.7658 | 0.7583 | 2.6 | 19.7 |
| 16,000 | **0.8090** | 0.7785 | 0.7852 | 5.3 | 34.6 |
| 32,000 | **0.8230** | 0.7894 | 0.7929 | 11.7 | 50.3 |

The advantage does not break, and at the large end it consolidates: +0.030 at 32,000 rows. And the split of times opens in the direction opposite to intuition: 11.7 seconds against 50.3.

It is worth saying precisely what grows and what does not, because the difference matters. What rises steadily is **TabICL’s absolute accuracy**: 0.7533, 0.7733, 0.7800, 0.7817, 0.7958, 0.8090, 0.8230, monotone across all seven measurements. The **advantage over XGBoost**, by contrast, is irregular: 0.000, +0.020, +0.013, +0.009, +0.038, +0.024, +0.030. It rises and falls.

And at 4,000 rows that +0.009 advantage is **smaller than the spread across the three seeds** (TabICL ranges from 0.768 to 0.799; tuned XGBoost from 0.758 to 0.790), so at that point it is indistinguishable from noise and I do not count it as a win.

Where it is solid is at the top: at 32,000 rows TabICL’s **worst** seed (0.8216) sits above XGBoost’s **best** (0.7950). There is no possible overlap there.

The only place XGBoost wins cleanly is the small end, at 500 rows, where the variability between seeds is so high that I would not bet anything on that difference.

If you were expecting, as I was, the curve to flip at some point, it does not do so here. You would have to go considerably higher to find it.

![Illustration: a robot straining to push an enormous wall of glowing data columns.](/media/tablas/ancha.png)

Bioresponse has 419 columns. The table’s length does not stop them; its width does.

Where they do break
-------------------

Bioresponse is the telltale dataset: 419 columns.

TabPFN 2.2.1 falls to 0.7567, the worst of the four contenders, below even untuned XGBoost. And it costs it 18.1 seconds, twenty-five times more than on a normal dataset. TabICL holds up much better (0.7922, the best of the four) but pays too: 6.0 seconds against the usual 0.8.

The reading is that the table’s width, not its length, is the axis that genuinely squeezes. That makes sense: the number of columns enters the transformer’s attention cost, and the synthetic pretraining covers tables of tens of columns well, not hundreds.

What this measurement does not say
----------------------------------

I would rather list the limits than pretend they do not exist:

* **Binary classification only.** I did not test regression or multiclass.
* **A 3,000-row ceiling in the main table.** The scale sweep reaches 32,000, but on a single dataset.
* **The hyperparameter search was twenty-five combinations.** More aggressive tuning would close part of the gap; how much, I do not know, because I did not measure it.
* **XGBoost’s search optimized accuracy, and afterwards I also compare by area under the curve.** Which means the “fourteen of fourteen on AUC” is against a boosting model that was not tuned for that metric. Tuning it for AUC would probably improve it there; I did not measure that.
* **Categoricals were integer-encoded for everyone.** Better treatment would favour XGBoost more than the others.
* **The encoding and null-filling were computed over the whole table, before splitting.** It is the same leak for all four models, so it does not change who wins, but it inflates everyone slightly and should not be done that way.
* **Several accuracy wins are smaller than the variation between seeds.** `Diabetes130US` is won by 0.0011 when the per-seed difference ranges from −0.011 to +0.049: there the sign depends on which seed comes up. The area-under-the-curve count does hold seed by seed; the accuracy one, on three or four datasets, does not.
* **The wide-table finding rests on a single dataset.** `Bioresponse` is the only one with hundreds of columns, so “width is what squeezes” is a hypothesis with one observation, not a rule.
* **The current version of TabPFN, 8.3.0, went unmeasured** because of the license barrier. TabPFN’s numbers are from 2.2.1, two series behind.
* **The CPU was shared** with other work on the machine. That affects XGBoost’s times more than the GPU’s, so if anything it plays against the foundation models in the timing comparison.

When I would use it and when not
--------------------------------

**I would use it** on any table between one thousand and thirty thousand rows with fewer than a hundred columns, where a person’s time is worth more than the last hundredth. A second of compute, zero tuning, and a result that in my measurement was consistently better. For an initial exploration it is hard to justify not doing it.

**I would not use it** on very wide tables, where it degrades and gets expensive. Nor in production without a GPU, nor where you need a small artifact that can be inspected and deployed in a lightweight container: a trained tree weighs kilobytes and runs anywhere, whereas here you have to load a transformer.

And if the criteria include being able to audit where the weights came from, today the answer is TabICL. Not for performance, though it was also the better of the two, but because it is the one you can still download and run without asking anyone’s permission.

---

*Measured on 16 August 2026 on a 16 GB RTX 4070 Ti SUPER, with torch 2.9.1+cu128, XGBoost 3.4.1, TabICL 2.1.1 and TabPFN 2.2.1. Data from the `inria-soda/tabular-benchmark` tabular suite. The main table took 585 seconds and the scale sweep 514.*

Sources
-------

* [Accurate predictions on small data with a tabular foundation model](https://www.nature.com/articles/s41586-024-08328-6), Hollmann et al., *Nature* 637 (2025). The TabPFN v2 paper, with the synthetic-table pretraining method the whole idea comes from.
* [TabPFN: A Transformer That Solves Small Tabular Classification Problems in a Second](https://arxiv.org/abs/2207.01848), arXiv:2207.01848. The original 2022 work, useful for seeing what changed between the first version and the current one.
* [TabICL: A Tabular Foundation Model for In-Context Learning on Large Data](https://arxiv.org/abs/2502.05564), arXiv:2502.05564. The model from Inria’s Soda team that won my measurement, with its proposal for scaling to large tables.
* [soda-inria/tabicl](https://github.com/soda-inria/tabicl). The implementation, three-clause BSD licensed: it downloads without registering.
* [PriorLabs/TabPFN](https://github.com/PriorLabs/TabPFN). TabPFN’s repository, where the license and account-token barrier introduced from series 8 onward is visible.
* [The scripts, seeds and raw results](https://gist.github.com/EfrainGaray/9811e47590d17bbe1e8ffaa01af460fe). The full bench to reproduce it: the main run and a second one with XGBoost’s search tuned for AUC, plus the size sweep. `python bench.py --modo tabla`.

Comments
--------

No comments yet. The first one is yours.
