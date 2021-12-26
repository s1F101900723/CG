import cv2
import numpy as np
import os

# load image, change color spaces, and smoothing
img = cv2.imread(os.path.dirname(os.path.abspath(__file__))+"/INIAD_logo.png")
img_HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
img_HSV = cv2.GaussianBlur(img_HSV, (9, 9), 3)
cv2.imshow("a",img_HSV)
k = cv2.waitKey(0)
# detect tulips
img_H, img_S, img_V = cv2.split(img_HSV)

ret,img_flowers = cv2.threshold(img_H, 50, 255, cv2.THRESH_BINARY)
cv2.imwrite(os.path.dirname(os.path.abspath(__file__))+"/flower.bmp", img_flowers)
ret,img_flowers2 = cv2.threshold(img_H, 1, 255, cv2.THRESH_BINARY)
cv2.imwrite(os.path.dirname(os.path.abspath(__file__))+"/flower2.bmp", img_flowers2)

# find tulips
contours, hierarchy = cv2.findContours(img_flowers, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

for i in range(0, len(contours)):
    if len(contours[i]) > 0:

        # remove small objects
        if cv2.contourArea(contours[i]) < 500:
            continue

        cv2.polylines(img, contours[i], True, (255, 255, 255), 5)

# save
cv2.imwrite(os.path.dirname(os.path.abspath(__file__))+"/flower1.bmp", img)

