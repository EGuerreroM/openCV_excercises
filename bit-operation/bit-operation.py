import cv2
import numpy as np

rectangle = np.zeros((300, 300), dtype='uint8')
circle = np.zeros((300, 300), dtype='uint8')
rectangleMask = cv2.rectangle(rectangle, (25, 25), (275, 275), 255, -1)
circleMask = cv2.circle(circle, (150, 150), 150, 255, -1)

bitwiseAnd = cv2.bitwise_and(rectangleMask, circleMask)
cv2.imshow('Rectangle', rectangleMask)
cv2.imshow('Circle', circleMask)
cv2.imshow('Bitwise AND', bitwiseAnd)
cv2.waitKey(0)


bitwiseOR = cv2.bitwise_or(rectangleMask, circleMask)
cv2.imshow('Bitwise OR', bitwiseOR)
cv2.waitKey(0)

bitwiseXOR = cv2.bitwise_xor(rectangleMask, circleMask)
cv2.imshow('Bitwise XOR', bitwiseXOR)
cv2.waitKey(0)
