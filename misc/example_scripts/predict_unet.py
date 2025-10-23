# This is an example script for running prediction with a 3D UNet.
# The prediction runs in a tiled manner.
# It can easily be adapted to 2D segmentation as well.

import imageio.v3 as imageio
import napari
import torch_em
from torch_em.util.prediction import predict_with_halo
from torch_em.util import load_model

# First we load our data. Here, we load example data for 3D nucleus segmentation.
# CHANGE THIS TO LOAD YOUR DATA.
path = "data/Mouse-Skull-Nuclei-CBG/test/images/X2_right.tif"
image = imageio.imread(path)

# Now we load our trained model.
# CHANGE THIS FOR YOUR MODEL.
model = load_model("./checkpoints/my-3d-model")

# Run the prediction with tiling. There are two important parameters:
tile_shape = (32, 256, 256)  # This is the inner shape of the tile.
overlap = (8, 32, 32)  # This is the overlap between tiles. It is added to the inner shape.
# You can do the same in 2D, you just have to select a 2d tile shape and overlap.
prediction = predict_with_halo(
    input_=image,
    model=model,
    gpu_ids=[0],
    block_shape=tile_shape,
    halo=overlap,
    # Important: use the same data preprocessing as in training.
    preprocess=torch_em.transform.raw.standardize,
)

# In the end we check the result in napari.
viewer = napari.Viewer()
viewer.add_iamge(image)
viewer.add_image(prediction)
napari.run()

# Next, you can save the data or further process it.
# For saving the prediction you can use imageio.imwrite.
