import pygame
import os
from ambiente import Suelo

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

        # Modo inicial de persecución
        self.perseguir = True

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
        self.dibujar_barras(ventana)

    def dibujar_barras(self, ventana):
        """Dibuja las barras de salud y energía en la parte superior derecha."""
        # Barra de salud (roja)
        barra_salud_ancho = 200
        barra_salud_alto = 20
        salud_porcentaje = self.salud_actual / self.salud_max
        pygame.draw.rect(ventana, (255, 0, 0), (600, 10, barra_salud_ancho * salud_porcentaje, barra_salud_alto))
        pygame.draw.rect(ventana, (255, 255, 255), (600, 10, barra_salud_ancho, barra_salud_alto), 2)

        # Barra de energía (azul)
        barra_energia_ancho = 200
        barra_energia_alto = 20
        energia_porcentaje = self.energia_actual / self.energia_max
        pygame.draw.rect(ventana, (0, 0, 255), (600, 40, barra_energia_ancho * energia_porcentaje, barra_energia_alto))
        pygame.draw.rect(ventana, (255, 255, 255), (600, 40, barra_energia_ancho, barra_energia_alto), 2)

    def mover(self, personaje, suelo):
        """Mueve el enemigo según su estrategia."""
        if self.perseguir:
            self.perseguir_personaje(personaje)

        # Evaluar si debe esquivar un rayo
        elif self.detectar_rayo_cercano(personaje) and self.energia_actual >= 20:
            self.saltar()

        # Estrategia ofensiva
        elif abs(self.x - personaje.x) < 100:  # Si está cerca del personaje
            if self.y > personaje.y:
                self.x -= self.velocidad if self.x > personaje.x else -self.velocidad
                self.y -= self.velocidad

        # Estrategia defensiva
        elif self.salud_actual < self.salud_max * 0.3:
            self.x += self.velocidad if self.x < personaje.x else -self.velocidad

        # Aplicar gravedad
        self.velocidad_y += self.gravedad
        self.y += self.velocidad_y

        # Limitar movimiento con el suelo
        suelo.limitar_movimiento(self)

        # Recuperar energía
        self.recuperar_energia()

        # Actualizar animación
        self.tiempo_animacion += 1
        if self.tiempo_animacion >= 5:  # Cambiar frame cada 5 ticks
            self.tiempo_animacion = 0
            self.indice_animacion = (self.indice_animacion + 1) % len(self.animacion)

    def perseguir_personaje(self, personaje):
        """Movimiento inicial para perseguir al personaje."""
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

        # Desactivar el modo de persecución después de alcanzarlo
        if abs(self.x - personaje.x) < 10 and abs(self.y - personaje.y) < 10:
            self.perseguir = False

    def detectar_rayo_cercano(self, personaje):
        """Detecta si un rayo del personaje está cerca del enemigo."""
        for rayo in personaje.rayos:
            if (self.x < rayo["fin"][0] < self.x + self.width or
                self.x < rayo["inicio"][0] < self.x + self.width):
                return True
        return False

    def saltar(self):
        """Realiza un salto si hay energía suficiente."""
        if self.en_suelo:
            self.velocidad_y = self.velocidad_salto
            self.en_suelo = False
            self.energia_actual -= 20

    def recuperar_energia(self):
        """Recupera energía del enemigo gradualmente."""
        self.energia_actual = min(self.energia_actual + 0.25 + (self.salud_max - self.salud_actual) / 100, self.energia_max)




