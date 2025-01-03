from constantes import CONFIGURACION

def manejar_gravedad(personaje, suelo):
    """
    Aplica la gravedad al personaje y verifica si está en el suelo.

    Args:
        personaje: Instancia del personaje al que se le aplica la gravedad.
        suelo: Objeto que limita el movimiento del personaje.
    """
    # Aplicar gravedad
    personaje.velocidad_y += personaje.gravedad
    personaje.y += personaje.velocidad_y

    # Verificar interacción con el suelo
    suelo.limitar_movimiento(personaje)

    # Restablecer saltos si el personaje está en el suelo
    if personaje.en_suelo:
        personaje.saltos_restantes = CONFIGURACION["personaje"]["saltos_maximos"]



