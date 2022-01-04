import skimage.io as io
from utilities import getSymboles
from utilities import predict
%matplotlib inline
import matplotlib
import matplotlib.pyplot as plt

def main():
    image = io.imread("Grouping/AcetoFive.jpeg", as_gray=True)
    plt.imshow(image)
    symbolesList = getSymboles(image)
    for symbol in symbolesList:
        prediction = predict(symbol)
        print("Prediction:", prediction)
        

if __name__ == "__main__":
    try:
        main()
        pass

    except:
        print("Sea7k trb")
