import skimage.io as io
from utilities import getSymboles
from utilities import predict
from utilities import classification_mapping
from utilities import grouping
import matplotlib
import matplotlib.pyplot as plt

def main():
    image = io.imread("Grouping/AcetoFive.jpeg", as_gray=True)
    symbolesList = getSymboles(image)
    features = []
    for symbol in symbolesList:
        prediction = predict(symbol[0])
        prediction = classification_mapping(prediction)
        features.append((prediction, symbol[1], symbol[2]))
    cards = grouping(features)
    print(cards)

if __name__ == "__main__":
    main()
    try:
        pass

    except:
        print("Sea7k trb")
