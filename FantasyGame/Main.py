import pygame
from personaje import Personaje
from enemigo import Enemigo
from ambiente import Suelo
from combate import Combate

# Inicialización de Pygame
pygame.init()

# Configuración de la ventana
ANCHO, ALTO = 800, 600
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Juego: Combate entre Personaje y Enemigo")

# Colores
BLANCO = (255, 255, 255)
COLOR_SUELO = (50, 200, 50)

# Ruta de sprites
RUTA_PERSONAJE = "C:\\Users\\Yessenia\\OneDrive\\Escritorio\\FantasyGame\\assets\\sprites\\jugador"
RUTA_ENEMIGO = "C:\\Users\\Yessenia\\OneDrive\\Escritorio\\FantasyGame\\assets\\sprites\\enemigos"

# Crear instancias
suelo = Suelo(y=500, color=COLOR_SUELO, altura=100)
personaje = Personaje(x=50, y=suelo.y - 50, width=50, height=50, ruta_sprites=RUTA_PERSONAJE)
enemigo = Enemigo(x=700, y=suelo.y - 50, width=50, height=50, ruta_sprites=RUTA_ENEMIGO)
combate = Combate(personaje, enemigo)

# Posiciones iniciales
POSICION_INICIAL_PERSONAJE = (50, suelo.y - 50)
POSICION_INICIAL_ENEMIGO = (700, suelo.y - 50)

# Loop principal del juego
corriendo = True
reloj = pygame.time.Clock()

while corriendo:
    reloj.tick(30)  # 30 FPS
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    # Capturar teclas presionadas
    teclas = pygame.key.get_pressed()

    # Actualizar estados
    personaje.mover(teclas, suelo)
    enemigo.mover(personaje, suelo)
    combate.detectar_colisiones()
    combate.regenerar_salud(POSICION_INICIAL_PERSONAJE, POSICION_INICIAL_ENEMIGO)

    # Dibujar todo
    ventana.fill(BLANCO)  # Limpiar la pantalla
    suelo.dibujar(ventana, ANCHO)  # Dibujar el suelo
    personaje.dibujar(ventana)
    enemigo.dibujar(ventana)
    pygame.display.flip()  # Actualizar la pantalla

pygame.quit()












