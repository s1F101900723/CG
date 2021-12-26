from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math
import numpy as np


def julia(max, comp):
    re, im = comp[0], comp[1]
    #実部が-0.7、虚部が-0.3の複素数cを作成(ここの数値を変えればさまざまなジュリア集合を作れる)
    c = complex(-0.7, -0.3)

    #実部がre、虚部がimの複素数zを作成
    z = complex(re, im)

    for i in range(max):
        z = z*z + c
        #zの絶対値が一度でも2を超えればzが発散することを利用
        if abs(z) >= 2:
            
            return i        #発散する場合には何回目のループで終わったかを返す
    
    return max     #無限大に発散しない場合にはmaxを返す







win_x = 400
win_y = 400


'''
draw_2D_ScalarField
sf: scalar field stored in a 2D list.
min: minimum value of scalar field
max: maximum value of scalar field

As shown below, obtain the 255 step values at each vertex of a small square named index__, 
and convert them to RGB values by assigning to a colormap.

index01      index11
      ●------●
      |      |
      |      |
      ●------●
index00      index10
'''


def reshape(width, height):
    global win_x, win_y
    glutReshapeWindow(width, height)
    win_x = width
    win_y = height
    glViewport(0, 0, win_x, win_y)

def idle():
    glutPostRedisplay()

def main():

    # Instantiate the Metaballs class and add to the global list named "metabo" 

    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE)
    glutInitWindowSize(win_x, win_y)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"metaball")
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    init()
    glutIdleFunc(idle)
    glutMainLoop()

def init():
    glViewport(0, 0, win_x, win_y)
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    """ gluOrtho2D(left, right, bottom, top) """
    gluOrtho2D(0.0, 1.0, 0.0, 1.0)    # The coordinate system to draw


def display():
    re = np.linspace(-2, 2, 2000)
    im = np.linspace(2, -2, 2000)

    #実部と虚部の組み合わせを作成
    Re, Im = np.meshgrid(re, im)
    comp = np.c_[Re.ravel(), Im.ravel()]

    #計算結果を格納するための零行列を作成
    Julia = np.zeros(len(comp))

    #マンデルブロ集合に属するかの計算
    for i, c_point in enumerate(comp):
        Julia[i] = julia(200, c_point)

    Julia = Julia.reshape((2000, 2000))




    glClear(GL_COLOR_BUFFER_BIT)
    glBegin(GL_POINTS)
    glColor3f(1,0,0)
    julia(10,comp)
    glEnd()
    # Calculate a scalar field from some metaball


    # Draw a scalar field

    glFlush()
    glutSwapBuffers()


if __name__ == "__main__":
    main()