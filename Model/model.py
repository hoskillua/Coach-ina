import sys

from joblib import load

import cv2
from cv2 import imread
import numpy as np

PATH = "./rf_model.joblib"


def load_random_forest_model(path):
    return load(path)


model = load_random_forest_model(PATH)


def predict(image_path, isImage=True):
    """
    Expected Input: a grey scale image of shape (w_old, h_old)
    output: the output class of the image
    """
    if isImage == True:
        image = image_path

        if np.max(image_path) > 1:  # If the image is not normaized
            image /= 255.0

    else:
        image = imread(image_path, cv2.COLOR_BGR2GRAY) / 255.0

    image.resize(40, 30)

    image = image.flatten()
    y_pred = model.predict([image])
    return y_pred


if __name__ == "__main__":

    try:
        file_path = sys.argv[1]

        prediction = predict(file_path)
        print(f"Class for the image is {prediction}")

    except:
        print("You Should enter the input image file path")
