import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# 1. 读取噪点图像
# 这张图片通常包含大量高斯噪声，导致直方图不平滑
img = cv.imread('data/noisy2.png')
# 转换为灰度图 (Otsu 算法是基于灰度直方图计算的)
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# -----------------------------------------------------------
# 情况 1: 普通的全局阈值 (Global Thresholding)
# -----------------------------------------------------------
# 硬性规定阈值为 127。
# 缺点: 无法适应噪声，噪点会被误判为前景或背景。
ret1, th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)

# -----------------------------------------------------------
# 情况 2: 直接使用 Otsu 阈值 (Otsu's Thresholding)
# -----------------------------------------------------------
# 参数解释:
# - 127: 在这里被忽略。当使用了 THRESH_OTSU 标志时，OpenCV 会忽略这个参数。
# - cv.THRESH_OTSU: 开启大津算法，自动计算最优阈值。
# 返回值 ret2: 算法计算出的最优阈值。
ret2, th2 = cv.threshold(img, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)

# -----------------------------------------------------------
# 情况 3: 高斯模糊 + Otsu 阈值 (Gaussian Blur + Otsu)
# -----------------------------------------------------------
# 3.1 先进行高斯模糊
# 作用: 平滑图像，去除噪点。
# 关键点: 模糊会将直方图中杂乱的锯齿抹平，使其呈现出明显的“双峰”结构 (Bimodal)。
#
blur = cv.GaussianBlur(img, (5, 5), 0)

# 3.2 对模糊后的图像应用 Otsu
# 由于直方图现在有两个清晰的峰值，Otsu 能非常准确地找到两峰之间的低谷作为阈值。
ret3, th3 = cv.threshold(blur, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)

# -----------------------------------------------------------
# 4. 可视化对比 (原图 vs 直方图 vs 结果)
# -----------------------------------------------------------
# 组织数据以便循环绘图
# 结构: [原图/模糊图, 0(占位), 结果图, ...]
images = [img, 0, th1,
          img, 0, th2,
          blur, 0, th3]

titles = ['Original Noisy Image', 'Histogram', 'Global Thresholding (v=127)',
          'Original Noisy Image', 'Histogram', f"Otsu Thresholding (v={int(ret2)})",
          'Gaussian filtered Image', 'Histogram', f"Otsu Thresholding (v={int(ret3)})"]

plt.figure(figsize=(10, 8)) # 设置画布大小，防止挤在一起

for i in range(3):
    # 第一列: 显示输入图像
    plt.subplot(3, 3, i * 3 + 1)
    plt.imshow(images[i * 3], 'gray')
    plt.title(titles[i * 3], fontsize=10)
    plt.xticks([]), plt.yticks([])

    # 第二列: 显示直方图
    # plt.hist(数据源, 桶的数量)
    # images[i*3].ravel(): 将二维图像数组展平为一维数组，因为 hist 需要一维数据
    plt.subplot(3, 3, i * 3 + 2)
    plt.hist(images[i * 3].ravel(), 256)
    plt.title(titles[i * 3 + 1], fontsize=10)
    plt.xticks([]), plt.yticks([])

    # 第三列: 显示二值化结果
    plt.subplot(3, 3, i * 3 + 3)
    plt.imshow(images[i * 3 + 2], 'gray')
    plt.title(titles[i * 3 + 2], fontsize=10)
    plt.xticks([]), plt.yticks([])

plt.tight_layout() # 自动调整子图间距
plt.show()