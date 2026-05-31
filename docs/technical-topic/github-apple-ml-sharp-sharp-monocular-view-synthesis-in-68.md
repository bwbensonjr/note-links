---
id: 68
url: https://github.com/apple/ml-sharp
title: 'GitHub - apple/ml-sharp: Sharp Monocular View Synthesis in Less Than a Second'
domain: github.com
source_date: '2025-12-27'
tags:
- github-repo
- ai
- python
summary: Apple's SHARP is a neural network model that converts a single 2D photograph
  into a 3D Gaussian representation in under one second on standard GPUs, enabling
  photorealistic view synthesis and real-time rendering of nearby viewpoints. The
  approach achieves state-of-the-art results with significant improvements over prior
  methods (25-34% reduction in LPIPS metric) while being three orders of magnitude
  faster, and demonstrates robust zero-shot generalization across different datasets.
  The project is open-source and includes command-line tools for predicting 3D Gaussian
  splats from images and rendering video trajectories.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# GitHub - apple/ml-sharp: Sharp Monocular View Synthesis in Less Than a Second

Sharp Monocular View Synthesis in Less Than a Second
====================================================

[![Project Page](https://camo.githubusercontent.com/cafdcb5612b1ab28528d47af9245604f8f7b0792562c7c5151fff90340a3d6cc/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f50726f6a6563742d506167652d677265656e)](https://apple.github.io/ml-sharp/)
[![arXiv](https://camo.githubusercontent.com/dba21084a03f7471ad5ab1cbe4b2eeb9c6c4333dde6dae06cd437bc9b9163cf7/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f61725869762d323531322e31303638352d6233316231622e737667)](https://arxiv.org/abs/2512.10685)

This software project accompanies the research paper: *Sharp Monocular View Synthesis in Less Than a Second*
by *Lars Mescheder, Wei Dong, Shiwei Li, Xuyang Bai, Marcel Santos, Peiyun Hu, Bruno Lecouat, Mingmin Zhen, Amaël Delaunoy,
Tian Fang, Yanghai Tsin, Stephan Richter and Vladlen Koltun*.

[![](/apple/ml-sharp/raw/main/data/teaser.jpg)](/apple/ml-sharp/blob/main/data/teaser.jpg)

We present SHARP, an approach to photorealistic view synthesis from a single image. Given a single photograph, SHARP regresses the parameters of a 3D Gaussian representation of the depicted scene. This is done in less than a second on a standard GPU via a single feedforward pass through a neural network. The 3D Gaussian representation produced by SHARP can then be rendered in real time, yielding high-resolution photorealistic images for nearby views. The representation is metric, with absolute scale, supporting metric camera movements. Experimental results demonstrate that SHARP delivers robust zero-shot generalization across datasets. It sets a new state of the art on multiple datasets, reducing LPIPS by 25–34% and DISTS by 21–43% versus the best prior model, while lowering the synthesis time by three orders of magnitude.

Getting started
---------------

We recommend to first create a python environment:

```
conda create -n sharp python=3.13
```

Afterwards, you can install the project using

```
pip install -r requirements.txt
```

To test the installation, run

```
sharp --help
```

Using the CLI
-------------

To run prediction:

```
sharp predict -i /path/to/input/images -o /path/to/output/gaussians
```

The model checkpoint will be downloaded automatically on first run and cached locally at `~/.cache/torch/hub/checkpoints/`.

Alternatively, you can download the model directly:

```
wget https://ml-site.cdn-apple.com/models/sharp/sharp_2572gikvuh.pt
```

To use a manually downloaded checkpoint, specify it with the `-c` flag:

```
sharp predict -i /path/to/input/images -o /path/to/output/gaussians -c sharp_2572gikvuh.pt
```

The results will be 3D gaussian splats (3DGS) in the output folder. The 3DGS `.ply` files are compatible to various public 3DGS renderers. We follow the OpenCV coordinate convention (x right, y down, z forward). The 3DGS scene center is roughly at (0, 0, +z). When dealing with 3rdparty renderers, please scale and rotate to re-center the scene accordingly.

### Rendering trajectories (CUDA GPU only)

Additionally you can render videos with a camera trajectory. While the gaussians prediction works for all CPU, CUDA, and MPS, rendering videos via the `--render` option currently requires a CUDA GPU. The gsplat renderer takes a while to initialize at the first launch.

```
sharp predict -i /path/to/input/images -o /path/to/output/gaussians --render

# Or from the intermediate gaussians:
sharp render -i /path/to/output/gaussians -o /path/to/output/renderings
```

Evaluation
----------

Please refer to the paper for both quantitative and qualitative evaluations.
Additionally, please check out this [qualitative examples page](https://apple.github.io/ml-sharp/) containing several video comparisons against related work.

Citation
--------

If you find our work useful, please cite the following paper:

```
@inproceedings{Sharp2025:arxiv,
  title      = {Sharp Monocular View Synthesis in Less Than a Second},
  author     = {Lars Mescheder and Wei Dong and Shiwei Li and Xuyang Bai and Marcel Santos and Peiyun Hu and Bruno Lecouat and Mingmin Zhen and Ama\"{e}l Delaunoy and Tian Fang and Yanghai Tsin and Stephan R. Richter and Vladlen Koltun},
  journal    = {arXiv preprint arXiv:2512.10685},
  year       = {2025},
  url        = {https://arxiv.org/abs/2512.10685},
}
```

Acknowledgements
----------------

Our codebase is built using multiple opensource contributions, please see [ACKNOWLEDGEMENTS](/apple/ml-sharp/blob/main/ACKNOWLEDGEMENTS) for more details.

License
-------

Please check out the repository [LICENSE](/apple/ml-sharp/blob/main/LICENSE) before using the provided code and
[LICENSE\_MODEL](/apple/ml-sharp/blob/main/LICENSE_MODEL) for the released models.
