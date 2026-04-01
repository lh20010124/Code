import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)
print(cap.get(cv.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
if not cap.isOpened():
    print("Cannot open camera")
    exit()

ret1 = cap.set(cv.CAP_PROP_FRAME_WIDTH, 1920)
print(ret1)
ret2 = cap.set(cv.CAP_PROP_FRAME_HEIGHT, 1080)
print(ret2)
print(cap.get(cv.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
while True:
    ret, frame = cap.read()
    if not(ret):
        break
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow('frame', frame)
    cv.imshow('gray', gray)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv.destroyAllWindows()