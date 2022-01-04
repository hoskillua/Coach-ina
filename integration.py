import skimage.io as io
from utilities import getSymboles
from utilities import predict
from utilities import classification_mapping
from utilities import grouping


def main():
    image = io.imread("Grouping/cards4.jpg", as_gray=True)
    # io.imshow(image) 
    # io.show()
    symbolesList = getSymboles(image)
    features = []
    for symbol in symbolesList:
        # io.imshow(symbol[0]) 
        # io.show()
        prediction = predict(symbol[0])
        prediction = classification_mapping(prediction)
        features.append((prediction, symbol[1], symbol[2]))
    cards = grouping(features)
    print("Cards are:", cards)
    print("Total Number of Cards:", len(cards))

if __name__ == "__main__":
    try:
        main()
        pass

    except:
        print("Sea7k trb")
