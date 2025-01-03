import pygame
from constantes import CONFIGURACION

def manejar_ataques(personaje, teclas):
    """
    Gestiona los ataques del personaje, como lanzar rayos.

    Args:
        personaje: Instancia del personaje que realiza los ataques.
        teclas: Objeto de teclas presionadas de Pygame.
    """
    if teclas[pygame.K_SPACE] and personaje.energia_actual >= CONFIGURACION["rayo"]["costo_energia"]:
        lanzar_rayo(personaje)

def lanzar_rayo(personaje):
    """
    Lanza un rayo y reduce la energía del personaje.

    Args:
        personaje: Instancia del personaje que lanza el rayo.
    """
    inicio = (personaje.x + personaje.width // 2, personaje.y + personaje.height // 2)
    direccion = -1 if personaje.mirando_izquierda else 1
    personaje.gestion_rayos.lanzar_rayo(inicio, direccion)
    personaje.energia_actual -= CONFIGURACION["rayo"]["costo_energia"]
