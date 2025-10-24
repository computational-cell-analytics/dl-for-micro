# This is an example script for running prediction with a 3D UNet.
# The prediction runs in a tiled manner.
# It can easily be adapted to 2D segmentation as well.

import h5py
import napari
import torch_em
from torch_em.util.prediction import predict_with_halo
from torch_em.util import load_model

# First we load our data. Here, we load example data for 3D nucleus segmentation.
# CHANGE THIS TO LOAD YOUR DATA.
path = "../data/covid-if/gt_image_000.h5"
with h5py.File(path, "r") as f:
    image = f["/raw/serum_IgG/s0"][:]

# Now we load our trained model.
# CHANGE THIS FOR YOUR MODEL.
model = load_model("./checkpoints/my-model")

# Run the prediction with tiling. There are two important parameters:
tile_shape = (512, 512)  # This is the inner shape of the tile.
overlap = (32, 32)  # This is the overlap between tiles. It is added to the inner shape.
# You can do the same in 3D, you just have to select a 3D tile shape and overlap.
prediction = predict_with_halo(
    input_=image,
    model=model,
    gpu_ids=[0],
    block_shape=tile_shape,
    halo=overlap,
    # Important: use the same data preprocessing as in training.
    preprocess=torch_em.transform.raw.standardize,
)

# We can compute the segmentation based on the distance predictions.
# CHANGE / REMOVE THIS IF YOU HAVE TRAINED A U-NET FOR A DIFFERENT PURPOSE.
from torch_em.util.segmentation import watershed_from_center_and_boundary_distances
foreground, center_distances, boundary_distances  = prediction
segmentation = watershed_from_center_and_boundary_distances(
    center_distances=center_distances,
    boundary_distances=boundary_distances,
    foreground_map=foreground,
    min_size=15,
)

# In the end we check the result in napari.
viewer = napari.Viewer()
viewer.add_image(image)
viewer.add_image(prediction)
viewer.add_labels(segmentation)
napari.run()

# Next, you can save the data or further process it.
# For saving the prediction you can use imageio.imwrite.
