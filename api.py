from flask import Flask, flash, request
# import tensorflow as tf
#from werkzeug.utils import secure_filename
import cv2
import numpy
from model import ORC

PREDICT = ORC()
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
	if request.method == 'POST':
		f = request.files['data']
		img = cv2.imdecode(numpy.fromstring(request.files['data'].read(), numpy.uint8), 1)
		return PREDICT.predict(img)
	return '''
    <h1>Upload new File</h1>
    <form method="post" enctype="multipart/form-data">
      <input type="file" name="data">
      <input type="submit">
    </form>
    '''

if __name__ == '__main__':
	app.run(debug=True, port=5050)	
