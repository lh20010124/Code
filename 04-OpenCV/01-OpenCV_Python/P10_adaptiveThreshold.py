import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# 1. 读取灰度图像
# 'data/sudoku.png' 是一个典型的光照不均的例子（可能有阴影覆盖）
img = cv.imread('data/sudoku.png', cv.IMREAD_GRAYSCALE)

# 2. 预处理：中值模糊 (Median Blur)
# 在进行阈值处理前，去噪非常关键。
# 中值滤波对去除“椒盐噪声”特别有效，同时能保留边缘信息。
# 参数 5 表示使用 5x5 的卷积核。
img = cv.medianBlur(img, 5)

# -----------------------------------------------------------
# 方法一：全局阈值 (Global Thresholding)
# -----------------------------------------------------------
# 整张图使用同一个阈值 127。
# 缺点：如果图片一部分很亮，一部分很暗（阴影），127 可能对亮部太低，对暗部太高，
# 导致结果中出现大片的黑色或白色区域，丢失信息。
ret1, th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)

# -----------------------------------------------------------
# 方法二：自适应阈值 (Adaptive Thresholding)
# -----------------------------------------------------------
# 这种方法会将图像分成很多小块，分别计算每一小块的阈值。
# 函数参数详解:
# cv.adaptiveThreshold(src, maxValue, adaptiveMethod, thresholdType, blockSize, C)

# 参数解释：
# - maxValue (255): 超过阈值的像素被赋予的值。
# - thresholdType (cv.THRESH_BINARY): 二值化类型。
# - blockSize (11): 邻域大小。计算阈值时参考当前像素周围 11x11 的区域。
# - C (2): 常数。最终阈值 = (区域计算出的平均值或加权值) - C。
#          这个 C 用于微调，正值有助于去除噪声（使背景更纯净）。

# 2.1 自适应 - 均值法 (Mean C)
# 阈值 T = (11x11 邻域内的平均值) - C
# 这种方法计算速度快，得到的线条较粗，但在去噪方面稍弱。
th2 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C,
                           cv.THRESH_BINARY, 11, 2)

# 2.2 自适应 - 高斯法 (Gaussian C)
# 阈值 T = (11x11 邻域内的加权和) - C
# 离中心点越近的像素权重越高。
# 这种方法通常能保留更多细节，图像看起来更自然。
th3 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C,
                           cv.THRESH_BINARY, 11, 2)

# 3. 可视化对比
titles = ['Original Image', 'Global Thresholding (v = 127)',
          'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
images = [img, th1, th2, th3]

for i in range(4):
    plt.subplot(2, 2, i + 1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()