import pygame, random


class Objeto:
    def __init__(self, x, y):
        # Leer una imagen
        imagen_dona = pygame.image.load("Recursos/esfera.png")
        imagen_dona = pygame.transform.scale(imagen_dona, (30, 30))
        rect_dona = imagen_dona.get_rect()
        rect_dona.x = x
        rect_dona.y = y
        self.dict_dona = {"surface": imagen_dona, "rect": rect_dona, "visible": True}



    def update(self):
        self.dict_dona["rect"].y += 5  # Puedes ajustar la velocidad de caída según sea necesario

    def es_visible(self):
        return self.dict_dona["visible"]

    def hacer_invisible(self):
        self.dict_dona["visible"] = False

     