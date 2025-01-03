import pygame
from personaje import Personaje
from ventana import crear_ventana
from suelo import Suelo
from constantes_ventana import DIMENSIONES_PANTALLA, TITULO_VENTANA, COLOR_FONDO

# Crear ventana
ventana = crear_ventana(DIMENSIONES_PANTALLA[0], DIMENSIONES_PANTALLA[1], TITULO_VENTANA)

# Crear personaje
personaje = Personaje(100, 300, 50, 100, DIMENSIONES_PANTALLA)

# Crear suelo
suelo = Suelo(DIMENSIONES_PANTALLA[0], DIMENSIONES_PANTALLA[1], altura_suelo=30, color=(150, 75, 0))

# Loop principal
reloj = pygame.time.Clock()
ejecutando = True

while ejecutando:
    delta_time = reloj.tick(60)  # Tiempo entre frames
    ventana.fill(COLOR_FONDO)  # Limpiar la pantalla

    # Manejo de eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    # Obtener teclas presionadas
    teclas = pygame.key.get_pressed()

    # Actualizar personaje
    personaje.mover(teclas, suelo, delta_time)

    # Actualizar rayos
    personaje.actualizar_rayos()

    # Dibujar suelo
    suelo.dibujar(ventana)

    # Dibujar personaje
    personaje.dibujar(ventana)

    # Dibujar rayos
    personaje.gestion_rayos.dibujar_rayos(ventana)

    # Actualizar pantalla
    pygame.display.flip()

pygame.quit()









