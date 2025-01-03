import pygame
from typing import List, Tuple
from constantes import CONFIGURACION
from carga_sprites import cargar_sprites
from dibujo_barras import dibujar_barras
from control_movimiento import manejar_movimiento
from gestion_animaciones import actualizar_animacion
from recuperacion_atributos import manejar_recuperacion_energia
from gestion_salto import manejar_salto
from gestion_gravedad import manejar_gravedad
from gestion_ataques import manejar_ataques
from gestion_rayos import GestionRayos

class Personaje:
    def __init__(self, x: int, y: int, width: int, height: int, dimensiones_pantalla: Tuple[int, int]):
        """Inicializa un personaje con posición, tamaño y animaciones."""
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocidad = CONFIGURACION["personaje"]["velocidad"]
        self.animacion: List[pygame.Surface] = cargar_sprites(width, height)
        self.indice_animacion = 0
        self.tiempo_animacion = 0
        self.en_suelo = False
        self.saltos_restantes = CONFIGURACION["personaje"]["saltos_maximos"]
        self.velocidad_salto = CONFIGURACION["personaje"]["velocidad_salto"]
        self.gravedad = CONFIGURACION["personaje"]["gravedad"]
        self.velocidad_y = 0
        self.mirando_izquierda = False
        self.tecla_f_presionada = False
        self.tecla_salto_presionada = False

        # Dimensiones de la pantalla
        self.ancho_pantalla, self.alto_pantalla = dimensiones_pantalla

        # Atributos de salud y energía
        self.salud_max = CONFIGURACION["personaje"]["salud_max"]
        self.energia_max = CONFIGURACION["personaje"]["energia_max"]
        self.salud_actual = self.salud_max
        self.energia_actual = self.energia_max
        self.tiempo_ultimo_recarga = 0

        # Gestión de rayos
        self.gestion_rayos = GestionRayos(self.ancho_pantalla)

    def lanzar_rayo(self):
        """Lanza un rayo y reduce la energía."""
        inicio = (self.x + self.width // 2, self.y + self.height // 2)
        direccion = -1 if self.mirando_izquierda else 1
        self.gestion_rayos.lanzar_rayo(inicio, direccion)
        self.energia_actual -= CONFIGURACION["rayo"]["costo_energia"]

    def dibujar(self, ventana: pygame.Surface):
        """Dibuja al personaje en la ventana."""
        if self.animacion:
            imagen_actual = self.animacion[self.indice_animacion]
            if self.mirando_izquierda:
                imagen_actual = pygame.transform.flip(imagen_actual, True, False)
            ventana.blit(imagen_actual, (self.x, self.y))

        dibujar_barras(ventana, self.salud_actual, self.salud_max, self.energia_actual, self.energia_max)
        self.gestion_rayos.dibujar_rayos(ventana)

    def mover(self, teclas: pygame.key.ScancodeWrapper, suelo, delta_time):
        """Controla el movimiento del personaje, la gravedad y las animaciones."""
        manejar_movimiento(self, teclas)
        manejar_salto(self, teclas)
        manejar_gravedad(self, suelo)
        manejar_recuperacion_energia(self, delta_time)
        actualizar_animacion(self, delta_time)
        manejar_ataques(self, teclas)

    def actualizar_rayos(self):
        """Actualiza los rayos usando la gestión de rayos."""
        self.gestion_rayos.actualizar_rayos()







    
    
        

       


























