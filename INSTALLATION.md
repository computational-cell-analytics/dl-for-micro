# Installation instructions

You can set up an environment that contains all dependencies using `mamba / conda`. If you don't have `mamba` or `conda` installed yet see [here](https://github.com/mamba-org/mamba) for installation insructions.

You can then create an environment with all necessary dependencies. You have the choice between a cpu or gpu version:
- CPU Version: [environment_cpu.yaml](https://github.com/computational-cell-analytics/dl-for-micro/blob/main/environment_cpu.yaml)
  Create the environment via
```
mamba env create -f environment_cpu.yaml
``` 
- GPU version: [environment_gpu.yaml](https://github.com/computational-cell-analytics/dl-for-micro/blob/main/environment_gpu.yaml)
  Create the environment via
```
mamba env crete -f environment_gpu.yaml
```

Note: you may need to change the CUDA version to match your system [here](https://github.com/computational-cell-analytics/dl-for-micro/blob/main/environment_gpu.yaml#L15).

This will install the environment `dl-for-micro` with all necessary dependencies.
After setting up the environment the following should work (activate the environment first with `mamba/conda activate dl-for-micro`):
```
$ python -c "import torch_em"
$ python -c "import micro_sam"
```

