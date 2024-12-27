import pygame
from typing import Tuple

class Nivel:
    def __init__(self, numero: int, gestor_enemigos, personaje, objetivo: int, color_suelo: Tuple[int, int, int]):
        """Inicializa un nivel con su número, gestor de enemigos, personaje y objetivo."""
        self.numero = numero
        self.gestor_enemigos = gestor_enemigos
        self.personaje = personaje
        self.objetivo = objetivo
        self.color_suelo = color_suelo
        self.esqueletos_eliminados = 0
        self.completado = False

    def ha_completado_objetivo(self) -> bool:
        """Verifica si el objetivo del nivel ha sido alcanzado."""
        return self.esqueletos_eliminados >= self.objetivo

    def reiniciar(self):
        """Reinicia el nivel y restablece el progreso."""
        self.esqueletos_eliminados = 0
        self.completado = False
        self.gestor_enemigos.enemigos = []
        self.gestor_enemigos.enemigos_nivel = []

    def actualizar(self, ventana: pygame.Surface):
        """Actualiza el estado del nivel."""
        self.dibujar_entorno(ventana)
        self.actualizar_progreso()
        self.gestor_enemigos.actualizar_enemigos(self.personaje, ventana)

    def dibujar_entorno(self, ventana: pygame.Surface):
        """Dibuja el entorno del nivel."""
        # Dibujar el fondo
        ventana.fill((0, 0, 0))  # Fondo negro

        # Dibujar el suelo
        suelo_rect = pygame.Rect(0, 500, ventana.get_width(), 100)  # Suelo en la parte inferior
        pygame.draw.rect(ventana, self.color_suelo, suelo_rect)

    def actualizar_progreso(self):
        """Actualiza el progreso del nivel basado en enemigos eliminados."""
        self.esqueletos_eliminados = self.gestor_enemigos.contador_muertes
        self.completado = self.ha_completado_objetivo()

    def dibujar_indicadores(self, ventana: pygame.Surface):
        """Dibuja los indicadores del nivel (número, progreso, etc.)."""
        fuente = pygame.font.Font(None, 36)
        texto_nivel = fuente.render(f"Nivel: {self.numero}", True, (255, 255, 255))
        texto_objetivo = fuente.render(f"Progreso: {self.esqueletos_eliminados}/{self.objetivo}", True, (255, 255, 255))

        ventana.blit(texto_nivel, (10, 10))
        ventana.blit(texto_objetivo, (10, 50))




