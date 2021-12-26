from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np

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

def triangle():
    glBegin(GL_LINE_LOOP)
    glColor3f(1, 0, 0)
    glVertex3f(0, 0, 0)
    glVertex3f(1, 0, 0)
    glVertex3f(1, 1, 0)
    glEnd()

def skew(p,sx,sy,sz):   
    arr=[[1,sx,0],[sy,1,0],[sz,0,1]]
    arr1=p
    l_1=np.matmul(arr, arr1[0])
    l_2=np.matmul(arr, arr1[1])
    l_3=np.matmul(arr, arr1[2])
    glBegin(GL_TRIANGLES)
    glVertex3f(l_1[0],l_1[1],l_1[2])
    glVertex3f(l_2[0],l_2[1],l_2[2])
    glVertex3f(l_3[0],l_3[1],l_3[2])
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0.0, 0.0, 5.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)

    triangle()
    p=[[0,0,0],[1,0,0],[1,1,0]]

    glColor3f(0, 1, 0)
    skew(p,0,-2,0)

    glColor3f(0, 0, 1)
    skew(p,0,0,-2)


    
    glFlush()

def reshape(width, height):
    """callback function resize window"""
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(width)/float(height), 0.1, 100.0)

if __name__ == "__main__":
    main()