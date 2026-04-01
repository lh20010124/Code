import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('data/messi5.jpg')
# 为了避免计算溢出 (uint8 加法超过 255 会回卷)，先转换为浮点数
img_float = img.astype(np.float32)

# 1. 生成高斯噪声矩阵
# 参数: (均值, 标准差, 形状)
# mean = 0: 噪声平均值为 0，不改变图像整体亮度
# sigma = 25: 标准差越大，噪声越明显
mean = 0
sigma = 25
noise = np.random.normal(mean, sigma, img_float.shape)

# 2. 将噪声叠加到图像上
noisy_img = img_float + noise

# 3. 截断与转换 (非常重要!)
# 加法可能导致像素值 < 0 或 > 255，需要用 clip 限制范围
noisy_img = np.clip(noisy_img, 0, 255)
# 转回 uint8 以便显示
noisy_img = noisy_img.astype(np.uint8)

# 显示
plt.figure(figsize=(10, 5))
plt.subplot(121), plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB)), plt.title('Original')
plt.subplot(122), plt.imshow(cv.cvtColor(noisy_img, cv.COLOR_BGR2RGB)), plt.title('Gaussian Noise')
plt.show()