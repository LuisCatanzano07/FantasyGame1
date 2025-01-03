import pygame

class Suelo:
    def __init__(self, y, color=None, altura=10, textura=None, velocidad=0, color_cambio=None):
        """
        Inicializa el suelo.
        :param y: Altura del suelo en píxeles desde la parte superior de la ventana.
        :param color: Color inicial del suelo (tuple RGB).
        :param altura: Altura del suelo en píxeles.
        :param textura: Imagen de textura para el suelo (opcional).
        :param velocidad: Velocidad de movimiento vertical (positivo hacia abajo, negativo hacia arriba).
        :param color_cambio: Color alternativo para cambiar dinámicamente (tuple RGB).
        """
        self.y = y
        self.color = color
        self.altura = altura
        self.textura = textura
        self.velocidad = velocidad
        self.color_cambio = color_cambio
        self.color_actual = color  # Color que se renderiza actualmente
        self.tiempo_cambio = 0  # Contador para alternar colores

    def mover(self):
        """
        Mueve el suelo verticalmente según su velocidad.
        """
        self.y += self.velocidad

    def alternar_color(self, tiempo_actual, intervalo):
        """
        Cambia el color del suelo dinámicamente.
        :param tiempo_actual: Tiempo actual (en milisegundos).
        :param intervalo: Intervalo en milisegundos para alternar el color.
        """
        if self.color and self.color_cambio:
            if tiempo_actual - self.tiempo_cambio > intervalo:
                self.color_actual = self.color_cambio if self.color_actual == self.color else self.color
                self.tiempo_cambio = tiempo_actual

    def dibujar(self, ventana, ancho):
        """
        Dibuja el suelo en la ventana proporcionada.
        :param ventana: Superficie de pygame donde se dibujará el suelo.
        :param ancho: Ancho de la ventana.
        """
        if self.textura:
            # Si se proporciona una textura, se dibuja la imagen repetidamente para llenar el ancho
            for x in range(0, ancho, self.textura.get_width()):
                ventana.blit(self.textura, (x, self.y))
        else:
            # Dibujar un rectángulo sólido si no hay textura
            pygame.draw.rect(ventana, self.color_actual, (0, self.y, ancho, self.altura))

    def limitar_movimiento(self, entidad):
        """
        Asegura que la entidad no pase por debajo del suelo.
        :param entidad: Objeto que tiene propiedades 'y', 'height' y 'en_suelo'.
        """
        if entidad.y + entidad.height > self.y:
            entidad.y = self.y - entidad.height
            entidad.en_suelo = True
        else:
            entidad.en_suelo = False

