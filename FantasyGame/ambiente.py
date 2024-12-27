import pygame

class Suelo:
    def __init__(self, y, color, altura):
        """Inicializa el suelo."""
        self.y = y  # Altura del suelo
        self.color = color
        self.altura = altura

    def dibujar(self, ventana, ancho):
        """Dibuja el suelo en la ventana proporcionada."""
        pygame.draw.rect(ventana, self.color, (0, self.y, ancho, self.altura))

    def limitar_movimiento(self, entidad):
        """Asegura que la entidad no pase por debajo del suelo."""
        if entidad.y + entidad.height > self.y:
            entidad.y = self.y - entidad.height
            entidad.en_suelo = True
        else:
            entidad.en_suelo = False
