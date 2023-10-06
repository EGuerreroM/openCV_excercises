import numpy as np
import cv2

image = cv2.imread('assets/chicky.png')
cv2.imshow('Original', image)
cv2.waitKey()

yStart = 30
yEnd = 120

xStart = 60
xEnd = 500

cut = image[yStart:yEnd, xStart:xEnd]
cv2.imshow('Cut', cut)
cv2.waitKey()
