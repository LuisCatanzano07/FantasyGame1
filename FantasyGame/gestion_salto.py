import pygame
def manejar_salto(personaje, teclas):
    """
    Controla los saltos del personaje.

    Args:
        personaje: Instancia del personaje que está realizando el salto.
        teclas: Objeto de teclas presionadas de Pygame.
    """
    if teclas[pygame.K_w]:
        if not personaje.tecla_salto_presionada and personaje.saltos_restantes > 0:
            personaje.velocidad_y = personaje.velocidad_salto
            personaje.saltos_restantes -= 1
            personaje.en_suelo = False
        personaje.tecla_salto_presionada = True
    else:
        personaje.tecla_salto_presionada = False

