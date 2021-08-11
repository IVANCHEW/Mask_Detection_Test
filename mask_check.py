import cv2
import sys
from imutils import face_utils
import numpy as np
import argparse
import imutils
# ~ import dlib

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

for i in range(1,9):
	fileName = "/home/ivan/Documents/AdB_Data/LOAB_Mask_Check/images/maksssksksss" + str(i) + ".png"
	print(fileName)
	img = cv2.imread(fileName)
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	gray = cv2.equalizeHist(gray)
	faces = face_cascade.detectMultiScale(gray, 1.05, 4)
	for (x, y, w, h) in faces:+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
		cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
	# ~ eyes = eye_cascade.detectMultiScale(gray)
	# ~ for (x2, y2, w2, h2) in eyes:
		# ~ eye_center = 
	cv2.imshow('image' + str(i),img)
	cv2.waitKey(0)

# ~ img = cv2.imread("/home/ivan/Documents/AdB_Data/LOAB_Mask_Check/images/maksssksksss1.png")
# ~ gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# ~ faces = face_cascade.detectMultiScale(gray, 1.1, 4)
# ~ faces = face_cascade.detectMultiScale(image=gray, scaleFactor=1.05, minNeighbors=4, minSize=(20,20), maxSize=(100,100))

# ~ for (x, y, w, h) in faces:
        # ~ cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

# ~ cv2.imshow('image',img)
# ~ cv2.waitKey(0)
