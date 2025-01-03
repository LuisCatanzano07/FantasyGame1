import pygame
import random
from enemigo import Enemigo
from typing import List

class GestorEnemigos:
    def __init__(self, ruta_sprites: str, suelo, ancho_ventana: int):
        """Inicializa el gestor de enemigos."""
        self.enemigos: List[Enemigo] = []
        self.ruta_sprites = ruta_sprites
        self.suelo = suelo
        self.ancho_ventana = ancho_ventana
        self.tiempo_ultimo_generado = 0
        self.intervalo_generacion = 5000  # Milisegundos entre la generación de enemigos
        self.nivel_actual = 1
        self.enemigos_nivel: List[Enemigo] = []  # Enemigos específicos del desafío por nivel
        self.fuente = pygame.font.Font(None, 24)  # Fuente para texto
        self.contador_esqueletos = 0
        self.contador_muertes = 0
        self.max_enemigos = 15  # Límite de enemigos activos en pantalla

        # Generar el primer enemigo inmediatamente
        self.generar_primer_enemigo()

    def generar_primer_enemigo(self):
        """Genera un enemigo inicial al inicio del juego."""
        self.agregar_enemigo()

    def agregar_enemigo(self, x: int = None):
        """Agrega un enemigo a la lista de enemigos."""
        if len(self.enemigos) >= self.max_enemigos:
            return  # No agregar más enemigos si se alcanzó el límite

        if x is None:
            x = random.choice([-50, self.ancho_ventana + 50])
        nuevo_enemigo = Enemigo(x=x, y=self.suelo.y - 50, width=50, height=50, ruta_sprites=self.ruta_sprites)
        self.enemigos.append(nuevo_enemigo)
        self.contador_esqueletos += 1

    def generar_enemigos(self, tiempo_actual: int):
        """Genera enemigos periódicamente y al completar un nivel."""
        if tiempo_actual - self.tiempo_ultimo_generado >= self.intervalo_generacion:
            self.tiempo_ultimo_generado = tiempo_actual
            self.agregar_enemigo()

        # Generar enemigos específicos del nivel
        while len(self.enemigos_nivel) < self.nivel_actual and len(self.enemigos) < self.max_enemigos:
            self.agregar_enemigo()
            self.enemigos_nivel.append(self.enemigos[-1])

    def actualizar_enemigos(self, personaje, ventana: pygame.Surface):
        """Actualiza el estado y dibuja todos los enemigos."""
        self.generar_enemigos(pygame.time.get_ticks())

        # Actualizar y dibujar enemigos
        for enemigo in self.enemigos[:]:
            enemigo.mover(personaje, self.suelo)
            enemigo.dibujar(ventana)
            enemigo.dibujar_barra_salud(ventana)
            if enemigo.salud_actual <= 0:
                self.enemigos.remove(enemigo)
                self.contador_esqueletos -= 1
                self.contador_muertes += 1

        # Verificar avance de nivel
        if not self.enemigos_nivel and self.nivel_actual <= 10:
            self.nivel_actual += 1

        self.dibujar_indicadores(ventana)

    def dibujar_indicadores(self, ventana: pygame.Surface):
        """Dibuja indicadores de esqueletos activos y muertes."""
        texto_esqueletos = f"E: {self.contador_esqueletos}"
        texto_muertes = f"M: {self.contador_muertes}"

        render_esqueletos = self.fuente.render(texto_esqueletos, True, (0, 0, 0))
        render_muertes = self.fuente.render(texto_muertes, True, (0, 0, 0))

        ventana.blit(render_esqueletos, (220, 10))
        ventana.blit(render_muertes, (220, 40))







