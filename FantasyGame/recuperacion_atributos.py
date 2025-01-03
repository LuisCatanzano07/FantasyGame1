import pygame
from constantes import CONFIGURACION

def manejar_recuperacion_energia(personaje, delta_time):
    """
    Recupera la energía del personaje con el tiempo.

    Args:
        personaje: Instancia del personaje cuyas propiedades dinámicas se están recuperando.
        delta_time: Tiempo transcurrido desde la última actualización.
    """
    tiempo_actual = pygame.time.get_ticks()
    intervalo_recarga = CONFIGURACION["personaje"]["recuperacion_energia_intervalo"]
    cantidad_recarga = CONFIGURACION["personaje"]["recuperacion_energia_cantidad"]

    if tiempo_actual - personaje.tiempo_ultimo_recarga > intervalo_recarga:
        personaje.energia_actual = min(personaje.energia_actual + cantidad_recarga, personaje.energia_max)
        personaje.tiempo_ultimo_recarga = tiempo_actual
