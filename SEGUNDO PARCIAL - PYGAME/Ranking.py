import pygame
from Constantes import *
from Funciones import *
pygame.init()
 
fondo_pantalla = pygame.transform.scale(pygame.image.load(r"SEGUNDO PARCIAL - PYGAME\texturas\textura_2.jpg"), VENTANA)

lista_texturas = [r"SEGUNDO PARCIAL - PYGAME\texturas\Medalla_1.png", r"SEGUNDO PARCIAL - PYGAME\texturas\Medalla_2.png", r"SEGUNDO PARCIAL - PYGAME\texturas\Medalla_3.png"]

cuadrado_general_ranking = crear_elemento_juego_textura(r"SEGUNDO PARCIAL - PYGAME\texturas\Cuadrado_ranking.png", 370, 477, 65, 8)
lista_posiciones = crear_lista_ranking(r"SEGUNDO PARCIAL - PYGAME\texturas\Superficie_posiciones.png", 320, 38, 90, 42)
boton_atras = crear_elemento_juego((65, 73, 120), 20, 20, 410, 13)
lista_medallas = crear_lista_medallas(lista_texturas, 35, 35, 93, 42)

FUENTE_DATOS = pygame.font.SysFont("Arial Narrow", 18)

def mostrar_ranking(pantalla: pygame.Surface, lista_ranking: list, cola_eventos: list[pygame.event.Event], lista_posiciones: list, datos_juego: dict) -> str:
    """Muestra en pantalla el ranking de los jugadores con sus nombres, puntajes y fechas. También permite volver al menú principal mediante un botón.

    Parámetros:
        pantalla (pygame.Surface): Superficie principal donde se dibuja el ranking.
        lista_ranking (list): Lista de diccionarios que contiene los datos del ranking (nombre, puntuación, fecha).
        cola_eventos (list[pygame.event.Event]): Lista de eventos capturados (ej: clics del mouse, cerrar ventana).
        lista_posiciones (list): Lista de elementos visuales donde se dibujarán las posiciones del ranking.

    Retorna:
        str: Estado posterior a la visualización:
            - "ranking": si no hubo interacción del usuario.
            - "menu": si el usuario hace clic en el botón de volver.
            - "salir": si se cierra la ventana del juego.
    """
    retorno = "ranking"

    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            retorno = "salir"
        elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            if boton_atras['rectangulo'].collidepoint(evento.pos):
                activar_sonido(SONIDO_BOTON, datos_juego['volumen_sfx'], datos_juego['bandera_mutear_sfx'])
                retorno = "menu"

    pantalla.blit(fondo_pantalla,(0,0))
    dibujar_elemento(pantalla, cuadrado_general_ranking)
    dibujar_lista_ranking(pantalla, lista_ranking, lista_posiciones, lista_medallas)

    for i in range(len(lista_ranking)):
        if i < 10:
            mostrar_texto(lista_posiciones[i]["superficie"], f"{lista_ranking[i]["nombre"]}", (45,2), FUENTE_TEXTO, (196, 123, 46))
            mostrar_texto(lista_posiciones[i]["superficie"], f"Fecha: {lista_ranking[i]["fecha"]}  |  Puntos: {lista_ranking[i]["puntuacion"]}", (45, 22), FUENTE_DATOS, (252, 232, 173))

    for i in range(len(lista_posiciones)):
        distancia_x = 15

        if i > 8:
            distancia_x = 10

        if i > 2:
            mostrar_texto(lista_posiciones[i]["superficie"], f"{i + 1}", (distancia_x,10), FUENTE_TEXTO, (193, 208, 236))
            
    mostrar_texto(boton_atras['superficie'], "<", (5,0), FUENTE_TEXTO, (152, 162, 219))
    dibujar_elemento(pantalla, boton_atras)

    if retorno != "ranking":
        reiniciar_ranking(lista_posiciones)

    return retorno

