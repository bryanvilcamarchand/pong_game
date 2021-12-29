
# Módulos
 
import sys, pygame
from pygame.locals import *


# Constantes

width = 480
height = 480

# Clases
# ---------------------------------------------------------------------
 
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


# ---------------------------------------------------------------------
 
def main():
    screen = pygame.display.set_mode((width,height))    
    pygame.display.set_caption('Mi primer juego')

    background_imagen = load_image('images/fondo.jpg')



    while True:    # creo un bucle infinito para mantener la ventana abierta
        for eventos in pygame.event.get() :   # el for recorre el evento
            if eventos.type == QUIT:     # el evento es darle a la X, es decir QUIT
                sys.exit(0)    # sys me permite cerrar la ventana

        
        screen.blit(background_imagen,(0,0))
        pygame.display.flip()
    return 0
 
if __name__ == '__main__':
    pygame.init()
    main()
