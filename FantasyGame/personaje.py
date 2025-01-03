import pygame
import os
from typing import List, Tuple

# Configuración global
CONFIGURACION = {
    "colores": {
        "barra_salud": (0, 0, 255),
        "barra_energia": (255, 0, 0),
        "borde_barra": (255, 255, 255),
        "rayo": (255, 255, 0)
    },
    "dimensiones_barras": {
        "ancho": 200,
        "alto_salud": 20,
        "alto_energia": 20
    },
    "animacion": {
        "duracion_frame": 100
    },
    "sprites": {
        "cantidad_frames": 7,
        "nombres_personalizados": None  # Lista de nombres personalizados o None para usar el formato predeterminado
    }
}

class Rayo:
    def __init__(self, inicio: Tuple[int, int], direccion: int, velocidad: int):
        self.inicio = list(inicio)
        self.fin = [inicio[0] + 50 * direccion, inicio[1]]
        self.direccion = direccion
        self.velocidad = velocidad

    def actualizar(self):
        """Actualiza la posición del rayo."""
        self.inicio[0] += self.velocidad * self.direccion
        self.fin[0] += self.velocidad * self.direccion

    def fuera_de_pantalla(self, ancho_pantalla: int) -> bool:
        """Verifica si el rayo está fuera de la pantalla."""
        return self.fin[0] < 0 or self.inicio[0] > ancho_pantalla

