import pygame
import os
from typing import List

class Enemigo:
    def __init__(self, x: int, y: int, width: int, height: int, ruta_sprites: str, velocidad: int = 3):
        """Inicializa un enemigo con posición, tamaño, animación y velocidad."""
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocidad = velocidad
        self.animacion: List[pygame.Surface] = []
        self.animacion_espejada: List[pygame.Surface] = []
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

    def cargar_sprites(self, ruta_sprites: str):
        """Carga las imágenes de la animación desde la ruta especificada."""
        for i in range(10):  # Intenta cargar las imágenes del 0 al 9
            try:
                imagen = pygame.image.load(os.path.join(ruta_sprites, f"Esqueleton_{i}.png"))
                self.animacion.append(pygame.transform.scale(imagen, (self.width, self.height)))
                self.animacion_espejada.append(pygame.transform.flip(imagen, True, False))
            except FileNotFoundError:
                print(f"Sprite no encontrado: {os.path.join(ruta_sprites, f'Esqueleton_{i}.png')}")

        if not self.animacion or not self.animacion_espejada:
            print("Advertencia: No se pudieron cargar sprites. Verifica la ruta y los archivos.")

    def dibujar(self, ventana: pygame.Surface):
        """Dibuja el enemigo animado en la ventana proporcionada."""
        if not self.animacion or not self.animacion_espejada:
            print("Advertencia: Las listas de animación están vacías.")
            return

        if self.mirando_izquierda:
            imagen_actual = self.animacion_espejada[self.indice_animacion]
        else:
            imagen_actual = self.animacion[self.indice_animacion]
        ventana.blit(imagen_actual, (self.x, self.y))

    def dibujar_barra_salud(self, ventana: pygame.Surface):
        """Dibuja la barra de salud del enemigo sobre su posición."""
        barra_ancho = self.width
        barra_alto = 5
        salud_porcentaje = self.salud_actual / self.salud_max
        barra_x = self.x
        barra_y = self.y - barra_alto - 5  # Justo encima del enemigo

        # Dibujar la barra de salud
        pygame.draw.rect(ventana, (255, 0, 0), (barra_x, barra_y, barra_ancho * salud_porcentaje, barra_alto))
        pygame.draw.rect(ventana, (255, 255, 255), (barra_x, barra_y, barra_ancho, barra_alto), 1)

    def actualizar_animacion(self, velocidad_animacion: int = 5):
        """Actualiza la animación del enemigo."""
        if not self.animacion:
            return

        self.tiempo_animacion += 1
        if self.tiempo_animacion >= velocidad_animacion:  # Cambiar frame según velocidad de animación
            self.tiempo_animacion = 0
            self.indice_animacion = (self.indice_animacion + 1) % len(self.animacion)

    def mover(self, personaje, suelo, comportamiento: str = "perseguir"):
        """Mueve el enemigo según un comportamiento definido."""
        if comportamiento == "perseguir":
            if self.x < personaje.x:
                self.x += self.velocidad
                self.mirando_izquierda = False
            elif self.x > personaje.x:
                self.x -= self.velocidad
                self.mirando_izquierda = True

        # Aplicar gravedad
        self.velocidad_y += self.gravedad
        self.y += self.velocidad_y

        # Limitar movimiento con el suelo
        suelo.limitar_movimiento(self)

        # Actualizar la animación
        self.actualizar_animacion()









