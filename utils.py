# General imports.
import os
import zipfile
from glob import glob
from shutil import copyfile
from shutil import copytree
from shutil import copyfileobj
from shutil import move
import h5py
import numpy as np
from skimage.measure import regionprops
import requests
from tqdm import tqdm
# saving images to tif formats
import imageio.v3 as imageio

# this is the folder where all data is stored.
data_folder = "data"
os.makedirs(data_folder, exist_ok=True)

# the data is on zenodo
data_url = "https://zenodo.org/record/5092850/files/covid-if-groundtruth.zip?download=1"

# download the data using the requests library

# this function is for downloading the data.
# you don't need to understand what's going on here.
def download_url(url, path):
    if os.path.isfile(path):
        return 
    with requests.get(url, stream=True) as r:
        if r.status_code != 200:
            r.raise_for_status()
            raise RuntimeError(f"Request to {url} returned status code {r.status_code}")
        file_size = int(r.headers.get("Content-Length", 0))
        desc = f"Download {url} to {path}"
        if file_size == 0:
            desc += " (unknown file size)"
        with tqdm.wrapattr(r.raw, "read", total=file_size, desc=desc) as r_raw, open(path, "wb") as f:
            copyfileobj(r_raw, f)


# run the download function to donwnload the data to the file 'data.zip' in the data folder
download_url(data_url, os.path.join(data_folder, "data.zip"))

# unzip the data using the zipfile library
# function for unzipping the archive we have just downloaded and then removing the zip
def unzip(zip_path, dst, remove=True):
    with zipfile.ZipFile(zip_path, "r") as f:
        f.extractall(dst)
    if remove:
        os.remove(zip_path)
unzip(os.path.join(data_folder, "data.zip"), data_folder, remove=False)

# You should see that 49 files have been downloaded and that they have the file extension .h5.
# This extension stands for HDF5 files. HDF5 is a hierarchical data format that can store multiple datasets in a single file.
# Now we inspect the content of one of these files using the h5py library:
file_paths = glob(os.path.join(data_folder, "*.h5"))
file_path = file_paths[0]

# We use a visitor pattern to check out the contents of the file.
# the 'inspector' function will be called for each element in the file hierarchy.

def inspector(name, node):
    # hdf5 files contain 'Dataset' that hold the actual data. With the function below we print
    # the name and shape if the inspector function encounters a dataset
    if isinstance(node, h5py.Dataset):
        print("The h5 file contains a dataset @", name, "with shape", node.shape)

with h5py.File(file_path, "r") as f:
    f.visititems(inspector)

# get all image file paths using glob, which allows to select files with '*' wildcards
# e.g. glob('*.h5') will select all files that have the .h5 file ending
file_paths = glob(os.path.join(data_folder, "*.h5"))
file_paths.sort()
print("You have selected", len(file_paths), "files")

# convert images from hd5 to tiff:
# extract 5 images from 1 hd5 file and
# put them in a designated directory
def convert_hdf5_to_tif(paths, file_folders):
    count = 0
    for file_path in tqdm(paths):
      with h5py.File(file_path,'r') as f:
        # get image dataset
        marker = f["raw/marker/s0"][:]
        nucleus_image = f["raw/nuclei/s0"][:]
        cells = f["labels/cells/s0"][:]
        infected_labels = f["labels/infected/nuclei/s0"][:]
        serum_image = f["raw/serum_IgG/s0"][:]
        #print(f'Image Dataset info: Shape={marker.shape},Dtype={marker.dtype}')
        img_ds = {
            "marker": marker, 
            "nucleus_image": nucleus_image, 
            "cells": cells, 
            "infected_labels": infected_labels,
            "serum_image": serum_image 
        }
        # create a subdirectory for each hd5 file
        folder_name = f"gt_image_{count:03}"
        file_folders.append(folder_name)
        img_dir = os.path.join(data_folder, folder_name)
        os.makedirs(img_dir, exist_ok=True)

        for key, value in img_ds.items():
            img_name = f"{img_dir}_{key}.tif"
            imageio.imwrite(img_name, value, compression="zlib")
            # copy to subdirectoy
            move(img_name, os.path.join(img_dir, os.path.basename(img_name)))

        count += 1

# need file_folder names for later use
file_folders = []
convert_hdf5_to_tif(file_paths, file_folders)

# get new file_paths of the .tif images and
# get file_dir_paths to each folder containing .tif files
file_paths = []
file_dir_paths = []
for path, subdirs, files in os.walk(data_folder):
    for name in files:
        if name.endswith(".tif"):
            file_paths.append(os.path.join(path, name))
file_dir_paths = [x[0] for x in os.walk(data_folder)]
file_dir_paths.remove("data")
file_dir_paths.sort()

# create the train, validation (val) and test splits by creating sub-folders for each split
# and copying the respective files there
# 

def divide_data(n_train, n_val): 

    train_folder = os.path.join(data_folder, "train")
    os.makedirs(train_folder, exist_ok=True)
    for train_image_dir in file_folders[:n_train]:
        if(not os.path.exists(os.path.join(train_folder, train_image_dir))):
            move(os.path.join(data_folder, train_image_dir), os.path.join(train_folder, os.path.basename(train_image_dir)))
 
    val_folder = os.path.join(data_folder, "val")
    os.makedirs(val_folder, exist_ok=True)
    for val_image_dir in file_folders[n_train:n_train+n_val]:
        if(not os.path.exists(os.path.join(val_folder, val_image_dir))):
            move(os.path.join(data_folder,val_image_dir), os.path.join(val_folder, os.path.basename(val_image_dir)))

    test_folder = os.path.join(data_folder, "test")
    os.makedirs(test_folder, exist_ok=True)
    for test_image_dir in file_folders[n_train+n_val:]:
        if(not os.path.exists(os.path.join(test_folder, test_image_dir))):
            move(os.path.join(data_folder,test_image_dir), os.path.join(test_folder, os.path.basename(test_image_dir)))
    return train_folder, val_folder, test_folder

train_folder, val_folder, test_folder = divide_data(35, 5)

# double check that we have the correct number of images in the split folders
print("We have", len(os.listdir(train_folder)), "training images")
print("We have", len(os.listdir(val_folder)), "validation images")
print("We have", len(os.listdir(test_folder)), "test images")