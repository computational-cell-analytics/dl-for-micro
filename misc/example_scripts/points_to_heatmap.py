import numpy as np
import pandas as pd
from scipy.ndimage import gaussian_filter


# The shape of the image. You have to adapt this for your data.
image_shape = (872, 1000)
# Load the points you have saved via napari. Adapt the filepath.
points = pd.read_csv("points.csv")

# Load the points, map them to pixel coordinates, and clamp them to the image boarders.
coordinates = points[["axis-0", "axis-1"]].to_numpy()
coordinates = np.rint(coordinates).astype(int)
valid = (
    (coordinates[:, 0] >= 0)
    & (coordinates[:, 0] < image_shape[0])
    & (coordinates[:, 1] >= 0)
    & (coordinates[:, 1] < image_shape[1])
)
coordinates = coordinates[valid]

# Create the heatmap by writing ones for all detected points.
heatmap = np.zeros(image_shape, dtype="float32")
np.add.at(heatmap, (coordinates[:, 0], coordinates[:, 1]), 1)

# Then apply smoothing and normalize the heatmap.
heatmap = gaussian_filter(heatmap, sigma=2)
heatmap -= heatmap.min()
heatmap /= heatmap.max()

# You can save the result as a tiff image and use it as target for training.

# Here, we just display the result in napari.
import napari
viewer = napari.Viewer()
viewer.add_image(heatmap, name="heatmap")
napari.run()
