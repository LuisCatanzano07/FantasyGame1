import pygame
from personaje import Personaje
from enemigo_manager import GestorEnemigos
from ambiente import Suelo
from combate import Combate

# Inicialización de Pygame
pygame.init()

# Configuración de la ventana
ANCHO, ALTO = 800, 600
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Fantasy Game")

# Colores
BLANCO = (255, 255, 255)
COLOR_SUELO = (50, 200, 50)

# Ruta de sprites
RUTA_PERSONAJE = "C:\\Users\\Yessenia\\OneDrive\\Escritorio\\FantasyGame\\assets\\sprites\\jugador"
RUTA_ENEMIGOS = "C:\\Users\\Yessenia\\OneDrive\\Escritorio\\FantasyGame\\assets\\sprites\\enemigos"

# Crear instancias
suelo = Suelo(y=500, color=COLOR_SUELO, altura=100)
personaje = Personaje(x=50, y=suelo.y - 50, width=50, height=50, ruta_sprites=RUTA_PERSONAJE)
gestor_enemigos = GestorEnemigos(ruta_sprites=RUTA_ENEMIGOS, suelo=suelo)

# Instanciar combate (actualiza dinámicamente la lista de enemigos)
combate = Combate(personaje, gestor_enemigos.enemigos)

# Loop principal del juego
corriendo = True
reloj = pygame.time.Clock()

while corriendo:
    tiempo_actual = pygame.time.get_ticks()
    reloj.tick(30)  # Limitar a 30 FPS

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    # Capturar teclas presionadas
    teclas = pygame.key.get_pressed()

    # Actualizar estados
    personaje.mover(teclas, suelo)
    gestor_enemigos.generar_enemigos(tiempo_actual)

    # Actualizar lista de enemigos en combate
    combate.enemigos = gestor_enemigos.enemigos + gestor_enemigos.enemigos_nivel

    # Detectar colisiones
    combate.detectar_colisiones()

    # Dibujar todo
    ventana.fill(BLANCO)  # Limpiar la pantalla
    suelo.dibujar(ventana, ANCHO)  # Dibujar el suelo
    personaje.dibujar(ventana)
    gestor_enemigos.actualizar_enemigos(personaje, ventana)

    pygame.display.flip()  # Actualizar la pantalla

pygame.quit()














