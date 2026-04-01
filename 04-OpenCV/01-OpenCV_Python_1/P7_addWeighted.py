import numpy as np
import cv2 as cv

# x = np.uint8([250])
# y = np.uint8([10])

# OpenCV加法是饱和运算
# Numpy加法是模运算
# print(cv.add(x,y))
# print(x + y)

img1 = cv.imread('data/ml.png')
img2 = cv.imread('data/opencv-logo.png')
img2 = cv.resize(img2,(308,380))
print(img2.shape)
assert img1 is not None, "1"
assert img2 is not None, "2"
dst = cv.addWeighted(img1,0.7,img2,0.3,0)
cv.imshow('dst',dst)
cv.waitKey(0)
cv.destroyAllWindows()