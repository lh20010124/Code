import cv2 as cv
import numpy as np

img = cv.imread('data/messi5.jpg')

# 1. 获取图像尺寸
# img.shape 返回 (高度/行数, 宽度/列数, 通道数)
# 我们只需要前两个值：行数 (rows) 和 列数 (cols)
rows, cols = img.shape[:2]

# 2. 定义平移矩阵 M
# 这是一个 2x3 的变换矩阵，格式必须是 np.float32
# 矩阵结构: [[1, 0, tx], [0, 1, ty]]
# tx: 沿 x 轴移动的距离 (正数向右，负数向左) -> 这里是向右移动 100 像素
# ty: 沿 y 轴移动的距离 (正数向下，负数向上) -> 这里是向下移动 50 像素
M = np.float32([[1, 0, 100], [0, 1, 50]])

# 3. 应用仿射变换 (Affine Transformation)
# cv.warpAffine(输入图像, 变换矩阵, 输出图像大小)
# 注意第三个参数是 (width, height)，即 (cols, rows)，这与 shape 的顺序相反
dst = cv.warpAffine(img, M, (cols, rows))

# 4. 显示结果
cv.imshow('dst', dst)
cv.waitKey(0)
cv.destroyAllWindows()