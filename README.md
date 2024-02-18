# Introduction to Deep Learning for Microscopy

Do you want to learn how to use deep learning for solving your microscopy image analysis tasks?
Then you have come to the right spot!

We offer materials for an introductory course on the topic, containing video lectures, exercises that show step by step how to build deep learning models for microscopy with [PyTorch](https://pytorch.org/) and advanced examples that explain how to use several of the most popular deep learning based tools.

Sparked your interest?
- Check out the [content](#content)!
- See how you can work on the exercises [on publicly available resources](#on-band) or how to [set them up on your own computer](#on-your-own-computer).
- Check out the [recommended prior knowledge and further reading](#recommended-knowledge-and-further-reading).

## Content

Under construction!

### Video Lectures

### PyTorch Exercises

### Advanced Examples


## Getting started

### On BAND

[BAND](https://band.embl.de/#) is a online service for image analysis. It is free of charge and it offers a pre-installed environment for the [exercises](pytorch-exercises). Follow [this link](https://github.com/computational-cell-analytics/dl-for-micro/blob/main/BAND.md) for a step-by-step guide for how to run the course on BAND.

### On your own computer

<!---
If you do not have a conda installation we suggest to install [mamba](https://github.com/mamba-org/mamba) via the [mambaforge](https://github.com/conda-forge/miniforge#mambaforge) installation.

Create the conda environment from `environment-gpu.yaml`. Note: you may need to change the cuda version [here](https://github.com/computational-cell-analytics/dl-for-micro/blob/main/environment_gpu.yaml#L15).
```
$ conda env create -f environment_gpu.yaml
```
This will install the environment `dl-for-micro` with all necessary dependencies.
After setting up the environment the following should work (activate the environment first with `conda activate dl-for-micro`):
```
$ python -c "import torch_em"
$ python -c "import micro_sam"
```
Tip: use [mamba](https://github.com/mamba-org/mamba) instead of `conda` if creating the environment with `conda` takes very long.
-->

## Recommended Knowledge and Further Reading


<!---
This repository contains tutorials for deep learning applications in microscopy, with the focus on segmentation and classification tasks.
Currently, we provide notebooks that demonstrate:
- Applying pre-trained models from [bioimage.io](https://bioimage.io/).
- Training your own models for segmentation and classification tasks with the [torch_em](https://github.com/constantinpape/torch-em) library, which wraps [PyTorch](https://pytorch.org/) for deep learning applications in microscopy.

The data used here is from the publication [Microscopy-based assay for semi-quantitative detection of SARS-CoV-2 specific antibodies in human sera](https://onlinelibrary.wiley.com/doi/full/10.1002/bies.202000257), which introduces an imaging based sereological assay for Covid-19.

In the future we will also add:
- Segmentation and classification training in PyTorch.
- Using (pre-trained) [StarDist](https://github.com/stardist/stardist) models for nucleus segmentation.
- Using (pre-trained) [Cellpose](https://github.com/MouseLand/cellpose) models for cell segmentation.

**Data annotation:** a common problem when applying deep learning methods in microscopy is the lack of annotated data and the long and tedious effort to then annotate it.
For instance segmentation and tracking tasks new methods like [Segment Anything](https://segment-anything.com/) can significantly speed this up.
We are building [tools](https://github.com/computational-cell-analytics/micro-sam) around it to make data annotation much more convenient; check out the `segment-anything.ipynb` notebook for an example on how to use them for the data here. This also works on [BAND](#band).


## What do you need to know before starting?

You should be familiar with python and numpy. Experience with other libraries in the "python scientific stack" like scipy, scikit-image and scikit-learn are helpful.
In addition to these libraries we will use [napari](https://napari.org/stable/) for visualization.

There are many good tutorials for learning how to use python and its libraries online, for example:
- [The python tutorial](https://www.pythontutorial.net/) for a general introduction to python.
- [The python data science handbook](https://jakevdp.github.io/PythonDataScienceHandbook/) for scientific python libraries.


## How to get started?

First, you need to set up a conda environment with the necessary dependencies for the notebooks. See the [installation section](#installation) below for details.
Or you can use the pre-installed environment on [BAND](https://band.embl.de/#), see the [BAND section](#band) below.

Once you have the environment set-up, start with the `data_preparation.ipynb` notebook where you will get to know the data we are using and prepare it for the other tasks.
Each notebook contains a section **What's next?** at the end that tells you how to continue.
In addition there is an **Exercise** section that lists optional exercises you can do after running the tutorial to further your understanding of the lesson in the notebook.


### Installation


### BAND

-->
