import numpy as np
import cv2
from utils import imUtils

image = cv2.imread('assets/lena.jpg')
cv2.imshow('Original', image)
cv2.waitKey(0)

# Store height and width of the image
height, width = image.shape[:2]

# get center coordinates of the image
center = (width/2, height/2)

M = cv2.getRotationMatrix2D(center, 45, 1.0)
rotatedImage = cv2.warpAffine(image, M, (width, height))
cv2.imshow('Rotated Image', rotatedImage)
cv2.waitKey(0)

# using imutils from utils/imUtils.py
rotatedImage2 = imUtils.rotateImage(image, 180)
cv2.imshow('Rotated Image 2', rotatedImage2)
cv2.waitKey(0)
