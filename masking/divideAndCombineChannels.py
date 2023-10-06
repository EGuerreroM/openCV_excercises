import numpy as np
import cv2

image = cv2.imread('./assets/fruits.jpg')
cv2.imshow('Original', image)

(b, g, r) = cv2.split(image)
cv2.imshow('Red', r)
cv2.imshow('Green', g)
cv2.imshow('Blue', b)
cv2.waitKey(0)

comb = cv2.merge([b, g, r])
cv2.imshow('Combined', comb)
cv2.waitKey(0)
cv2.destroyAllWindows()

zeros = np.zeros(image.shape[:2], dtype='uint8')
cv2.imshow('Red', cv2.merge([zeros, zeros, r]))
cv2.imshow('Green', cv2.merge([zeros, g, zeros]))
cv2.imshow('Blue', cv2.merge([b, zeros, zeros]))
cv2.waitKey(0)
