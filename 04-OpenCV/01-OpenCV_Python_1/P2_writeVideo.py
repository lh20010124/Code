import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

fourcc = cv.VideoWriter_fourcc(*'DIVX')
out = cv.VideoWriter('output.avi', fourcc, 20.0, (640,480))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    frame = cv.flip(frame, 0)
    out.write(frame)
    cv.imshow('frame', frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()