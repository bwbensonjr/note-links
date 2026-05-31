---
id: 283
url: https://eli.thegreenplace.net/2025/reproducing-word2vec-with-jax/
title: Reproducing word2vec with JAX - Eli Bendersky's website
domain: eli.thegreenplace.net
source_date: '2025-08-18'
tags:
- ai
- tutorial
- python
- llm
summary: This article demonstrates how to reimplement the word2vec model—a foundational
  2013 machine learning technique for creating semantic word embeddings—using the
  JAX framework. The post explains how embeddings convert words into meaningful dense
  vectors for neural networks, describes the CBOW (Continuous Bag Of Words) architecture
  that predicts center words from context, and provides a clean JAX implementation
  with training code using the text8 dataset. Key takeaways include understanding
  embeddings as the bridge between symbolic words and semantic vector representations,
  and seeing how the relatively simple forward pass and loss computation can be efficiently
  implemented in modern JAX.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# Reproducing word2vec with JAX - Eli Bendersky's website

The word2vec model was proposed in a 2013 paper by Google researchers called
["Efficient Estimation of Word Representations in Vector Space"](https://arxiv.org/pdf/1301.3781),
and was further refined by additional papers from the same team. It kick-started
the modern use of *embeddings* - dense vector representation of words (and later
tokens) for language models.

Also, the code - with some instructions - [was made available openly](https://code.google.com/archive/p/word2vec/).
This post reproduces the word2vec results using JAX, and also talks about
reproducing it using the original C code (see the *Original word2vec code*
section for that).

Embeddings
----------

First, a brief introduction to embeddings.
Wikipedia has a good definition:

> In natural language processing, a word embedding is a representation of a
> word. The embedding is used in text analysis. Typically, the representation is a
> real-valued vector that encodes the meaning of the word in such a way that the
> words that are closer in the vector space are expected to be similar in meaning

Here's a framework that made sense to me when I was first learning about
embeddings many years ago:

* ML models and NNs specifically are all about vector math.
* Words in a human language (like English) are just sequences of characters
  with no semantic meaning (there's nothing in the word "dog" that conveys
  dog-ness any more than the same concept in other human languages). Also, words
  have different lengths which isn't convenient.
* To represent words as vectors, we typically use indices into a vocabulary;
  equivalently, this can be seen as a one-hot vector with the value at the
  correct vocabulary index being 1, and the rest 0.
* This latter vector representation has no semantic meaning either, because
  "Paris" and "France" will be as different from each other as "Paris" and
  "Armadillo". Also, these vectors are huge (a typical vocabulary can have
  tens of thousands of words, just for a single language!)
* Therefore, we need some magic to convert words into vectors that carry
  meaning.

Embeddings are that magic. They are dense vectors of floats - with typically
hundreds or thousands of elements, and serve as representations of these words
in high-dimensional space.

The word2vec CBOW architecture
------------------------------

The word2vec paper proposed two related architectures: CBOW (Continuous Bag Of
Words) and Continuous Skip Gram. The two are fairly similar, and in this post
I'm going to focus on CBOW.

The idea of the CBOW approach is to teach the model to predict a word from its
surrounding words. Here's an example with window size of four [[1]](#footnote-1):

![CBOW - showing word in center of window, with context words around](https://eli.thegreenplace.net/images/2025/word2vec-cbow.png)

The goal here is to have the model predict that "liberty" should be the word
in the middle, given the context words in peach-colored boxes. This is an
*unsupervised* model - it learns by consuming text, sliding its window word
by word over arbitrary amounts of (properly formatted and sanitized) input.

Concretely, the following diagram shows the model architecture; here are
the dimensions involved:

* B: batch (for computational efficiency, whole batches are processed together)
* V: vocabulary size (the number of unique words in our vocabulary)
* D: model depth (the size of the dense embedding vectors we're trying to learn)
* W: window size

![word2vec CBOW model architecture](https://eli.thegreenplace.net/images/2025/word2vec-arch.png)

Here's the flow of data in the forward pass:

* context is the context words for a given position. For example, in the
  sample diagram above the context would be of length 8. Each element is an
  integer representation of a word (its index into the vocabulary). Since
  we're processing batches, the shape of this array is (B,2W).
* The context *indexes* into a projection matrix P, which has the learned
  embedding per row - one for each word in the vocabulary. The result is
  projection with shape (B,2W,D). The first two dimensions remain the same
  (because we still have the same batch and window size), but every integer
  is replaced with the word's embedding - so an extra dimension is added.
* Next, a *mean* (arithmetic average) is taken across the window dimension.
  The embeddings of all the words in the window are averaged together. The
  result is (B,D) where each row is the average of the embeddings of 2W words.
* Finally, the *hidden* layer matrix H is used to map the dense
  representation back into a sparse one [[2]](#footnote-2) - this is the prediction of the middle
  word. Recall that this tries to predict a one-hot encoding of the word's
  vocabulary index.

For training, the loss is calculated by comparing out to the one-hot
encoding of the actual target word for this window, and the calculated gradient
is propagated backwards to train the model.

JAX implementation
------------------

The JAX implementation of the model described above is clean and compact:

```
@jax.jit
def word2vec_forward(params, context):
    """Forward pass of the word2Vec model.

    context is a (batch_size, 2*window_size) array of word IDs.

    V is the vocabulary size, D is the embedding dimension.
    params["projection"] is a (V, D) matrix of word embeddings.
    params["hidden"] is a (D, V) matrix of weights for the hidden layer.
    """
    # Indexing into (V, D) matrix with a batch of IDs. The output shape
    # is (batch_size, 2*window_size, D).
    projection = params["projection"][context]

    # Compute average across the context word. The output shape is
    # (batch_size, D).
    avg_projection = jnp.mean(projection, axis=1)

    # (batch_size, D) @ (D, V) -> (batch_size, V)
    hidden = jnp.dot(avg_projection, params["hidden"])
    return hidden


@jax.jit
def word2vec_loss(params, target, context):
    """Compute the loss of the word2Vec model."""
    logits = word2vec_forward(params, context)  # (batch_size, V)

    target_onehot = jax.nn.one_hot(target, logits.shape[1])  # (batch_size, V)
    loss = optax.losses.softmax_cross_entropy(logits, target_onehot).mean()
    return loss
```

Training
--------

For training, I've been relying on the same dataset used by the original word2vec
code - a 100MB text file downloaded from <http://mattmahoney.net/dc/text8.zip>

This file contains all-lowercase text with no punctuation, so it requires very
little cleaning and processing. What it *does* require for higher-quality
training is *subsampling*: throwing away some of the most common words (e.g.
"and", "is", "not" in English), since they appear so much in the text. Here's
my code for this:

```
def subsample(words, threshold=1e-4):
    """Subsample frequent words, return a new list of words.

    Follows the subsampling procedure described in the paper "Distributed
    Representations of Words and Phrases and their Compositionality" by
    Mikolov et al. (2013).
    """
    word_counts = Counter(words)
    total_count = len(words)
    freqs = {word: count / total_count for word, count in word_counts.items()}

    # Common words (freq(word) > threshold) are kept with a computed
    # probability, while rare words are always kept.
    p_keep = {
        word: math.sqrt(threshold / freqs[word]) if freqs[word] > threshold else 1
        for word in word_counts
    }
    return [word for word in words if random.random() < p_keep[word]]
```

We also have to create a vocabulary with some limited size:

```
def make_vocabulary(words, top_k=20000):
    """Creates a vocabulary from a list of words.

    Keeps the top_k most common words and assigns an index to each word. The
    index 0 is reserved for the "<unk>" token.
    """
    word_counts = Counter(words)
    vocab = {"<unk>": 0}
    for word, _ in word_counts.most_common(top_k - 1):
        vocab[word] = len(vocab)
    return vocab
```

The preprocessing step generates the list of subsampled words and the
vocabulary, and stores them in a pickle file for future reference. The
training loop uses these data to train a model from a random initialization.
Pay special attention to the hyper-parameters defined at the top of the
train function. I set these to be as close as possible to the original
word2vec code:

```
def train(train_data, vocab):
    V = len(vocab)
    D = 200
    LEARNING_RATE = 1e-3
    WINDOW_SIZE = 8
    BATCH_SIZE = 1024
    EPOCHS = 25

    initializer = jax.nn.initializers.glorot_uniform()
    params = {
        "projection": initializer(jax.random.PRNGKey(501337), (V, D)),
        "hidden": initializer(jax.random.PRNGKey(501337), (D, V)),
    }

    optimizer = optax.adam(LEARNING_RATE)
    opt_state = optimizer.init(params)

    print("Approximate number of batches:", len(train_data) // BATCH_SIZE)

    for epoch in range(EPOCHS):
        print(f"=== Epoch {epoch + 1}")
        epoch_loss = []
        for n, (target_batch, context_batch) in enumerate(
            generate_train_vectors(
                train_data, vocab, window_size=WINDOW_SIZE, batch_size=BATCH_SIZE
            )
        ):
            # Shuffle the batch.
            indices = np.random.permutation(len(target_batch))
            target_batch = target_batch[indices]
            context_batch = context_batch[indices]

            # Compute the loss and gradients; optimize.
            loss, grads = jax.value_and_grad(word2vec_loss)(
                params, target_batch, context_batch
            )
            updates, opt_state = optimizer.update(grads, opt_state)
            params = optax.apply_updates(params, updates)

            epoch_loss.append(loss)
            if n > 0 and n % 1000 == 0:
                print(f"Batch {n}")

        print(f"Epoch loss: {np.mean(epoch_loss):.2f}")
        checkpoint_filename = f"checkpoint-{epoch:03}.pickle"
        print("Saving checkpoint to", checkpoint_filename)
        with open(checkpoint_filename, "wb") as file:
            pickle.dump(params, file)
```

The only thing I'm not showing here is the generate\_train\_vectors function,
as it's not particularly interesting; you can find it
[in the full code](https://github.com/eliben/deep-learning-samples/blob/main/word2vec-jax/train.py).

I don't have a particularly powerful GPU, so on my machine training this model
for 25 epochs takes 20-30 minutes.

Extracting embeddings and finding word similarities
---------------------------------------------------

The result of the training is the P and H arrays with trained weights;
P is exactly the embedding matrix we need! It maps vocabulary words to their
dense embedding representation. Using P, we can create the fun word demos
that made word2vec famous. The full code has a script named similar-words.py
that does this. Some examples:

```
$ uv run similar-words.py -word paris \
      -checkpoint checkpoint.pickle \
      -traindata train-data.pickle
Words similar to 'paris':
paris           1.00
france          0.50
french          0.49
la              0.42
le              0.41
henri           0.40
toulouse        0.38
brussels        0.38
petit           0.38
les             0.38
```

And:

```
$ uv run similar-words.py -analogy berlin,germany,tokyo \
      -checkpoint checkpoint.pickle \
      -traindata train-data.pickle
Analogies for 'berlin is to germany as tokyo is to ?':
tokyo           0.70
japan           0.45
japanese        0.44
osaka           0.40
china           0.36
germany         0.35
singapore       0.32
han             0.31
gu              0.31
kyushu          0.31
```

This brings us to the intuition for how word2vec works: the basic idea is that
semantically similar words will appear in the vicinity of roughly similar
context words, but also that words are generally related to words in the
context their appear in. This lets the model learn that some words are more
related than others; for example:

```
$ uv run similar-words.py -sims soccer,basketball,chess,cat,bomb \
      -checkpoint checkpoint.pickle \
      -traindata train-data.pickle
Similarities for 'soccer' with context words ['basketball', 'chess', 'cat', 'bomb']:
basketball      0.40
chess           0.22
cat             0.14
bomb            0.13
```

Optimizations
-------------

The word2vec model can be optimized in several ways, many of which are focused
on avoiding the giant matrix multiplication by H at the very end. The
word2vec authors have a followup paper called ["Distributed Representations of
Words and Phrases and their Compositionality"](https://arxiv.org/pdf/1310.4546)
where these are described; I'm leaving them out of my implementation, for
simplicity.

Implementing these optimizations could help us improve the model's quality
considerably, by increasing the model depth (it's currently 200, which is
very low by modern LLM standards) and the amount of data we train on. That
said, these days word2vec is mostly of historical interest anyway; the
*Modern text embeddings* section will have more to say on how embeddings are
trained as part of modern LLMs.

Original word2vec code
----------------------

As mentioned above, the original website for the word2vec model is available
on an [archived version of Google Code](https://code.google.com/archive/p/word2vec/).
That page is still useful reading, but the Subversion instructions to obtain
the actual code no longer work.

I was able to find a GitHub mirror with a code export here: <https://github.com/tmikolov/word2vec>
(the username certainly checks out, though it's hard to know for sure!)

The awesome thing is that this code still builds and runs perfectly, many years
later. Hurray to self-contained C programs with no dependencies; all I needed
was to run make, and then use the included shell scripts to download the
data and run training. This code uses the CPU for training; it takes a while,
but I was able to reproduce the similarity / analogy results fairly easily.

Modern text embeddings
----------------------

The word2vec model trains an embedding matrix; this *pre-trained* matrix can
then be used as part of other ML models. This approach was used for a while,
but it's no longer popular.

These days, an embedding matrix is trained as part of a larger model.
For example, GPT-type transformer-based LLMs have an embedding matrix as the
first layer in the model. This is basically just the P matrix from the
diagram above [[3]](#footnote-3). LLMs learn both the
embeddings and their specific task (generating tokens from a given context)
at the same time. This makes some sense because:

* LLMs process enormous amounts of data, and consuming this data multiple times
  to train embeddings separately is wasteful.
* Embeddings trained together with the LLM are inherently tuned to the LLM's
  specific task and hyper-parameters (i.e. the kind of tokenizer used, the
  model depth etc.)

Specifically, modern embedding matrices differ from word2vec in two important
aspects:

* Instead of being *word* embeddings, they are *token* embeddings. I wrote much
  more on [tokens for LLMs here](https://eli.thegreenplace.net/2024/tokens-for-llms-byte-pair-encoding-in-go/).
* The model depth (D) is *much* larger; GPT-3 has D=12288, and in newer models
  it's probably even larger. Deep embedding vectors help the models capture more
  nuance and semantic meaning about tokens. Naturally, they also require much
  more data to be trained effectively.

Full code
---------

The full code for this post is [available here](https://github.com/eliben/deep-learning-samples/tree/main/word2vec-jax).
If you want to reproduce the my word2vec results, check out the README file - it
contains full instructions on which scripts to run and in which order.

---

|  |  |
| --- | --- |
| [[1]](#footnote-reference-1) | The window size is how many words to the left and right of the target word to take into account, and it's a configurable hyper-parameter during training. |

|  |  |
| --- | --- |
| [[2]](#footnote-reference-2) | The terms *dense* and *sparse* are used in the post in the following sense:  A sparse array is one where almost all entries are 0. This is true for one-hot vectors representing vocabulary words (all entries are 0 except a single one that has the value 1).  A dense array is filled with arbitrary floating-point values. An embedding vector is dense in this sense - it's typically short compared to the sparse vector (in the word2vec example used in this post D=200, while V=20000), but full of data (hence "dense"). An embedding matrix is dense since it consists of dense vectors (one per word index). |

|  |  |
| --- | --- |
| [[3]](#footnote-reference-3) | The rest (mean calculation, hidden layer) isn't needed since it's only there to *train* the word2vec CBOW model. |



---

For comments, please send me
 [an email](mailto:eliben@gmail.com).
