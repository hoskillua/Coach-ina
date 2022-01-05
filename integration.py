from re import T
import skimage.io as io
from utilities import getSymboles
from utilities import getGreyImage
from utilities import predict
from utilities import classification_mapping
from utilities import grouping
from utilities import ApplyOnImage


def OverLapping(path, modelPath):

    image = io.imread(path)
    # io.imshow(image)
    # io.show()
    if len(image.shape) == 2:
        greyImage = image
    else:
        greyImage = getGreyImage(image)/255.0

    symbolesList = getSymboles(greyImage)

    features = []
    for symbol in symbolesList:
        io.imshow(symbol[0]); io.show()
        prediction, prob = predict(symbol[0], modelPath)
        if (prob > 0.8):
            prediction = classification_mapping(prediction)
            features.append((prediction, symbol[1], symbol[2]))
    cards = grouping(features)
    print("Cards are:", cards)
    print("Total Number of Cards:", len(cards))
    io.imshow(image)
    io.show()


def NonOverLapping(path, modelPath):

    image = io.imread(path)

    splitedCorners = ApplyOnImage(image)

    cards = []

    for corner in splitedCorners:
        io.imshow(corner[0]/255.0)
        io.show()
        io.imshow(corner[1]/255.0)
        io.show()
        p1 = predict(corner[0]/255.0, modelPath)
        p2 = predict(corner[1]/255.0, modelPath)

        p1 = classification_mapping(p1)
        p2 = classification_mapping(p2)
        cards.append((p1, p2))

    print("Cards are:", cards)
    print("Total Number of Cards:", len(cards))


def main():

    path = "../special/1.jpeg"
    modelPath = "Model/KNN_model.joblib"
    AlgoNum = 1

    if(AlgoNum == 0 or AlgoNum == 2):
        OverLapping(path, modelPath)
    if(AlgoNum == 1 or AlgoNum == 2):
        NonOverLapping(path, modelPath)


if __name__ == "__main__":
    main()

    try:
        pass

    except:
        print("Sea7k trb")
