# suelo.py
import pygame

class Suelo:
    def __init__(self, ancho_pantalla, alto_pantalla, altura_suelo=20, color=(100, 100, 100)):
        """
        Clase que representa el suelo del juego.

        Args:
            ancho_pantalla (int): Ancho de la pantalla.
            alto_pantalla (int): Alto de la pantalla.
            altura_suelo (int): Altura del suelo.
            color (tuple): Color del suelo (RGB).
        """
        self.ancho_pantalla = ancho_pantalla
        self.alto_pantalla = alto_pantalla
        self.altura_suelo = altura_suelo
        self.color = color

        # Define el rectángulo del suelo
        self.rect = pygame.Rect(0, alto_pantalla - altura_suelo, ancho_pantalla, altura_suelo)

    def limitar_movimiento(self, personaje):
        """
        Verifica si el personaje está tocando el suelo y ajusta su posición.

        Args:
            personaje: El objeto del personaje que tiene atributos como `y`, `height`, y `velocidad_y`.
        """
        if personaje.y + personaje.height >= self.rect.top:
            personaje.y = self.rect.top - personaje.height
            personaje.en_suelo = True
            personaje.velocidad_y = 0
        else:
            personaje.en_suelo = False

    def dibujar(self, ventana):
        """
        Dibuja el suelo en la ventana.

        Args:
            ventana: La superficie donde se dibuja el suelo.
        """
        pygame.draw.rect(ventana, self.color, self.rect)


