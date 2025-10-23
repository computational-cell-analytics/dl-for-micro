# Example scripts for training and prediction of networks

This example folder contains three scripts:
- `train_2d_unet.py`: For training a 2D UNet with [torch_em](https://github.com/constantinpape/torch-em).
- `train_3d_unet.py`: For training a 3D UNet with [torch_em](https://github.com/constantinpape/torch-em).
- `predict_unet.py`: For running prediction with your trained model.

If you want to train a custom `microSAM` model you can check out this notebook:
- https://github.com/computational-cell-analytics/micro-sam/blob/master/notebooks/sam_finetuning.ipynb 

And to run prediction with `microSAM` you can use the command line tool `micro_sam.automatic_segmentation`. See [the documentation](https://computational-cell-analytics.github.io/micro-sam/micro_sam.html#using-the-command-line-interface-cli) for details.
