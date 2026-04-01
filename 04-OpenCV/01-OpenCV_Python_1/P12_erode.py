import numpy as np
import cv2 as cv

img = cv.imread('data/i.png',flags=cv.IMREAD_GRAYSCALE)

kernel = np.ones((15,15),np.uint8)
erosion = cv.erode(img,kernel,iterations = 1)
cv.imshow('img',img)
cv.imshow('erosion',erosion)
cv.waitKey(0)