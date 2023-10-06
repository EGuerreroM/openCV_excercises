import cv2

image = cv2.imread('assets/lena.jpg')
cv2.imshow('original', image)
cv2.waitKey(0)
# (b, g, r) = image[0, 0]
# print("Pixel in (0,0) - red :{}, green :{}, blue :{}".format(r, g, b))
# image[0, 0] = (0, 0, 255)
# (b, g, r) = image[0, 0]
# print("Pixel in (0,0) - red :{}, green :{}, blue :{}".format(r, g, b))
# cv2.imshow("modified", image)
# cv2.waitKey(0)

# parse image
corner = image[0:100, 0:100]
cv2.imshow("corner", corner)
cv2.waitKey(0)
image[0:100, 0:100] = (0, 255, 0)
cv2.imshow("modified", image)
cv2.waitKey(0)
