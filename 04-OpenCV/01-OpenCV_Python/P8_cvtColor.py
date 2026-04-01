import cv2 as cv
import numpy as np

# 1. 获取摄像头视频流
# 参数 0 通常代表计算机的默认网络摄像头
cap = cv.VideoCapture(0)

while True:
    # 2. 逐帧读取视频
    # ret: 布尔值，表示是否成功读取帧 (True/False)
    # frame: 读取到的当前图像帧 (NumPy 数组)
    ret, frame = cap.read()

    # 如果没有读取到帧（例如摄像头断开），则跳出循环
    if not ret:
        print("无法接收帧，正在退出...")
        break

    # 3. 颜色空间转换: BGR -> HSV
    # OpenCV 默认使用 BGR (蓝绿红)，但 HSV (色调/饱和度/亮度) 模型更适合进行颜色分割
    # [Image of HSV color space cylinder model]
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    # 4. 定义蓝色的阈值范围 (在 HSV 空间中)
    # H (Hue 色调): 蓝色通常在 110-130 之间 (OpenCV中 H范围是0-179)
    # S (Saturation 饱和度) 和 V (Value 亮度): 设置下限以过滤掉发白或发暗的蓝色
    lower_blue = np.array([100, 50, 50])      # 蓝色的下限
    upper_blue = np.array([140, 255, 255])    # 蓝色的上限

    # 5. 创建掩模 (Mask)
    # cv.inRange 会将图像中介于 lower_blue 和 upper_blue 之间的像素设为 255 (白)，
    # 其余像素设为 0 (黑)。这就形成了一个黑白二值图像。
    mask = cv.inRange(hsv, lower_blue, upper_blue)

    # 6. 对原图像和掩模进行“按位与”运算
    # 只有掩模中为白色 (255) 的区域，原图像的色彩才会被保留；
    # 掩模中为黑色 (0) 的区域，结果图像中也会变黑。
    # [Image of computer vision image masking process]
    res = cv.bitwise_and(frame, frame, mask=mask)

    # 7. 显示结果窗口
    cv.imshow('frame', frame) # 显示原始视频画面
    cv.imshow('mask', mask)   # 显示黑白掩模 (用于调试，看是否准确提取了物体轮廓)
    cv.imshow('res', res)     # 显示最终结果 (只保留了蓝色物体)

    # 8. 退出控制
    # 等待 20 毫秒监听键盘输入，如果按下 'q' 键 (ASCII码) 则中断循环
    if cv.waitKey(20) == ord('q'):
        break

# 9. 资源释放 (重要)
# 释放摄像头资源，防止程序关闭后摄像头仍被占用
cap.release()
# 关闭所有 OpenCV 创建的窗口
cv.destroyAllWindows()