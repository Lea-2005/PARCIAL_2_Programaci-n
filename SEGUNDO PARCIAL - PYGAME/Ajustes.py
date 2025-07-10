import pygame
from Constantes import *
from Funciones import *
pygame.init()

botones_textura = [r"SEGUNDO PARCIAL - PYGAME\texturas\signo_menos.png", r"SEGUNDO PARCIAL - PYGAME\texturas\signo_mas.png", r"SEGUNDO PARCIAL - PYGAME\texturas\signo_mute.png"]

fondo_pantalla = pygame.transform.scale(pygame.image.load(r"SEGUNDO PARCIAL - PYGAME\texturas\fondo_ajustes.png"), VENTANA)

cuadrado_general = crear_elemento_juego_textura(r"SEGUNDO PARCIAL - PYGAME\texturas\Cuadrado_ajustes.png", 400, 450, 45, 10)
lista_botones_musica = crear_lista_volumen(botones_textura, 30, 30, 80, 106)
lista_botones_sfx = crear_lista_volumen(botones_textura, 30, 30, 80, 205)
cuadrado_volumenes = crear_cuadrados_volumen(r"SEGUNDO PARCIAL - PYGAME\texturas\barra.png", 350, 65, 25, 80)
boton_atras = crear_elemento_juego(BLANCO, 20, 20, 415, 20)
boton_default = crear_elemento_juego_textura(r"SEGUNDO PARCIAL - PYGAME\texturas\Boton_default.png", 80, 30, 340, 335)

textura_control = r"SEGUNDO PARCIAL - PYGAME\texturas\punto_volumen.png"

control_musica = crear_elemento_juego_textura(textura_control, 15, 15, 272, 105)
control_sfx = crear_elemento_juego_textura(textura_control, 15, 15, 272, 201)

def mostrar_ajustes(pantalla: pygame.Surface, cola_eventos: list[pygame.event.Event], datos_juego: dict) -> str:
    retorno = "ajustes"

    if datos_juego['bandera_mutear_musica'] == True:
        datos_juego["volumen_musica"] = 0

    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            retorno = "salir"
        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            if boton_atras['rectangulo'].collidepoint(evento.pos):
                activar_sonido(SONIDO_BOTON, datos_juego['volumen_sfx'], datos_juego['bandera_mutear_sfx'])
                retorno = "menu"
            elif boton_default["rectangulo"].collidepoint(evento.pos):
                activar_sonido(SONIDO_BOTON, datos_juego['volumen_sfx'], datos_juego['bandera_mutear_sfx'])
                restablecer_configuracion_sonido(datos_juego, control_musica, control_sfx)

            boton_click_musica = detectar_click(lista_botones_musica, evento.pos)
            boton_click_sfx = detectar_click(lista_botones_sfx, evento.pos)
            
            if boton_click_musica != None:
                manejar_volumen(boton_click_musica, datos_juego, "musica", control_musica)
            elif boton_click_sfx != None:
                manejar_volumen(boton_click_sfx, datos_juego, "sfx", control_sfx)

    pantalla.blit(fondo_pantalla,(0,0))
    dibujar_elemento(pantalla, cuadrado_general)
    dibujar_elemento_lista(cuadrado_general["superficie"], cuadrado_volumenes)
    dibujar_elemento_lista(pantalla, lista_botones_musica)
    dibujar_elemento_lista(pantalla, lista_botones_sfx)
    dibujar_elemento(pantalla, boton_default)
    dibujar_elemento(cuadrado_general["superficie"], control_musica)
    dibujar_elemento(cuadrado_general["superficie"], control_sfx)
    
    actualizar_texto_volumen(datos_juego, cuadrado_volumenes[0], "musica", r"SEGUNDO PARCIAL - PYGAME\texturas\barra.png")
    actualizar_texto_volumen(datos_juego, cuadrado_volumenes[1], "sfx", r"SEGUNDO PARCIAL - PYGAME\texturas\barra.png")

    mostrar_texto(boton_atras['superficie'], "<", (5,5), FUENTE_TEXTO, ROJO)
    dibujar_elemento(pantalla, boton_atras)

    return retorno
