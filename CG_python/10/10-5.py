#!/usr/bin/python
'''
    OpenCV seamlessCloning : Normal vs Mixed
    Copyright 2015 by Satya Mallick <spmallick@gmail.com>
    
'''
import cv2
import os
import numpy as np

# Read images : src image will be cloned into dst
im = cv2.imread(os.path.dirname(os.path.abspath(__file__))+"/73599.jpg")
obj= cv2.imread(os.path.dirname(os.path.abspath(__file__))+"/HORSE.bmp")
obj1= cv2.imread(os.path.dirname(os.path.abspath(__file__))+"/boy1.jpg")
obj2= cv2.imread(os.path.dirname(os.path.abspath(__file__))+"/airplane.jpg")
obj3= cv2.imread(os.path.dirname(os.path.abspath(__file__))+"/boy.jpg",cv2.IMREAD_GRAYSCALE)

# Create an all white mask
mask = 255 * np.ones(obj.shape, obj.dtype)
mask1 = 255 * np.ones(obj1.shape, obj1.dtype)
mask2 = 255 * np.ones(obj2.shape, obj2.dtype)
mask3 = 255 * np.ones(obj2.shape, obj2.dtype)
# The location of the center of the src in the dst
width, height, channels = im.shape
center = (int(height/2), int(width/2))
center1 = (int(height/3), int(width/3))
center2 = (int(height/3), int(width*2/3))
center3 = (int(height*2/3), int(width*2/3))

# Seamlessly clone src into dst and put the results in output
normal_clone = cv2.seamlessClone(obj, im, mask, center1, cv2.NORMAL_CLONE)
mixed_clone = cv2.seamlessClone(obj, im, mask, center, cv2.MIXED_CLONE)
mixed_clone1 = cv2.seamlessClone(obj1, mixed_clone, mask1, center1, cv2.MIXED_CLONE)
mixed_clone2 = cv2.seamlessClone(obj2, mixed_clone1, mask2, center2, cv2.MIXED_CLONE)
mixed_clone3 = cv2.seamlessClone(obj3, mixed_clone2, mask3, center3, cv2.MIXED_CLONE)
# Write results
#cv2.imwrite(os.path.dirname(os.path.abspath(__file__))+"/10-5_1.bmp", normal_clone1)
cv2.imwrite(os.path.dirname(os.path.abspath(__file__))+"/10-5_2.bmp", mixed_clone3)