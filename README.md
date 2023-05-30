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


### BAND

[BAND](https://band.embl.de/#) is a cloud desktop for image analysis provided by EMBL Heidelberg. We provide an environment with the necessary dependencies to run the notebooks there.
To use it follow these steps:
- Log in to BAND
- Go to `Applications` (top left) and select `Applications->Programming->DL-Course(Pytorch)`
- This will open jupyter lab. You can run the notebooks with it using the `dl-for-micro` kernel.
    - When you first open a notebook you will be asked which kernel to use. Choose `dl-for-micro`. You can also change the kernel later in the notebook by clicking on the kernel name on the top right of the notebook.

Tip: BAND offers using a GPU. When you start the desktop you can request it by setting `No. of. GPUs` to 1. Also, to run all notebooks smoothly you may want to increase the `No. of. CPUs` to 4 and the `Memory` to 16.
