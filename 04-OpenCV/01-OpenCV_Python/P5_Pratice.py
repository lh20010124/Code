import cv2 as cv
import numpy as np

def nothing(x):
    pass
def draw_circle(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        cv.circle(img, (x, y), radius, (b, g, r), -1)

img = np.zeros((300, 512, 3), np.uint8)
cv.namedWindow('img')
cv.setMouseCallback('img', draw_circle)

cv.createTrackbar('R','img',0,255,nothing)
cv.createTrackbar('G','img',0,255,nothing)
cv.createTrackbar('B','img',0,255,nothing)
cv.createTrackbar('Radius','img',50,250,nothing)

while True:

    cv.imshow('img',img)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

    r = cv.getTrackbarPos('R','img')
    g = cv.getTrackbarPos('G','img')
    b = cv.getTrackbarPos('B','img')
    radius = cv.getTrackbarPos('Radius','img')


cv.destroyAllWindows()
