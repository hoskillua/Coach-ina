import cv2
import numpy as np
from PIL import Image
import os
import glob
import sys


def rotate(inputFolder, output_folder):

    sub_dirs = []
    for subdir, dirs, files in os.walk(inputFolder):
        sub_dirs.append(subdir)

    sub_dirs.pop(0)
    for subdir in sub_dirs:
        label = subdir.replace(input_folder, "")
        os.mkdir(f"{output_folder}/{label}")

        folderlen = len(subdir)
        for img in glob.glob(subdir + "/*.jpg"):
            image = cv2.imread(img)
            height, width = image.shape[:2]
            rotation_matrix = cv2.getRotationMatrix2D((width / 2, height / 2), 45, 0.5)
            rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))
            cv2.imwrite(f"{output_folder}/{label}" + img[folderlen:], rotated_image)


if __name__ == "__main__":
    input_folder = sys.argv[1]
    output_folder = sys.argv[2]
    rotate(input_folder, output_folder)
