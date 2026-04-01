import numpy as np
import cv2 as cv

img1 = cv.imread('data/messi5.jpg')
img2 = cv.imread('data/opencv-logo-white.png')
assert img1 is not None, "1"
assert img2 is not None, "2"

rows,cols,channels = img2.shape

# 在主图 (img1) 的左上角划出一块和 logo 一样大的区域 (ROI)
# 我们将要把 logo 放进这个区域里
roi = img1[0:rows,0:cols]

# 将 logo 转为灰度图
img2gray = cv.cvtColor(img2,cv.COLOR_BGR2GRAY)

# 二值化处理 (Threshold)
# 像素值 > 10 的变为 255 (白色)，否则为 0 (黑色)
# 这一步是为了把 Logo 的图案（非黑色部分）抠出来
ret,mask = cv.threshold(img2gray,10,255,cv.THRESH_BINARY)

# 制作反向掩膜
# 原来白的地方变黑，黑的地方变白
mask_inv = cv.bitwise_not(mask)

# 【背景处理】: 在 ROI (主图区域) 上“挖”出一个 Logo 形状的洞
# bitwise_and 运算规则：1 & 1 = 1, 1 & 0 = 0
# mask_inv 中，Logo 区域是黑色(0)。
# 任何颜色 和 0 做与运算，都变成 0 (黑色)。
# 结果：img1_bg 是梅西的背景图，但左上角有一个黑色的 OpenCV Logo 形状的空洞。
img1_bg = cv.bitwise_and(roi,roi,mask = mask_inv)

# 【前景处理】: 提取纯净的 Logo
# mask 中，Logo 区域是白色(255/全1)。
# 任何颜色 和 1 做与运算，保持原色。
# 结果：img2_fg 只有 Logo 的颜色，Logo 以外的背景全是黑色。
img2_fg = cv.bitwise_and(img2,img2,mask = mask)

# 将背景(挖了坑的) 和 前景(抠出来的Logo) 相加
# 黑色像素值是 0。
# 0 + Logo颜色 = Logo颜色
# 背景颜色 + 0 = 背景颜色
dst = cv.add(img1_bg,img2_fg)
img1[0:rows,0:cols] = dst
cv.imshow('res',img1)
cv.waitKey(0)
cv.destroyAllWindows()