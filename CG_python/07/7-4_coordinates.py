from ctypes import pointer
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from PIL import Image
from PIL import ImageOps
import math
import sys
import os
import numpy as np

win_x = 400
win_y = 400
step = 0
dt = 1

point1 =np.array([[0.5, 0.7],[0.5-0.2*math.sqrt(2)/2, 0.5+0.2*math.sqrt(2)/2,]])




octagon = np.array([[0.5, 0.7], [0.5-0.2*math.sqrt(2)/2, 0.5+0.2*math.sqrt(2)/2], [0.3, 0.5], [0.5-0.2*math.sqrt(2)/2, 0.5-0.2*math.sqrt(2)/2], 
         [0.5, 0.3], [0.5+0.2*math.sqrt(2)/2, 0.5-0.2*math.sqrt(2)/2], [0.7, 0.5], [0.5+0.2*math.sqrt(2)/2, 0.5+0.2*math.sqrt(2)/2]])
cross   = np.array([[0.5, 0.7], [0.5-0.05*math.sqrt(2)/2, 0.5+0.05*math.sqrt(2)/2], [0.3, 0.5], [0.5-0.05*math.sqrt(2)/2, 0.5-0.05*math.sqrt(2)/2], 
         [0.5, 0.3], [0.5+0.05*math.sqrt(2)/2, 0.5-0.05*math.sqrt(2)/2], [0.7, 0.5], [0.5+0.05*math.sqrt(2)/2, 0.5+0.05*math.sqrt(2)/2]])