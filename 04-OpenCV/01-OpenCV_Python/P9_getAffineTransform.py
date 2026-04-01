import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# 1. 读取图像
img = cv.imread('data/sudoku.png')

# 获取图像维度：行数(高), 列数(宽), 通道数
rows, cols, channels = img.shape

# 2. 定义变换前的三个点 (源坐标)
# 仿射变换只需要 3 个点来确定变换矩阵 (因为它是线性的，保持平行性)
# 格式必须是 np.float32
pts1 = np.float32([[50, 50], [200, 50], [50, 200]])

# 3. 定义变换后的三个点 (目标坐标)
# !!! 注意 !!! 你的代码里 pts2 和 pts1 完全一样
# 这意味着你告诉程序：“把(50,50)移动到(50,50)...”，所以图像不会有任何变化。
# 如果想看到效果，试着修改 pts2，例如把第三个点 [50, 200] 改为 [10, 200] (产生剪切效果)
pts2 = np.float32([[50, 50], [200, 50], [50, 200]])

# 4. 计算仿射变换矩阵 M
# cv.getAffineTransform 根据这三对点，解方程算出一个 2x3 的矩阵
#
M = cv.getAffineTransform(pts1, pts2)

# 5. 应用变换
dst = cv.warpAffine(img, M, (cols, rows))

# 6. 使用 Matplotlib 显示结果
# 注意：OpenCV 读取的是 BGR 格式，而 Matplotlib 使用 RGB。
# 如果直接显示颜色可能会不对 (蓝色变红色)。通常需要 cv.cvtColor(img, cv.COLOR_BGR2RGB)
plt.subplot(121), plt.imshow(img), plt.title('Input')
plt.subplot(122), plt.imshow(dst), plt.title('Output')
plt.show()