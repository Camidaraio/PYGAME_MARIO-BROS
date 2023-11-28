import pygame, sys, random
from class_personaje import *
from class_enemigo import *
from configuraciones import *
from pygame.locals import *
from modo import *
from datetime import datetime
from dona import Objeto

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
diccionario_animaciones_enemigo = {"derecha" : enemigo_derecha, "aplastado": enemigo_aplastado, "izquierda":enemigo_izquierda}
un_enemigo = Enemigo(diccionario_animaciones_enemigo)
d = {"aplasta": diccionario_animaciones_enemigo["aplastado"]}
reescalar_imagenes(d, (55, 25))

un_enemigo.rectangulo.bottom = piso["rectangulo"].top

########## ENEMIGO2 ###########
diccionario_animaciones_enemigo2 = {"derecha" : enemigo_derecha, "aplastado": enemigo_aplastado, "izquierda":enemigo_izquierda}
un_enemigo2 = Enemigo(diccionario_animaciones_enemigo2)
d2 = {"aplasta": diccionario_animaciones_enemigo["aplastado"]}
reescalar_imagenes(d2, (100, 25))

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


### SCORE ####


# Inicialización de la puntuación

factor_de_conversion = 1  # Ajusta según la velocidad deseada
tiempo_inicial = datetime.now()
puntuacion = 0

# Crear el objeto de texto fuera del bucle
font = pygame.font.Font(None, 36)

# CREACIN DE ELEMENTOS
timer = pygame.USEREVENT + 0
pygame.time.set_timer(timer,100)

# CREACIN DE ELEMENTOS
timer = pygame.USEREVENT + 0
pygame.time.set_timer(timer, 100)

# CREACIN DE ELEMENTOS
player = mario
lista_donas = [Objeto(random.randrange(0, 740, 60), random.randrange(-1000, 0, 60)) for _ in range(20)]
# max_donas = 5
donas_creadas = 0



