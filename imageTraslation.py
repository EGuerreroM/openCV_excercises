import cv2
import numpy as np
from utils import imUtils


image = cv2.imread("assets/lena.jpg")
cv2.imshow("original", image)
cv2.waitKey(0)

M = np.float32([[1, 0, 25], [0, 1, 50]])
displacement = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("displacement down-right", displacement)
cv2.waitKey(0)
M = np.float32([[1, 0, -50], [0, 1, -90]])
displacement = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("displacement up-left", displacement)
cv2.waitKey(0)


# using imUtils
movedImage = imUtils.translate(image, 0, 100)
cv2.imshow("moved down", movedImage)
cv2.waitKey(0)
