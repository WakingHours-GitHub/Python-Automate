import cv2 as cv

img = cv.imread("soucre.png")
img = cv.resize(img, (130, 50))
cv.imwrite("resize_img.png", img)