class Personaje:
    def __init__(self, x: int, y: int, width: int, height: int, ruta_sprites: str, dimensiones_pantalla: Tuple[int, int]):
        """Inicializa un personaje con posición, tamaño y animaciones."""
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocidad = 5
        self.animacion: List[pygame.Surface] = []
        self.cargar_sprites(ruta_sprites)
        self.indice_animacion = 0
        self.tiempo_animacion = 0
        self.en_suelo = False
        self.saltos_restantes = 2
        self.velocidad_salto = -15
        self.gravedad = 1
        self.velocidad_y = 0
        self.mirando_izquierda = False
        self.tecla_f_presionada = False
        self.tecla_salto_presionada = False

        # Dimensiones de la pantalla
        self.ancho_pantalla, self.alto_pantalla = dimensiones_pantalla

        # Atributos de salud y energía
        self.salud_max = 100
        self.energia_max = 100
        self.salud_actual = 100
        self.energia_actual = 100
        self.tiempo_ultimo_recarga = 0

        # Rayos
        self.rayos: List[Rayo] = []
        self.costo_rayo = 20
        self.velocidad_rayo = 10

    def cargar_sprites(self, ruta_sprites: str):
        """Carga las imágenes de la animación desde la ruta especificada."""
        config_sprites = CONFIGURACION["sprites"]
        nombres_personalizados = config_sprites["nombres_personalizados"]
        cantidad_frames = config_sprites["cantidad_frames"]

        if not os.path.exists(ruta_sprites):
            print(f"Error: La ruta de los sprites '{ruta_sprites}' no existe.")
            return

        try:
            if nombres_personalizados:
                for nombre in nombres_personalizados:
                    imagen = pygame.image.load(os.path.join(ruta_sprites, nombre))
                    self.animacion.append(pygame.transform.scale(imagen, (self.width, self.height)))
            else:
                for i in range(cantidad_frames):
                    imagen = pygame.image.load(os.path.join(ruta_sprites, f"Player_{i}.png"))
                    self.animacion.append(pygame.transform.scale(imagen, (self.width, self.height)))
        except FileNotFoundError as e:
            print(f"Error al cargar sprites: {e}")
        except pygame.error as e:
            print(f"Error al procesar una imagen de sprite: {e}")

    def dibujar(self, ventana: pygame.Surface):
        """Dibuja el personaje animado en la ventana proporcionada."""
        if not self.animacion:
            print("Advertencia: No hay sprites cargados para dibujar el personaje.")
            return

        imagen_actual = self.animacion[self.indice_animacion]
        if self.mirando_izquierda:
            imagen_actual = pygame.transform.flip(imagen_actual, True, False)
        ventana.blit(imagen_actual, (self.x, self.y))
        self.dibujar_barras(ventana)
        self.dibujar_rayos(ventana)

    def dibujar_barras(self, ventana: pygame.Surface):
        """Dibuja las barras de salud y energía en la pantalla."""
        config_barras = CONFIGURACION["dimensiones_barras"]
        colores = CONFIGURACION["colores"]

        barra_salud_ancho = config_barras["ancho"]
        barra_salud_alto = config_barras["alto_salud"]
        salud_porcentaje = self.salud_actual / self.salud_max
        pygame.draw.rect(ventana, colores["barra_salud"], (10, 10, barra_salud_ancho * salud_porcentaje, barra_salud_alto))
        pygame.draw.rect(ventana, colores["borde_barra"], (10, 10, barra_salud_ancho, barra_salud_alto), 2)

        barra_energia_ancho = config_barras["ancho"]
        barra_energia_alto = config_barras["alto_energia"]
        energia_porcentaje = self.energia_actual / self.energia_max
        pygame.draw.rect(ventana, colores["barra_energia"], (10, 40, barra_energia_ancho * energia_porcentaje, barra_energia_alto))
        pygame.draw.rect(ventana, colores["borde_barra"], (10, 40, barra_energia_ancho, barra_energia_alto), 2)

    def dibujar_rayos(self, ventana: pygame.Surface):
        """Dibuja los rayos en la pantalla."""
        color_rayo = CONFIGURACION["colores"]["rayo"]
        for rayo in self.rayos:
            pygame.draw.line(ventana, color_rayo, rayo.inicio, rayo.fin, 5)

    def mover(self, teclas: pygame.key.ScancodeWrapper, suelo, delta_time):
        """Controla el movimiento del personaje, la gravedad y las animaciones."""
        self.manejar_movimiento(teclas)
        self.manejar_salto(teclas)
        self.manejar_gravedad(suelo)
        self.manejar_recuperacion_energia(delta_time)
        self.actualizar_animacion(delta_time)
        self.manejar_ataques(teclas)

    def manejar_movimiento(self, teclas: pygame.key.ScancodeWrapper):
        """Mueve el personaje horizontalmente y actualiza su orientación."""
        if teclas[pygame.K_a]:
            self.x -= self.velocidad
        if teclas[pygame.K_d]:
            self.x += self.velocidad

        if teclas[pygame.K_f] and not self.tecla_f_presionada:
            self.mirando_izquierda = not self.mirando_izquierda
            self.tecla_f_presionada = True
        elif not teclas[pygame.K_f]:
            self.tecla_f_presionada = False

    def manejar_salto(self, teclas: pygame.key.ScancodeWrapper):
        """Controla los saltos del personaje."""
        if teclas[pygame.K_w]:
            if not self.tecla_salto_presionada and self.saltos_restantes > 0:
                self.velocidad_y = self.velocidad_salto
                self.saltos_restantes -= 1
                self.en_suelo = False
            self.tecla_salto_presionada = True
        else:
            self.tecla_salto_presionada = False

    def manejar_gravedad(self, suelo):
        """Aplica la gravedad al personaje y verifica si está en el suelo."""
        self.velocidad_y += self.gravedad
        self.y += self.velocidad_y
        suelo.limitar_movimiento(self)
        if self.en_suelo:
            self.saltos_restantes = 2

    def manejar_recuperacion_energia(self, delta_time):
        """Recupera la energía del personaje con el tiempo."""
        tiempo_actual = pygame.time.get_ticks()
        if tiempo_actual - self.tiempo_ultimo_recarga > 100:
            self.energia_actual = min(self.energia_actual + 1, self.energia_max)
            self.tiempo_ultimo_recarga = tiempo_actual

    def manejar_ataques(self, teclas: pygame.key.ScancodeWrapper):
        """Lanza un rayo si se presiona la tecla SPACE y hay suficiente energía."""
        if teclas[pygame.K_SPACE] and self.energia_actual >= self.costo_rayo:
            self.lanzar_rayo()

    def actualizar_animacion(self, delta_time):
        """Actualiza la animación del personaje si está en movimiento."""
        duracion_frame = CONFIGURACION["animacion"]["duracion_frame"]

        if any([pygame.key.get_pressed()[k] for k in [pygame.K_a, pygame.K_d]]):
            self.tiempo_animacion += delta_time

        if self.tiempo_animacion >= duracion_frame:
            self.tiempo_animacion = 0
            self.indice_animacion = (self.indice_animacion + 1) % len(self.animacion)
        else:
            self.indice_animacion = 0

    def lanzar_rayo(self):
        """Lanza un rayo y reduce la energía."""
        inicio = (self.x + self.width // 2, self.y + self.height // 2)
        direccion = -1 if self.mirando_izquierda else 1
        self.rayos.append(Rayo(inicio, direccion, self.velocidad_rayo))
        self.energia_actual -= self.costo_rayo

    def actualizar_rayos(self):
        """Actualiza la posición de los rayos en movimiento y elimina los que salen de la pantalla."""
        self.rayos = [
            rayo for rayo in self.rayos
            if not rayo.fuera_de_pantalla(self.ancho_pantalla) and not rayo.actualizar()
        ]

    def recuperar_energia(self, delta_time):
        """Recupera energía con el tiempo."""
        tiempo_actual = pygame.time.get_ticks()
        if tiempo_actual - self.tiempo_ultimo_recarga > 100:
            self.energia_actual = min(self.energia_actual + 1, self.energia_max)
            self.tiempo_ultimo_recarga = tiempo_actual

























