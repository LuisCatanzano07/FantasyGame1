import pygame

def crear_ventana(ancho, alto, titulo="Mi Juego"):
    """
    Crea y configura una ventana de Pygame.

    Args:
        ancho (int): El ancho de la ventana.
        alto (int): La altura de la ventana.
        titulo (str): El título de la ventana.

    Returns:
        surface: La superficie principal de la ventana.
    """
    pygame.init()
    ventana = pygame.display.set_mode((ancho, alto))
    pygame.display.set_caption(titulo)
    return ventana
