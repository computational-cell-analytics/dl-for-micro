# Example scripts for projects

This example folder contains the follwoing examples:
- `train_2d_unet.py`: Train a 2D UNet with [torch_em](https://github.com/constantinpape/torch-em).
- `train_3d_unet.py`: Train a 3D UNet with [torch_em](https://github.com/constantinpape/torch-em).
- `predict_unet.py`: Run tile-based prediction with your trained model.
- `sam_finetuning.ipynb`: Fine-tune a microSAM model on your own data.
- `convert_to_8bit.py`: Convert tiff images to 8bit. For microSAM training.

The folder `distance_unet` contains alternative versions of the scripts for training U-Nets for distance-based instance segmentation (rather than boundary-based segmentation as in the current version).

To run prediction with `microSAM` you can use the command line tool `micro_sam.automatic_segmentation`. See [the documentation](https://computational-cell-analytics.github.io/micro-sam/micro_sam.html#using-the-command-line-interface-cli) for details.
