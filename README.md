# Tutorials for Deep Learning in Microscopy

This repository contains tutorials for deep learning applications in microscopy, with the focus on segmentation and classification tasks.
Currently, we provide notebooks that demonstrate:
- Applying pre-trained models from [bioimage.io](https://bioimage.io/).
- Training your own models for segmentation and classification tasks with the [torch_em](https://github.com/constantinpape/torch-em) library, which wraps [PyTorch](https://pytorch.org/) for deep learning applications in microscopy.

The data used here is from the publication [Microscopy-based assay for semi-quantitative detection of SARS-CoV-2 specific antibodies in human sera](https://onlinelibrary.wiley.com/doi/full/10.1002/bies.202000257), which introduces an imaging based sereological assay for Covid-19.

In the future we will also add:
- Segmentation and classification training in PyTorch.
- Using (pre-trained) [StarDist](https://github.com/stardist/stardist) models for nucleus segmentation.
- Using (pre-trained) [Cellpose](https://github.com/MouseLand/cellpose) models for cell segmentation.


## What do you need to know before starting?

You should be familiar with python and numpy. Experience with other libraries in the "python scientific stack" like scipy, scikit-image and scikit-learn are helpful.
In addition to these libraries we will use [napari](https://napari.org/stable/) for visualization.

There are many good tutorials for learning how to use python and its libraries online, for example:
- [The python tutorial](https://www.pythontutorial.net/) for a general introduction to python.
- [The python data science handbook](https://jakevdp.github.io/PythonDataScienceHandbook/) for scientific python libraries.


## How to get started?

First, you need to set up a conda environment with the necessary dependencies for the notebooks. See the installation section below for details. TODO: explain set-up on BAND

Once you have the environment set-up, start with the `data_preparation.ipynb` notebook where you will get to know the data we are using and prepare it for the other tasks.
Each notebook contains a section **What's next?** at the end that tells you how to continue.
In addition there is an **Exercise** section that lists optional exercises you can do after running the tutorial to further your understanding of the lesson in the notebook.


### Installation

TODO: provide link for how to install conda / mamba

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
