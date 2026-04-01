import cv2 as cv
import numpy as np

img = cv.imread('data/messi5.jpg')

# 获取图像的高度和宽度
# 注意：shape 返回的是 (行数/高度, 列数/宽度)，所以 rows 是高，cols 是宽
rows, cols = img.shape[:2]

# 1. 生成旋转矩阵 M
# cv.getRotationMatrix2D(center, angle, scale)
# 参数解释：
#   center: 旋转中心点坐标 (x, y)。这里设为图像中心 (cols/2, rows/2)
#   angle:  旋转角度。正值表示逆时针旋转，负值表示顺时针旋转。这里是逆时针 90 度。
#   scale:  缩放比例。1.0 表示保持原大小，0.5 表示缩小一半等。
M = cv.getRotationMatrix2D((cols / 2, rows / 2), 90, 1)

#

# 2. 应用仿射变换
# 第三个参数 (cols, rows) 依然是输出图像的画布尺寸 (宽度, 高度)
dst = cv.warpAffine(img, M, (cols, rows))

cv.imshow('dst', dst)
cv.waitKey(0)
cv.destroyAllWindows()