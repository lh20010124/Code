import cv2 as cv
import numpy as np

# 创建一个黑色图像
img = np.zeros((512, 512, 3), np.uint8)
# 绘制一条粗细为5像素的蓝色对角线
cv.line(img, (0, 0), (512, 512), (255, 0, 0), 5)
cv.rectangle(img, (0, 0), (100, 100), (0, 255, 0), 3)
cv.circle(img, (180, 180), 50, (0, 0, 255), 3)
cv.ellipse(img, (280, 280), (80, 60), 0, 0, 360, 255, -1)
pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
pts = pts.reshape((-1, 1, 2))
cv.polylines(img, [pts], True, (0, 255, 255), 3)
font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img, 'OpenCV', (10, 500), font, 1, (255, 255, 255), 3, cv.LINE_AA)

cv.imshow('img', img)
cv.waitKey(0)