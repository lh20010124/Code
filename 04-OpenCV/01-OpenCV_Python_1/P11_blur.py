import cv2 as cv
import numpy as np

# 1. 读取原始图片
img = cv.imread('data/messi5.jpg')

# 2. 应用均值滤波 (Averaging / Box Blur)
# cv.blur(src, ksize)
# 参数 ksize=(5,5): 定义了 5x5 的卷积核。
# 意味着：每个像素的新值 = 它周围 5x5 区域内所有像素的平均值。
blured = cv.blur(img, (5, 5))

# 3. 显示结果
cv.imshow('Img', img)       # 原图 (清晰)
cv.imshow('Blurred', blured) # 模糊图 (细节丢失，变平滑)

cv.waitKey(0)
cv.destroyAllWindows()