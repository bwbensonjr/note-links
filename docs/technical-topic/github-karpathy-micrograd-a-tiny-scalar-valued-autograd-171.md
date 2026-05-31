---
id: 171
url: https://github.com/karpathy/micrograd
title: 'GitHub - karpathy/micrograd: A tiny scalar-valued autograd engine and a neural
  net library on top of it with PyTorch-like API'
domain: github.com
source_date: '2025-10-31'
tags:
- github-repo
- python
- ai
- tutorial
summary: Micrograd is a tiny, educational Python library that implements backpropagation
  and automatic differentiation in just ~100 lines of code, operating on scalar values
  to build neural networks with a PyTorch-like API. It enables training of neural
  networks for tasks like binary classification and includes visualization tools to
  understand how gradients flow through the computation graph. The project is designed
  primarily for educational purposes to help understand how machine learning frameworks
  work under the hood.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# GitHub - karpathy/micrograd: A tiny scalar-valued autograd engine and a neural net library on top of it with PyTorch-like API

micrograd
=========

[![awww](/karpathy/micrograd/raw/master/puppy.jpg)](/karpathy/micrograd/blob/master/puppy.jpg)

A tiny Autograd engine (with a bite! :)). Implements backpropagation (reverse-mode autodiff) over a dynamically built DAG and a small neural networks library on top of it with a PyTorch-like API. Both are tiny, with about 100 and 50 lines of code respectively. The DAG only operates over scalar values, so e.g. we chop up each neuron into all of its individual tiny adds and multiplies. However, this is enough to build up entire deep neural nets doing binary classification, as the demo notebook shows. Potentially useful for educational purposes.

### Installation

```
pip install micrograd
```

### Example usage

Below is a slightly contrived example showing a number of possible supported operations:

```
from micrograd.engine import Value

a = Value(-4.0)
b = Value(2.0)
c = a + b
d = a * b + b**3
c += c + 1
c += 1 + c + (-a)
d += d * 2 + (b + a).relu()
d += 3 * d + (b - a).relu()
e = c - d
f = e**2
g = f / 2.0
g += 10.0 / f
print(f'{g.data:.4f}') # prints 24.7041, the outcome of this forward pass
g.backward()
print(f'{a.grad:.4f}') # prints 138.8338, i.e. the numerical value of dg/da
print(f'{b.grad:.4f}') # prints 645.5773, i.e. the numerical value of dg/db
```

### Training a neural net

The notebook `demo.ipynb` provides a full demo of training an 2-layer neural network (MLP) binary classifier. This is achieved by initializing a neural net from `micrograd.nn` module, implementing a simple svm "max-margin" binary classification loss and using SGD for optimization. As shown in the notebook, using a 2-layer neural net with two 16-node hidden layers we achieve the following decision boundary on the moon dataset:

[![2d neuron](/karpathy/micrograd/raw/master/moon_mlp.png)](/karpathy/micrograd/blob/master/moon_mlp.png)

### Tracing / visualization

For added convenience, the notebook `trace_graph.ipynb` produces graphviz visualizations. E.g. this one below is of a simple 2D neuron, arrived at by calling `draw_dot` on the code below, and it shows both the data (left number in each node) and the gradient (right number in each node).

```
from micrograd import nn
n = nn.Neuron(2)
x = [Value(1.0), Value(-2.0)]
y = n(x)
dot = draw_dot(y)
```

[![2d neuron](/karpathy/micrograd/raw/master/gout.svg)](/karpathy/micrograd/blob/master/gout.svg)

### Running tests

To run the unit tests you will have to install [PyTorch](https://pytorch.org/), which the tests use as a reference for verifying the correctness of the calculated gradients. Then simply:

```
python -m pytest
```

### License

MIT
