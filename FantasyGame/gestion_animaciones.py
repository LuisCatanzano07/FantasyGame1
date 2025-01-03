import pygame
from constantes import CONFIGURACION

def actualizar_animacion(personaje, delta_time):
    """
    Actualiza la animación del personaje si está en movimiento.

    Args:
        personaje: Instancia del personaje cuyas animaciones se están actualizando.
        delta_time: Tiempo transcurrido desde la última actualización.
    """
    duracion_frame = CONFIGURACION["animacion"]["duracion_frame"]

    # Verificar si hay teclas de movimiento presionadas
    if any([pygame.key.get_pressed()[k] for k in [pygame.K_a, pygame.K_d]]):
        personaje.tiempo_animacion += delta_time

    # Cambiar el índice de animación si ha pasado suficiente tiempo
    if personaje.tiempo_animacion >= duracion_frame:
        personaje.tiempo_animacion = 0
        personaje.indice_animacion = (personaje.indice_animacion + 1) % len(personaje.animacion)



