
# Módulos
 
from os import sendfile
import sys, pygame
from pygame.locals import *


# Constantes

width = 640
height = 480

# Clases
# ---------------------------------------------------------------------

class Bola(pygame.sprite.Sprite):    #creamos la clase pelota, manejo de Sprites.
    def __init__(self):     # el método init inica una clase
        pygame.sprite.Sprite.__init__(self)   # inicia el método init de la clase heredada
        self.image = load_image('images/pedro.png', True)  #cargamos la imagen pelota. Tenemos True por tiene zonas transparentes
        self.rect = self.image.get_rect()  #obtiene un rectángulo con las dimensiones y posición de la imagen
        self.rect.centerx = width/2  #definimos la ubicacion de la pelota en el centro de la pantalla
        self.rect.centery = height/2  #definimos la ubicacion de la pelota en el centro de la pantalla
        self.speed = [0.5, -0.5]   #separamos la velocidad de la pelota en 2, en x e y

    def actualizar(self,time, pala_jug, pala_cpu, puntos):   #definimos el metodo, con los parametros self y time
        self.rect.centerx += self.speed[0] * time   # espacio = velocidad * tiempo . centro es centerx y le sumamos la veloc.*time
        self.rect.centery += self.speed[1] * time

        if self.rect.left &lt;= 0:
            puntos[1] += 1

        if self.rect.right &gt;= width:
            puntos[0] +=1

        if self.rect.left &lt;= 0 or self.rect.right &lt;= width:
            self.speed[0] = -self.speed[0]
            self.rect.centerx += self.speed[0] * time

        if self.rect.top &lt;= 0 or self.rect.bottom &lt;= height:
            self.speed[1] = -self.speed[1]
            self.rect.centery += self.speed[1] * time
        
        if pygame.sprite.collide_rect(self, pala_jug):
            self.speed[0] = -self.speed[0]
            self.rect.centerx += self.speed[0]*time
        
        if pygame.sprite.collide_rect(self, pala_cpu):
            self.speed[0] = -self.speed[0]
            self.rect.centerx += self.speed[0]*time

        return puntos

# get_rect() tiene unos parámetros muy útiles que podemos modificar para posicionar y redimensionar nuestra imagen

#top, left, bottom, right
#topleft, bottomleft, topright, bottomright
#midtop, midleft, midbottom, midright
#center, centerx, centery
#size, width, height
#w, h

class Pala(pygame.sprite.Sprite):
    def __init__(self,x):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image('images/bandera.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = height/2
        self.speed = 0.5
    
    def mover(self, time, keys):
        if self.rect.top >= 0:
            if keys[K_UP]:
                self.rect.centery -= self.speed*time
        if self.rect.bottom <= height:
            if keys[K_DOWN]:
                self.rect.centery += self.speed*time

    def ia(self, time, bola):
        if bola.speed[0] >= 0 and bola.rect.centerx >= width/2:
            if self.rect.centery < bola.rect.centery:
                self.rect.centery += self.speed * time
            if self.rect.centery > bola.rect.centery:
                self.rect.centery -= self.speed*time


# ---------------------------------------------------------------------
 
# Funciones
# ---------------------------------------------------------------------
 
def load_image(filename, transparent=False):
    try: image = pygame.image.load(filename)
    except pygame.error.message:
        raise SystemExit.message
    image = image.convert()
    if transparent:
            color = image.get_at((0,0))
            image.set_colorkey(color,RLEACCEL)
    return image

# &quot;images/DroidSans.ttf&quot;
def texto(texto, posx, posy, color=(255, 255, 255)):
    fuente = pygame.font.Font('images/DroidSans.ttf', 25)
    salida = pygame.font.Font.render(fuente, texto, 1, color)
    salida_rect = salida.get_rect()
    salida_rect.centerx = posx
    salida_rect.centery = posy
    return salida, salida_rect

# ---------------------------------------------------------------------
 
def main():
    screen = pygame.display.set_mode((width,height))    
    pygame.display.set_caption('Mi primer juego')

    background_imagen = load_image('images/fondo.jpg')   #definimos el fondo que usaremos
    bola = Bola()   # definimos la bola que usaremos
    pala_jug = Pala(30)
    pala_cpu = Pala(width-30)

    clock = pygame.time.Clock()  #crear un reloj que controle el juego, va antes del bucle.

    puntos = [0,0]



    while True:    # creo un bucle infinito para mantener la ventana abierta
        time = clock.tick(60)   # para saber cuanto tiempo pasa cada vez que se ejecuta una intereccion del bucle.
        keys = pygame.key.get_pressed()
        for eventos in pygame.event.get() :   # el for recorre el evento
            if eventos.type == QUIT:     # el evento es darle a la X, es decir QUIT
                sys.exit(0)    # sys me permite cerrar la ventana

        puntos = bola.actualizar(time, pala_jug, pala_cpu, puntos)  #actualizar la posicion de la bola antes de actualizar en la ventana
        pala_jug.mover(time,keys)
        pala_cpu.ia(time,bola)

        p_jug, p_jug_rect = texto(str(puntos[0]), width/4, 40)
        p_cpu, p_cpu_rect = texto(str(puntos[1]), width-width/4, 40)

        screen.blit(background_imagen,(0,0))   #colocamos el fondo en la ventana
        screen.blit(bola.image, bola.rect)   #colocamos la bola en la ventana
        screen.blit(pala_jug.image, pala_jug.rect)
        screen.blit(pala_cpu.image, pala_cpu.rect)
        screen.blit(pala_jug.image, pala_jug.rect)
        screen.blit(pala_cpu.image, pala_cpu.rect)
        pygame.display.flip()
    return 0
 
if __name__ == '__main__':
    pygame.init()
    main()
