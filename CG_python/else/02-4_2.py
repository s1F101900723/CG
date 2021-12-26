from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import numpy as np
import math

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB | GLUT_SINGLE | GLUT_DEPTH)
    glutInitWindowSize(300, 300)     # window size
    glutInitWindowPosition(100, 100) # window position
    glutCreateWindow(b"teapot")      # show window
    glutDisplayFunc(display)         # draw callback function
    glutReshapeFunc(reshape)         # resize callback function
    init(300, 300)
    glutMainLoop()

def init(width, height):
    """ initialize """
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glEnable(GL_DEPTH_TEST) # enable shading

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    ##set perspective
    gluPerspective(45.0, float(width)/float(height), 0.1, 100.0)

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
    

def display():
    """ display """
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    ##set camera
    gluLookAt(0.0, 1.0, 15.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
    line()
    ##draw a teapot
    glColor3f(1.0, 0.945, 1.0)
    glRotatef(180, 0, 1, 0)
    glutWireTeapot(1.0)   # wireframe
    transform()
    glFlush()  # enforce OpenGL command

def transform():   
    arr1=[[1,0,0],[0,0,5],[0,0,1]]
    arr2=[[1,0,0],[0,math.cos(90),-math.sin(90)],[0,math.sin(90),math.cos(90)]]
    arr3=[0,0,0]
    l_1=np.matmul(arr1, arr2)
    l_2=np.matmul(l_1, arr3)
    glColor3f(1.0, 0.945, 0.0)
    glTranslatef(l_2[0],l_2[1],l_2[2])
    glutWireTeapot(1.0)  
    
    l_3=np.matmul(arr2, arr1)
    l_4=np.matmul(l_3, arr3)
    glColor3f(0.0, 0.945, 1.0)
    glTranslatef(l_4[0],l_4[1],l_4[2])
    glutWireTeapot(1.0)   # wireframe

    


def reshape(width, height):
    """callback function resize window"""
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(width)/float(height), 0.1, 100.0)

if __name__ == "__main__":
    main()