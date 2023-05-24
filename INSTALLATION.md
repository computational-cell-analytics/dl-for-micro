# Installation instructions

## Full environment including micro-sam (with GPU)

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
