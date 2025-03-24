
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *
import Acciones.objetos as pinta

def pinta_Enojado():
    pinta.pinta_cono(x=0, y=-1.5, z=0, radio_base=1, altura=1.5, color=(0.9921, 0.654, 0.4), rotacion=(0, 0, 0))
    pinta.pinta_cono(x=0, y=1.5, z=0, radio_base=1, altura=1.5, color=(0.9921, 0.654, 0.4), rotacion=(180, 0, 0))
    pinta.pinta_cubo(x=0, y=2.25, z=0, size=1.5, color=(0.9176, 0.298, 0.2745))
    pinta.pinta_piramide(x=0, y=3.0, z=0, base=1.5, altura=1, color=(0.1764, 0.415, 0.309))
    pinta.pinta_prisma(x=-0.7, y=0.7, z=0, escala=(0.3, 1.0, 0.3), rotacion=(0, 0, 0), color=(0.9176, 0.298, 0.2745))  # Izquierdo
    pinta.pinta_prisma(x=0.7, y=0.7, z=0, escala=(0.3, 1.0, 0.3), rotacion=(0, 0, 0), color=(0.9176, 0.298, 0.2745))  # Der
    pinta.pinta_prisma(x=-0.4, y=-1.8, z=0, escala=(0.3, 0.9, 0.3), rotacion=(0, 0, 0), color=(0.9176, 0.298, 0.2745))  # Izq
    pinta.pinta_prisma(x=0.4, y=-1.8, z=0, escala=(0.3, 0.9, 0.3), rotacion=(0, 0, 0), color=(0.9176, 0.298, 0.2745))  # Der
    pinta.pinta_esfera(x=0, y=2.4, z=0.76, radio=0.2, color=(0, 0, 0)) 
    pinta.pinta_boca(x=0, y=1.7, z=0.76,  radius= 0.4, segments=20, rotacion=(0, 0, 0), color=(0, 0, 0))
    pinta.pinta_linea(0, -0.2, 0, -0.3,3,0.76, 0.3, 3,0.76 , color= (0, 0, 0), grosor= 10.0)  


def pinta_Feliz():

    pinta.pinta_cono(x=0, y=-1.5, z=0, radio_base=1, altura=1.5, color=(0.9921, 0.654, 0.4), rotacion=(0, 0, 0))
    pinta.pinta_cono(x=0, y=1.5, z=0, radio_base=1, altura=1.5, color=(0.9921, 0.654, 0.4), rotacion=(180, 0, 0))
    pinta.pinta_cubo(x=0, y=2.25, z=0, size=1.5, color=(0.9176, 0.298, 0.2745))
    pinta.pinta_piramide(x=0, y=3.0, z=0, base=1.5, altura=1, color=(0.1764, 0.415, 0.309))
    pinta.pinta_prisma(x=-0.7, y=0.7, z=0, escala=(0.3, 1.0, 0.3), rotacion=(0, 0, 0), color=(0.9176, 0.298, 0.2745))  # Izquierdo
    pinta.pinta_prisma(x=0.7, y=0.7, z=0, escala=(0.3, 1.0, 0.3), rotacion=(0, 0, 0), color=(0.9176, 0.298, 0.2745))  # Der
    pinta.pinta_prisma(x=-0.4, y=-1.8, z=0, escala=(0.3, 0.9, 0.3), rotacion=(0, 0, 0), color=(0.9176, 0.298, 0.2745))  # Izq
    pinta.pinta_prisma(x=0.4, y=-1.8, z=0, escala=(0.3, 0.9, 0.3), rotacion=(0, 0, 0), color=(0.9176, 0.298, 0.2745))  # Der
    pinta.pinta_esfera(x=0, y=2.4, z=0.76, radio=0.2, color=(0, 0, 0)) 
    pinta.pinta_boca(x=0, y=2.0, z=0.76,  radius= 0.4, segments=20, rotacion=(180, 0, 0), color=(0, 0, 0))
    pinta.pinta_arco(x=0, y=2.3, z=0.76, radius=0.5, start_angle=50, end_angle=130, segments=50, thickness=7)


