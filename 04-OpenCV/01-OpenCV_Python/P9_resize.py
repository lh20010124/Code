import cv2 as cv
import numpy as np

# 1. 读取图像
# 请确保当前目录下有 'data/messi5.jpg'，否则 img 为 None 会报错
img = cv.imread('data/messi5.jpg')

# -----------------------------------------------------------
# 方法一：使用缩放比例因子 (Scale Factors)
# -----------------------------------------------------------
# dsize=None: 表示我们不手动指定具体的长宽像素值
# fx=2, fy=2: x轴(宽度)和 y轴(高度) 都扩大为原来的 2 倍
# interpolation=cv.INTER_CUBIC: 使用“双三次插值”算法。
#   - 这种算法在放大图像时，比默认的线性插值(INTER_LINEAR)更清晰，
#   - 但计算量稍大，速度稍慢。
res1 = cv.resize(img, None, fx=2, fy=2, interpolation=cv.INTER_CUBIC)

# -----------------------------------------------------------
# 方法二：指定目标像素尺寸 (Specific Dimensions)
# -----------------------------------------------------------
# img.shape 返回的是一个元组: (高度 height, 宽度 width, 通道数 channels)
# [:2] 取前两个值，即高度和宽度
height, width = img.shape[:2]

# 计算目标尺寸
# !!! 注意坑点 !!!
# OpenCV 的 resize 函数中，dsize 参数的顺序是 (宽度, 高度) -> (x, y)
# 而 numpy shape 读出的顺序是 (高度, 宽度) -> (row, col)
# 所以这里必须写成 (2*width, 2*height)
target_size = (2 * width, 2 * height)

res2 = cv.resize(img, target_size, interpolation=cv.INTER_CUBIC)

# 3. 显示结果
cv.imshow('img', img)   # 原图
cv.imshow('res1', res1) # 方法一放大的图
cv.imshow('res2', res2) # 方法二放大的图 (效果应与 res1 完全一致)

# 4. 等待按键并退出
# 0 表示无限等待，直到用户按任意键
cv.waitKey(0)
cv.destroyAllWindows()