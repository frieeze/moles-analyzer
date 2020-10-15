import os
import sys

from flask import Flask
from flask import render_template
from flask import request

import fastai
from fastai.vision.all import *
from fastai.vision.widgets import *

fastai.layers.CrossEntropyLossFlat = fastai.losses.CrossEntropyLossFlat

# app = Flask(__name__)


learner = load_learner('./export.pkl', cpu=True)

# model = pickle.load(open(os.path.join(path, 'export.pkl'), 'rb'))

# @app.route('/', methods=['GET', 'POST'])


def upload_predict():
    if request.method == "POST":
        image_file = request.files["image"]
        if image_file:
            img = PILImage.create(image_file)

            pred, _, _ = learner.predict(img)
            return render_template("index.html", prediction=1, pred=pred)

    return render_template("index.html", prediction=0)


if __name__ == "__main__":
    # app.run(port=12000, debug=True)
    print("fin")
