import pygame
from typing import List, Tuple
from constantes import CONFIGURACION
from rayo import Rayo

class GestionRayos:
    def __init__(self, ancho_pantalla: int):
        """
        Inicializa la gestión de rayos.
        
        Args:
            ancho_pantalla (int): El ancho de la pantalla para verificar si los rayos están fuera.
        """
        self.rayos: List[Rayo] = []
        self.ancho_pantalla = ancho_pantalla

    def lanzar_rayo(self, inicio: Tuple[int, int], direccion: int):
        """
        Lanza un nuevo rayo.

        Args:
            inicio (Tuple[int, int]): Coordenadas iniciales del rayo.
            direccion (int): Dirección del rayo (-1 para izquierda, 1 para derecha).
        """
        self.rayos.append(Rayo(inicio, direccion))

    def actualizar_rayos(self):
        """
        Actualiza la posición de los rayos en movimiento y elimina los que salen de la pantalla.
        """
        for rayo in self.rayos:
            rayo.actualizar()

        # Filtrar rayos fuera de pantalla
        self.rayos = [rayo for rayo in self.rayos if not rayo.fuera_de_pantalla(self.ancho_pantalla)]

    def dibujar_rayos(self, ventana: pygame.Surface):
        """
        Dibuja todos los rayos en la ventana.

        Args:
            ventana (pygame.Surface): La ventana de Pygame donde se dibujarán los rayos.
        """
        color_rayo = CONFIGURACION["colores"]["rayo"]
        for rayo in self.rayos:
            pygame.draw.line(ventana, color_rayo, tuple(rayo.inicio), tuple(rayo.fin), 5)


