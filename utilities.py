# imports
import os
from matplotlib import pyplot as plt
from skimage.color import rgb2gray
from skimage import data, io, filters, feature, measure, transform, morphology
import matplotlib.pylab as plt
import numpy as np
import skimage
import skimage.exposure
import skimage.feature
import skimage.filters
import skimage.io as io
import skimage.morphology
import skimage.transform
from joblib import load
from skimage import transform, util
from skimage.filters import gaussian, threshold_otsu
from skimage.transform import AffineTransform, rotate, warp
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier
import cv2

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
    stack.append((i, j))
    while (len(stack) != 0):
        (i, j) = stack.pop()

        if i+1 < r and v[i+1][j] == 0 and img[i+1][j] < 0.5:
            v[i+1][j] = 1
            s = s + 1
            stack.append((i+1, j))

        if i-1 > -1 and v[i-1][j] == 0 and img[i-1][j] < 0.5:
            v[i-1][j] = 1
            s = s + 1
            stack.append((i-1, j))

        if j+1 < c and v[i][j+1] == 0 and img[i][j+1] < 0.5:
            v[i][j+1] = 1
            s = s + 1
            stack.append((i, j+1))

        if j-1 > -1 and v[i][j-1] == 0 and img[i][j-1] < 0.5:
            v[i][j-1] = 1
            s = s + 1
            stack.append((i, j-1))
    return s


def connected_components(img):
    r, c = np.shape(img)
    v = np.zeros((r, c))
    t = []
    for i in range(r):
        for j in range(c):
            if v[i][j] == 0 and img[i][j] < 0.5:
                t.append(dfs(img, v, r, c, i, j))
    return t


def getGreyImage(image):
    image = image.astype(float)
    R = image[:, :, 0]
    G = image[:, :, 1]
    B = image[:, :, 2]
    mask = (R - G > 70) & (R - B > 70)
    R[mask] = 0
    return rgb2gray(image).astype(float)


def getSymboles(image):
    k = 0
    img = image

    # if np.shape(img)[0] > 500 and np.shape(img)[1] > 500:
    #     img = skimage.morphology.erosion(img + 0.0)

    img = skimage.filters.gaussian(img, sigma=2)
    segm = segmentation(img)
    
    io.imshow(segm); io.show()

    countours = contour_detection(segm)
    rem_countors = [False] * len(countours)

    for i in range(len(countours)):
        countour = countours[i]
        if not (max(countour[:, 0]) - min(countour[:, 0]) > img.shape[0]*0.016 and
                max(countour[:, 1]) - min(countour[:, 1]) > img.shape[1]*0.016 and
                max(countour[:, 0]) - min(countour[:, 0]) < img.shape[0]*0.083 and
                max(countour[:, 1]) - min(countour[:, 1]) < img.shape[1]*0.083 and
                len(countour[:, 0]) > (img.shape[1] + img.shape[0])/25 and
                (max(countour[:, 0]) - min(countour[:, 0]))/(max(countour[:, 1]) - min(countour[:, 1])) < 2.53 and
                (max(countour[:, 1]) - min(countour[:, 1]))/(max(countour[:, 0]) - min(countour[:, 0])) < 2.53):
            rem_countors[i] = True

    for i in range(len(countours)):
        if not rem_countors[i]:
            xi = min(countours[i][:, 0])
            yi = min(countours[i][:, 1])
            Xi = max(countours[i][:, 0])
            Yi = max(countours[i][:, 1])
            Ai = (Xi-xi)*(Yi-yi)
            for j in range(len(countours)):
                if not rem_countors[j]:
                    xj = min(countours[j][:, 0])
                    yj = min(countours[j][:, 1])
                    Xj = max(countours[j][:, 0])
                    Yj = max(countours[j][:, 1])
                    Aj = (Xj-xj)*(Yj-yj)
                    if xi <= xj and yi <= yj and Xi >= Xj and Yi >= Yj and i != j:
                        if Ai > 9 * Aj:
                            rem_countors[i] = True
                        else:
                            rem_countors[j] = True

    symbolesList = []
    for i in range(len(countours)):
        countour = countours[i]
        if not rem_countors[i]:
            img_sec = image[int(min(countour[:, 0])): int(max(countour[:, 0])), int(
                min(countour[:, 1])): int(max(countour[:, 1]))] + 0.0
            avg_x = (min(countour[:, 0]) + max(countour[:, 0])) / 2
            avg_y = (min(countour[:, 1]) + max(countour[:, 1])) / 2
            img_sec_seg = segmentation(img_sec)
            t = connected_components(img_sec_seg)
            if not (len(t) > 5 or (min(t) > 20 and len(t) > 2)) and \
                    max(t)/(len(img_sec_seg)*len(img_sec_seg[0])) > 0.175 and max(t)/(len(img_sec_seg)*len(img_sec_seg[0])) < 0.875:
                # io.imsave('./imagesList/' + str(k) + '.jpg', skimage.transform.resize(img_sec_seg, (40,30)) + 0.0 )
                k = k + 1
                symbolesList.append((skimage.transform.resize(
                    img_sec_seg, (40, 30)), avg_x, avg_y))

    return symbolesList


