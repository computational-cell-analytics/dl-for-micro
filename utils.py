# General imports.
import os
import zipfile
from glob import glob
from shutil import copyfileobj
from shutil import move
import h5py
from skimage.measure import regionprops
import requests
from tqdm import tqdm
# saving images to tif formats
import imageio.v3 as imageio
#from numpyencoder import NumpyEncoder
import json
import numpy as np


# download the data using the requests library
# this function is for downloading the data.
# you don't need to understand what's going on here.
def download_url(url, path):
    # If the file to be downloaded already exists, quit here.
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


# unzip the data using the zipfile library
# function for unzipping the archive we have just downloaded and then removing the zip
def unzip(zip_path, dst, remove=True):
    with zipfile.ZipFile(zip_path, "r") as f:
        f.extractall(dst)
    if remove:
        os.remove(zip_path)


# We use a visitor pattern to check out the contents of the file.
# the 'inspector' function will be called for each element in the file hierarchy.
def inspector(name, node):
    # hdf5 files contain 'Dataset' that hold the actual data. With the function below we print
    # the name and shape if the inspector function encounters a dataset
    if isinstance(node, h5py.Dataset):
        print("The h5 file contains a dataset @", name, "with shape", node.shape)


# Assuming labels is a dictionary containing various types including NumPy arrays
def convert_to_serializable(obj):
    if isinstance(obj, np.ndarray):
        return obj.tolist()
    elif isinstance(obj, np.int64):
        return int(obj)
    elif isinstance(obj, list):
        return [convert_to_serializable(item) for item in obj]
    else:
        return obj

class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        elif isinstance(obj, np.int64):
            return int(obj)
        return super(CustomEncoder, self).default(obj)

        
# convert images from hd5 to tiff:
# extract 5 images from 1 hd5 file and
# put them in a designated directory
def convert_hdf5_to_tif(paths, file_folders, data_folder):
    count = 0
    for file_path in tqdm(paths):
        with h5py.File(file_path, 'r') as f:
            # get image dataset
            marker = f["raw/marker/s0"][:]
            nucleus_image = f["raw/nuclei/s0"][:]
            cells = f["labels/cells/s0"][:]
            infected_labels = f["labels/infected/nuclei/s0"][:]
            serum_image = f["raw/serum_IgG/s0"][:]
            nuclei_labels = f["labels/nuclei/s0"][:]
            table_infected = f["tables/infected_labels/cells"][:]
            # print(f'Image Dataset info: Shape={marker.shape},Dtype={marker.dtype}')
            img_ds = {
                "marker_image": marker,
                "nucleus_image": nucleus_image,
                "cell_labels": cells,
                "infected_labels": infected_labels,
                "serum_image": serum_image,
                "nucleus_labels": nuclei_labels
            }
            # create a subdirectory for each hd5 file
            folder_name = f"gt_image_{count:03}"
            file_folders.append(folder_name)
            img_dir = os.path.join(data_folder, folder_name)
            os.makedirs(img_dir, exist_ok=True)
            bboxes = {}
            for key, value in img_ds.items():
                img_name = f"{img_dir}_{key}.tif"
                imageio.imwrite(img_name, value, compression="zlib")
                if "cell" in img_name:
                    im = imageio.imread(img_name)
                    regions = regionprops(im)
                    for props in regions:
                        bboxes[props.label] = props.bbox
                # copy to subdirectoy
                move(img_name, os.path.join(img_dir, os.path.basename(img_name)))
            # convert from byte to float, then to int
            table_infected = (table_infected.astype(float)).astype(int)
            labels = {
                "cells": [
                    {
                        "cell_id": id_value,
                        "infected_label": status,
                        "bbox": bboxes[id_value] if id_value in bboxes.keys() else None
                    } for id_value, status in zip(table_infected[:, 0], table_infected[:, 1])
                ]
            }
            # Assuming labels is a dictionary containing various types including NumPy arrays and int64
            labels_serializable = {key: value for key, value in labels.items()}
            
            # Write to JSON file using the custom encoder
            with open("labels.json", "w") as f:
                json.dump(labels_serializable, f, ensure_ascii=False, cls=CustomEncoder)

            move("labels.json", os.path.join(img_dir, "labels.json"))
            count += 1
    return file_folders


def divide_data(n_train, n_val, file_folders, data_folder):

    train_folder = os.path.join(data_folder, "train")
    os.makedirs(train_folder, exist_ok=True)
    for train_image_dir in file_folders[:n_train]:
        if (not os.path.exists(os.path.join(train_folder, train_image_dir))):
            move(
                os.path.join(data_folder, train_image_dir),
                os.path.join(train_folder, os.path.basename(train_image_dir))
            )

    val_folder = os.path.join(data_folder, "val")
    os.makedirs(val_folder, exist_ok=True)
    for val_image_dir in file_folders[n_train:n_train+n_val]:
        if (not os.path.exists(os.path.join(val_folder, val_image_dir))):
            move(os.path.join(data_folder, val_image_dir), os.path.join(val_folder, os.path.basename(val_image_dir)))

    test_folder = os.path.join(data_folder, "test")
    os.makedirs(test_folder, exist_ok=True)
    for test_image_dir in file_folders[n_train+n_val:]:
        if (not os.path.exists(os.path.join(test_folder, test_image_dir))):
            move(os.path.join(data_folder, test_image_dir), os.path.join(test_folder, os.path.basename(test_image_dir)))
    return train_folder, val_folder, test_folder


# function to combine all data preparation steps
def prepare_data(data_folder="data", remove_h5=True):
    """
    :param string data_folder: folder for saving the data
    :param remove_h5: remove the h5 files after converting to tif
    :returns:
        - train_folder - path to folder with subfolders for training data
        - val_folder - path to folder with subfolders for validation data
        - test_folder - path to folder with subfolders for testing data
    """
    os.makedirs(data_folder, exist_ok=True)
    data_url = "https://zenodo.org/record/5092850/files/covid-if-groundtruth.zip?download=1"
    download_url(data_url, os.path.join(data_folder, "data.zip"))
    unzip(os.path.join(data_folder, "data.zip"), data_folder, remove=True)
    file_paths = glob(os.path.join(data_folder, "*.h5"))
    file_folders = []
    file_folders = convert_hdf5_to_tif(file_paths, file_folders, data_folder)
    train_folder, val_folder, test_folder = divide_data(35, 5, file_folders, data_folder)
    if remove_h5:
        for h5_file in file_paths:
            os.remove(h5_file)
    # double check that we have the correct number of images in the split folders
    print("We have", len(os.listdir(train_folder)), "training images in", train_folder)
    print("We have", len(os.listdir(val_folder)), "validation images in", val_folder)
    print("We have", len(os.listdir(test_folder)), "test images in", test_folder)


if __name__ == "__main__":
    prepare_data()
