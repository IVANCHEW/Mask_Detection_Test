import cv2
import os
from xml.dom import minidom

i = 1
maskCount = 0
noMaskCount = 0

for i in range(0,852):
	imageFileName = "/home/ivan/Documents/AdB_Data/dataset/images/maksssksksss" + str(i) + ".png"
	xmlFile = minidom.parse("dataset/annotations/maksssksksss" + str(i) + ".xml")
	print(imageFileName)
	img = cv2.imread(imageFileName)

	classification = xmlFile.getElementsByTagName('name')
	xmin = xmlFile.getElementsByTagName('xmin')
	xmax = xmlFile.getElementsByTagName('xmax')
	ymin = xmlFile.getElementsByTagName('ymin')
	ymax = xmlFile.getElementsByTagName('ymax')

	print("Number of objects:" + str(classification.length))
	for j in range(0, classification.length):	

		extract = img[int(ymin[j].firstChild.data):
			int(ymax[j].firstChild.data),
			int(xmin[j].firstChild.data)
			:int(xmax[j].firstChild.data)]
				
		if classification[j].firstChild.data == "without_mask":
			cv2.imwrite("dataset/without_mask/without_mask" + str(noMaskCount) +'.png', extract)
			noMaskCount=noMaskCount+1
		elif classification[j].firstChild.data == "with_mask":
			cv2.imwrite("dataset/with_mask/with_mask" + str(maskCount) +'.png', extract)
			maskCount=maskCount+1
