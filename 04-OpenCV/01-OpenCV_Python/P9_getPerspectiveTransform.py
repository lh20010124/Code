import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# 1. 读取图像
# 假设 'data/sudoku.png' 是一张拍摄的有透视变形的数独图片
img = cv.imread('data/sudoku.png')

# 获取原图尺寸 (仅作参考，下面变换时用了自定义尺寸)
rows, cols, channels = img.shape

# 2. 定义源图像中的 4 个点 (pts1)
# 这些点通常对应原图中物体的四个角（左上、右上、左下、右下）。
# 必须使用 np.float32 类型。
# 注意：这 4 个点的顺序必须与 pts2 中的顺序一一对应。
pts1 = np.float32([[56, 65],   # 左上角 (Top-Left)
                   [368, 52],  # 右上角 (Top-Right)
                   [28, 387],  # 左下角 (Bottom-Left)
                   [389, 390]]) # 右下角 (Bottom-Right)

# 3. 定义目标图像中的 4 个点 (pts2)
# 我们希望变换后，这四个点构成一个正方形（或长方形）。
# 这里我们将它们映射到一个 300x300 的正方形区域。
# 对应的顺序必须是：左上 -> (0,0), 右上 -> (300,0), 左下 -> (0,300), 右下 -> (300,300)
pts2 = np.float32([[0, 0],
                   [300, 0],
                   [0, 300],
                   [300, 300]])

# 4. 计算透视变换矩阵 M
# cv.getPerspectiveTransform 需要 4 对点来计算矩阵
# 得到的 M 是一个 3x3 的矩阵
#
M = cv.getPerspectiveTransform(pts1, pts2)

# 5. 应用透视变换
# cv.warpPerspective 使用 3x3 矩阵进行变换
# 第三个参数 (300, 300) 是输出图像的大小，这里我们限制为 300x300 以匹配 pts2
dst = cv.warpPerspective(img, M, (300, 300))

# 6. 使用 Matplotlib 显示结果
# 注意：Matplotlib 默认 RGB，OpenCV 默认 BGR，直接显示颜色可能会反转（红蓝互换）。
# 若要颜色正确，建议先 cv.cvtColor(img, cv.COLOR_BGR2RGB)
plt.subplot(121), plt.imshow(img), plt.title('Input')
plt.subplot(122), plt.imshow(dst), plt.title('Output')
plt.show()