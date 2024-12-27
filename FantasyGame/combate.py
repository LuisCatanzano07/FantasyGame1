class Combate:
    def __init__(self, personaje, enemigos):
        """Inicializa el sistema de combate entre el personaje y los enemigos."""
        self.personaje = personaje
        self.enemigos = enemigos

    def detectar_colisiones(self):
        """Detecta y gestiona todas las colisiones entre el personaje y los enemigos."""
        self.colision_personaje_enemigos()
        self.colision_rayos_enemigos()

    def colision_personaje_enemigos(self):
        """Detecta y gestiona colisiones entre el personaje y cada enemigo."""
        for enemigo in self.enemigos[:]:
            if self._rectangulos_colisionan(self.personaje, enemigo):
                self.personaje.salud_actual -= 1
                enemigo.salud_actual -= 3
                if enemigo.salud_actual <= 0:
                    self.enemigos.remove(enemigo)

    def colision_rayos_enemigos(self):
        """Detecta y gestiona colisiones entre los rayos del personaje y los enemigos."""
        for rayo in self.personaje.rayos[:]:
            for enemigo in self.enemigos[:]:
                if self._rayo_colisiona_con_enemigo(rayo, enemigo):
                    enemigo.salud_actual = 0  # El rayo quita toda la salud del enemigo
                    self.enemigos.remove(enemigo)
                    self.personaje.rayos.remove(rayo)
                    break

    def _rectangulos_colisionan(self, personaje, enemigo):
        """Verifica si los rectángulos de personaje y enemigo colisionan."""
        return (
            personaje.x < enemigo.x + enemigo.width and
            personaje.x + personaje.width > enemigo.x and
            personaje.y < enemigo.y + enemigo.height and
            personaje.y + personaje.height > enemigo.y
        )

    def _rayo_colisiona_con_enemigo(self, rayo, enemigo):
        """Verifica si un rayo colisiona con un enemigo."""
        return (
            max(rayo["inicio"][0], rayo["fin"][0]) > enemigo.x and
            min(rayo["inicio"][0], rayo["fin"][0]) < enemigo.x + enemigo.width and
            max(rayo["inicio"][1], rayo["fin"][1]) > enemigo.y and
            min(rayo["inicio"][1], rayo["fin"][1]) < enemigo.y + enemigo.height
        )





