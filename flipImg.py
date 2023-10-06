import numpy as np
import cv2

image = cv2.imread('assets/chicky.png')
cv2.imshow('Original', image)
cv2.waitKey()
flipHorizontal = cv2.flip(image, 1)
cv2.imshow('Horizontal Flip', flipHorizontal)
cv2.waitKey()
flipVertical = cv2.flip(image, 0)
cv2.imshow('Vertical Flip', flipVertical)
cv2.waitKey()
flipBoth = cv2.flip(image, -1)
cv2.imshow('Both Flip', flipBoth)
cv2.waitKey()
