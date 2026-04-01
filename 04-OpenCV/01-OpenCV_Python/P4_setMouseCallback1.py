import cv2 as cv
import numpy as np

def draw_circle(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        cv.circle(img, (x, y), 100, (0, 0, 255), -1)

img = np.zeros((512, 512, 3), np.uint8)
cv.namedWindow('img')
cv.setMouseCallback('img', draw_circle)

while True:
    cv.imshow('img', img)
    if cv.waitKey(20) & 0xFF == ord('q'):
        break
cv.destroyAllWindows()