import pygame
from OpenGL.GL import *
from OpenGL.GLU import *

pygame.init()
display = (800, 600)
pygame.display.set_mode(display, pygame.DOUBLEBUF | pygame.OPENGL)
gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
glTranslatef(0.0,0.0, -5)

def draw():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

    # Fundo degradê
    glBegin(GL_QUADS)
    glColor3f(0, 0, 1)
    glVertex2f(-3,3)
    glColor3f(1, 0, 0)
    glVertex2f(-3, -3)
    glColor3f(1, 0, 0)
    glVertex2f(3, -3)
    glColor3f(0, 0, 1)
    glVertex2f(3, 3)
    glEnd()

    # Barra verde
    glBegin(GL_QUADS)
    glColor3f(0, 1, 0)  # Verde
    glVertex2f(-3, -3)
    glVertex2f(3, -3)
    glVertex2f(3, -1)
    glVertex2f(-3, -1)
    glEnd()

    # Triforce dourado
    glBegin(GL_TRIANGLES)
    glColor3f(1, 0.84, 0)  # Dourado
    # Triângulo externo
    glVertex3f(-1.25, 1.25, 0)
    glVertex3f(-2.5, -0.8, 0)
    glVertex3f(0.10, -0.8, 0)
    # Triângulo interno invertido
    glColor3f(0.6, 0, 0)
    glVertex3f(-1.2, -0.8, 0)
    glColor3f(0, 0, 0.5) 
    glVertex3f(-1.9, 0.18, 0)
    glColor3f(0, 0, 0.5) 
    glVertex3f(-0.55, 0.18, 0)
    glEnd()

    pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    draw()