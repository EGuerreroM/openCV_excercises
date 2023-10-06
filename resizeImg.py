import numpy as np
import cv2
from utils import imUtils

image = cv2.imread("assets/lena.jpg")
cv2.imshow("Original", image)
cv2.waitKey(0)
# resize to 100X120
resized = imUtils.resize(image, width=100)
cv2.imshow("Resized", resized)
cv2.waitKey(0)
resized = imUtils.resize(image, width=100, height=120)
cv2.imshow("Resized2", resized)
cv2.waitKey(0)

resized2 = imUtils.resize(image, width=600, height=600)
cv2.imshow("Resized3", resized2)
cv2.waitKey(0)
