import cv2
import pytesseract 
from pytesseract import image_to_string
import matplotlib.pyplot as plt
from pytesseract import Output

img = cv2.imread('japanese.jpg')
print(image_to_string(img,"jpn"))
d = pytesseract.image_to_data(img, output_type=Output.DICT)
print(d.keys())
n_boxes = len(d['text'])
for i in range(n_boxes):
    if int(d['conf'][i]) <100:
        (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.imwrite("ok.jpg",img)
