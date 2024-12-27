import pygame
import os

class Enemigo:
    def __init__(self, x, y, width, height, ruta_sprites):
        """Inicializa un enemigo con posición, tamaño y animación."""
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocidad = 3
        self.animacion = []
        self.animacion_espejada = []
        self.mirando_izquierda = True  # Comienza mirando a la izquierda
        self.cargar_sprites(ruta_sprites)
        self.indice_animacion = 0
        self.tiempo_animacion = 0
        self.en_suelo = False  # Estado respecto al suelo

        # Atributos de salud y energía
        self.salud_max = 100
        self.energia_max = 100
        self.salud_actual = 100
        self.energia_actual = 100
        self.velocidad_salto = -15  # Velocidad inicial del salto
        self.gravedad = 1  # Fuerza de la gravedad
        self.velocidad_y = 0

    def cargar_sprites(self, ruta_sprites):
        """Carga las imágenes de la animación desde la ruta especificada."""
        for i in range(10):  # Hay 10 imágenes Esqueleton_0.png a Esqueleton_9.png
            imagen = pygame.image.load(os.path.join(ruta_sprites, f"Esqueleton_{i}.png"))
            self.animacion.append(pygame.transform.scale(imagen, (self.width, self.height)))
            self.animacion_espejada.append(pygame.transform.flip(imagen, True, False))

    def dibujar(self, ventana):
        """Dibuja el enemigo animado en la ventana proporcionada."""
        if self.mirando_izquierda:
            imagen_actual = self.animacion_espejada[self.indice_animacion]
        else:
            imagen_actual = self.animacion[self.indice_animacion]
        ventana.blit(imagen_actual, (self.x, self.y))

    def dibujar_barra_salud(self, ventana):
        """Dibuja la barra de salud del enemigo sobre su posición."""
        barra_ancho = self.width
        barra_alto = 5
        salud_porcentaje = self.salud_actual / self.salud_max
        barra_x = self.x
        barra_y = self.y - barra_alto - 5  # Justo encima del enemigo

        # Dibujar la barra de salud
        pygame.draw.rect(ventana, (255, 0, 0), (barra_x, barra_y, barra_ancho * salud_porcentaje, barra_alto))
        pygame.draw.rect(ventana, (255, 255, 255), (barra_x, barra_y, barra_ancho, barra_alto), 1)

    def actualizar_animacion(self):
        """Actualiza la animación del enemigo."""
        self.tiempo_animacion += 1
        if self.tiempo_animacion >= 5:  # Cambiar frame cada 5 ticks
            self.tiempo_animacion = 0
            self.indice_animacion = (self.indice_animacion + 1) % len(self.animacion)

    def mover(self, personaje, suelo):
        """Mueve el enemigo según su estrategia."""
        if self.x < personaje.x:
            self.x += self.velocidad
            self.mirando_izquierda = False
        elif self.x > personaje.x:
            self.x -= self.velocidad
            self.mirando_izquierda = True

        if self.y < personaje.y:
            self.y += self.velocidad
        elif self.y > personaje.y:
            self.y -= self.velocidad

        # Aplicar gravedad
        self.velocidad_y += self.gravedad
        self.y += self.velocidad_y

        # Limitar movimiento con el suelo
        suelo.limitar_movimiento(self)

        # Actualizar la animación
        self.actualizar_animacion()






