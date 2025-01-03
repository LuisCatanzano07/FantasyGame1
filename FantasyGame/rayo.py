from typing import Tuple
from constantes import CONFIGURACION

class Rayo:
    def __init__(self, inicio: Tuple[int, int], direccion: int):
        """
        Inicializa un rayo con su posición inicial, dirección y velocidad.
        
        Args:
            inicio (Tuple[int, int]): Coordenadas iniciales del rayo (x, y).
            direccion (int): Dirección del rayo (1 para derecha, -1 para izquierda).
        """
        self.inicio = list(inicio)
        self.fin = [
            inicio[0] + CONFIGURACION["rayo"]["largo"] * direccion,
            inicio[1],
        ]
        self.direccion = direccion
        self.velocidad = CONFIGURACION["rayo"]["velocidad"]

    def actualizar(self):
        """
        Actualiza la posición del rayo en función de su velocidad y dirección.
        """
        desplazamiento = self.velocidad * self.direccion
        self.inicio[0] += desplazamiento
        self.fin[0] += desplazamiento

    def fuera_de_pantalla(self, ancho_pantalla: int) -> bool:
        """
        Verifica si el rayo está fuera de los límites de la pantalla.
        
        Args:
            ancho_pantalla (int): El ancho de la pantalla.
        
        Returns:
            bool: True si el rayo está fuera de la pantalla, False en caso contrario.
        """
        return self.fin[0] < 0 or self.inicio[0] > ancho_pantalla

