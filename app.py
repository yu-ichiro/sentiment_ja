#!/usr/bin/env python
# coding:utf-8

import sys

import re
import time
import pickle
import sentiment
from keras.preprocessing.sequence import pad_sequences
from keras.models import load_model
import pickle

from flask import Flask, jsonify, request, abort, render_template

app = Flask(__name__, template_folder='templates')
app.config['JSON_AS_ASCII'] = False

maxlen = 280
model, graph = sentiment.load("models/model_2018-08-28-15:00.h5")

with open("models/tokenizer_cnn_ja.pkl", "rb") as f:
    tokenizer = pickle.load(f)

emolabels = ["happy", "sad", "disgust", "angry", "fear", "surprise"]

    

@app.route('/predict', methods=['POST'])
def prediction():
    if not request.form or 'sentence' not in request.form:
        abort(400)
    else:
        sentences = request.form['sentence'].split("\n")

    print(sentences)
    start_t = time.time()   
    results = sentiment.predict(sentences, graph, emolabels, tokenizer, model, maxlen)
    
    print('Elapsed: {:3.2f} msec'.format((time.time()-start_t)*1000))
    return jsonify(results), 201


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=False, port=18970, host="0.0.0.0", threaded=True)
