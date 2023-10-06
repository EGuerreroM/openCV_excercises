import numpy as np
import cv2

image = cv2.imread('./assets/chicky.png')
cv2.imshow('Original', image)

mask = np.zeros(image.shape[:2], dtype='uint8')
(cX, cY) = (image.shape[1]//2, image.shape[0]//2)
cv2.rectangle(mask, (cX-150, cY-150), (cX+150, cY+150), 255, -1)
# cv2.rectangle(mask, (60, 30), (500, 350), 255, -1)
cv2.imshow('Mask', mask)

enmask = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow('Mask Applied to Image', enmask)
cv2.waitKey(0)

circleMask = np.zeros(image.shape[:2], dtype='uint8')
cv2.circle(circleMask, (cX, cY), 200, 255, -1)
circleEnMask = cv2.bitwise_and(image, image, mask=circleMask)
cv2.imshow('Circle Mask', circleMask)
cv2.imshow('Circle Mask Applied to Image', circleEnMask)
cv2.waitKey(0)
