'''
    Author: wjh776a68
    Date: 2021/01/03
    Function: Using Stitcher to stitch images with opencv's SIFT algorithm

'''

import cv2
from Stitcher import Stitcher
from matplotlib import pyplot as plt


imageA = cv2.imread("IMG_0077.JPEG")
imageB = cv2.imread("IMG_0078.JPEG")

# 把图像拼接成全景图
stitcher = Stitcher()
(result, vis) = stitcher.stitch([imageA, imageB], showMatches=True)

# 显示所有图片
cv2.imshow("Result", result)
cv2.imwrite("Result.jpg",result)
cv2.waitKey(0)
cv2.destroyAllWindows()
