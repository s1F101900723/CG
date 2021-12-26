from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
import math

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB | GLUT_SINGLE)
    glutInitWindowSize(300, 300)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"2-3")
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    init(300,300)
    glutMainLoop()

def init(width, height):
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glEnable(GL_DEPTH_TEST)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(width)/float(height), 0.1, 100.0)

def yellow_cone(p,N):
    glColor3f(1, 0.945, 0)
    th=0
    l_4=p[1]
    glBegin(GL_LINE_LOOP)
    for i in range(N):

        th+=math.radians(360/N)
        arr=[[math.cos(th),0,math.sin(th)],[0,1,0],[-math.sin(th),0,math.cos(th)]]
        arr1=p
        l_1=np.matmul(arr, arr1[0])
        l_2=np.matmul(arr, arr1[1])
        l_3=np.matmul(arr, arr1[2])
        glVertex3f(l_4[0],l_4[1],l_4[2])
        
        glVertex3f(l_2[0],l_2[1],l_2[2])
        glVertex3f(l_1[0],l_1[1],l_1[2])
        glVertex3f(l_3[0],l_3[1],l_3[2])
        l_4=l_2

    glEnd()

def Circle(p, r, s, d):
    th = math.radians(360/d)
    p1 = p[0]+r
    y = p[1]
    for x in range(0, s):
        glBegin(GL_LINE_LOOP)
        for t in range(0, d):
            c = np.zeros(3)
            c[0] = (p1 * math.cos(th*t)) - (p[2] * math.sin(th*t))
            c[1] = y
            c[2] = (p1 * math.sin(th*t)) + (p[2] * math.cos(th*t))
            glVertex3f(c[0], c[1], c[2])
        p1 -= r/s
        y += r/s
        glEnd()

    p1 = p[0]+r
    y = p[1]
    for t in range(0, d):
        glBegin(GL_LINE_LOOP)
        c = np.zeros(3)
        c[0] = (p1 * math.cos(th*t)) - (p[2] * math.sin(th*t))
        c[1] = y
        c[2] = (p1 * math.sin(th*t)) + (p[2] * math.cos(th*t))
        glVertex3f(p[0], p[1]+r, p[2])
        glVertex3f(c[0], c[1], c[2])
        glEnd()
        

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0.0, 2.0, 10.0, 0.0, -1, 0.0, 0.0, 1.0, 0.0)


    p1=[[0,0,0],[2,0,0],[0,2,0]]

    
    yellow_cone(p1,15)
    p2 = np.array([0, -4, 0])
    glColor3f(0.0, 1.0, 1.0)
    Circle(p2, 2, 4, 15)


    
    glFlush()

def reshape(width, height):
    """callback function resize window"""
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(width)/float(height), 0.1, 100.0)

if __name__ == "__main__":
    main()