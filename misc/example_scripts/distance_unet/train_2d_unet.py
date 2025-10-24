# Import functionality for getting filepaths.
from glob import glob

# Import the required functionality from torch-em.
import torch_em
from torch_em.model import UNet2d
from torch_em.util.debug import check_loader

from sklearn.model_selection import train_test_split


# Download the example data. Here, we use the same data as in the exercises.
def download_example_data():
    from torch_em.data.datasets.light_microscopy.covid_if import get_covid_if_data
    get_covid_if_data("../data/covid-if", download=True)


# Get the paths to the data. The data we have downloaded is stored in hdf5 files.
# Your data will likely be stored as tif files, which is also supported.
def get_data_paths(split):
    # Get all file paths, then split them into a training and validation set
    # with functionality from scikit-learn.
    all_paths = sorted(glob("../data/covid-if/*.h5"))
    train_paths, val_paths = train_test_split(all_paths, test_size=0.1, random_state=42)
    # Return the file paths for training images and labels, or for validation images
    # and labeles, depending on which split was requested.
    if split == "train":
        # Note: The hdf5 files contain both the image data and the label data,
        # stored i different internal datasets. That's why we return two times
        # the same list of paths, for images and labels here.
        # If you have tifs then you have to return the image paths and the label paths.
        return train_paths, train_paths
    elif split == "val":
        return val_paths, val_paths
    else:
        raise ValueError(f"Invalid split: {split}")


# Create the 2D U-Net.
model = UNet2d(
    in_channels=1,  # The number of input channels, 1 for a single input channel, etc.
    out_channels=3,  # The number of output channels. Here, we predict foreground and two distance channels.
    final_activation="Sigmoid",  # The activation applied to the output channels.
)


# Define the label and image transformation:
# The label transformation is applied to the label data within the data loader.
# Here, we use the transform to create per object normalized center and boundary
# distances + a foreground channel.
label_transform = torch_em.transform.label.PerObjectDistanceTransform(
    distances=True, boundary_distances=True, foreground=True
)
# The transformation appied to the image data. Here, we standardize the data,
# which means subtracting its mean and dividing by its standard deviation.
raw_transform = torch_em.transform.raw.standardize

# Define the loss function and the metric:
# Here, we use a dice loss for the distances, both as loss function and as metric.
loss = torch_em.loss.distance_based.DiceBasedDistanceLoss(mask_distances_in_bg=True)
metric = torch_em.loss.distance_based.DiceBasedDistanceLoss(mask_distances_in_bg=True)

# YOU NEED TO ADAPT THE NEXT LINES FOR YOUR DATA.
# Download the example data and get the paths for training and val sets.
download_example_data()
train_image_paths, train_label_paths = get_data_paths(split="train")
val_image_paths, val_label_paths = get_data_paths(split="val")

# The internal dataset names for the hdf5 files.
raw_key = "/raw/serum_IgG/s0"
label_key = "/labels/cells/s0"
# If you have tif files, then set 'raw_key' and 'label_key' to None:
# raw_key = None
# label_key = None

# Create the data loaders:
# The function below automatically creates suitable data loaders.
batch_size = 4  # Set the batch size.
patch_shape = (256, 256)  # Set the patch shape: how big is an image tile for training.
train_loader = torch_em.segmentation.default_segmentation_loader(
    raw_paths=train_image_paths,
    raw_key=raw_key,
    label_paths=train_label_paths,
    label_key=label_key,
    batch_size=batch_size,
    patch_shape=patch_shape,
    label_transform=label_transform,
    raw_transform=raw_transform,
)
val_loader = torch_em.segmentation.default_segmentation_loader(
    raw_paths=val_image_paths,
    raw_key=raw_key,
    label_paths=val_label_paths,
    label_key=label_key,
    batch_size=batch_size,
    patch_shape=patch_shape,
    label_transform=label_transform,
    raw_transform=raw_transform,
)

# If set to True, this will open 4 samples from the training loader and from
# the validation loader in napari. This is very helpful to check that your
# training data is loaded correctly and that data and label transformation are
# applied in a correct manner.
check_loaders = True
if check_loaders:
    check_loader(train_loader, n_samples=4)
    check_loader(val_loader, n_samples=4)

# Create the trainer:
# The trainer class implements all relevant logic for model training, validation, etc.
name = "my-model"  # Set the name of your model. Checkpoints will be saved under this name.
# IMPORTANT: IF YOU START A NEW TRAINING YOU HAVE TO CHANGE THE NAME.
# OTHERWISE YOUR PREVIOUS CHECKPOINTS WILL BE OVER-WRITTEN.
learning_rate = 1e-4  # Set the learning rate.
trainer = torch_em.default_segmentation_trainer(
    name=name,
    model=model,
    train_loader=train_loader,
    val_loader=val_loader,
    loss=loss,
    metric=loss,
    learning_rate=learning_rate,
    # These are advanced settings you don't need to change.
    mixed_precision=True,
    compile_model=False,
)

# Run training:
# Now we start the training. We can set either a number of iterations for training
# (set here to 5000) or set a number of epochs (use "epochs=number_of_epochs" instead).
number_of_iterations = 5000
trainer.fit(iterations=number_of_iterations)

# The checkpoints of your trained model will be saved in the folder 'checkpoints':
# checkpoints/{name}/best.pt   <- contains the best model (according to val metric)
# checkpoints/{name}/latest.pt <- contains the latest model
# You should use the best checkpoint after training.

# The trainer creates the data necessary for monitoring the training in tensorboard.
# To check your tensorboard you have to run the following in a separate terminal:
# tensorboard --logdir logs
# You can then open tensorboard by clicking on the link that will be printed.
