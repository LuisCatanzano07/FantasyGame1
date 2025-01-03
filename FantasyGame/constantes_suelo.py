# constantes_suelo.py

# Dimensiones y posición del suelo
ALTURA_SUELO = 30  # Altura del suelo en píxeles
POSICION_INICIAL_X = 0  # Coordenada X donde comienza el suelo
POSICION_INICIAL_Y = None  # Coordenada Y donde se coloca el suelo (None para usar el borde inferior de la pantalla)

# Color del suelo
COLOR_SUELO = (150, 75, 0)  # Marrón (RGB)

# Número de plataformas
NUMERO_SUELOS = 10  # Cantidad de plataformas o suelos diferentes

# Espaciado entre plataformas (para plataformas flotantes)
ESPACIADO_HORIZONTAL = 20  # Espaciado horizontal entre plataformas
ESPACIADO_VERTICAL = 100  # Espaciado vertical entre plataformas

# Configuración de plataformas flotantes
PLATAFORMA_ANCHO = 150  # Ancho de cada plataforma
PLATAFORMA_ALTO = 20  # Altura de cada plataforma


# constantes físicas del suelo
FRICCION_SUELO = 0.8  # Reducción de velocidad cuando el personaje está en el suelo
REBOTE_SUELO = 0.0  # Coeficiente de rebote (0: sin rebote, 1: rebote completo)

# Gravedad (relacionada con el suelo y el personaje)
GRAVEDAD = 9.8  # Aceleración gravitacional (en píxeles por segundo al cuadrado)


# Opciones de diseño visual
USAR_TEXTURA = False  # Indica si se usa una textura en lugar de un color sólido
RUTA_SPRITE_SUELO = "assets/sprites/suelo.png"  # Ruta a la textura del suelo

# Decoraciones
DECORAR_SUELO = True  # Indica si se dibujan elementos decorativos en el suelo
RUTA_DECORACION = "assets/sprites/decoracion_suelo.png"  # Ruta a las decoraciones

# Configuración para terrenos dinámicos o complejos
TERRENO_IRREGULAR = False  # Indica si el terreno tiene alturas variables
ALTURAS_TERRENO = [0, 50, 30, 20, 0]  # Ejemplo de alturas irregulares (en píxeles)

# Movimiento de plataformas
PLATAFORMAS_MOVILES = False  # Indica si hay plataformas móviles
VELOCIDAD_PLATAFORMAS = 2  # Velocidad de movimiento de las plataformas móviles (en píxeles por frame)

# Colisiones avanzadas
COLISION_PRECISA = False  # Usar detección precisa de colisiones para formas irregulares
