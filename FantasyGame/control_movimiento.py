import pygame
def manejar_movimiento(personaje, teclas):
    """
    Mueve el personaje horizontalmente y actualiza su orientación.

    Args:
        personaje: Instancia del personaje que se está moviendo.
        teclas: Objeto de teclas presionadas de Pygame.
    """
    if teclas[pygame.K_a]:
        personaje.x -= personaje.velocidad
    if teclas[pygame.K_d]:
        personaje.x += personaje.velocidad

    if teclas[pygame.K_f] and not personaje.tecla_f_presionada:
        personaje.mirando_izquierda = not personaje.mirando_izquierda
        personaje.tecla_f_presionada = True
    elif not teclas[pygame.K_f]:
        personaje.tecla_f_presionada = False
