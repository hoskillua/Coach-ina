import os
import random

from skimage import transform
from skimage.transform import AffineTransform, rotate
from sklearn.neighbors import KNeighborsClassifier


def augmentImage(img):
    # original image
    augmentedImages=[img.flatten()]
    augmentedImages.append(img.flatten()) # add the image multiple times
    augmentedImages.append(img.flatten()) # add the image multiple times
    augmentedImages.append(img.flatten()) # add the image multiple times
    # rotation by i
    for i in range(1, 8):
        randomNum = random.randint(-5,5)
        image = rotate(img, angle=i*20 + randomNum, cval=1); augmentedImages.append(image.flatten())
        image = rotate(img, angle=-i*20 + randomNum, cval=1); augmentedImages.append(image.flatten())
    # Shearing
    image = transform.warp(img, AffineTransform(shear=-0.4), order=1, preserve_range=True, mode='wrap'); augmentedImages.append(image.flatten())
    image = transform.warp(img, AffineTransform(shear=0.4), order=1, preserve_range=True, mode='wrap'); augmentedImages.append(image.flatten())
    # Cropping by 7
    image = img.copy(); image[:, 23:] = 0; augmentedImages.append(image.flatten())
    image = img.copy(); image[:, 0:7] = 0; augmentedImages.append(image.flatten())
    image = img.copy(); image[0:7,:] = 0; augmentedImages.append(image.flatten())
    image = img.copy(); image[33:, :] = 0; augmentedImages.append(image.flatten())
    # Cropping by 10
    image = img.copy(); image[:, 20:] = 0; augmentedImages.append(image.flatten())
    image = img.copy(); image[:, 0:10] = 0; augmentedImages.append(image.flatten())
    image = img.copy(); image[0:10,:] = 0; augmentedImages.append(image.flatten())
    image = img.copy(); image[30:, :] = 0; augmentedImages.append(image.flatten())
    # inverse
    image = 1 - img.copy(); augmentedImages.append(image.flatten())
    return augmentedImages


# "model/DataSet/trainData" 
def getSets(path):
    trainData = []
    trainLabels = []
    dire=path
    numClassesWithLimit = 0
    LIMIT = 100000 # to have the same number of items in all classes
    for innerDir in os.listdir(dire):
        count = 0
        for filename in os.listdir(dire+'/' +innerDir):
            # read image
            image = cv2.imread(dire+'/' + innerDir +'/' +filename, cv2.COLOR_BGR2GRAY)/255.0

            # augmentImage
            augmentedImages = augmentImage(image.copy())
            count +=  len(augmentedImages)

            # append images
            trainData+=augmentedImages
            trainLabels+=[innerDir] * len(augmentedImages)

            # to break the inner loop if the number of items in the class exceeded the LIMIT
            if (count >= LIMIT):
                numClassesWithLimit+=1
                print("Class", innerDir , "has", count, "items")
                break
    return trainData, trainLabels

def getModel(trainData, trainLabels):
    model_KNN = KNeighborsClassifier(n_neighbors=17, weights='distance',n_jobs=-1) 
    model_KNN.fit(trainData, trainLabels)
