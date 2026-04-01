import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

# 1. 读取图像
img = cv.imread('data/opencv-logo.png')

# 2. 定义卷积核 (Kernel)
# 这是一个 5x5 的矩阵，所有元素都是 1。
# 最后除以 25 (5*5=25) 是为了"归一化" (Normalization)。
# 归一化的目的：保证处理后图像的总体亮度不变。
# 如果不除以 25，所有像素值会累加，图像会变得非常亮（甚至全白）。
#
kernel = np.ones((5, 5), np.float32) / 25

# 3. 应用 2D 卷积
# cv.filter2D(src, ddepth, kernel)
# 参数解析：
#   src: 输入图像
#   ddepth: 目标图像深度。 -1 表示与原图像保持一致 (即 src.depth())。
#   kernel: 我们上面定义的卷积核。
# 这一步会将核在图像上滑动，计算核覆盖区域的像素平均值，替换中心像素。
dst = cv.filter2D(img, -1, kernel)

# 4. 显示结果
# !!! 注意坑点 !!!
# OpenCV 读入是 BGR 格式，Matplotlib 显示是 RGB 格式。
# 直接显示会导致红蓝颜色互换。为了正确显示颜色，建议先转换颜色空间：
img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
dst_rgb = cv.cvtColor(dst, cv.COLOR_BGR2RGB)

plt.subplot(121), plt.imshow(img_rgb), plt.title('Original')
plt.xticks([]), plt.yticks([])

plt.subplot(122), plt.imshow(dst_rgb), plt.title('Filtered (Blurred)')
plt.xticks([]), plt.yticks([])

plt.show()