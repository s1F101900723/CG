from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from PIL import Image
from PIL import ImageOps
import numpy as np
import math
import sys
import random
import time

y1 = 0
y2 = 0
y3 = 0
x1 = 0
x2 = 0
x3 = 0


def combination(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r)) ## Calcurate and return combination _n C_r ##

'''
drawRationalBezier
cp: 2D control points
N: number of divisions
'''

def line():
    glBegin(GL_LINES)
    glColor3f(1, 0, 0)
    glVertex3f(0, 0, 0)
    glVertex3f(100, 0, 0)
    glEnd()
    glBegin(GL_LINES)
    glColor3f(0, 1, 0)
    glVertex3f(0, 0, 0)
    glVertex3f(0, 100, 0)
    glEnd()
    glBegin(GL_LINES)
    glColor3f(0, 0, 1)
    glVertex3f(0, 0, 0)
    glVertex3f(0, 0, 100)
    glEnd()


def drawRationalBezier(cp, w, N, next_cp):
    number_cp = len(cp) # number of control points
    n = number_cp - 1   # value n of n-th Bezier
    glBegin(GL_QUAD_STRIP)
    for t in np.linspace(0, 1, N):
        c = np.zeros(3) # Numerator of a Ratinal Bezier curve equation
        sum_weight = 0  # Denominator of a Ratinal Bezier curve equation
        next_c = np.zeros(3) # Numerator of a Ratinal Bezier curve equation
        for i in range(0, number_cp):
            c += w[i] * cp[i] * (combination(n, i) * t**i * (1-t)**(n-i)) ## Calcurate the numerator c on Bezier curve from control point cp, w and etc... ##
            sum_weight += w[i] * (combination(n, i) * t**i * (1-t)**(n-i)) ## Calcurate the denominator w on Bezier curve from weight list w and etc... ##
            next_c += w[i] * next_cp[i] * (combination(n, i) * t**i * (1-t)**(n-i)) ## Calcurate the numerator c on Bezier curve from control point cp, w and etc... ##
        glVertex3f(c[0]/sum_weight, c[1]/sum_weight,c[2]/sum_weight)
        glVertex3f(next_c[0]/sum_weight, next_c[1]/sum_weight,next_c[2]/sum_weight) ## Specifying a vertex ##
    glEnd()

def drawLineBetweenControlPoint(cp):
    glEnable(GL_LINE_STIPPLE)
    glLineStipple(1, 0xF0F0)
    glBegin(GL_LINE_STRIP)
    for i in range(0, len(cp)):
        glVertex3f(cp[i][0], cp[i][1], cp[i][2])
    glEnd()
    glDisable(GL_LINE_STIPPLE)

def drawControlPoint(cp):
    glPointSize(5.0)
    glEnable(GL_POINT_SMOOTH)
    glBegin(GL_POINTS)
    for i in range(0, len(cp)):
        glVertex3f(cp[i][0], cp[i][1],cp[i][2])
    glEnd()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB | GLUT_SINGLE)
    glutInitWindowSize(400, 400)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"2-3")
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    init(400,400)
    glutIdleFunc(idle)
    glutMainLoop()

def init(width, height):
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glEnable(GL_DEPTH_TEST)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(width)/float(height), 0.1, 100.0)

def idle():
    global y1, y2, y3
    y1 = random.uniform(-5, 1)
    y2 = random.uniform(-1, 5)
    y3 = random.uniform(-3, 1)
    x1 = random.uniform(-5, 1)
    x2 = random.uniform(-1, 5)
    x3 = random.uniform(-3, 1)
    time.sleep(0.1)
    glutPostRedisplay()
    glutIdleFunc(idle)

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0.0, 5.0, 5.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
    line()
    # Draw Bezier curve
    cp1 = np.array([[-1.5, -0.5, 0.0], [-1.0, y1+1.0, 0.0], [1.0, y2-2.5, 0.0], [1.5, y3+0.5, 0.0]])
    cp2 = np.array([[-1.5, -0.5,-0.5], [-1.0, y1+1.0,-0.5], [1.0, y2-2.5,-0.5], [1.5, y3+0.5,-0.5]])
    cp3 = np.array([[-1.5, -0.5,-1.0], [-1.0, y1+1.0,-1.0], [1.0, y2-2.5,-1.0], [1.5, y3+0.5,-1.0]])
    cp4 = np.array([[-1.5, -0.5,-1.5], [-1.0, y1+1.0,-1.5], [1.0, y2-2.5,-1.5], [1.5, y3+0.5,-1.5]])
    w1 = np.array([1, 1, 1, 1])
    glColor3f(1.0, 1.0, 1.0)
    drawLineBetweenControlPoint(cp1)
    drawLineBetweenControlPoint(cp2)
    drawLineBetweenControlPoint(cp3)
    drawLineBetweenControlPoint(cp4)
    glColor3f(0.0, 0.0, 1.0)
    drawRationalBezier(cp1, w1, 100,cp2)
    glColor3f(0.0, 0.5, 1.0)
    drawRationalBezier(cp2, w1, 100,cp3)
    glColor3f(0.5, 1.0, 1.0)
    drawRationalBezier(cp3, w1, 100,cp4)

    glColor3f(33/255, 173/255, 229/255)
    drawControlPoint(cp1)
    drawControlPoint(cp2)
    drawControlPoint(cp3)
    drawControlPoint(cp4)

    glFlush()

def reshape(width, height):
    """callback function resize window"""
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(width)/float(height), 0.1, 100.0)

if __name__ == "__main__":
    main()