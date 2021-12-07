import cv2
import pycapt
from PIL import Image
import ddddocr

test2 = cv2.imread("test2.png")

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
with open("test2.png", "rb") as f:
    img = f.read()
    print("处理前的识别 -> ", ocr.classification(img))


# cv2.waitKey(0)


