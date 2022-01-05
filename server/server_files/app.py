from flask import Flask, request, Response
import numpy as np
import model
from model import predict
import base64
import cv2 as cv
from PIL import Image

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Welcome to COACH-INA"


@app.route("/api/get_games", methods=["GET"])
def get_games():
    return Response(["counter", "shayeb", "komy"], status=200)


@app.route("/api/predict", methods=["POST"])
def predict_img():
    try:
        file = request.files["image"]
        selected_game = request.form["selected_game"]

        print(selected_game)

        img = Image.open(file.stream).convert("L")

        img = np.array(img)

        prediction = predict(img)

        pred_str = "{" + f'"prediction" : {prediction}' + "}"

        return Response(pred_str, status=200)

    except Exception as err:
        return Response(err, status=501)


if __name__ == "__main__":

    app.run(port=8000)
