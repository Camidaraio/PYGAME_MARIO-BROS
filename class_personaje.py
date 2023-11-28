from configuraciones import *
from class_enemigo import *
from class_disparo import *

class Personaje:
    def __init__(self,animaciones, pos_x, pos_y, tamaño, velocidad, que_hace):
        self.animaciones = animaciones
        reescalar_imagenes(self.animaciones, tamaño)
        self.rectangulo = pygame.Rect(pos_x,pos_y, *tamaño) #primera forma
        # self.rectangulo = self.animaciones["quieto"][0].get_rect() #De esta forma, toma el rectangulo de la imagen
        self.rectangulo.x = pos_x
        self.rectangulo.y = pos_y
        self.velocidad = velocidad
        self.que_hace = que_hace
        self.contador_pasos = 0        
        self.animacion_actual = self.animaciones[self.que_hace]
    
        self.gravedad = 1
        self.desplazamiento_y = 0
        self.potencia_salto = -20
        self.limite_velocidad_salto = 20
        self.esta_saltando = False

        self.vida = 2
        self.esta_muriendo = False 

        self.lista_proyectiles = []

        self.score = 0 

        
    
    
    def aplicar_gravedad(self, pantalla, lista_plataformas):
        if self.esta_saltando:
            self.animar(pantalla)
            self.rectangulo.y+= self.desplazamiento_y
            if self.desplazamiento_y + self.gravedad <self.limite_velocidad_salto:
                self.desplazamiento_y += self.gravedad
                
        for plataforma in lista_plataformas:
            if self.rectangulo.colliderect(plataforma["rectangulo"]):
                self.esta_saltando = False
                self.desplazamiento_y = 0
                self.rectangulo.bottom = plataforma["rectangulo"].top
                break
            else:
                self.esta_saltando = True


    def desplazar(self):
        velocidad_actual = self.velocidad
        if self.que_hace == "izquierda":
            velocidad_actual *= -1
        
        self.rectangulo.x += velocidad_actual


    def animar(self, pantalla):
        largo = len(self.animacion_actual)
        if self.contador_pasos >= largo:
            self.contador_pasos = 0

        pantalla.blit(self.animacion_actual[self.contador_pasos], self.rectangulo)
        self.contador_pasos += 1

    #Que hace el personaje
    def actualizar(self, pantalla, lista_plataformas):
        match self.que_hace:
            case "derecha":
                if not self.esta_saltando:
                    self.animacion_actual = self.animaciones["derecha"]
                    self.animar(pantalla)
                self.desplazar()
            case "izquierda":
                if not self.esta_saltando:
                    self.animacion_actual = self.animaciones["izquierda"]
                    self.animar(pantalla)
                self.desplazar()
            case "quieto":
                if not self.esta_saltando:
                    self.animacion_actual = self.animaciones["quieto"]
                    self.animar(pantalla)
            case "salta":
                if not self.esta_saltando:
                    self.esta_saltando = True
                    self.desplazamiento_y = self.potencia_salto
                    self.animacion_actual = self.animaciones["salta"]

        self.actualizar_proyectiles(pantalla)
        self.aplicar_gravedad(pantalla, lista_plataformas)
    
    def verificar_colision_enemigo(self, enemigo: Enemigo, pantalla):
        if self.rectangulo.colliderect(enemigo.rectangulo):
            enemigo.esta_muriendo = False
            # enemigo.rectangulo.y += 5
            enemigo.animacion_actual = enemigo.animaciones["derecha"]
            enemigo.animar(pantalla)
            
            # Restar vida al personaje
            self.restar_vida()



    def lanzar_proyectil(self):
        x  = None
        margen = 47
        
        y = self.rectangulo.centery + 10 # De donde sale el disparo
        if self.que_hace == "derecha" or self.que_hace == "quieto":
            x=  self.rectangulo.right - margen 
        elif self.que_hace == "izquierda": 
            x=  self.rectangulo.left - 100 + margen 

        if x is not None:
            self.lista_proyectiles.append(Disparo (x,y, self.que_hace))

    def actualizar_proyectiles(self, pantalla):
        i = 0
        while i < len(self.lista_proyectiles):
            p = self.lista_proyectiles[i]
            p.actualizar(pantalla)
            if p.rectangulo.centerx < 0 or p.rectangulo.centerx > pantalla.get_width():
                self.lista_proyectiles.pop(i)
                i -= 1
            i += 1
    
    # def verificar_colision_proyectil_enemigo(self, enemigo, pantalla):
    #     for proyectil in self.lista_proyectiles:
    #         if proyectil.rectangulo.colliderect(enemigo.rectangulo):
    #             proyectil.destruir()
    #             enemigo.recibir_danio()

    def verificar_colision_proyectil_enemigo(self, enemigo, pantalla):
        for proyectil in self.lista_proyectiles:
            if proyectil.rectangulo.colliderect(enemigo.rectangulo):
                # El proyectil impactó al enemigo
                enemigo.recibir_ataque()  # Método para cambiar el estado del enemigo
                self.lista_proyectiles.remove(proyectil) 
                enemigo.esta_muriendo = True

    def restar_vida(self,  cantidad=1):
        self.vida -= cantidad
        if self.vida <= 0:
            # Aquí puedes implementar lógica adicional cuando el personaje se queda sin vida
            self.esta_muriendo = True


    
    def aumentar_puntuacion(self):
        self.score += 1







# caracteristicas
# atributo
#         rectangulo
#         animaciones
#         tamaño
#         posicion
#         velocidad

# acciones
# metodos
#         correr
#         caminar
#         saltar
#         agacharse
#         agacharse
#         animar
#         atacar