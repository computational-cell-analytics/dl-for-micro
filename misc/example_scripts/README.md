# Example scripts for training and prediction of networks

This example folder contains three scripts:
- `train_2d_unet.py`: For training a 2D UNet with [torch_em](https://github.com/constantinpape/torch-em).
- `train_3d_unet.py`: For training a 3D UNet with [torch_em](https://github.com/constantinpape/torch-em).
- `predict_unet.py`: For running prediction with your trained model.

The folder `distance_unet` contains alternate versions of the scripts for training U-Nets for distance-based instance segmentation.

It also contains a script for fine-tuning micro-sam:
- `sam_finetuning.ipynb`

Note: in order to do this you need to change the source code and remove the `"verbose" = True` in `scheduler_kwargs`.
We can help you with that.

To run prediction with `microSAM` you can use the command line tool `micro_sam.automatic_segmentation`. See [the documentation](https://computational-cell-analytics.github.io/micro-sam/micro_sam.html#using-the-command-line-interface-cli) for details.
