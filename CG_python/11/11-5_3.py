import cv2
import numpy as np
import os
import svgwrite

# load image, change color spaces, and smoothing
img = cv2.imread(os.path.dirname(os.path.abspath(__file__))+"/INIAD_logo.png")
im=cv2.resize(img,(10000,10000))

im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
retval, im_bw = cv2.threshold(im_gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# 輪郭の検出
contours, hierarchy = cv2.findContours(im_bw, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

# 全ての輪郭を書き込んで出力
#im_con = im.copy()
#cv2.drawContours(im_con, contours, -1, (0,255,0), 2)

# 輪郭直線近似
approx = []
for i in range(len(contours)):
    cnt = contours[i]
    epsilon = 0.0001*cv2.arcLength(cnt,True)
    a = len(cv2.approxPolyDP(cnt,epsilon,True))
    for j in range(a):
        x = cv2.approxPolyDP(cnt,epsilon,True)[j][0][0]*0.01
        y = cv2.approxPolyDP(cnt,epsilon,True)[j][0][1]*0.01
        #print(x)
        approx.append([x, y])
    #print(cv2.approxPolyDP(cnt,epsilon,True))
    #approx.append(cv2.approxPolyDP(cnt,epsilon,True))

#print(approx)
dwg = svgwrite.Drawing(os.path.dirname(os.path.abspath(__file__))+"/INIAD_logo1.svg")
dwg.add( dwg.polygon( points=approx ) )
dwg.save()