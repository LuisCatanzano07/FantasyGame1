import pygame
import os
from constantes import CONFIGURACION

def cargar_sprites(ancho: int, alto: int):
    """
    Carga los sprites desde la ruta especificada en la configuración.

    Args:
        ancho (int): El ancho al que se escalarán las imágenes.
        alto (int): El alto al que se escalarán las imágenes.

    Returns:
        list[pygame.Surface]: Lista de superficies de Pygame con los sprites cargados.
    """
    sprites = []
    config_sprites = CONFIGURACION["sprites"]
    ruta_sprites = config_sprites["ruta"]
    cantidad_frames = config_sprites["cantidad_frames"]

    try:
        for i in range(cantidad_frames):
            ruta_imagen = ruta_sprites.format(i)
            if not os.path.exists(ruta_imagen):
                raise FileNotFoundError(f"No se encontró el archivo de sprite: {ruta_imagen}")
            imagen = pygame.image.load(ruta_imagen)
            sprites.append(pygame.transform.scale(imagen, (ancho, alto)))
    except FileNotFoundError as e:
        print(f"Error al cargar sprites: {e}")
    except pygame.error as e:
        print(f"Error al procesar una imagen de sprite: {e}")

    return sprites
