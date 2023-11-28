import pygame

#GIRA IMAGENES 
def girar_imagenes(lista_original, flip_x, flirp_y):
    lista_girada = []

    for imagen in lista_original:
        lista_girada.append(pygame.transform.flip(imagen, flip_x, flirp_y))


    return lista_girada





#MODIFICA TAMAÑO SPRITE
def reescalar_imagenes(diccionario_animaciones, tamaño):
    for clave in diccionario_animaciones:
        for i in range(len(diccionario_animaciones[clave])):
            superficie = diccionario_animaciones[clave][i]
            diccionario_animaciones[clave][i] = pygame.transform.scale(superficie, tamaño)


################################### PERSONAJE ###########################################


personaje_quieto_izquierda = [
                    pygame.image.load(r"personaje\4.png")
                    # pygame.image.load(r"personaje\5.png"),
                    # pygame.image.load(r"personaje\6.png")
                    ]

personaje_quieto = girar_imagenes(personaje_quieto_izquierda, True, False)

personaje_izquierda = [
                    pygame.image.load(r"personaje\4.png"),
                    pygame.image.load(r"personaje\3.png"),
                    pygame.image.load(r"personaje\2.png"),
                    pygame.image.load(r"personaje\1.png"),
                    pygame.image.load(r"personaje\0.png"),

                    ]


personaje_derecha = girar_imagenes(personaje_izquierda, True, False)

personaje_salta = [pygame.image.load(r"personaje\12.png"),
                    
                   ]

################################### ENEMIGO ###########################################

enemigo_camina_izquieda = [pygame.image.load(r"enemigos\5.png")]

enemigo_camina = girar_imagenes(enemigo_camina_izquieda, True, False)

enemigo_izquierda = [pygame.image.load(r"enemigos\0.png"),
                     pygame.image.load(r"enemigos\1.png"),
                     pygame.image.load(r"enemigos\2.png"),
                     pygame.image.load(r"enemigos\3.png")]

enemigo_derecha = girar_imagenes(enemigo_izquierda, True, False)

enemigo_aplastado = girar_imagenes(enemigo_izquierda, True, False)


################################### ENEMIGO2 ###########################################

# enemigo_camina_izquieda2 = [pygame.image.load(r"enemigos\5.png")]

# enemigo_camina2 = girar_imagenes(enemigo_camina_izquieda2, True, False)

# enemigo_izquierda2 = [pygame.image.load(r"enemigos\0.png"),
#                      pygame.image.load(r"enemigos\1.png"),
#                      pygame.image.load(r"enemigos\2.png"),
#                      pygame.image.load(r"enemigos\3.png")]

# enemigo_derecha2 = girar_imagenes(enemigo_izquierda2, True, False)

# enemigo_aplastado2 = girar_imagenes(enemigo_izquierda2, True, False)