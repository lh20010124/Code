import cv2 as cv
import numpy as np

img1 = cv.imread('data/messi5.jpg')
img2 = cv.imread('data/lena.jpg')

# 1. 统一尺寸：必须确保两张图一样大，否则 addWeighted 会报错
# 这里强制将两张图都缩放到 512x512
img1 = cv.resize(img1, (512, 512))
img2 = cv.resize(img2, (512, 512))

# 2. 增加帧数，减少延迟，实现“平滑”
# 步长改为 100 步，每步看起来变化很小，视觉就流畅了
steps = 100
for i in range(steps + 1):
    alpha = i / steps  # 从 0.0 变到 1.0
    beta = 1.0 - alpha  # 从 1.0 变到 0.0

    # img1 慢慢出现，img2 慢慢消失
    res = cv.addWeighted(img1, alpha, img2, beta, 0)

    cv.imshow('res', res)

    # 3. 缩短等待时间，大约 30ms 一帧，接近 30FPS 的流畅度
    if cv.waitKey(20) == ord('q'):
        break

cv.waitKey(0)
cv.destroyAllWindows()