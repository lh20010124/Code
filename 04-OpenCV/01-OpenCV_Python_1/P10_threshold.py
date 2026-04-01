import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# 1. 以灰度模式读取图像
# 'data/gradient.png' 应该是一张从黑到白的渐变图，这样能最直观地看到阈值切割的位置
# cv.IMREAD_GRAYSCALE (或 0): 强制以单通道灰度模式读取
img = cv.imread('data/gradient.png', cv.IMREAD_GRAYSCALE)

# 2. 应用 5 种不同的阈值处理模式
# cv.threshold(src, thresh, maxval, type)
# - src: 输入图
# - thresh: 阈值 (这里设为 127，即中点)
# - maxval: 最大值 (这里设为 255)，当像素满足条件时赋予的值
# - type: 阈值模式

# 模式 1: Binary (二值化)
# 规则: 像素 > 127 ? 设为 255 : 设为 0
# 效果: 图像只有黑(0)和白(255)两种颜色，界限分明
ret1, thresh1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)

# 模式 2: Binary Inverse (反向二值化)
# 规则: 像素 > 127 ? 设为 0 : 设为 255
# 效果: 与上面相反，亮的地方变黑，暗的地方变白
ret2, thresh2 = cv.threshold(img, 127, 255, cv.THRESH_BINARY_INV)

# 模式 3: Truncate (截断)
# 规则: 像素 > 127 ? 设为 127 : 保持原值
# 效果: 亮于 127 的部分被“削平”为灰色(127)，暗部细节保留。整张图不会有纯白。
ret3, thresh3 = cv.threshold(img, 127, 255, cv.THRESH_TRUNC)

# 模式 4: To Zero (化零)
# 规则: 像素 > 127 ? 保持原值 : 设为 0
# 效果: 亮部细节保留，暗于 127 的部分全部变黑(0)。
ret4, thresh4 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO)

# 模式 5: To Zero Inverse (反向化零)
# 规则: 像素 > 127 ? 设为 0 : 保持原值
# 效果: 暗部细节保留，亮于 127 的部分全部变黑(0)。
ret5, thresh5 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO_INV)

# 3. 准备绘图数据
titles = ['Original Image', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]

# 4. 使用 Matplotlib 显示对比
for i in range(6):
    # 创建 2行3列 的子图，当前绘制第 i+1 个
    plt.subplot(2, 3, i + 1)

    # 绘制图像
    # 'gray': 指定颜色映射为灰度
    # vmin=0, vmax=255: 关键参数！
    # 强制 Matplotlib 将 0 映射为全黑，255 映射为全白。
    # 如果不加这两个参数，Matplotlib 会自动根据当前图片的最小/最大值拉伸对比度，导致视觉误导（比如 TRUNC 模式看起来像 BINARY）。
    plt.imshow(images[i], 'gray', vmin=0, vmax=255)

    # 设置标题
    plt.title(titles[i])

    # 隐藏 x 和 y 轴的刻度
    plt.xticks([]), plt.yticks([])

plt.show()