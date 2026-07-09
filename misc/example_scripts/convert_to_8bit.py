import os
from glob import glob
import imageio.v3 as imageio

# The folder with your images.
input_folder = "..."

# The output folder where the images converted to 8bit will be stored.
output_folder = "..."
os.makedirs(output_folder, exist_ok=True)


# The conversion to 8bit.
def convert_to_8bit(image):
    image = image.astype("float32")
    image -= image.min()
    image /= image.max()
    image *= 255
    return image.astype("uiint8")


# Select all input images --- assumes images stored as tiff files with file ending .tif.
image_files = glob(os.path.join(input_folder, "*.tif"))
for image_file in image_files:
    image = imageio.imread(image_file)
    image = convert_to_8bit(image)
    # Write the output.
    output_file = os.path.join(output_folder, os.path.basename(image_file))
    imageio.imwrite(output_file, image, compression="zlib")
