import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

width, height = 800, 600                                                    # width and height of the screen created

def drawAxes():                                                             # draw x-axis and y-axis
    glLineWidth(3.0)                                                        # specify line size (1.0 default)
    glBegin(GL_LINES)                                                       # replace GL_LINES with GL_LINE_STRIP or GL_LINE_LOOP
    glColor3f(1.0, 0.0, 0.0)                                                # x-axis: red
    glVertex3f(0.0, 0.0, 0.0)                                               # v0
    glVertex3f(100.0, 0.0, 0.0)                                             # v1
    glColor3f(0.0, 1.0, 0.0)                                                # y-axis: green
    glVertex3f(0.0, 0.0, 0.0)                                               # v0
    glVertex3f(0.0, 100.0, 0.0)                                             # v1
    glColor3f(0.0, 0.0, 1.0)                                                # z-axis: blue
    glVertex3f(0.0, 0.0, 0.0)                                               # v0
    glVertex3f(0.0, 0.0, 100.0)                                             # v1
    glEnd()

def draw_cube():
    v_0 = [-10, -10, -10]
    v_1 = [-10, -10, 10]
    v_2 = [10, -10, 10]
    v_3 = [10, -10, -10]
    v_4 = [-10, 10, -10]
    v_5 = [-10, 10, 10]
    v_6 = [10, 10, 10]
    v_7 = [10, 10, -10]

    verticesList = [v_0, v_1, v_2, v_3, v_4, v_5, v_6, v_7]

    triangle_strips = [
                [0,1,2,3],
                [4,5,6,7],
                [1,5,6,2,7,3,4,0,3,1]
                ]
    
    edgesList = [
        [1,0], [1,2], [1,5],
        [3,0], [3,2], [3,7],
        [6,2], [6,7], [6,5],
        [4,7], [4,0], [4,5]
    ]
    
    trianglesList = [
                [0,2,1], [0,3,2],   # Bottom Face
                [5,7,4], [5,6,7],   # Top Face
                [1,6,5], [1,2,6],   # Front Face
                [3,4,7], [3,0,4],   # Back Face
                [2,7,6], [2,3,7],   # Right Face
                [0,5,4], [0,1,5]    # Left Face
    ]

    colorsList = [
        [0,1,0],                    # (green)
        [0,0,1],                    # (blue)
        [1,0,0],                    # (red)
    ]

    indexOfColor = 0
    count = 0
    glBegin(GL_TRIANGLES)
    for triangle in trianglesList:
        glColor3fv(colorsList[indexOfColor])
        for vertex in triangle:
            glVertex3fv(verticesList[vertex])

        if count >= 3:
            count = 0
            indexOfColor += 1
        else:
            count += 1
    glEnd()

    glLineWidth(5)
    glColor3f(1.0,1.0,1.0)
    glBegin(GL_LINES)
    for edge in edgesList:
        for vertex in edge:
            glVertex3fv(verticesList[vertex])
    glEnd()
    pass

def draw_pyramid():
    v_0 = [-10, 0, -10]         # Back left corner
    v_1 = [-10, 0, 10]          # Front left corner
    v_2 = [10, 0, 10]           # Front right corner
    v_3 = [10, 0, -10]          # Back right corner
    v_4 = [0, 20, 0]            # Top Vertex

    verticesList = [v_0, v_1, v_2, v_3, v_4]

    edgesList = [
        [4,1], [4,2], [4,0], [3,4],
        [1,2], [1,0], [3,2], [3,0]
    ]
    
    triangle_fan = [4, 0, 1, 2, 3, 0]

    trianglesList = [
        [4,0,1],
        [4,1,2],
        [4,2,3],
        [4,3,0],
        [0,2,1],            # Bottom Face - First Triangle
        [0,3,2]             # Bottom Face - Second Triangle
    ]

    pyramidColorsList = [
        [1,0,0],            # Left (red)
        [1,1,0],            # Front (yellow)
        [0,1,0],            # Right (green)
        [0,1,1],            # Back (turquoise)
        [0,0,1],            # Bottom (blue) - First Triangle Color
        [0,0,1]             # Bottom (blue) - Second Triangle Color
    ]

    # Draw triangles using GL_TRIANGLES
    # indexOfColor = 0
    # glBegin(GL_TRIANGLES)
    # for triangle in trianglesList:
    #     glColor3fv(pyramidColorsList[indexOfColor])
    #     for vertex in triangle:
    #         glVertex3fv(verticesList[vertex])
    #     indexOfColor += 1
    # glEnd()

    # Draw side triangles using GL_TRIANGLE_FAN
    indexOfColor = 0
    glBegin(GL_TRIANGLE_FAN)
    for vertex in triangle_fan:
        glColor3fv(pyramidColorsList[indexOfColor])
        glVertex3fv(verticesList[vertex])
        indexOfColor += 1
    glEnd()

    # Draw pyramid base (2 triangles) using GL_TRIANGLE_FAN
    # indexOfColor = 4
    # glBegin(GL_TRIANGLE_FAN)
    # for vertex in base_triangle_fan:
    #     glColor3fv(pyramidColorsList[indexOfColor])
    #     glVertex3fv(verticesList[vertex])
    # glEnd()

    glLineWidth(5)
    glColor3f(1.0, 1.0, 1.0)  
    glBegin(GL_LINES)
    for edge in edgesList:
        for vertex in edge:
            glVertex3fv(verticesList[vertex])
    glEnd()
    pass

def draw():
    glClearColor(0, 0, 0, 1)                                                # set background RGBA color 
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)                        # clear the buffers initialized in the display mode
    glEnable(GL_CULL_FACE)                                                  # enable front/back face culling
    glCullFace(GL_BACK)                                                     # specify which face NOT drawing (culling)
    
    #TODO: write your code for Question 1.d inside draw_cube()
    #draw_cube()

    #TODO: write your code for Question 2.d inside draw_pyramid()
    draw_pyramid()


def main():
    pygame.init()                                                           # initialize a pygame program
    glutInit()                                                              # initialize glut library 

    screen = (width, height)                                                # specify the screen size of the new program window
    display_surface = pygame.display.set_mode(screen, DOUBLEBUF | OPENGL)   # create a display of size 'screen', use double-buffers and OpenGL
    pygame.display.set_caption('CPSC 360 - Ethan Clunie')                   # set title of the program window

    glEnable(GL_DEPTH_TEST)
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)                                             # set mode to projection transformation
    glLoadIdentity()                                                        # reset transf matrix to an identity
    glOrtho(-40, 40, -30, 30, 10, 80)                                       # specify an orthogonal-projection view volume

    glMatrixMode(GL_MODELVIEW)                                              # set mode to modelview (geometric + view transf)
    gluLookAt(0, 0, 50, 0, 0, 0, 0, 1, 0)                                   # set camera's eye, look-at, and view-up in the world
    initmodelMatrix = glGetFloat(GL_MODELVIEW_MATRIX)
    while True:
        bResetModelMatrix = False

        # user interface event handling
        for event in pygame.event.get():

            # quit the window
            if event.type == pygame.QUIT:
                pygame.quit()

            # mouse event
            if event.type == pygame.MOUSEMOTION:
                if pygame.mouse.get_pressed()[0]:
                    glRotatef(event.rel[1], 1, 0, 0)
                    glRotatef(event.rel[0], 0, 1, 0)

            # keyboard event
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_0:
                    bResetModelMatrix = True

        # reset the current model-view back to the initial matrix
        if (bResetModelMatrix):
            glLoadMatrixf(initmodelMatrix)
        
        draw()
        drawAxes()

        pygame.display.flip()
        pygame.time.wait(10)

main()