def predict(image, modelPath='model/KNN_model.joblib'):
    # load the model
    model = load(modelPath)
    prediction =  model.predict([image.flatten()])[0]
    probabilities = model.predict_proba([image.flatten()])[0]
    classIndex =  np.where(model.classes_ == prediction)[0]

    return prediction, 1  # probabilities[classIndex]


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


############################################## Non Overlapping Algo  #######################################################################################

import os

import cv2
import numpy as np
from matplotlib import pyplot as plt
###Imports###
from skimage import data, feature, filters, io, measure, morphology, transform
from skimage.color import rgb2gray

####Algo Constants###
MAX_ANGLE = 160
MIN_ANGLE = 20

MAX_AREA = 0
MIN_AREA = 0

TRANS_CARD_HIEGHT = 350
TRANS_CARD_WIDTH = 250

CORNER_HIEGHT = 100
CORNER_WIDTH = 42
CORNER_THRESH = 60

SYMBOL_WIDTH = 30
SYMBOL_HEIGHT = 40

SUIT_BEGIN = 40
RANK_END = 50

###Helper Functions###

# calculate the distance between two points


def CalcDist(p1, p2):
    p1 = np.copy(p1)
    p2 = np.copy(p2)
    dist = np.sqrt((((p1-p2)**2).sum()))
    return dist

# calculate the perimeter of a contour


def CalcPerimeter(contour):
    ret = 0
    prev = contour[-1]
    for cur in contour:
        ret += CalcDist(cur, prev)
        prev = cur
    return ret

# caculate angle of three points using law of cosines
#arccos((P12^2 + P13^2 - P23^2) / (2 * P12 * P13))


def CalcAngle(points):
    p12 = CalcDist(points[0], points[1])
    p13 = CalcDist(points[2], points[1])
    p23 = CalcDist(points[0], points[2])

    angle = np.arccos((p12**2+p13**2-p23**2)/(2*p12*p13))
    return angle*180/np.arccos(-1)

# caculate Area a polygon using Shoelace formula


def CalcArea(x, y):
    area = 0.5*np.abs(np.dot(x, np.roll(y, 1))-np.dot(y, np.roll(x, 1)))
    return area


###Preprocessing Step###
def preprocessingStep(img):

    global MAX_AREA, MIN_AREA

    h = img.shape[0]
    w = img.shape[1]

    MAX_AREA = 0.314*w*h
    MIN_AREA = 0.014*w*h

    grayImg = rgb2gray(img)

    if(np.max(grayImg) < 1.01):
        grayImg = grayImg*255

    gaussedImg = filters.gaussian(grayImg)

    addedConst = 0
    thresh = filters.threshold_otsu(grayImg)+addedConst
    threImg = np.copy(gaussedImg)
    threImg[threImg > thresh] = 255
    threImg[threImg <= thresh] = 0

    return threImg

###Find and Filter Contours###

# check if the contour is likely to be a card


