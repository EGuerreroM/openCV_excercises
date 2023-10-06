from matplotlib import pyplot as plt
import numpy as np
import cv2

imagen = cv2.imread("assets/fruits.jpg")
imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

eq = cv2.equalizeHist(imagen)

cv2.imshow("Ecualización del histograma", np.hstack([imagen, eq]))
cv2.waitKey(0)

plt.figure()
plt.title("Histograma de la imagen")
plt.xlabel("Bins")
plt.ylabel("# de pixeles")
plt.plot(eq)
plt.xlim([0, 256])
plt.show()
cv2.waitKey(0)
