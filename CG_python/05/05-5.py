import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def display():
    
    glClear(GL_COLOR_BUFFER_BIT)


    glEnable(GL_TEXTURE_2D)
    glColor3f(1,0,0)
    glBegin(GL_QUADS)
    glVertex3d( 1.0, -1.0,  -1.0)
    glVertex3d( 1.0, -1.0,  1.0)
    glVertex3d( 1.0,  1.0,  -1.0)
    glVertex3d( 1.0,  1.0,  1.0)
    glEnd()
    glColor3f(0,0,1)
    glBegin(GL_QUADS)
    glTexCoord2d(0.0, 1.0)
    glVertex3d( 1.0, 1.0,  1.0)
    glVertex3d( 1.0, -1.0,  0.0)
    glVertex3d( 1.0,  1.0,  0.0)
    glVertex3d(-1.0,  1.0,  0.0)
    glEnd()
    glColor3f(1,0,1)
    glBegin(GL_QUADS)
    glVertex3d(-1.0, -1.0,  0.0)
    glVertex3d( 1.0, -1.0,  0.0)
    glVertex3d( 1.0,  1.0,  0.0)
    glVertex3d(-1.0,  1.0,  0.0)
    glEnd()
    glColor3f(1,1,0)
    glBegin(GL_QUADS)
    glVertex3d(-1.0, -1.0,  0.0)
    glVertex3d( 1.0, -1.0,  0.0)
    glVertex3d( 1.0,  1.0,  0.0)
    glVertex3d(-1.0,  1.0,  0.0)
    glEnd()

    glDisable(GL_TEXTURE_2D)

    glDisable(GL_BLEND)

    glFlush()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(300, 300)
    glutCreateWindow(b"TextureSample1")
    glutDisplayFunc(display)
    glClearColor(0.0, 0.0, 1.0, 1.0)

    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

    glutMainLoop()

if __name__ == '__main__':
    main()