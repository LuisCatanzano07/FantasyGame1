import pygame
from constantes import CONFIGURACION

def dibujar_barras(ventana: pygame.Surface, salud_actual: int, salud_max: int, energia_actual: int, energia_max: int):
    """
    Dibuja las barras de salud y energía en la pantalla.

    Args:
        ventana (pygame.Surface): Superficie donde se dibujarán las barras.
        salud_actual (int): Valor actual de salud del personaje.
        salud_max (int): Valor máximo de salud del personaje.
        energia_actual (int): Valor actual de energía del personaje.
        energia_max (int): Valor máximo de energía del personaje.
    """
    config_barras = CONFIGURACION["dimensiones_barras"]
    colores = CONFIGURACION["colores"]

    # Barra de salud
    barra_salud_ancho = config_barras["ancho"]
    barra_salud_alto = config_barras["alto_salud"]
    salud_porcentaje = salud_actual / salud_max
    pygame.draw.rect(ventana, colores["barra_salud"], (10, 10, barra_salud_ancho * salud_porcentaje, barra_salud_alto))
    pygame.draw.rect(ventana, colores["borde_barra"], (10, 10, barra_salud_ancho, barra_salud_alto), 2)

    # Barra de energía
    barra_energia_ancho = config_barras["ancho"]
    barra_energia_alto = config_barras["alto_energia"]
    energia_porcentaje = energia_actual / energia_max
    pygame.draw.rect(ventana, colores["barra_energia"], (10, 40, barra_energia_ancho * energia_porcentaje, barra_energia_alto))
    pygame.draw.rect(ventana, colores["borde_barra"], (10, 40, barra_energia_ancho, barra_energia_alto), 2)
