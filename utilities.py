# imports
import matplotlib.pylab as plt
import numpy as np
import skimage
import skimage.io as io
import skimage.exposure
import skimage.feature
import skimage.filters
import skimage.morphology
import skimage.transform
from skimage.filters import threshold_otsu
from joblib import load
import sys


def segmentation(img):
    th = threshold_otsu(img)
    img1 = img > th
    return img1 + 0.0

def contour_detection(img):
    return skimage.measure.find_contours(img)

def dfs(img, v, r, c, i, j):
    s = 1
    v[i][j] = 1
    stack = []
    stack.append((i,j))
    while (len(stack) != 0):
        (i,j) = stack.pop()
        
        if i+1 < r and v[i+1][j] == 0 and img[i+1][j] < 0.5:
            v[i+1][j] = 1
            s = s + 1
            stack.append((i+1,j))

        if i-1 > -1 and v[i-1][j] == 0 and img[i-1][j] < 0.5:
            v[i-1][j] = 1
            s = s + 1
            stack.append((i-1,j))

    
        if j+1 < c and v[i][j+1] == 0 and img[i][j+1] < 0.5:
            v[i][j+1] = 1
            s = s + 1
            stack.append((i,j+1))


        if j-1 > -1 and v[i][j-1] == 0 and img[i][j-1] < 0.5:
            v[i][j-1] = 1
            s = s + 1
            stack.append((i,j-1))
    return s
    
def connected_components(img):
    r,c = np.shape(img)
    v = np.zeros((r, c))
    t = []
    for i in range(r):
        for j in range(c):
            if v[i][j] == 0 and img[i][j] < 0.5:
                t.append(dfs(img, v, r, c, i, j))
    return t

def getSymboles(image):
    k = 0
    img = skimage.exposure.equalize_adapthist(image)
    
    if np.shape(img)[0] > 500 and np.shape(img)[1] > 500:
        img = skimage.morphology.erosion(image + 0.0)

    img = skimage.filters.gaussian(img, sigma=2)
    segm = segmentation(img)

    countours = contour_detection(segm)
    rem_countors = [False] * len(countours)

    for i in range(len(countours)):
        countour = countours[i]
        if not (max(countour[:,0]) - min(countour[:,0]) > img.shape[0]*0.016 and \
            max(countour[:,1]) - min(countour[:,1]) > img.shape[1]*0.016 and \
            max(countour[:,0]) - min(countour[:,0]) < img.shape[0]*0.083 and \
            max(countour[:,1]) - min(countour[:,1]) < img.shape[1]*0.083 and \
            len(countour[:,0]) > (img.shape[1] + img.shape[0])/25 and \
            (max(countour[:,0]) - min(countour[:,0]))/(max(countour[:,1]) - min(countour[:,1])) < 2.53 and \
            (max(countour[:,1]) - min(countour[:,1]))/(max(countour[:,0]) - min(countour[:,0])) < 2.53):
                rem_countors[i] = True  

    for i in range(len(countours)):
        if not rem_countors[i]:
            xi = min(countours[i][:,0])
            yi = min(countours[i][:,1])
            Xi = max(countours[i][:,0])
            Yi = max(countours[i][:,1])
            Ai = (Xi-xi)*(Yi-yi)
            for j in range(len(countours)):
                if not rem_countors[j]:
                    xj = min(countours[j][:,0])
                    yj = min(countours[j][:,1])
                    Xj = max(countours[j][:,0])
                    Yj = max(countours[j][:,1])
                    Aj = (Xj-xj)*(Yj-yj)
                    if  xi <= xj and yi <= yj and Xi >= Xj and Yi >= Yj and i != j:
                        if Ai > 9 * Aj:
                            rem_countors[i] = True
                        else:
                            rem_countors[j] = True

    symbolesList=[]
    for i in range(len(countours)):
        countour = countours[i]
        if not rem_countors[i]:
            img_sec = image[int(min(countour[:,0])) : int(max(countour[:,0])),int(min(countour[:,1])) : int(max(countour[:,1]))] + 0.0
            avg_x = (min(countour[:,0]) + max(countour[:,0])) / 2
            avg_y = (min(countour[:,1]) + max(countour[:,1])) / 2
            img_sec_seg = segmentation(img_sec)
            t = connected_components(img_sec_seg)
            if not (len(t) > 5 or (min(t) > 20 and len(t) > 2)) and \
                max(t)/(len(img_sec_seg)*len(img_sec_seg[0])) > 0.175 and max(t)/(len(img_sec_seg)*len(img_sec_seg[0])) < 0.875:                
                # io.imsave('./imagesList/' + str(k) + '.jpg', skimage.transform.resize(img_sec_seg, (40,30)) + 0.0 )
                k = k + 1
                symbolesList.append((skimage.transform.resize(img_sec_seg, (40,30)), avg_x, avg_y))

    return symbolesList

def predict(image, modelPath='model/KNN_model.joblib'):
    # load the model
    model = load(modelPath)
    prediction =  model.predict([image.flatten()])[0]
    return prediction


# map the classes names
def classification_mapping(classification):
    if classification != '10':
        return classification[0].upper()
    else:
        return '10'


def isSymbol(variable):
    letters = ['C', 'S', 'D', 'H']
    if (variable[0] in letters):
        return True
    else:
        return False


def isNumber(variable):
    return not isSymbol(variable)

def grouping(features):
    symbols = list(filter(isSymbol, features))
    numbers = list(filter(isNumber, features))

    minDists = [('-1', sys.maxsize)] * len(numbers)

    cards = [()] * len(numbers)
    for n in range(len(numbers)):
        for s in range(len(symbols)):
            dist = (numbers[n][1] - symbols[s][1]) ** 2 + \
                (numbers[n][2] - symbols[s][2]) ** 2
            if dist < minDists[n][1]:
                minDists[n] = (symbols[s][0], dist)
        cards[n] = (numbers[n][0], minDists[n][0])
        
    return set(cards) 
    

