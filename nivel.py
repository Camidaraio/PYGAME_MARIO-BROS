import pygame
from maincopy import *

class Nivel:
    def __init__(self, pantalla, personaje_principal, lista_playaformas, imagen_fondo):
        self._slave = pantalla
        self.jugador = personaje_principal
        self.plataformas = lista_plataformas
        self.img_fondo = imagen_fondo
        self.enemigos = enemigo
        self.enemigos2 = enemigo2

    def update(self, lista_eventos):
        for evento in lista_eventos:
            if evento.type == KEYDOWN:
                if evento.key == pygame.K_TAB:
                    cambiar_modo()
            elif evento.type == MOUSEBUTTONDOWN:
                print(evento.pos)
        self.leer_inputs()
        self.actualizar_pantalla()

    def leer_inputs(self):
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_RIGHT]:
            self.jugador = "derecha"
            flag_disparo = True

        elif teclas[pygame.K_LEFT]:
            self.jugador = "izquierda"
            flag_disparo = True

        elif teclas[pygame.K_UP]:
            self.jugador = "salta"
            flag_disparo = True

        else:
            self.jugador = "quieto"
            flag_disparo = True

        #### DISPARO ###########
        if flag_disparo and teclas[pygame.K_w]:
            tiempo_actual= pygame.time.get_ticks()
            if  tiempo_actual - tiempo_ultimo_disparo >= 500:
                self.jugador.lanzar_proyectil()
                flag_disparo = False
                tiempo_ultimo_disparo = tiempo_actual


    def dibujar_rectangulos(self):
        #MODO DEBUG
        if obtener_modo():
            pygame.draw.rect(self._slave, "pink", self.jugador.rectangulo, 3)
            for enemigo in self.enemigos:
                if not un_enemigo.esta_muerto:
                    pygame.draw.rect(self._slave, "green", self.enemigos.rectangulo, 3)

                if not un_enemigo2.esta_muerto:
                    pygame.draw.rect(self._slave, "black", self.enemigos2.rectangulo, 3)
                    
            for plataforma in  self.plataformas:
                pygame.draw.rect(self._slave, "red", plataforma["rectangulo"], 3)

    def actualizar_pantalla(self):
        ### fondo #########

        x_relativa = x % fondo.get_rect().width
        self._slave.blit(fondo,(x_relativa - fondo.get_rect().width,0))

        if(x_relativa < ANCHO):
            self._slave.blit(fondo,(x_relativa,0))
        x -= 2
        ########

        self._slave.blit(fondo, (0,0))

        self.jugador.actualizar(self._slave, self.plataformas)

        
        self.jugador.actualizar_proyectiles(self._slave)

            
