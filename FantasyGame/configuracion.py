import pygame
import json


class ConfiguracionControles:
    def __init__(self, archivo_config: str):
        """Inicializa la configuración de controles y carga desde un archivo si existe."""
        self.archivo_config = archivo_config
        self.controles = {
            "mover_arriba": pygame.K_w,
            "mover_abajo": pygame.K_s,
            "mover_izquierda": pygame.K_a,
            "mover_derecha": pygame.K_d,
            "saltar": pygame.K_RETURN,
            "disparar": pygame.K_SPACE,
            "abrir_menu": pygame.K_c
        }
        self.cargar_configuracion()

    def cargar_configuracion(self):
        """Carga la configuración desde un archivo JSON."""
        try:
            with open(self.archivo_config, "r") as archivo:
                data = json.load(archivo)
                if isinstance(data, dict):
                    self.controles.update(data)
        except (FileNotFoundError, json.JSONDecodeError):
            self.guardar_configuracion()  # Guarda la configuración predeterminada si no existe o está corrupta

    def guardar_configuracion(self):
        """Guarda la configuración actual en un archivo JSON."""
        with open(self.archivo_config, "w") as archivo:
            json.dump(self.controles, archivo, indent=4)

    def asignar_tecla(self, accion: str, nueva_tecla: int):
        """Asigna una nueva tecla a una acción específica."""
        if accion in self.controles:
            self.controles[accion] = nueva_tecla
            self.guardar_configuracion()
        else:
            raise ValueError(f"La acción '{accion}' no existe en la configuración.")

    def obtener_tecla(self, accion: str) -> int:
        """Obtiene la tecla asignada a una acción específica."""
        return self.controles.get(accion, None)

    def mostrar_menu(self, ventana: pygame.Surface):
        """Muestra un menú para configurar las teclas."""
        pygame.init()
        fuente = pygame.font.Font(None, 36)
        instrucciones = "Flechas para mover, Enter para configurar, C para salir."

        acciones = list(self.controles.keys())
        indice_seleccionado = 0
        ejecutando_menu = True

        while ejecutando_menu:
            ventana.fill((0, 0, 0))
            render_instrucciones = fuente.render(instrucciones, True, (255, 255, 255))
            ventana.blit(render_instrucciones, (50, 10))

            # Mostrar todas las acciones con sus teclas
            for i, accion in enumerate(acciones):
                color = (255, 255, 0) if i == indice_seleccionado else (255, 255, 255)
                texto = f"{accion}: {pygame.key.name(self.controles[accion])}"
                render = fuente.render(texto, True, color)
                ventana.blit(render, (50, 50 + i * 40))

            pygame.display.flip()

            for evento in pygame.event.get():
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_DOWN:
                        indice_seleccionado = (indice_seleccionado + 1) % len(acciones)
                    elif evento.key == pygame.K_UP:
                        indice_seleccionado = (indice_seleccionado - 1) % len(acciones)
                    elif evento.key == pygame.K_RETURN:
                        self._asignar_tecla_interactiva(ventana, acciones[indice_seleccionado], fuente)
                    elif evento.key == self.obtener_tecla("abrir_menu"):
                        ejecutando_menu = False
                elif evento.type == pygame.QUIT:
                    ejecutando_menu = False

    def _asignar_tecla_interactiva(self, ventana: pygame.Surface, accion: str, fuente: pygame.font.Font):
        """Muestra una pantalla para asignar una nueva tecla a una acción."""
        asignando = True
        while asignando:
            ventana.fill((0, 0, 0))
            texto = f"Presiona una nueva tecla para: {accion}"
            render = fuente.render(texto, True, (255, 255, 255))
            ventana.blit(render, (50, 100))
            pygame.display.flip()

            for evento in pygame.event.get():
                if evento.type == pygame.KEYDOWN:
                    self.asignar_tecla(accion, evento.key)
                    asignando = False
                elif evento.type == pygame.QUIT:
                    asignando = False