def CheckContour(contour):

    if(len(contour) != 5):
        return False

    area = CalcArea(contour[:4, 1], contour[:4, 0])
    if(area > MAX_AREA or area < MIN_AREA):
        return False

    points = np.copy(contour)
    points = np.vstack([points, points[1]])

    for i in range(4):
        angle = CalcAngle(points[i:i+3])
        if(angle > MAX_ANGLE or angle < MIN_ANGLE):
            return False

    return True

# get candidate cards


def findCardsStep(threImg):

    contours = measure.find_contours(threImg)

    cards = []
    for contour in contours:
        perimeter = CalcPerimeter(contour)
        approx = measure.approximate_polygon(contour, .08*perimeter)
        if(CheckContour(approx) == True):
            cards.append(approx)

    return cards

###Sort Card Corners###

# sort the corners of the card


def SortCorners(approxContour):

    corners = np.copy(approxContour[:4])

    maxIndx = 0
    maxDis = 0

    for i in range(4):
        dis = CalcDist(corners[i], corners[(i+1) % 4])
        if(dis > maxDis):
            maxIndx = i
            maxDis = dis

    shift = 0
    if(CalcDist(corners[maxIndx], corners[(maxIndx+1) % 4]) < CalcDist(corners[(maxIndx+1) % 4], corners[(maxIndx+2) % 4])):
        shift = maxIndx
    else:
        shift = maxIndx+1

    corners = np.roll(corners, -shift, axis=0)

    return corners

###Perspective Transform Step###


def perspectiveStep(cards, img):

    transCards = []

    for card in cards:
        dst = (SortCorners(card))[:, [1, 0]].astype(int)
        src = np.array([
            [0, 0],
            [TRANS_CARD_WIDTH, 0],
            [TRANS_CARD_WIDTH, TRANS_CARD_HIEGHT],
            [0, TRANS_CARD_HIEGHT]
        ])
        transMatrix = transform.ProjectiveTransform()
        transMatrix.estimate(src, dst)
        warpedImg = transform.warp(img, transMatrix, output_shape=(
            TRANS_CARD_HIEGHT, TRANS_CARD_WIDTH))
        transCards.append(warpedImg)

    return transCards

# Cut and Threshold the Top Left Corner

# get the rank,suit


def GetCorner(transImg):

    corner = transImg[10:CORNER_HIEGHT, 5:CORNER_WIDTH]

    grayCorner = rgb2gray(corner)

    if(np.max(grayCorner) < 1.01):
        grayCorner = grayCorner*255

    thresh = filters.threshold_otsu(grayCorner)

    threCorner = grayCorner.copy()
    threCorner[threCorner >= thresh] = 255
    threCorner[threCorner < thresh] = 0

    return threCorner

###Integrate and Get Corners###


def applyAlgo(img):
    threImg = preprocessingStep(img)
    cards = findCardsStep(threImg)
    transCards = perspectiveStep(cards, img)

    ret = []
    for transCard in transCards:
        ret.append(GetCorner(transCard))

    return ret

###Get the Largest Contour In The Corner -> which is the wanted symbol###

# get largest contour


def LargestContour(img):

    contours = measure.find_contours(img)

    maxArea = 0
    ret = []
    for contour in contours:
        area = CalcArea(contour[:, 1], contour[:, 0])
        if(area > maxArea):
            maxArea = area
            ret = contour

    if(len(ret) == 0):
        img = 125
        return img

    l = round(np.min(ret[:, 1]))
    r = round(np.max(ret[:, 1]))
    t = round(np.min(ret[:, 0]))
    b = round(np.max(ret[:, 0]))

    img = img[t:b, l:r]
    img = cv2.resize(img, (SYMBOL_WIDTH, SYMBOL_HEIGHT), 0, 0)

    return img

###Apply The Non Overlapping Algo On An Image###


def ApplyOnImage(image):

    corners = applyAlgo(image)

    splitedCorners = []

    for corner in corners:
        rankImg = corner[:RANK_END, :]
        suitImg = corner[SUIT_BEGIN:, :]

        rankImg = LargestContour(rankImg)
        suitImg = LargestContour(suitImg)

        splitedCorners.append((rankImg, suitImg))

    return splitedCorners
