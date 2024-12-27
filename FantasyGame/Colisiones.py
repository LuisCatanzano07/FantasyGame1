import pygame

def verificar_colision(sprite1, sprite2):
    """
    Verifica si dos sprites colisionan.
    :param sprite1: El primer sprite (pygame.sprite.Sprite)
    :param sprite2: El segundo sprite (pygame.sprite.Sprite)
    :return: True si hay colisión, False en caso contrario.
    """
    return sprite1.rect.colliderect(sprite2.rect)

def verificar_colisiones_grupo(sprite, grupo):
    """
    Verifica si un sprite colisiona con alguno en un grupo.
    :param sprite: El sprite a verificar (pygame.sprite.Sprite)
    :param grupo: Grupo de sprites (pygame.sprite.Group)
    :return: Lista de sprites con los que colisiona.
    """
    return pygame.sprite.spritecollide(sprite, grupo, False)

def manejar_colision_jugador_enemigo(jugador, enemigos):
    """
    Maneja la colisión entre el jugador y los enemigos.
    :param jugador: El sprite del jugador.
    :param enemigos: Grupo de enemigos (pygame.sprite.Group).
    :return: True si colisionó con algún enemigo, False en caso contrario.
    """
    colisiones = verificar_colisiones_grupo(jugador, enemigos)
    if colisiones:
        print("¡Colisión detectada! Perdiste una vida o reinicia el nivel.")
        return True
    return False
