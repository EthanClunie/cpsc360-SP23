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

def draw_Scarecrow():                                                  # This is the drawing function drawing all graphics (defined by you)
    glClearColor(0, 0, 0, 1)                                                # set background RGBA color 
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)                        # clear the buffers initialized in the display mode

    # configure quatratic drawing
    quadratic = gluNewQuadric()
    gluQuadricDrawStyle(quadratic, GLU_FILL)  

    # Head (sphere: radius=2.5) 
    glPushMatrix()
    glTranslatef(0.0, 12.5, 0.0)
    glColor3f(0.0, 1.0, 0.0)
    gluSphere(quadratic, 2.5, 32, 32)
    glPopMatrix()

    # Nose (cylinder: radius=0.2, length=2)
    glPushMatrix()
    glTranslatef(0.0, 12.5, 2.5)
    glColor3f(1.0, 0.0, 0.0)
    gluCylinder(quadratic, 0.3, 0.0, 1.8, 32, 32)
    glPopMatrix()    

    # Torso (cylinder: radius=2.5, length=10)
    glPushMatrix()
    glRotatef(-90.0, 1, 0, 0)
    glColor3f(1.0, 1.0, 0.0)
    gluCylinder(quadratic, 2.5, 2.5, 10.0, 32, 32)
    glPopMatrix()

    # Left Leg (cylinders: radius=1.0, length=12)
    glPushMatrix()
    glTranslatef(-1.2, 0.0, 0.0)
    glRotatef(90.0, 1, 0, 0)
    glColor3f(1.0, 0.0, 0.0)
    gluCylinder(quadratic, 1.0, 1.0, 12.0, 32, 32)
    glPopMatrix()

    # Right Leg (cylinders: radius=1.0, length=12)
    glPushMatrix()
    glTranslatef(1.2, 0.0, 0.0)
    glRotatef(90.0, 1, 0, 0)
    glColor3f(1.0, 0.0, 0.0)
    gluCylinder(quadratic, 1.0, 1.0, 12.0, 32, 32)
    glPopMatrix()

    # Left Arm (cylinders: radius=0.8, length=10)
    glPushMatrix()
    glTranslatef(-2.5, 9.0, 0.0)
    glRotatef(-90.0, 0, 1, 0)
    glColor3f(0.0, 0.0, 1.0)
    gluCylinder(quadratic, 1.0, 1.0, 12.0, 32, 32)
    glPopMatrix()

    # Right Arm (cylinders: radius=0.8, length=10)
    glPushMatrix()
    glTranslatef(2.5, 9.0, 0.0)
    glRotatef(90.0, 0, 1, 0)
    glColor3f(0.0, 0.0, 1.0)
    gluCylinder(quadratic, 1.0, 1.0, 12.0, 32, 32)
    glPopMatrix()

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
    glOrtho(-40, 40, -30, 30, 0, 100)                                       # specify an orthogonal-projection view volume

    glMatrixMode(GL_MODELVIEW)                                              # set mode to modelview (geometric + view transf)
    initmodelMatrix = glGetFloat(GL_MODELVIEW_MATRIX)
    whichQuestion = 1

    # Question 1 values
    offset_x = 0
    offset_y = 0

    # Question 2 values
    eye_x = 0
    eye_y = 0
    eye_z = 50
    lookat_x = 0
    lookat_y = 0
    lookat_z = 0
    up_x = 0
    up_y = 1
    up_z = 0

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
                elif event.key == pygame.K_UP:      # pan camera up by 1
                    offset_y += 1
                elif event.key == pygame.K_DOWN:    # pan camera down by 1
                    offset_y -= 1
                elif event.key == pygame.K_RIGHT:   # pan camera right by 1
                    offset_x += 1
                elif event.key == pygame.K_LEFT:    # pan camera left by 1
                    offset_x -= 1
                elif event.key == pygame.K_a:       # view left side: y-up, z-right
                    eye_x = -50
                    eye_y = 0
                    eye_z = 0
                    lookat_x = 1
                    lookat_y = 0
                    lookat_z = 0
                    up_x = 0
                    up_y = 1
                    up_z = 0
                elif event.key == pygame.K_d:       # view right side: y-up, z-left
                    eye_x = 50
                    eye_y = 0
                    eye_z = 0
                    lookat_x = -1
                    lookat_y = 0
                    lookat_z = 0
                    up_x = 0
                    up_y = 1
                    up_z = 0
                elif event.key == pygame.K_w:       # view back side: y-up, x-left
                    eye_x = 0
                    eye_y = 0
                    eye_z = -50
                    lookat_x = -1
                    lookat_y = 0
                    lookat_z = 0
                    up_x = 0
                    up_y = 1
                    up_z = 0
                elif event.key == pygame.K_s:       # view front side: y-up, x-right
                    eye_x = 0
                    eye_y = 0
                    eye_z = 50
                    lookat_x = 0
                    lookat_y = 0
                    lookat_z = 0
                    up_x = 0
                    up_y = 1
                    up_z = 0
                elif event.key == pygame.K_q:       # view top side: z-up, x-left
                    eye_x = 0
                    eye_y = 50
                    eye_z = 0
                    lookat_x = 0
                    lookat_y = 0
                    lookat_z = 0
                    up_x = 0
                    up_y = 0
                    up_z = 1
                elif event.key == pygame.K_e:       # view bottom side: z-up, x-right
                    eye_x = 0
                    eye_y = -50
                    eye_z = 0
                    lookat_x = 1
                    lookat_y = 0
                    lookat_z = 0
                    up_x = 0
                    up_y = 0
                    up_z = 1

        # obtain the current model-view matrix after mouse rotation (if any)
        curmodelMatrix = glGetFloat(GL_MODELVIEW_MATRIX)

        # reset the current view to the initial view
        if (bResetModelMatrix):
            glLoadMatrixf(initmodelMatrix)
        
        # transform the camera and draw the model
        glPushMatrix()
        glLoadMatrixf(initmodelMatrix)

        if whichQuestion == 1:
            gluLookAt(offset_x, offset_y, 50, offset_x, offset_y, 0, 0, 1, 0)

        #TODO: Question 2: Modify the below gluLookAt()
        elif whichQuestion == 2:
            gluLookAt(eye_x, eye_y, eye_z, lookat_x, lookat_y, lookat_z, up_x, up_y, up_z)
        
        glPushMatrix()
        glMultMatrixf(curmodelMatrix) # multiply with the m-v matrix after mouse rotation
        draw_Scarecrow()
        glPopMatrix()
        drawAxes()
        glPopMatrix()

        pygame.display.flip()
        pygame.time.wait(10)

main()