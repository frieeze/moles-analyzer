import os
import sys

from flask import Flask
from flask import render_template
from flask import request

import fastai
from fastai.vision.all import *
from fastai.vision.widgets import *

fastai.layers.CrossEntropyLossFlat = fastai.losses.CrossEntropyLossFlat

app = Flask(__name__, static_url_path='', static_folder='templates',
            template_folder='templates')
learner = load_learner('./Resnet34_dataset1_6_modele.model', cpu=True)


@app.route('/', methods=['GET'])
def serve_index():
    return render_template("index.html")


@app.route('/', methods=['POST'])
def upload_predict():
    image_file = request.files["image"]
    if image_file:
        img = PILImage.create(image_file)

        pred, _, _ = learner.predict(img)
        return render_template("index.html", prediction=pred)


if __name__ == "__main__":
    app.run(port=int(os.environ.get("PORT", 12000)), debug=False)
