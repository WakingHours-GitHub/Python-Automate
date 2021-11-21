import cv2
import ddddocr
import numpy as np

ocr = ddddocr.DdddOcr()


img = cv2.imread("test2.png")
# img = cv2.pyrMeanShiftFiltering(img, sp=0, sr=50)
img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
ret, binary = cv2.threshold(img, 5, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
# 形态学操作   腐蚀  膨胀
# erode = cv2.erode(binary, None, iterations=1)
# dilate = cv2.dilate(erode, None, iterations=1)
# blur = cv2.GaussianBlur(dilate, (5, 5), 0)  # 高斯滤波
cv2.imwrite("test3.png", binary)

with open("test3.png", "rb") as f:
    buff = f.read()
print(ocr.classification(buff))


# cv2.imshow("img", img)
cv2.waitKey(0)

"""
img = cv2.imread("test2.png", cv2.IMREAD_GRAYSCALE)
a = 1
# 线性变换  定义float类型
O = float(a) * img
# 数据截取  如果大于255 取 255
O[0 > 255] = 255
# 数据类型的转换
O = np.round(O)
O = O.astype(np.uint8)
cv2.imshow("img2", img)
cv2.imshow('enhance', O)
cv2.imwrite("test3.png",O)

cv2.waitKey(0)
cv2.destroyAllWindows()
"""
