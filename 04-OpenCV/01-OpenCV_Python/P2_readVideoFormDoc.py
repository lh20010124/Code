import cv2 as cv
import numpy as np

cap = cv.VideoCapture("vtest.avi")

while cap.isOpened():
    ret, frame = cap.read()
    if not(ret):
        break
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow("frame", gray)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()