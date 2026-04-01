import numpy as np
import cv2 as cv
import math

drawing = False
mode = True
ix, iy = -1, -1


def draw_circle(event, x, y, flags, param):
    global ix, iy, drawing, mode, img
    global radius

    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    elif event == cv.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == True:
                # 1. 复制原图，避免直接修改原图造成拖影
                img_copy = img.copy()
                # 2. 在副本上画矩形
                cv.rectangle(img_copy, (ix, iy), (x, y), (0, 0, 255), -1)  # 也可以改成 1 做空心矩形
                # 3. 显示副本
                cv.imshow('img', img_copy)
            else:
                # 1. 复制原图，避免直接修改原图造成拖影
                img_copy = img.copy()
                # 2. 在副本上画矩形
                radius = int(math.sqrt((x - ix) ** 2 + (y - iy) ** 2))
                cv.circle(img_copy,(ix,iy),radius,(0,0,255),5)  # 也可以改成 1 做空心圆
                # 3. 显示副本
                cv.imshow('img', img_copy)
                pass

    elif event == cv.EVENT_LBUTTONUP:

        drawing = False
        # 松手时，才真正的画在原图 img 上
        if mode == True:
            cv.rectangle(img, (ix, iy), (x, y), (0, 0, 255), -1)
        else:
            cv.circle(img, (ix, iy), radius, (0, 0, 255), -1)
        # 更新显示原图
        cv.imshow('img', img)


img = np.zeros((512, 512, 3), np.uint8)
cv.namedWindow('img')
cv.setMouseCallback('img', draw_circle)

while True:
    # 注意：如果使用了上面的 img_copy 方法，这里就不需要重复 imshow 了，
    # 或者仅在非绘图状态下显示 img
    if not drawing:
        cv.imshow('img', img)

    k = cv.waitKey(1) & 0xff
    if k == ord('m'):
        mode = not mode
        print(f"切换模式: {'矩形' if mode else '圆形'}")
    elif k == ord('q'):
        break

cv.destroyAllWindows()