while bandera:
    RELOJ.tick(FPS)
    for evento in pygame.event.get():
        if evento.type == QUIT:
            bandera = False
        elif evento.type == KEYDOWN:
            if evento.key == pygame.K_TAB:
                cambiar_modo()
        elif evento.type == MOUSEBUTTONDOWN:
            print(evento.pos)

    

    pygame.display.update()


    
    ####################


    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_RIGHT]:
        mario.que_hace = "derecha"
        flag_disparo = True

    elif teclas[pygame.K_LEFT]:
        mario.que_hace = "izquierda"
        flag_disparo = True

    elif teclas[pygame.K_UP]:
        mario.que_hace = "salta"
        flag_disparo = True

    else:
        mario.que_hace = "quieto"
        flag_disparo = True

    #### DISPARO ###########
    if flag_disparo and teclas[pygame.K_w]:
        tiempo_actual= pygame.time.get_ticks()
        if  tiempo_actual - tiempo_ultimo_disparo >= 500:
            mario.lanzar_proyectil()
            flag_disparo = False
            tiempo_ultimo_disparo = tiempo_actual

    for proyectil in mario.lista_proyectiles:
        proyectil.actualizar(PANTALLA)

    # Eliminar proyectiles que salieron de la pantalla
    #mario.lista_proyectiles = [p for p in mario.lista_proyectiles if 0 < p.rectangulo.centerx < ANCHO]

    
 


    if mario.esta_muriendo:
        if mario.esta_muriendo:
            print("El personaje ha muerto. El juego se cerrará.")
            pygame.quit()  # Cierra Pygame
            sys.exit()
    
    ### fondo #########

    x_relativa = x % fondo.get_rect().width
    PANTALLA.blit(fondo,(x_relativa - fondo.get_rect().width,0))

    if(x_relativa < ANCHO):
        PANTALLA.blit(fondo,(x_relativa,0))
    x -= 2
    ########

    PANTALLA.blit(fondo, (0,0))

    mario.actualizar(PANTALLA, lista_plataformas)

    
    mario.actualizar_proyectiles(PANTALLA)


    PANTALLA.blit(plataforma_caño["superficie"], plataforma_caño["rectangulo"]) #pasar a clase plataforma
    #PANTALLA.blit(plataforma_invisible["superficie"], plataforma_invisible["rectangulo"]) 
    #PANTALLA.blit(plataforma_invisible1["superficie"], plataforma_invisible1["rectangulo"]) 
    PANTALLA.blit(plataforma_invisible2["superficie"], plataforma_invisible2["rectangulo"]) 
    PANTALLA.blit(plataforma_invisible3["superficie"], plataforma_invisible3["rectangulo"]) 



       # Verificar colisiones de proyectiles con el enemigo
    mario.verificar_colision_proyectil_enemigo(un_enemigo, PANTALLA)
    mario.verificar_colision_proyectil_enemigo(un_enemigo2, PANTALLA)

    # Verificar colisiones del personaje con los enemigos
    #for enemigo in lista_enemigos:
    if not un_enemigo.esta_muerto and not un_enemigo2.esta_muerto :
        un_enemigo.actualizar(PANTALLA, mario)
        un_enemigo2.actualizar(PANTALLA, mario)


        if un_enemigo.esta_muerto:
                lista_enemigos.remove(un_enemigo)
        elif un_enemigo2.esta_muerto:
                lista_enemigos.remove(un_enemigo2)
        if mario.vida <= 0:
        
            # Implementa acciones cuando el personaje se queda sin vida
            bandera = True  # Puedes cambiar esto según tus necesidades

    if not un_enemigo.esta_muerto:
            un_enemigo.actualizar(PANTALLA, mario)
            if mario.verificar_colision_enemigo( un_enemigo, PANTALLA):
                direccion_enemigo = "izquierda"
                        # Realizar acciones cuando hay colisión con un_enemigo

    # Verificar colisión para el segundo enemigo
    if not un_enemigo2.esta_muerto:
        un_enemigo2.actualizar(PANTALLA, mario)
        if mario.verificar_colision_enemigo(un_enemigo2, PANTALLA):
            direccion_enemigo = "izquierda"
            # Realizar acciones cuando hay colisión con un_enemigo2
            
        
     
    ## enemigos disparos ###

    for enemigo in lista_enemigos:
        if not enemigo.esta_muerto:
            enemigo.actualizar(PANTALLA, mario)

        # Verificar si el enemigo ha salido completamente de la pantalla hacia la izquierda
        if enemigo.rectangulo.right < 0:
            # Colocar al enemigo en el lado derecho de la pantalla
            enemigo.rectangulo.x = ANCHO
        elif not enemigo.esta_muerto:
            enemigo.lanzar_proyectil()

            # Actualizar y verificar colisiones de proyectiles de enemigos con el personaje
            for proyectil in enemigo.lista_proyectiles:
                proyectil.actualizar(PANTALLA)
                if proyectil.rectangulo.colliderect(mario.rectangulo):
                    mario.restar_vida()
                    enemigo.lista_proyectiles.remove(proyectil)

    #### DONA ###
     # Actualizar posición de las donas
    for dona in lista_donas:
        dona.update()

    # Verificar colisiones con las donas
    for dona in lista_donas:
        if dona.es_visible() and player.rectangulo.colliderect(dona.dict_dona["rect"]):
            player.aumentar_puntuacion()
            dona.hacer_invisible()
            donas_creadas += 1  

    

    # Dibujar donas visibles
    for dona in lista_donas:
        if dona.es_visible():
            PANTALLA.blit(dona.dict_dona["surface"], dona.dict_dona["rect"])


    ########## ESFERAS ###########
    # Mostrar el puntaje del jugador en la esquina superior derecha
    font = pygame.font.Font(None, 36)
    texto_puntuacion2 = font.render(f"Esferas: {player.score}", True, (0, 0, 0))
    PANTALLA.blit(texto_puntuacion2, (770, 10))

    ### SCORE ####
    tiempo_actual = datetime.now()

    # Calcular la diferencia de tiempo en segundos
    tiempo_transcurrido = (tiempo_actual - tiempo_inicial).total_seconds()

    # Actualizar la puntuación
    puntuacion = int(tiempo_transcurrido * factor_de_conversion)

    # Mostrar la puntuación en la esquina superior izquierda
    font = pygame.font.Font(None, 36)
    texto_puntuacion = font.render(f"Tiempo: {puntuacion}", True, (0, 0, 0))
    PANTALLA.blit(texto_puntuacion, (10, 10))


    #MODO DEBUGw
    if obtener_modo():
        pygame.draw.rect(PANTALLA, "pink", mario.rectangulo, 3)
        for enemigo in lista_enemigos:
            if not un_enemigo.esta_muerto:
                pygame.draw.rect(PANTALLA, "green", un_enemigo.rectangulo, 3)

            if not un_enemigo2.esta_muerto:
                pygame.draw.rect(PANTALLA, "black", un_enemigo2.rectangulo, 3)
                
        for plataforma in  lista_plataformas:
            pygame.draw.rect(PANTALLA, "red", plataforma["rectangulo"], 3)


    pygame.display.update()



pygame.quit()

