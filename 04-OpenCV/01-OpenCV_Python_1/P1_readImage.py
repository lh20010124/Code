import cv2 as cv
import sys

imagePath = 'data/starry_night.jpg'
print(type(imagePath))
img = cv.imread(imagePath)

if img is None:
    sys.exit("无法读取图像")

cv.imshow("img", img)
k = cv.waitKey(0)
if k == ord('s'):
    cv.imwrite('starry_night.png', img)