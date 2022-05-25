import numpy as np
import graphics
import pygame as pg
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *


cubeVertices = ((1,1,1),(1,1,-1),(1,-1,-1),(1,-1,1),(-1,1,1),(-1,-1,-1),(-1,-1,1),(-1,1,-1))
cubeEdges = ((0,1),(0,3),(0,4),(1,2),(1,7),(2,5),(2,3),(3,6),(4,6),(4,7),(5,6),(5,7))
cubeQuads = ((0,3,6,4),(2,5,6,3),(1,2,5,7),(1,0,4,7),(7,4,6,5),(2,3,0,1))
dimensions=(100, 30, 10)
ground_vertices = (
    (dimensions[0],-dimensions[1],-dimensions[2]),
    (-dimensions[0],dimensions[1],-dimensions[2]),
    (dimensions[0],-dimensions[1],dimensions[2]),
    (-dimensions[0],dimensions[1],dimensions[2]),
)

def drawGound():
    glBegin(GL_POLYGON)

    glColor4f(*[1,0,0,1])
    x = 0
    for vertex in ground_vertices:
        x+=1
        glColor3fv((0,1,1))
        glVertex3fv(vertex)
        
    glEnd()

def wireCube():
    glBegin(GL_LINES)
    for cubeEdge in cubeEdges:
        for cubeVertex in cubeEdge:
            glVertex3fv(cubeVertices[cubeVertex])
    glEnd()

def solidCube():
    glBegin(GL_QUADS)
    for cubeQuad in cubeQuads:
        for cubeVertex in cubeQuad:
            glVertex3fv(cubeVertices[cubeVertex])
    glEnd()

def generateCubes():
    iter=100
    spread=50
    sign=np.random.randint(-1, 1)
    func_=lambda x: x
    xs=np.linspace(-1, 1, iter)
    xs[-1]=xs[-1]-np.sum(xs)
    for x in xs:
        colors = np.random.rand(4)
        # glTranslated(func_(x), func_(x), func_(x))
        glTranslated(func_(x), 0, 0)
        # glRotatef(360/iter, np.random.randint(-100, 100), np.random.randint(-100, 100), np.random.randint(-10, 10))
        glColor4f(*colors)
        solidCube()
        glColor4f(colors[1], colors[2], colors[0], colors[3])
        wireCube()
    # glRasterPos4f(0,0, np.random.randint(1, 200), 10)

def main():
    pg.init()
    display = (1000, 1000)
    pg.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 150.0)
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glTranslatef(0, 0, -10)

    for i in range(100):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        drawGound()
        glRotatef(10*(i+1), 50, 50, 50)
        # generateCubes()
        glRotatef(-10*(i+1), 50, 50, 50)
        pg.display.flip()
        pg.time.wait(100)

if __name__ == "__main__":
    main()