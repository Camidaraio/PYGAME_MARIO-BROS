from configuraciones import *
from class_disparo import *

class Enemigo:
    def __init__(self, animaciones):
        self.animaciones = animaciones
        reescalar_imagenes(self.animaciones, (50,55))
        # self.rectangulo = self.animaciones["izquierda"][0].get_rect()
        self.rectangulo = pygame.Rect(600, 824, 70, 50)
        self.contador_pasos = 0

        self.animacion_actual = self.animaciones["derecha"]
        self.esta_muerto = False
        self.esta_muriendo = False

        self.direccion = "derecha"

        self.vidas = 1
        self.estado = "aplastado"  # Puede ser "normal" o "aplastado"
        self.animacion_actual = self.animaciones["derecha"]  # Puedes ajustar la animación inicial

        self.lista_proyectiles = []

        self.tiempo_ultimo_disparo = 0

    def recibir_ataque(self):
        if self.estado == "normal":
            self.estado = "aplastado"
            self.animacion_actual = self.animaciones["aplastado"]

    def animar(self, pantalla):
        largo = len(self.animacion_actual)
        if self.contador_pasos >= largo:
            self.contador_pasos = 0

        pantalla.blit(self.animacion_actual[self.contador_pasos], self.rectangulo)
        self.contador_pasos += 1

        if self.esta_muriendo and self.contador_pasos == largo:
            self.esta_muerto = True

    
    def avanzar(self):
        self.rectangulo.x -= 2

    def actualizar(self, pantalla, personaje):
        self.animar(pantalla)
        self.avanzar()

        if not self.esta_muerto and self.rectangulo.colliderect(personaje.rectangulo):
            personaje.restar_vida()  # Resta vida al personaje al colisionar con el enemigo



    def recibir_danio(self):
        self.vidas -= 1
        if self.vidas <= 0:
            self.esta_muriendo = True


    # def invertir_direccion(self):
    #     if self.direccion == "derecha":
    #         self.direccion = "izquierda"
    #     elif self.direccion == "izquierda":
    #         self.direccion = "derecha"


    def lanzar_proyectil(self):
        tiempo_actual = pygame.time.get_ticks()
        if tiempo_actual - self.tiempo_ultimo_disparo >= 1200:  # Ajusta el intervalo de disparo según sea necesario
            x = None
            margen = 47
            y = self.rectangulo.centery + 10

            if self.direccion == "derecha" or self.direccion == "quieto":
                x = self.rectangulo.right - margen
            elif self.direccion == "izquierda":
                x = self.rectangulo.left - 100 + margen

            if x is not None:
                self.lista_proyectiles.append(Disparo(x, y, "izquierda"))
                self.tiempo_ultimo_disparo = tiempo_actual