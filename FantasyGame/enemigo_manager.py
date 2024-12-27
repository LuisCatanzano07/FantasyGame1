import pygame
import random
from enemigo import Enemigo

class GestorEnemigos:
    def __init__(self, ruta_sprites, suelo):
        """Inicializa el gestor de enemigos."""
        self.enemigos = []
        self.ruta_sprites = ruta_sprites
        self.suelo = suelo
        self.tiempo_ultimo_generado = 0
        self.intervalo_generacion = 5000  # 5 segundos en milisegundos
        self.nivel_actual = 1
        self.enemigos_nivel = []  # Enemigos específicos del desafío por nivel
        self.fuente = pygame.font.Font(None, 24)  # Fuente más pequeña para texto

        # Contadores
        self.contador_esqueletos = 0
        self.contador_muertes = 0

        # Generar el primer enemigo inmediatamente
        self.generar_primer_enemigo()

    def generar_primer_enemigo(self):
        """Genera un enemigo inicial al inicio del juego."""
        nuevo_enemigo = Enemigo(x=-50 if random.choice([True, False]) else 850, y=self.suelo.y - 50, 
                                width=50, height=50, ruta_sprites=self.ruta_sprites)
        self.enemigos.append(nuevo_enemigo)
        self.contador_esqueletos += 1

    def generar_enemigos(self, tiempo_actual):
        """Genera enemigos periódicamente y al completar un nivel."""
        # Generar enemigos cada 5 segundos
        if tiempo_actual - self.tiempo_ultimo_generado >= self.intervalo_generacion:
            self.tiempo_ultimo_generado = tiempo_actual
            nuevo_enemigo = Enemigo(x=-50 if random.choice([True, False]) else 850, y=self.suelo.y - 50, 
                                    width=50, height=50, ruta_sprites=self.ruta_sprites)
            self.enemigos.append(nuevo_enemigo)
            self.contador_esqueletos += 1

        # Generar enemigos específicos del nivel
        if not self.enemigos_nivel and self.nivel_actual <= 10:
            for _ in range(self.nivel_actual):
                nuevo_enemigo = Enemigo(x=-50 if random.choice([True, False]) else 850, y=self.suelo.y - 50, 
                                        width=50, height=50, ruta_sprites=self.ruta_sprites)
                self.enemigos_nivel.append(nuevo_enemigo)
                self.contador_esqueletos += 1

    def actualizar_enemigos(self, personaje, ventana):
        """Actualiza el estado y dibuja todos los enemigos."""
        # Actualizar y dibujar enemigos regulares
        for enemigo in self.enemigos[:]:
            enemigo.mover(personaje, self.suelo)
            enemigo.dibujar(ventana)
            enemigo.dibujar_barra_salud(ventana)
            if enemigo.salud_actual <= 0:
                self.enemigos.remove(enemigo)
                self.contador_esqueletos -= 1
                self.contador_muertes += 1

        # Actualizar y dibujar enemigos del nivel
        for enemigo in self.enemigos_nivel[:]:
            enemigo.mover(personaje, self.suelo)
            enemigo.dibujar(ventana)
            enemigo.dibujar_barra_salud(ventana)
            if enemigo.salud_actual <= 0:
                self.enemigos_nivel.remove(enemigo)
                self.contador_esqueletos -= 1
                self.contador_muertes += 1

        # Avanzar al siguiente nivel si todos los enemigos del nivel han muerto
        if not self.enemigos_nivel and self.nivel_actual <= 10:
            self.nivel_actual += 1

        # Dibujar la representación general en la parte superior
        self.dibujar_indicadores(ventana)

    def dibujar_indicadores(self, ventana):
        """Dibuja indicadores de esqueletos y muertes al lado de las barras."""
        texto_esqueletos = f"E: {self.contador_esqueletos}"
        texto_muertes = f"M: {self.contador_muertes}"

        render_esqueletos = self.fuente.render(texto_esqueletos, True, (0, 0, 0))
        render_muertes = self.fuente.render(texto_muertes, True, (0, 0, 0))

        ventana.blit(render_esqueletos, (220, 10))  # Al lado de la barra de salud
        ventana.blit(render_muertes, (220, 40))  # Al lado de la barra de energía




