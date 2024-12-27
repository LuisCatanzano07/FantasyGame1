import pygame
import os
from ambiente import Suelo

class Personaje:
    def __init__(self, x, y, width, height, ruta_sprites):
        """Inicializa un personaje con posición, tamaño y animaciones."""
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocidad = 5
        self.animacion = []
        self.cargar_sprites(ruta_sprites)
        self.indice_animacion = 0
        self.tiempo_animacion = 0
        self.en_suelo = False  # Estado del personaje respecto al suelo
        self.velocidad_salto = -15  # Velocidad inicial del salto
        self.gravedad = 1  # Fuerza de la gravedad
        self.velocidad_y = 0
        self.mirando_izquierda = False  # Indica si el personaje está espejado
        self.tecla_f_presionada = False  # Controla el estado de la tecla F

        # Atributos de salud y energía
        self.salud_max = 100
        self.energia_max = 100
        self.salud_actual = 100
        self.energia_actual = 100

        # Control de recuperación de energía
        self.pasos_para_recuperar = 10
        self.pasos_actuales = 0

        # Rayos
        self.rayos = []
        self.costo_rayo = 20
        self.velocidad_rayo = 10

    def cargar_sprites(self, ruta_sprites):
        """Carga las imágenes de la animación desde la ruta especificada."""
        for i in range(7):  # Hay 7 imágenes Player_0.png a Player_6.png
            imagen = pygame.image.load(os.path.join(ruta_sprites, f"Player_{i}.png"))
            self.animacion.append(pygame.transform.scale(imagen, (self.width, self.height)))

    def dibujar(self, ventana):
        """Dibuja el personaje animado en la ventana proporcionada."""
        imagen_actual = self.animacion[self.indice_animacion]
        if self.mirando_izquierda:
            imagen_actual = pygame.transform.flip(imagen_actual, True, False)
        ventana.blit(imagen_actual, (self.x, self.y))
        self.dibujar_barras(ventana)
        self.dibujar_rayos(ventana)

    def dibujar_barras(self, ventana):
        """Dibuja las barras de salud y energía en la pantalla."""
        # Barra de salud (azul)
        barra_salud_ancho = 200
        barra_salud_alto = 20
        salud_porcentaje = self.salud_actual / self.salud_max
        pygame.draw.rect(ventana, (0, 0, 255), (10, 10, barra_salud_ancho * salud_porcentaje, barra_salud_alto))
        pygame.draw.rect(ventana, (255, 255, 255), (10, 10, barra_salud_ancho, barra_salud_alto), 2)

        # Barra de energía (roja)
        barra_energia_ancho = 200
        barra_energia_alto = 20
        energia_porcentaje = self.energia_actual / self.energia_max
        pygame.draw.rect(ventana, (255, 0, 0), (10, 40, barra_energia_ancho * energia_porcentaje, barra_energia_alto))
        pygame.draw.rect(ventana, (255, 255, 255), (10, 40, barra_energia_ancho, barra_energia_alto), 2)

    def dibujar_rayos(self, ventana):
        """Dibuja los rayos en la pantalla."""
        for rayo in self.rayos:
            pygame.draw.line(ventana, (255, 255, 0), rayo["inicio"], rayo["fin"], 5)

    def mover(self, teclas, suelo):
        """Mueve el personaje basado en las teclas presionadas y actualiza la animación."""
        movimiento = False

        if teclas[pygame.K_w]:
            self.y -= self.velocidad
            movimiento = True
        if teclas[pygame.K_s]:
            self.y += self.velocidad
            movimiento = True
        if teclas[pygame.K_a]:
            self.x -= self.velocidad
            movimiento = True
        if teclas[pygame.K_d]:
            self.x += self.velocidad
            movimiento = True

        # Espejar personaje con un solo toque de la tecla F
        if teclas[pygame.K_f]:
            if not self.tecla_f_presionada:
                self.mirando_izquierda = not self.mirando_izquierda
                self.tecla_f_presionada = True
        else:
            self.tecla_f_presionada = False

        # Lanzar rayo con la tecla SPACE si hay energía suficiente
        if teclas[pygame.K_SPACE] and self.energia_actual >= self.costo_rayo:
            self.lanzar_rayo()

        # Salto con tecla Enter
        if teclas[pygame.K_RETURN] and self.en_suelo:
            self.velocidad_y = self.velocidad_salto
            self.en_suelo = False

        # Aplicar gravedad
        self.velocidad_y += self.gravedad
        self.y += self.velocidad_y

        # Limitar movimiento con el suelo
        suelo.limitar_movimiento(self)

        # Recuperar energía cada ciertos pasos
        if movimiento:
            self.pasos_actuales += 1
            if self.pasos_actuales >= self.pasos_para_recuperar:
                self.pasos_actuales = 0
                self.energia_actual = min(self.energia_actual + 10, self.energia_max)

        # Actualizar rayos en movimiento
        self.actualizar_rayos()

        # Actualizar animación si hay movimiento
        if movimiento:
            self.tiempo_animacion += 1
            if self.tiempo_animacion >= 5:  # Cambiar frame cada 5 ticks
                self.tiempo_animacion = 0
                self.indice_animacion = (self.indice_animacion + 1) % len(self.animacion)

    def lanzar_rayo(self):
        """Lanza un rayo y reduce la energía."""
        inicio = (self.x + self.width // 2, self.y + self.height // 2)
        if self.mirando_izquierda:
            direccion = -1
        else:
            direccion = 1
        fin = (self.x + self.width // 2 + 50 * direccion, self.y + self.height // 2)
        self.rayos.append({"inicio": list(inicio), "fin": list(fin), "direccion": direccion})
        self.energia_actual -= self.costo_rayo

    def actualizar_rayos(self):
        """Actualiza la posición de los rayos en movimiento y elimina los que salen de la pantalla."""
        for rayo in self.rayos[:]:  # Iterar sobre una copia para poder modificar la lista
            rayo["inicio"][0] += self.velocidad_rayo * rayo["direccion"]
            rayo["fin"][0] += self.velocidad_rayo * rayo["direccion"]

            # Eliminar rayos que salgan de la pantalla
            if rayo["fin"][0] < 0 or rayo["inicio"][0] > 800:  # Asumiendo un ancho de pantalla de 800
                self.rayos.remove(rayo)











