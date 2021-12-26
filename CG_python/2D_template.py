from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB | GLUT_SINGLE)
    glutInitWindowSize(400, 400)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"2D template")
    glutDisplayFunc(display)
    init()
    glutMainLoop()

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    """ gluOrtho2D(left, right, bottom, top) """
    gluOrtho2D(0.0, 1.0, 0.0, 1.0)    # The coordinate system to draw

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 0.0)
    glEnable(GL_POINT_SMOOTH)
    glEnable(GL_LINE_SMOOTH)    
    glPointSize(6.0)
    glLineWidth(3.0)
    glBegin(GL_POINTS)
#    glBegin(GL_LINES)
#    glBegin(GL_LINE_STRIP)
#    glBegin(GL_LINE_LOOP)
#    glBegin(GL_TRIANGLE_STRIP)
#    glBegin(GL_QUAD_STRIP)
#    glBegin(GL_TRIANGLES)
#    glBegin(GL_QUADS)
#    glBegin(GL_TRIANGLE_FAN)
#    glBegin(GL_POLYGON)
    glVertex2f(0.5, 0.75)
    glVertex2f(0.1, 0.5)
    glVertex2f(0.25, 0.25)
    glVertex2f(0.5, 0.2)
    glVertex2f(0.75, 0.25)
    glVertex2f(0.9, 0.5)
    glEnd()
    glFlush()

if __name__ == "__main__":
    main()