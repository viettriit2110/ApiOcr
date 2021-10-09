from flask import Flask, flash, request
# import tensorflow as tf
#from werkzeug.utils import secure_filename
import cv2
import numpy
# from model import ORC

# PREDICT = ORC()
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    return "hello"

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8080)	