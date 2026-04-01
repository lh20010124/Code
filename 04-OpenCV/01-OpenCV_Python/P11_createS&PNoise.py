import cv2 as cv
import numpy as np
import random


def add_salt_and_pepper(image, prob):
    """
    image: 输入图像
    prob: 噪声比例 (例如 0.05 表示 5% 的像素会被噪声覆盖)
    """
    output = np.copy(image)

    # 1. 生成一个与图像同形状的随机矩阵 (0~1之间)
    # 如果是彩色图，只对二维坐标做掩模，以免破坏通道结构
    if len(image.shape) == 2:
        black = 0
        white = 255
    else:
        black = [0, 0, 0]
        white = [255, 255, 255]

    probs = np.random.random(output.shape[:2])

    # 2. 撒盐 (Salt) - 设置为白色
    # 如果随机数 < prob / 2，设为白
    output[probs < (prob / 2)] = white

    # 3. 撒椒 (Pepper) - 设置为黑色
    # 如果随机数 > 1 - prob / 2，设为黑
    output[probs > (1 - prob / 2)] = black

    return output


img = cv.imread('data/messi5.jpg')

# 添加 5% 的椒盐噪声
noisy_sp = add_salt_and_pepper(img, 0.05)

cv.imshow('Salt and Pepper', noisy_sp)
cv.waitKey(0)
cv.destroyAllWindows()