def pinta_Triste():

    pinta.pinta_cono(x=0, y=-1.5, z=0, radio_base=1, altura=1.5, color=(0.9921, 0.654, 0.4), rotacion=(0, 0, 0))
    pinta.pinta_cono(x=0, y=1.5, z=0, radio_base=1, altura=1.5, color=(0.9921, 0.654, 0.4), rotacion=(180, 0, 0))
    pinta.pinta_cubo(x=0, y=2.25, z=0, size=1.5, color=(0.9176, 0.298, 0.2745))
    pinta.pinta_piramide(x=0, y=3.0, z=0, base=1.5, altura=1, color=(0.1764, 0.415, 0.309))
    pinta.pinta_prisma(x=-0.7, y=0.7, z=0, escala=(0.3, 1.0, 0.3), rotacion=(0, 0, 0), color=(0.9176, 0.298, 0.2745))  # Izquierdo
    pinta.pinta_prisma(x=0.7, y=0.7, z=0, escala=(0.3, 1.0, 0.3), rotacion=(0, 0, 0), color=(0.9176, 0.298, 0.2745))  # Der
    pinta.pinta_prisma(x=-0.4, y=-1.8, z=0, escala=(0.3, 0.9, 0.3), rotacion=(0, 0, 0), color=(0.9176, 0.298, 0.2745))  # Izq
    pinta.pinta_prisma(x=0.4, y=-1.8, z=0, escala=(0.3, 0.9, 0.3), rotacion=(0, 0, 0), color=(0.9176, 0.298, 0.2745))  # Der
    pinta.pinta_esfera(x=0, y=2.4, z=0.76, radio=0.2, color=(0, 0, 0)) 
    pinta.pinta_arco(x=0, y=1.4, z=0.76, radius=0.5, start_angle=50, end_angle=130, segments=50, thickness=7)
    pinta.pinta_arco(x=0, y=2.3, z=0.76, radius=0.5, start_angle=50, end_angle=130, segments=50, thickness=7)


def pinta_Neutral():
     
    pinta.pinta_cono(x=0, y=-1.5, z=0, radio_base=1, altura=1.5, color=(0.9921, 0.654, 0.4), rotacion=(0, 0, 0))
    pinta.pinta_cono(x=0, y=1.5, z=0, radio_base=1, altura=1.5, color=(0.9921, 0.654, 0.4), rotacion=(180, 0, 0))
    pinta.pinta_cubo(x=0, y=2.25, z=0, size=1.5, color=(0.9176, 0.298, 0.2745))
    pinta.pinta_piramide(x=0, y=3.0, z=0, base=1.5, altura=1, color=(0.1764, 0.415, 0.309))
    pinta.pinta_prisma(x=-0.7, y=0.7, z=0, escala=(0.3, 1.0, 0.3), rotacion=(0, 0, 0), color=(0.9176, 0.298, 0.2745))  # Izquierdo
    pinta.pinta_prisma(x=0.7, y=0.7, z=0, escala=(0.3, 1.0, 0.3), rotacion=(0, 0, 0), color=(0.9176, 0.298, 0.2745))  # Der
    pinta.pinta_prisma(x=-0.4, y=-1.8, z=0, escala=(0.3, 0.9, 0.3), rotacion=(0, 0, 0), color=(0.9176, 0.298, 0.2745))  # Izq
    pinta.pinta_prisma(x=0.4, y=-1.8, z=0, escala=(0.3, 0.9, 0.3), rotacion=(0, 0, 0), color=(0.9176, 0.298, 0.2745))  # Der
    pinta.pinta_esfera(x=0, y=2.4, z=0.76, radio=0.2, color=(0, 0, 0)) 
    pinta.pinta_linea(x=0, y=-1.2,z= 0, x1=-0.3,y1=3,z1=0.76,x2= 0.3,y2= 3,z2=0.76 , color= (0, 0, 0), grosor= 10.0)
    pinta.pinta_arco(x=0, y=2.3, z=0.76, radius=0.5, start_angle=50, end_angle=130, segments=50, thickness=7)


