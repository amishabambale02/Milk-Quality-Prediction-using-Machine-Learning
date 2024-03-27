#!/usr/bin/env python
import os
import sys

from flask import Flask, request, jsonify, send_file, render_template
from io import BytesIO
from PIL import Image, ImageOps
import base64
import urllib
import pickle

import numpy as np
import scipy.misc
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
import os
import tensorflow as tf
import numpy as np
from tensorflow import keras
#from skimage import io
from tensorflow.keras.preprocessing import image


# Flask utils
from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer
from tensorflow.keras.models import load_model

from tensorflow.keras.models import load_model


app = Flask(__name__)
 

# Load your trained model
 


@app.route("/")
@app.route("/first")
def first():
	return render_template('first.html')
    
@app.route("/login")
def login():
	return render_template('login.html')

@app.route("/chart")
def chart():
	return render_template('chart.html')

@app.route("/performance")
def performance():
	return render_template('performance.html')


@app.route("/index",methods=['GET'])
def index():
	return render_template('index.html')



@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == "POST":


        Type = float(request.form['Type value'])
        pH = float(request.form['pH'])
        Temprature = float(request.form['Temprature'])
        Taste = float(request.form['Taste'])
        Odor = float(request.form['Odor'])
        Fat = float(request.form['Fat'])
        Turbidity = float(request.form['Turbidity'])
        Colour = float(request.form['Colour'])


        # create numpy array for all the inputs
        val = np.array([Type,pH, Temprature, Taste, Odor, Fat, Turbidity,Colour])

        # define save model and scaler path
        model_path = os.path.join(r'C:\Users\Shree\Downloads\Milk Quality Prediction using ML_11 JAN 2024\Milk Quality Prediction using ML_11 JAN 24\models', 'xgboost.sav')
        scaler_path = os.path.join(r'C:\Users\Shree\Downloads\Milk Quality Prediction using ML_11 JAN 2024\Milk Quality Prediction using ML_11 JAN 24\models', 'scaler.sav')

        # load the model and scaler
        model = pickle.load(open(model_path, 'rb'))
        scc = pickle.load(open(scaler_path, 'rb'))

        # transform the input data using pre fitted standard scaler
        data = scc.transform([val])

        # make a prediction for the given data
        res = model.predict(data)

        if res == 0:
            outcome = 'High Quality -> high quality milk has a very low number of somatic cells, a longer shelf-life, tastes better and is more nutritious. milk for dairy cows with a protein content of 7.39% - 9.63% indicating high quality'
        elif res == 1:
            outcome = 'Low Quality -> The classification of the quality of milk for dairy cows produces 3 levels of classification, namely milk for dairy cows with a protein content of 0% - 2.5% indicating low quality'
        else:
            outcome = 'Medium Quality -> The classification of the quality of milk for dairy cows produces 3 levels of classification, namely milk for dairy cows with a protein content of 2.51% - 7.38% indicating medium quality '
        return render_template('index.html', result=outcome)
    return render_template('index.html')
 
 

if __name__ == '__main__':
    app.run(debug=True)

