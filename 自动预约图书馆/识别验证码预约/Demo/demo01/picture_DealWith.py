import cv2 as cv
import pycapt
import numpy as np

import matplotlib.pyplot as plt

import ddddocr

"""
test2 = cv2.imread("soucre.png")

pra = 0.9
height, width = test2.shape[:2]
# 此处要做integer强转,因为.resize接收的参数为形成新图像的长宽像素点个数
#
size = (int(height * pra), int(width * pra))
d = cv2.resize(test2, size, interpolation=cv2.INTER_LINEAR  )



cv2.imshow("img", test2)

cv2.imwrite("test4.png", d)
ocr = ddddocr.DdddOcr()
with open("test4.png", "rb") as f:
    img = f.read()

    print("处理后的识别 -> ",ocr.classification(img))
with open("soucre.png", "rb") as f:
    img = f.read()
    print("处理前的识别 -> ", ocr.classification(img))


# cv2.waitKey(0)


"""



ocr = ddddocr.DdddOcr()

srcimg = cv.imread("test2.png")

rows, cols = srcimg.shape[:2]
# shape是获取图像的像素和通道数
srcimg = cv.resize(srcimg, (12*rows, 3*cols), srcimg)



# cv.resize(srcimg, None, srcimg, fx=3, fy=3)

cv.imwrite("test4.png", srcimg)


# 普通图片的识别效果
with open("test2.png", "rb") as f:
    img = f.read()
    print(f"原始图像识别的效果: {ocr.classification(img)}")

# 缩放之后识别效果
with open("test4.png", "rb") as f:
    img = f.read()
    print(f"缩放之后识别的效果: {ocr.classification(img)}")

# 经过形态学处理后:
with open("test3.png", "rb") as f:
    img = f.read()
    print(f"经过形态学处理后识别的效果: {ocr.classification(img)}")

test3 = cv.imread("test3.png")

rows, cols = test3.shape[:2]
test3 = cv.resize(test3, (12*rows, 3*cols), test3)
test3 = cv.cvtColor(test3, cv.COLOR_BGRA2GRAY)
cv.imwrite("test5.png", test3)



with open("test5.png", "rb") as f:
    img = f.read()
    print(f"缩放后的,图形学处理的. 识别的效果: {ocr.classification(img)}")

# 2508测试通过
# 2302测试通过


test5 = cv.imread("test5.png")
# 对test5 进行平移操作
M = np.float32([[1,0,-50], [0, 1, 0]])
rows, cols = test5.shape[:2]
test5 = cv.resize(test5, (12*rows, 2*cols), test5)
test5 = cv.warpAffine(test5, M, (12*rows, 2*cols))

cv.imwrite("test6.png", test5)

with open("test6.png", "rb") as f:
    img = f.read()
    print(f"经过8：2的比例，图形学，缩放后的识别效果：{ocr.classification(img)}")

# 建议: 针对o单独处理为0
# 针对密集型: 拉伸是可以很好的解决这种问题的.
# 针对聚集且数字摆动比较大, 此时就需要图形学进行腐蚀, 降噪, 然后在拉伸

# 综上, 认为经过缩放后的效果要哦更好一代你




# 下面是基于我自己创建的一些形态学操作
# 形态学操作: 进行腐蚀与膨胀
# 腐蚀: 是途中高亮区域消除, 所以对于有色图像来说就是膨胀
test2 = cv.imread("test2.png")
fushi = np.ones((2, 2), np.uint8) # 创建一个5*5的1的卷积矩阵
test2 = cv.erode(test2, fushi) # 腐蚀
cv.imwrite("fushi.png", test2)

# pengzhang = np.zeros((3, 3), np.uint8)
pengzhang = np.matrix([
    [0,1,0],
    [1,1,1],
    [0,1,0]], np.uint8)
test5 = cv.dilate(test2, pengzhang)
cv.imwrite("pengzhang.png", test5)


