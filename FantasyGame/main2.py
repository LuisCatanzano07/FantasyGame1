import pygame
from personaje import Personaje
from ambiente import Suelo
from enemigo import Enemigo

# Configuración inicial de Pygame
pygame.init()

# Dimensiones de la ventana
DIMENSIONES_PANTALLA = (800, 600)
VENTANA = pygame.display.set_mode(DIMENSIONES_PANTALLA)
pygame.display.set_caption("Prueba de Personaje y Enemigos")

# Colores
COLOR_FONDO = (50, 50, 50)

# Rutas de recursos
RUTA_SPRITES_PERSONAJE = "assets/sprites/jugador"  # Cambia esta ruta por la ubicación real de tus sprites
RUTA_SPRITES_ENEMIGO = "assets/sprites/enemigo"  # Cambia esta ruta por la ubicación real de los sprites del enemigo

# Crear una instancia de Suelo
suelo = Suelo(
    y=500,  # Altura desde la parte superior de la pantalla
    color=(100, 200, 100),  # Color inicial del suelo
    altura=20,  # Grosor del suelo
    velocidad=0,  # El suelo está estático por ahora
    color_cambio=(200, 100, 100)  # Color alternativo
)

# Crear una instancia de Personaje
personaje = Personaje(100, 400, 64, 64, RUTA_SPRITES_PERSONAJE, DIMENSIONES_PANTALLA)

# Crear instancias de enemigos
enemigos = [
    Enemigo(300, 400, 64, 64, RUTA_SPRITES_ENEMIGO),
    Enemigo(500, 400, 64, 64, RUTA_SPRITES_ENEMIGO, velocidad=2)
]

# Variables del juego
reloj = pygame.time.Clock()
ejecutando = True

# Manejo de eventos
def manejar_eventos():
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            return False
    return True

# Bucle principal del juego
while ejecutando:
    # Manejar eventos
    ejecutando = manejar_eventos()

    # Obtener teclas presionadas
    teclas = pygame.key.get_pressed()

    # Limpiar pantalla
    VENTANA.fill(COLOR_FONDO)

    # Actualizar lógica del suelo
    delta_time = reloj.tick(60)
    tiempo_actual = pygame.time.get_ticks()
    suelo.mover()
    suelo.alternar_color(tiempo_actual, 1000)

    # Actualizar personaje
    personaje.mover(teclas, suelo, delta_time)
    personaje.actualizar_rayos()
    suelo.limitar_movimiento(personaje)

    # Actualizar enemigos
    for enemigo in enemigos:
        enemigo.mover(personaje, suelo)
        suelo.limitar_movimiento(enemigo)
        enemigo.actualizar_animacion()

    # Dibujar suelo, personaje y enemigos
    suelo.dibujar(VENTANA, DIMENSIONES_PANTALLA[0])
    personaje.dibujar(VENTANA)
    for enemigo in enemigos:
        enemigo.dibujar(VENTANA)
        enemigo.dibujar_barra_salud(VENTANA)

    # Actualizar ventana
    pygame.display.flip()

# Salir de Pygame
pygame.quit()


