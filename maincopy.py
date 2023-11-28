import pygame, sys
from class_personaje import *
from class_enemigo import *
from configuraciones import *
from pygame.locals import *
from modo import *
from nivel import *

def crear_plataforma(es_visible, tamaño, posicion, path=""): #devuelve dicionario
    plataforma = {}
    if es_visible:
        plataforma["superficie"] = pygame.image.load(path)
        plataforma["superficie"] = pygame.transform.scale(plataforma["superficie"], tamaño)
    else:
        plataforma["superficie"] = pygame.Surface(tamaño)

    plataforma["rectangulo"] = plataforma["superficie"].get_rect()

    x,y = posicion

    plataforma["rectangulo"].x = x
    plataforma["rectangulo"].y = y

    return plataforma



    

##############################INICIALIZACIONES##########################################

############# Pantalla ##########

ANCHO, ALTO = 900,600
FPS = 18 #para desacelerar la pantalla
x = 0

pygame.init()
RELOJ = pygame.time.Clock()
PANTALLA = pygame.display.set_mode((ANCHO, ALTO)) # en pixeles

#Fondo
fondo = pygame.image.load(r"Recursos\fondo8.gif").convert()#Acelera el juego y hace que consuma menos recursos
fondo = pygame.transform.scale(fondo, (ANCHO, ALTO)) 


########### personaje ############
diccionario_animaciones = {}
diccionario_animaciones["derecha"] = personaje_derecha
diccionario_animaciones["izquierda"] = personaje_izquierda
diccionario_animaciones["quieto"] = personaje_quieto
diccionario_animaciones["salta"] = personaje_salta

mario = Personaje(diccionario_animaciones, 0,160,(80,80), 7, "quieto")


# piso = crear_plataforma(True, (100, 20), (10, 498), "Recursos\h.png")
#piso = crear_plataforma(True, (ANCHO,150), (0, 350), "Recursos\h.png")
piso = crear_plataforma(False, (ANCHO, 20), (0, 510))



plataforma_caño = crear_plataforma(True, (100  ,50), (150, 350), "Recursos\h.png")


#plataforma_invisible = crear_plataforma(True,  (95,55), (0, 480), "Recursos\h.png")

#plataforma_invisible1 = crear_plataforma(True,  (120,55), (260, 280), "Recursos\h.png")

plataforma_invisible2 = crear_plataforma(True,  (200,55), (200, 250), "Recursos\h.png")

plataforma_invisible3 = crear_plataforma(True,  (250,55), (500, 250), "Recursos\h.png")


lista_plataformas = [piso, plataforma_caño,plataforma_invisible2, plataforma_invisible3 ]

mario.rectangulo.bottom = piso["rectangulo"].top

# ...

########## ENEMIGO ###########
diccionario_animaciones_enemigo = {"derecha" : enemigo_derecha, "aplastado": enemigo_aplastado}
un_enemigo = Enemigo(diccionario_animaciones_enemigo)
d = {"aplasta": diccionario_animaciones_enemigo["aplastado"]}
reescalar_imagenes(d, (55, 25))

un_enemigo.rectangulo.bottom = piso["rectangulo"].top

########## ENEMIGO2 ###########
diccionario_animaciones_enemigo2 = {"derecha" : enemigo_derecha, "aplastado": enemigo_aplastado}
un_enemigo2 = Enemigo(diccionario_animaciones_enemigo2)
d = {"aplasta": diccionario_animaciones_enemigo["aplastado"]}
reescalar_imagenes(d, (100, 25))

un_enemigo2.rectangulo.bottom = piso["rectangulo"].top

# Modificar coordenadas iniciales de los enemigos
un_enemigo.rectangulo.x = 600
un_enemigo2.rectangulo.x = 300

lista_enemigos = [un_enemigo, un_enemigo2]
direccion_enemigo = "derecha"



############# PLATAFORMA ################


flag_disparo = False
tiempo_ultimo_disparo = 0

bandera = True

while bandera:
    RELOJ.tick(FPS)
    for evento in pygame.event.get():
        if evento.type == QUIT:
            bandera = False
        
    

    
    

    for proyectil in mario.lista_proyectiles:
        proyectil.actualizar(PANTALLA)

    # Eliminar proyectiles que salieron de la pantalla
    mario.lista_proyectiles = [p for p in mario.lista_proyectiles if 0 < p.rectangulo.centerx < ANCHO]

      
    


    PANTALLA.blit(plataforma_caño["superficie"], plataforma_caño["rectangulo"]) #pasar a clase plataforma

    #PANTALLA.blit(plataforma_invisible["superficie"], plataforma_invisible["rectangulo"]) 

    #PANTALLA.blit(plataforma_invisible1["superficie"], plataforma_invisible1["rectangulo"]) 

    PANTALLA.blit(plataforma_invisible2["superficie"], plataforma_invisible2["rectangulo"]) 
    PANTALLA.blit(plataforma_invisible3["superficie"], plataforma_invisible3["rectangulo"]) 






     
    if not un_enemigo.esta_muerto:
        un_enemigo.actualizar(PANTALLA)
        if mario.verificar_colision_enemigo(un_enemigo, PANTALLA):
            # Realizar acciones cuando hay colisión con un_enemigo
            for enemigo in  lista_enemigos:
                if un_enemigo.esta_muerto:
                    lista_enemigos.remove(enemigo)
    
    # Verificar colisión para el segundo enemigo
    if not un_enemigo2.esta_muerto:
        un_enemigo2.actualizar(PANTALLA)
        if mario.verificar_colision_enemigo(un_enemigo2, PANTALLA):
            # Realizar acciones cuando hay colisión con un_enemigo2
            for enemigo2 in  lista_enemigos:
                if un_enemigo2.esta_muerto:
                    lista_enemigos.remove(enemigo2)




  

pygame.quit()
