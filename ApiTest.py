from flask import Flask, flash, request
# import tensorflow as tf
#from werkzeug.utils import secure_filename
import cv2
import numpy
# from model import ORC

# PREDICT = ORC()
app = Flask(__name__)

@app.route('/')
def homepage():
    return "<h1> hello<h1>"

if __name__ == '__main__':
	app.run(debug=True, port=8080)	