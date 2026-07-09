import argparse
from pathlib import Path

import numpy as np
import pandas as pd
from skimage.color import rgb2gray
from skimage.feature import blob_log
from skimage.io import imread


TIFF_EXTENSIONS = {".tif", ".tiff"}


def find_images(input_folder):
    image_paths = [
        path
        for path in Path(input_folder).iterdir()
        if path.is_file() and path.suffix.lower() in TIFF_EXTENSIONS
    ]
    return sorted(image_paths)


def is_rgb_image(image):
    return image.ndim >= 3 and image.shape[-1] in (3, 4)


def spatial_ndim(image):
    if is_rgb_image(image):
        return image.ndim - 1
    return image.ndim


def image_for_detection(image):
    if is_rgb_image(image):
        return rgb2gray(image[..., :3])
    return image


def detect_spots(image, min_sigma, max_sigma, num_sigma, threshold):
    detection_image = image_for_detection(image)
    blobs = blob_log(
        detection_image,
        min_sigma=min_sigma,
        max_sigma=max_sigma,
        num_sigma=num_sigma,
        threshold=threshold,
    )
    ndim = detection_image.ndim
    if len(blobs) == 0:
        return np.empty((0, ndim), dtype="float64")
    return blobs[:, :ndim]


def empty_points(ndim):
    return np.empty((0, ndim), dtype="float64")


def save_points_csv(output_path, points):
    points = np.asarray(points, dtype="float64")
    if points.ndim != 2:
        raise ValueError(f"Expected point data with shape (n_points, ndim), got {points.shape}.")

    columns = [f"axis-{axis}" for axis in range(points.shape[1])]
    table = pd.DataFrame(points, columns=columns)
    table.insert(0, "index", np.arange(len(table)))
    table.to_csv(output_path, index=False)


def configure_cache_locations(output_folder):
    output_folder = Path(output_folder)
    output_folder.mkdir(parents=True, exist_ok=True)


class BatchPointAnnotator:
    def __init__(self, image_paths, output_folder, args):
        import napari
        from qtpy.QtWidgets import QLabel, QPushButton, QVBoxLayout, QWidget

        self.napari = napari
        self.image_paths = image_paths
        self.output_folder = Path(output_folder)
        self.output_folder.mkdir(parents=True, exist_ok=True)
        self.args = args

        self.viewer = napari.Viewer()
        self.image_layer = None
        self.points_layer = None
        self.current_index = 0

        self.status = QLabel()
        self.next_button = QPushButton("Save and load next")
        self.next_button.clicked.connect(self.next_image)

        widget = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(self.status)
        layout.addWidget(self.next_button)
        widget.setLayout(layout)
        self.viewer.window.add_dock_widget(widget, area="right", name="Batch point annotation")

        self.load_current_image()

    def output_path(self):
        return self.output_folder / f"{self.image_paths[self.current_index].stem}.csv"

    def load_current_image(self):
        image_path = self.image_paths[self.current_index]
        image = imread(image_path)
        ndim = spatial_ndim(image)

        self.viewer.layers.clear()
        self.image_layer = self.viewer.add_image(image, name=image_path.name, rgb=is_rgb_image(image))

        if self.args.detect_spots:
            points = detect_spots(
                image,
                min_sigma=self.args.min_sigma,
                max_sigma=self.args.max_sigma,
                num_sigma=self.args.num_sigma,
                threshold=self.args.threshold,
            )
        else:
            points = empty_points(ndim)

        self.points_layer = self.viewer.add_points(points, name="points", size=self.args.point_size)
        self.points_layer.mode = "add"
        self.viewer.layers.selection.active = self.points_layer

        n_images = len(self.image_paths)
        self.status.setText(f"{self.current_index + 1} / {n_images}: {image_path.name}")
        if self.current_index == n_images - 1:
            self.next_button.setText("Save and close")
        else:
            self.next_button.setText("Save and load next")

    def save_current_points(self):
        output_path = self.output_path()
        save_points_csv(output_path, self.points_layer.data)
        print(f"Saved {output_path}")

    def next_image(self):
        self.save_current_points()
        self.current_index += 1
        if self.current_index == len(self.image_paths):
            self.viewer.close()
            return
        self.load_current_image()


def parse_args():
    parser = argparse.ArgumentParser(
        description="Annotate point detections for a folder of tif images in napari."
    )
    parser.add_argument("input_folder", help="Folder containing .tif or .tiff images.")
    parser.add_argument("output_folder", help="Folder where point CSV files will be written.")
    parser.add_argument(
        "--detect-spots",
        action="store_true",
        help="Initialize the points layer with skimage.feature.blob_log detections.",
    )
    parser.add_argument(
        "--min-sigma",
        type=float,
        default=1,
        help="Minimum sigma for blob_log spot detection. Only used with --detect-spots.",
    )
    parser.add_argument(
        "--max-sigma",
        type=float,
        default=8,
        help="Maximum sigma for blob_log spot detection. Only used with --detect-spots.",
    )
    parser.add_argument(
        "--num-sigma",
        type=int,
        default=10,
        help="Number of sigma values for blob_log spot detection. Only used with --detect-spots.",
    )
    parser.add_argument(
        "--threshold",
        type=float,
        default=0.1,
        help="Detection threshold for blob_log spot detection. Only used with --detect-spots.",
    )
    parser.add_argument(
        "--point-size",
        type=float,
        default=8,
        help="Display size for the napari points layer.",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    image_paths = find_images(args.input_folder)
    if len(image_paths) == 0:
        raise RuntimeError(f"No tif images found in {args.input_folder}.")

    configure_cache_locations(args.output_folder)
    annotator = BatchPointAnnotator(image_paths, args.output_folder, args)
    annotator.napari.run()


if __name__ == "__main__":
    main()
