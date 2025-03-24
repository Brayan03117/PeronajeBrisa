
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math
def pinta_cono(x, y, z, radio_base, altura, color, rotacion):
    
    glPushMatrix()
    glTranslatef(x, y, z)
    glRotatef(rotacion[0], 1, 0, 0)
    glRotatef(rotacion[1], 0, 1, 0)
    glRotatef(rotacion[2], 0, 0, 1)

    glColor3f(*color)
    glRotatef(-90, 1, 0, 0)  # Alinea el cono en eje Y

    quad = gluNewQuadric()
    gluCylinder(quad, radio_base, 0.0, altura, 20, 20)

    # Base del cono
    glRotatef(180, 1, 0, 0)
    gluDisk(quad, 0.0, radio_base, 20, 1)

    glPopMatrix()

def pinta_cubo(x, y, z, size, color):
   
    glEnable(GL_DEPTH_TEST)  # Habilita el buffer de profundidad
    hs = size / 2.0  # mitad del tamaño para centrarlo
    glPushMatrix()
    glTranslatef(x, y, z)
    glColor3f(*color)

    # Caras del cubo
    glBegin(GL_QUADS)
    # Cara frontal
    glVertex3f(-hs, -hs,  hs)
    glVertex3f( hs, -hs,  hs)
    glVertex3f( hs,  hs,  hs)
    glVertex3f(-hs,  hs,  hs)

    # Cara trasera
    glVertex3f( hs, -hs, -hs)
    glVertex3f(-hs, -hs, -hs)
    glVertex3f(-hs,  hs, -hs)
    glVertex3f( hs,  hs, -hs)

    # Cara izquierda
    glVertex3f(-hs, -hs, -hs)
    glVertex3f(-hs, -hs,  hs)
    glVertex3f(-hs,  hs,  hs)
    glVertex3f(-hs,  hs, -hs)

    # Cara derecha
    glVertex3f( hs, -hs,  hs)
    glVertex3f( hs, -hs, -hs)
    glVertex3f( hs,  hs, -hs)
    glVertex3f( hs,  hs,  hs)

    # Cara superior
    glVertex3f(-hs,  hs,  hs)
    glVertex3f( hs,  hs,  hs)
    glVertex3f( hs,  hs, -hs)
    glVertex3f(-hs,  hs, -hs)

    # Cara inferior
    glVertex3f(-hs, -hs, -hs)
    glVertex3f( hs, -hs, -hs)
    glVertex3f( hs, -hs,  hs)
    glVertex3f(-hs, -hs,  hs)
    glEnd()

    glPopMatrix()

def pinta_piramide(x, y, z, base, altura, color):
    hs = base / 2.0  # mitad del tamaño base
    glPushMatrix()
    glTranslatef(x, y, z)
    glColor3f(*color)

    # Caras triangulares
    glBegin(GL_TRIANGLES)
    # Frente
    glVertex3f(-hs, 0, hs)
    glVertex3f(hs, 0, hs)
    glVertex3f(0, altura, 0)

    # Derecha
    glVertex3f(hs, 0, hs)
    glVertex3f(hs, 0, -hs)
    glVertex3f(0, altura, 0)

    # Atrás
    glVertex3f(hs, 0, -hs)
    glVertex3f(-hs, 0, -hs)
    glVertex3f(0, altura, 0)

    # Izquierda
    glVertex3f(-hs, 0, -hs)
    glVertex3f(-hs, 0, hs)
    glVertex3f(0, altura, 0)
    glEnd()

    # Base cuadrada
    glBegin(GL_QUADS)
    glVertex3f(-hs, 0, hs)
    glVertex3f(hs, 0, hs)
    glVertex3f(hs, 0, -hs)
    glVertex3f(-hs, 0, -hs)
    glEnd()

    glPopMatrix()

def pinta_prisma(x, y, z, escala, rotacion, color):

    glPushMatrix()
    glTranslatef(x, y, z)
    glRotatef(rotacion[0], 1, 0, 0)
    glRotatef(rotacion[1], 0, 1, 0)
    glRotatef(rotacion[2], 0, 0, 1)
    glScalef(*escala)
    glColor3f(*color)

    # Dibuja cubo base (prisma escalado)
    glBegin(GL_QUADS)
    # Cara frontal
    glVertex3f(-0.5, -0.5, 0.5)
    glVertex3f( 0.5, -0.5, 0.5)
    glVertex3f( 0.5,  0.5, 0.5)
    glVertex3f(-0.5,  0.5, 0.5)

    # Cara trasera
    glVertex3f( 0.5, -0.5, -0.5)
    glVertex3f(-0.5, -0.5, -0.5)
    glVertex3f(-0.5,  0.5, -0.5)
    glVertex3f( 0.5,  0.5, -0.5)

    # Izquierda
    glVertex3f(-0.5, -0.5, -0.5)
    glVertex3f(-0.5, -0.5,  0.5)
    glVertex3f(-0.5,  0.5,  0.5)
    glVertex3f(-0.5,  0.5, -0.5)

    # Derecha
    glVertex3f( 0.5, -0.5,  0.5)
    glVertex3f( 0.5, -0.5, -0.5)
    glVertex3f( 0.5,  0.5, -0.5)
    glVertex3f( 0.5,  0.5,  0.5)

    # Superior
    glVertex3f(-0.5, 0.5,  0.5)
    glVertex3f( 0.5, 0.5,  0.5)
    glVertex3f( 0.5, 0.5, -0.5)
    glVertex3f(-0.5, 0.5, -0.5)

    # Inferior
    glVertex3f(-0.5, -0.5, -0.5)
    glVertex3f( 0.5, -0.5, -0.5)
    glVertex3f( 0.5, -0.5,  0.5)
    glVertex3f(-0.5, -0.5,  0.5)
    glEnd()
    glPopMatrix()


def pinta_esfera(x, y, z, radio, color):
    glPushMatrix()
    glTranslatef(x, y, z)
    glColor3f(*color)
    quad = gluNewQuadric()
    gluSphere(quad, radio, 20, 20)
    glPopMatrix()


def pinta_boca(x, y, z, radius, segments, rotacion, color):###cambiar
   
    glPushMatrix()
    glTranslatef(x, y, z)
    
    glRotatef(rotacion[0], 1, 0, 0)
    
    glColor3f(*color)

    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(0, 0)  # Centro del semicírculo

    for i in range(segments + 1):
        angle = math.pi * (i / segments)  # De 0 a π (180 grados)
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        glVertex2f(x, y)

    glEnd()

    glPopMatrix()

def pinta_linea(x,y,z,x1, y1, z1, x2, y2, z2, color, grosor):
    
    glPushMatrix()
    glTranslatef(x, y, z)

    glColor3f(*color)   # Establece el color de la línea
    glLineWidth(grosor)  # Define el grosor de la línea
    glBegin(GL_LINES)
    glVertex3f(x1, y1, z1)  # Punto inicial
    glVertex3f(x2, y2, z2)  # Punto final
    glEnd()

    glPopMatrix()


def pinta_arco(x, y, z, radius=0.5, start_angle=50, end_angle=130, segments=50, thickness=7):
    
    glPushMatrix()

    glTranslatef(x,y,z)

    glLineWidth(thickness)  # Establece el grosor de la línea
    glBegin(GL_LINE_STRIP)  # Dibuja solo las líneas del arco

    for i in range(segments + 1):
        angle = math.radians(start_angle + (end_angle - start_angle) * i / segments)
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        glVertex2f(x, y)

    glEnd()
    glPopMatrix()


