class Evento:
    def __init__(self, tipo: str, tiempo_activacion: int, accion, objetivo_nivel: int):
        """Inicializa un evento con su tipo, tiempo de activación, acción y objetivo del nivel."""
        self.tipo = tipo
        self.tiempo_activacion = tiempo_activacion  # Tiempo en milisegundos para activar el evento
        self.accion = accion  # Función a ejecutar cuando se active el evento
        self.activado = False
        self.objetivo_nivel = objetivo_nivel  # Se relaciona con el progreso del nivel

    def verificar_activacion(self, tiempo_actual: int, progreso_actual: int):
        """Verifica si el evento debe activarse basado en el tiempo actual y el progreso del nivel."""
        if not self.activado and tiempo_actual >= self.tiempo_activacion and progreso_actual >= self.objetivo_nivel:
            self.activar_evento()

    def activar_evento(self):
        """Activa el evento y ejecuta la acción asociada."""
        self.activado = True
        if self.accion:
            self.accion()

    def reiniciar(self):
        """Reinicia el evento para que pueda ser reactivado."""
        self.activado = False

