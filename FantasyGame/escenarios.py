import pygame

class Escenario:
    def __init__(self, ruta_imagen, ancho, alto):
        self.imagen = pygame.image.load(ruta_imagen)
        self.ancho = ancho
        self.alto = alto
    
    def dibujar(self, ventana):
        ventana.blit(self.imagen, (0, 0))
