
import pygame
from OpenGL.GLU import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from pygame.locals import *
from Acciones import escenarios as es
from Acciones import sonidos as sd
from src.personaje import personaje

expresion=1

camara_z = -9
rotacion_y = 0.0
rotacion_x = 0.0

velocidad_zoom = 0.5


pygame.init()
pygame.mixer.init()
glutInit(sys.argv)
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
glClearColor(0.5, 0.8, 1.0, 1)
gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
glTranslatef(0.0, -1.0, camara_z)
glEnable(GL_DEPTH_TEST)
fondoAc='Imagenes/escenario1.jpg' #Controla el fondo actual


#Centra y hace invisible el cursor
pygame.event.set_grab(True)
pygame.mouse.set_visible(False)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False


            if event.key == K_w:#acercar
                camara_z += 0.5
                glLoadIdentity()
                gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
                glTranslatef(0.0, -1.0, camara_z)
            if event.key == K_s:#alejar
                camara_z -= 0.5
                glLoadIdentity()
                gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
                glTranslatef(0.0, -1.0, camara_z)
            if event.key == K_z:#original
                camara_z = -9
                rotacion_x = 0
                rotacion_y = 0
                glLoadIdentity()
                gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
                glTranslatef(0.0, -1.0, camara_z)
            if event.key == K_q:# arriba
                rotacion_x += 2
                glLoadIdentity()
                gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
                glTranslatef(0.0, -1.0, camara_z)
            if event.key == K_e:# abajo
                rotacion_x -= 2
                glLoadIdentity()
                gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
                glTranslatef(0.0, -1.0, camara_z)
            if event.key == K_d:# der
                rotacion_y -= 2
                glLoadIdentity()
                gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
                glTranslatef(0.0, -1.0, camara_z)
            if event.key == K_a:# Izq
                rotacion_y += 2
                glLoadIdentity()
                gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
                glTranslatef(0.0, -1.0, camara_z)
            
            



            if event.key == pygame.K_1:
                fondoAc='Imagenes/escenario1.jpg'#Se busca desde la carpeta donde esta el main, lo estabas buscando afuera de la carpeta
                sd.sonidoOn('Sonidos/sonido1.mp3')
            if event.key == pygame.K_2:
                fondoAc='Imagenes/escenario2.jpg'
                sd.sonidoOn('Sonidos/sonido2.mp3')
            if event.key == pygame.K_3:
                fondoAc='Imagenes/escenario3.jpg'
                sd.sonidoOn('Sonidos/sonido3.mp3')
            if event.key == pygame.K_4:
                fondoAc='Imagenes/escenario4.jpg'
                sd.sonidoOn('Sonidos/sonido4.mp3')
            if event.key == pygame.K_5:
                fondoAc='Imagenes/escenario5.png'
                sd.sonidoOn('Sonidos/sonido5.mp3')
                
            if event.key == pygame.K_6:# prender sonido general
                fondoAc='Imagenes/escenario5.png'
                sd.sonidoOn('Sonidos/sonido5.mp3')
            if event.key == pygame.K_7:# apagar sonido general
                fondoAc='Imagenes/escenario5.png'
                sd.sonidoOn('Sonidos/sonido5.mp3')




            if event.key == pygame.K_g:
                
                fondoAc='Imagenes/escenario1.jpg'
                sd.sonidoOn('Sonidos/sonido1.mp3')
                expresion=1
            if event.key == pygame.K_h:
                
                fondoAc='Imagenes/escenario1.jpg'
                sd.sonidoOn('Sonidos/sonido1.mp3')
                expresion=2
            
            if event.key == pygame.K_j:
                
                fondoAc='Imagenes/escenario1.jpg'
                sd.sonidoOn('Sonidos/sonido1.mp3')
                expresion=3
                
            if event.key == pygame.K_k:
                
                fondoAc='Imagenes/escenario1.jpg'
                sd.sonidoOn('Sonidos/sonido1.mp3')
                expresion=4
                
            if event.key == pygame.K_l:
                
                fondoAc='Imagenes/escenario1.jpg'
                sd.sonidoOn('Sonidos/sonido1.mp3')
                
                expresion=5
                
            if event.key == pygame.K_m:
                
                fondoAc='Imagenes/escenario1.jpg'
                sd.sonidoOn('Sonidos/sonido1.mp3')
                expresion=6
                
            #Acciones
            if event.key == pygame.K_x:#Brazo izquierdo arriba
                expresion=7
            if event.key == pygame.K_c:#Ambos brazos arriba
                expresion=8
            if event.key == pygame.K_v: #Señalar
                expresion=9
            #if event.key == pygame.K_b:
            #if event.key == pygame.K_n:
            
                

    #Se pueden movimientos mas fluidos con el mouse
    mouse_dx, mouse_dy = pygame.mouse.get_rel()
    rotacion_y += mouse_dx * 0.1
    rotacion_x += mouse_dy * 0.1
    rotacion_x = max(-90, min(90, rotacion_x))
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glPushMatrix()
    glRotatef(rotacion_x, 1, 0, 0)
    glRotatef(rotacion_y, 0, 1, 0)


    glColor3f(1.0, 1.0, 1.0)
    #sd.sonidoOn('Sonidos/sonido1.mp3')
    es.pinta_escenario(fondoAc) 

    personaje(expresion)
    

    glPopMatrix()
    pygame.display.flip()
    pygame.time.wait(10)

pygame.quit()