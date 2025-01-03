import pygame
from personaje import Personaje
from enemigo_manager import GestorEnemigos
from suelo import Suelo
from gestor_niveles import GestorNiveles
from eventos import Evento
from combate import Combate
from configuracion import ConfiguracionControles

# Inicialización de Pygame
pygame.init()

# Configuración de la ventana
ANCHO, ALTO = 800, 600
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Fantasy Game")

# Colores
BLANCO = (255, 255, 255)

# Ruta de sprites
RUTA_PERSONAJE = "C:\\Users\\Yessenia\\OneDrive\\Escritorio\\FantasyGame\\assets\\sprites\\jugador"
RUTA_ENEMIGOS = "C:\\Users\\Yessenia\\OneDrive\\Escritorio\\FantasyGame\\assets\\sprites\\enemigos"

# Crear instancias
dimensiones_pantalla = (ANCHO, ALTO)
suelo = Suelo(y=500, color=(50, 200, 50), altura=100)
personaje = Personaje(x=50, y=suelo.y - 50, width=50, height=50, ruta_sprites=RUTA_PERSONAJE, dimensiones_pantalla=dimensiones_pantalla)
gestor_enemigos = GestorEnemigos(ruta_sprites=RUTA_ENEMIGOS, suelo=suelo)
gestor_niveles = GestorNiveles(gestor_enemigos=gestor_enemigos, personaje=personaje)
combate = Combate(personaje=personaje, enemigos=gestor_enemigos.enemigos)
configuracion = ConfiguracionControles("controles.json")

# Crear eventos
evento_extra_enemigos = Evento(tipo="enemigos_extra", tiempo_activacion=30000, accion=lambda: gestor_enemigos.agregar_enemigo(), objetivo_nivel=10)

eventos = [evento_extra_enemigos]

# Función para mostrar el menú de configuración de controles
def mostrar_menu_controles():
    configuracion.mostrar_menu(ventana)

# Loop principal del juego
corriendo = True
reloj = pygame.time.Clock()

while corriendo:
    # Calcular delta_time
    delta_time = reloj.tick(30)  # Limitar a 30 FPS y obtener el tiempo entre frames en milisegundos
    tiempo_actual = pygame.time.get_ticks()

    # Manejo de eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False
        elif evento.type == pygame.KEYDOWN and evento.key == configuracion.obtener_tecla("abrir_menu"):
            mostrar_menu_controles()

    # Capturar teclas presionadas
    teclas = pygame.key.get_pressed()

    # Actualizar personaje
    personaje.mover(teclas, suelo, delta_time)

    # Actualizar nivel actual
    nivel_actual = gestor_niveles.cargar_nivel()
    if nivel_actual:
        nivel_actual.actualizar(ventana)
        nivel_actual.dibujar_indicadores(ventana)

        # Dibujar el personaje después de actualizar el entorno
        personaje.dibujar(ventana)

        if nivel_actual.ha_completado_objetivo():
            gestor_niveles.avanzar_nivel()

    # Manejar combate
    combate.enemigos = gestor_enemigos.enemigos
    combate.detectar_colisiones()

    # Manejar eventos
    for evento in eventos:
        if nivel_actual:
            evento.verificar_activacion(tiempo_actual, nivel_actual.esqueletos_eliminados)

    # Terminar el juego si no hay más niveles
    if not nivel_actual:
        fuente = pygame.font.Font(None, 72)
        texto_fin = fuente.render("¡Juego Completado!", True, (255, 255, 255))
        ventana.fill(BLANCO)
        ventana.blit(texto_fin, (ANCHO // 2 - texto_fin.get_width() // 2, ALTO // 2 - texto_fin.get_height() // 2))
        pygame.display.flip()
        pygame.time.wait(3000)
        corriendo = False

    # Actualizar pantalla
    pygame.display.flip()

pygame.quit()

