def pinta_Sorpendido():

    pinta.pinta_cono(x=0, y=-1.5, z=0, radio_base=1, altura=1.5, color=(0.9921, 0.654, 0.4), rotacion=(0, 0, 0))
    pinta.pinta_cono(x=0, y=1.5, z=0, radio_base=1, altura=1.5, color=(0.9921, 0.654, 0.4), rotacion=(180, 0, 0))
    pinta.pinta_cubo(x=0, y=2.25, z=0, size=1.5, color=(0.9176, 0.298, 0.2745))
    pinta.pinta_piramide(x=0, y=3.0, z=0, base=1.5, altura=1, color=(0.1764, 0.415, 0.309))
    pinta.pinta_prisma(x=-0.7, y=0.7, z=0, escala=(0.3, 1.0, 0.3), rotacion=(0, 0, 0), color=(0.9176, 0.298, 0.2745))  # Izquierdo
    pinta.pinta_prisma(x=0.7, y=0.7, z=0, escala=(0.3, 1.0, 0.3), rotacion=(0, 0, 0), color=(0.9176, 0.298, 0.2745))  # Der
    pinta.pinta_prisma(x=-0.4, y=-1.8, z=0, escala=(0.3, 0.9, 0.3), rotacion=(0, 0, 0), color=(0.9176, 0.298, 0.2745))  # Izq
    pinta.pinta_prisma(x=0.4, y=-1.8, z=0, escala=(0.3, 0.9, 0.3), rotacion=(0, 0, 0), color=(0.9176, 0.298, 0.2745))  # Der
    pinta.pinta_esfera(x=0, y=2.4, z=0.76, radio=0.2, color=(0, 0, 0)) 
    pinta.pinta_esfera(x=0, y=1.8, z=0.76, radio=0.2, color=(0, 0, 0))
    pinta.pinta_arco(x=0, y=2.4, z=0.76, radius=0.5, start_angle=50, end_angle=130, segments=50, thickness=7)


def pinta_Asustado():

    pinta.pinta_cono(x=0, y=-1.5, z=0, radio_base=1, altura=1.5, color=(0.9921, 0.654, 0.4), rotacion=(0, 0, 0))
    pinta.pinta_cono(x=0, y=1.5, z=0, radio_base=1, altura=1.5, color=(0.9921, 0.654, 0.4), rotacion=(180, 0, 0))
    pinta.pinta_cubo(x=0, y=2.25, z=0, size=1.5, color=(0.9176, 0.298, 0.2745))
    pinta.pinta_piramide(x=0, y=3.0, z=0, base=1.5, altura=1, color=(0.1764, 0.415, 0.309))
    pinta.pinta_prisma(x=-0.7, y=0.7, z=0, escala=(0.3, 1.0, 0.3), rotacion=(0, 0, 0), color=(0.9176, 0.298, 0.2745))  # Izquierdo
    pinta.pinta_prisma(x=0.7, y=0.7, z=0, escala=(0.3, 1.0, 0.3), rotacion=(0, 0, 0), color=(0.9176, 0.298, 0.2745))  # Der
    pinta.pinta_prisma(x=-0.4, y=-1.8, z=0, escala=(0.3, 0.9, 0.3), rotacion=(0, 0, 0), color=(0.9176, 0.298, 0.2745))  # Izq
    pinta.pinta_prisma(x=0.4, y=-1.8, z=0, escala=(0.3, 0.9, 0.3), rotacion=(0, 0, 0), color=(0.9176, 0.298, 0.2745))  # Der
    pinta.pinta_esfera(x=0, y=2.4, z=0.76, radio=0.2, color=(0, 0, 0)) 
    pinta.pinta_boca(x=0, y=1.7, z=0.76,  radius= 0.4, segments=20, rotacion=(0, 0, 0), color=(0, 0, 0))
    pinta.pinta_arco(x=0, y=2.4, z=0.76, radius=0.5, start_angle=50, end_angle=130, segments=50, thickness=7)


def personaje(expresion):
    if expresion == 1:
        pinta_Feliz()
    if expresion == 2:
        pinta_Enojado()
    if expresion == 3:
        pinta_Asustado()
    if expresion == 4:
        pinta_Triste()
    if expresion == 5:
        pinta_Sorpendido()
    if expresion == 6:
        pinta_Neutral()

    

    
