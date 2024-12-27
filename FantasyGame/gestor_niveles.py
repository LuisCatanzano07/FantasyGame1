import pygame
from nivel import Nivel
from typing import List

class GestorNiveles:
    def __init__(self, gestor_enemigos, personaje):
        """Inicializa el gestor de niveles."""
        self.niveles: List[Nivel] = []
        self.nivel_actual = 0
        self.gestor_enemigos = gestor_enemigos
        self.personaje = personaje
        self.configurar_niveles()

    def configurar_niveles(self):
        """Configura los niveles con sus objetivos y colores de suelo."""
        nivel1 = Nivel(numero=1, gestor_enemigos=self.gestor_enemigos, personaje=self.personaje, objetivo=50, color_suelo=(50, 200, 50))
        nivel2 = Nivel(numero=2, gestor_enemigos=self.gestor_enemigos, personaje=self.personaje, objetivo=100, color_suelo=(200, 100, 50))
        nivel3 = Nivel(numero=3, gestor_enemigos=self.gestor_enemigos, personaje=self.personaje, objetivo=150, color_suelo=(50, 50, 200))

        self.niveles.extend([nivel1, nivel2, nivel3])

    def cargar_nivel(self) -> Nivel:
        """Carga el nivel actual."""
        if self.nivel_actual < len(self.niveles):
            return self.niveles[self.nivel_actual]
        return None

    def avanzar_nivel(self):
        """Avanza al siguiente nivel."""
        if self.nivel_actual < len(self.niveles) - 1:
            self.nivel_actual += 1

    def reiniciar_nivel(self):
        """Reinicia el nivel actual."""
        nivel_actual = self.cargar_nivel()
        if nivel_actual:
            nivel_actual.reiniciar()

    def nivel_completado(self) -> bool:
        """Verifica si el nivel actual está completado."""
        nivel_actual = self.cargar_nivel()
        if nivel_actual:
            return nivel_actual.ha_completado_objetivo()
        return False

    def actualizar(self, ventana: pygame.Surface):
        """Actualiza y dibuja el nivel actual."""
        nivel_actual = self.cargar_nivel()
        if nivel_actual:
            nivel_actual.actualizar(ventana)
            nivel_actual.dibujar_indicadores(ventana)


