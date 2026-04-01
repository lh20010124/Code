import cv2
import cv2 as cv
import numpy as np

imagePath = 'data/messi5.jpg'
img = cv.imread(imagePath)

# 通过行列坐标访问像素值
px = img[100,100]
print(px)
# 只访问蓝色像素
blue = img[100,100,0]
print(blue)
# 修改像素值
img[100,100] = [255,255,255]
print(img[100,100])

# 图像属性
print(img.shape)
print(img.size)
print(img.dtype)

# ROI
ball = img[280:340,330:390]
img[273:333,100:160] = ball
cv2.imshow('img',img)

# 分割和合并图像通道
b,g,r = cv2.split(img)
img = cv2.merge((b,g,r))
b = img[:,:,0]
cv2.imshow('b',b)
img[:,:,2] = 0
cv2.imshow('img',img)





cv2.waitKey(0)