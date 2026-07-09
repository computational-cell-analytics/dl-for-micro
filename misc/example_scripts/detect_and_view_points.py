# A spot detector from skimage.
from skimage.feature import blob_log
import napari

# Load the sample data and create grayscale from the RGB image.
# (If you have grayscale data then you don't need to do the conversio)
from skimage import data
from skimage.color import rgb2gray

image = data.hubble_deep_field()
image_gray = rgb2gray(image)

# Detect the spots. Note: you may need to vary the parameters or use a different spot-detector for your data.
blobs = blob_log(image_gray, min_sigma=1, max_sigma=8, num_sigma=10, threshold=0.1)
points = blobs[:, :2]

viewer = napari.Viewer()
viewer.add_image(image, rgb=True)
viewer.add_points(points)
napari.run()

# You can then use the point layer controls to move, delete or add points to correct the initial results
# in order to obtain ground-truth detections.
# Then, save the corrected result by selecting the 'points' layer and clicking "File->Save Selected Layers ...".
# Choose a location and a name you can identify again.

# The script 'points_to_heatmap.py' shows how to create a heatmap for training a network based on the saved points.
