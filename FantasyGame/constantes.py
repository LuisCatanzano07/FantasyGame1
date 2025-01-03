# Configuración global
CONFIGURACION = {
    "colores": {
        "barra_salud": (0, 0, 255),
        "barra_energia": (255, 0, 0),
        "borde_barra": (255, 255, 255),
        "rayo": (255, 255, 0)
    },
    "dimensiones_barras": {
        "ancho": 200,
        "alto_salud": 20,
        "alto_energia": 20
    },
    "animacion": {
        "duracion_frame": 100
    },
    "sprites": {
        "cantidad_frames": 7,
        "nombres_personalizados": None,  # Lista de nombres personalizados o None para usar el formato predeterminado
        "ruta": "assets/sprites/jugador/Player_{}.png"  # Ruta con formato para los sprites
    },
    "rayo": {
        "largo": 50,
        "velocidad": 10,
        "costo_energia": 20
    },
    "personaje": {
        "velocidad": 5,
        "saltos_maximos": 2,
        "velocidad_salto": -15,
        "gravedad": 1,
        "salud_max": 100,
        "energia_max": 100,
        "recuperacion_energia_intervalo": 100,
        "recuperacion_energia_cantidad": 1
    }
}







