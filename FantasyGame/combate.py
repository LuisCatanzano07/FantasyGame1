class Combate:
    def __init__(self, personaje, enemigo):
        """Inicializa el sistema de combate entre el personaje y el enemigo."""
        self.personaje = personaje
        self.enemigo = enemigo

    def detectar_colisiones(self):
        """Detecta y gestiona todas las colisiones."""
        self.colision_personaje_enemigo()
        self.colision_rayos_enemigo()
        self.colision_ataque_area()

    def colision_personaje_enemigo(self):
        """Detecta y gestiona colisiones entre el personaje y el enemigo."""
        if (self.personaje.x < self.enemigo.x + self.enemigo.width and
            self.personaje.x + self.personaje.width > self.enemigo.x and
            self.personaje.y < self.enemigo.y + self.enemigo.height and
            self.personaje.y + self.personaje.height > self.enemigo.y):
            self.personaje.salud_actual -= 1
            self.enemigo.salud_actual -= 3

    def colision_rayos_enemigo(self):
        """Detecta y gestiona colisiones entre los rayos del personaje y el enemigo."""
        for rayo in self.personaje.rayos[:]:
            if (rayo["inicio"][0] < self.enemigo.x + self.enemigo.width and
                rayo["fin"][0] > self.enemigo.x and
                rayo["inicio"][1] < self.enemigo.y + self.enemigo.height and
                rayo["fin"][1] > self.enemigo.y):
                self.enemigo.salud_actual -= 10
                self.personaje.rayos.remove(rayo)

    def colision_ataque_area(self):
        """Detecta y gestiona daño cuando el enemigo está encima del personaje."""
        if (self.enemigo.x < self.personaje.x + self.personaje.width and
            self.enemigo.x + self.enemigo.width > self.personaje.x and
            self.enemigo.y + self.enemigo.height > self.personaje.y and
            self.enemigo.y < self.personaje.y + self.personaje.height / 2):
            self.personaje.salud_actual -= self.personaje.salud_max / 4
            self.enemigo.salud_actual -= self.enemigo.salud_max / 3

    def regenerar_salud(self, posicion_inicial_personaje, posicion_inicial_enemigo):
        """Regenera la salud y reposiciona las entidades si su salud llega a 0."""
        if self.personaje.salud_actual <= 0:
            self.personaje.salud_actual = self.personaje.salud_max
            self.personaje.x, self.personaje.y = posicion_inicial_personaje

        if self.enemigo.salud_actual <= 0:
            self.enemigo.salud_actual = self.enemigo.salud_max
            self.enemigo.x, self.enemigo.y = posicion_inicial_enemigo
