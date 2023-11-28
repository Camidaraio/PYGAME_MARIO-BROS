import  pygame

class Disparo:
    def __init__(self, x, y, direccion):
        self.superficie = pygame.image.load(r"Recursos/f0.png")
        self.superficie = pygame.transform.scale(self.superficie, (15,10))
        self.rectangulo = self.superficie.get_rect()
        self.rectangulo.x  = x
        self.rectangulo.centery = y
        self.direccion = direccion

    def actualizar(self, pantalla):
        if  self.direccion  ==  "derecha" or self.direccion == "quieto":
            self.rectangulo.x += 10
        elif self.direccion == "izquierda":
            self.rectangulo.x   -= 10
        pantalla.blit(self.superficie, self.rectangulo)

    def destruir(self):
        self.rectangulo.x = -100  # Mueve el proyectil fuera de la pantalla para eliminarlo
