import pygame
from Constantes import *
from Partida import *
from Menu import *
from Final import *
from Ranking import *
from Ajustes import *
pygame.init()

pygame.display.set_caption("2° parcial - Pygame: Preguntados")

datos_juego = {
    "puntuacion": 0,
    "vidas": CANTIDAD_VIDAS,
    "nombre": "",
    "fecha_actual": None, 
    "comodines": {
        "bomba": True,
        "saltar_turno": True,
        "X2": True,
        "doble_intento": True
    },
    "bandera": {
        "doble_intento": False,
        "X2": False,
        "bomba": False
    },
    "indice": 0,
    "tiempo_restante": 20,
    "respuestas_eliminadas": [],
    "bandera_respuesta": False,
    "contador_aciertos": 0,
    "bandera_nombre_error": False,
    "bandera_mutear_musica": False,
    "volumen_musica": 100,
    "volumen_actual_musica": 100,
    "bandera_mutear_sfx": False,
    "volumen_sfx": 100,
    "volumen_actual_sfx": 100
    }

pantalla = pygame.display.set_mode(VENTANA)
reloj = pygame.time.Clock()
corriendo = True
ventana_actual = "menu"
bandera_juego = False

lista_ranking = []

while corriendo == True:
    reloj.tick(FPS)
    cola_eventos = pygame.event.get()
    
    if ventana_actual == "menu":
        ventana_actual = mostrar_menu(pantalla, cola_eventos, datos_juego)
    elif ventana_actual == "salir":
        corriendo = False
    elif ventana_actual == "ranking":
        ordenar_mayor_a_menor(lista_ranking)
        ventana_actual = mostrar_ranking(pantalla, lista_ranking, cola_eventos, lista_posiciones, datos_juego)
    elif ventana_actual == "ajustes":
        ventana_actual = mostrar_ajustes(pantalla, cola_eventos, datos_juego)
    elif ventana_actual == "jugar":
        pygame.init()
        if bandera_juego == False:
            pygame.mixer.init()
            mezclar_lista(lista_preguntas)
            pygame.mixer.music.load("SEGUNDO PARCIAL - PYGAME\musica y sonidos\Starship Showdown.mp3")
            porcentaje_musica = datos_juego["volumen_musica"] / 100
            pygame.mixer.music.set_volume(porcentaje_musica)
            pygame.mixer.music.play(-1)
            bandera_juego = True
        ventana_actual = mostrar_partida(pantalla, cola_eventos, datos_juego, lista_preguntas)
    elif ventana_actual == "terminado":
        bandera = False
        ventana_actual = mostrar_pantalla_nombre(pantalla, datos_juego, cola_eventos, lista_ranking)
    elif ventana_actual == "reiniciar":
        reiniciar_valores(datos_juego)
        
        bandera_juego = False
        ventana_actual = "menu"
    
    pygame.display.flip()
pygame.quit()