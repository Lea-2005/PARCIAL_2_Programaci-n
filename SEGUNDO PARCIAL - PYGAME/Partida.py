import pygame
from Constantes import *
from Funciones import *

pygame.init()
 
lista_preguntas = []

leer_csv_preguntas(r"SEGUNDO PARCIAL - PYGAME\prueba_2.csv", lista_preguntas)

fondo_pantalla = pygame.transform.scale(pygame.image.load(r"SEGUNDO PARCIAL - PYGAME\texturas\textura_fondo.jpg"), VENTANA)

comodin_logos = [r"SEGUNDO PARCIAL - PYGAME\texturas\Comodin_bomba.png", r"SEGUNDO PARCIAL - PYGAME\texturas\Comodin_saltar_turno.png", r"SEGUNDO PARCIAL - PYGAME\texturas\Comodin_X2.png", r"SEGUNDO PARCIAL - PYGAME\texturas\Comodin_doble_chance.png"]

def crear_lista_comodines(lista_texturas: list, ancho: int, alto: int, pos_x: int, pos_y: int)-> list:
    """Crea una lista de 4 comodines con posiciones horizontales desplazadas.

    Parámetros:
        lista_texturas (list): Lista con las texturas de cada comodín.
        ancho (int): Ancho de cada comodín.
        alto (int): Alto de cada comodín.
        pos_x (int): Posición X inicial.
        pos_y (int): Posición Y fija para todos.

    Retorna:
        list: Lista de 4 comodines (diccionarios).
    """
    lista_comodines = []

    for i in range(4):
        comodin = crear_elemento_juego_textura(lista_texturas[i], ancho, alto, pos_x, pos_y)
    
        lista_comodines.append(comodin)

        pos_x += 74

    return lista_comodines
lista_respuestas = crear_lista_respuestas(BLANCO, 300, 40, 100, 240)
lista_comodines = crear_lista_comodines(comodin_logos, 40, 40, 120, 440)
cuadrado_general = crear_elemento_juego(GRIS, 370, 480, 65, 10)
cuadrado_pregunta = crear_elemento_juego(BLANCO, 320, 180, 90, 45)
cuadrado_superior = crear_elemento_juego(AZUL_ULTRAMAR, 370, 35, 65, 10)

evento_tiempo = pygame.USEREVENT 
pygame.time.set_timer(evento_tiempo,1000)

def mostrar_partida(pantalla: pygame.surface, cola_eventos: list[pygame.event.Event], datos_juego: dict, lista_preguntas: list) -> str:
    """Muestra la interfaz principal de la partida, actualiza el estado del juego según los eventos
    y gestiona la lógica de respuesta, uso de comodines y condiciones de fin de juego.

    Parámetros:
        pantalla (pygame.Surface): Superficie principal donde se dibuja la partida.
        cola_eventos (list[pygame.event.Event]): Lista de eventos capturados por pygame (clicks, tiempo, etc.).
        datos_juego (dict): Diccionario con el estado actual del juego (vidas, puntuación, comodines, etc.).
        lista_preguntas (list): Lista de preguntas del juego, cada una como un diccionario.

    Retorna:
        str: Estado de la partida. Puede ser:
            - "jugar": si la partida continúa normalmente.
            - "terminado": si el jugador pierde todas las vidas o se queda sin tiempo.
            - "salir": si se cierra la ventana.
    """
    retorno = "jugar"
    pregunta_actual = lista_preguntas[datos_juego['indice']]
    
    if datos_juego['vidas'] < 1 or datos_juego['tiempo_restante'] < 1:
        pygame.mixer.music.stop()
        activar_sonido(SONIDO_PERDER, datos_juego['volumen_sfx'], datos_juego['bandera_mutear_sfx'])
        pygame.time.delay(800)
        retorno = "terminado"
    elif datos_juego['contador_aciertos'] == 5:
        datos_juego['vidas'] += 1
        datos_juego['contador_aciertos'] = 0

    if datos_juego['bandera_respuesta'] == True:
    
        actualizar_cuadro_partida(cuadrado_general, cuadrado_pregunta, lista_respuestas)
        pygame.time.delay(500)
        datos_juego['bandera_respuesta'] = False
        
    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            retorno = "salir"
        elif evento.type == evento_tiempo:
            datos_juego['tiempo_restante'] -= 1
        
        elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1 and datos_juego['bandera_respuesta'] == False:
            respuesta_click = detectar_click(lista_respuestas, evento.pos)
            comodin_click = detectar_click(lista_comodines, evento.pos)

            if respuesta_click != None and respuesta_click not in datos_juego['respuestas_eliminadas']:
                if verificar_respuesta(datos_juego, pregunta_actual, respuesta_click) == True:
                    activar_sonido(SONIDO_CORRECTA, datos_juego['volumen_sfx'], datos_juego['bandera_mutear_sfx'])
                    datos_juego['contador_aciertos'] += 1
                    lista_respuestas[respuesta_click]['superficie'].fill(VERDE)

                    datos_juego['bandera']['doble_intento'] = False
                    datos_juego['bandera']['bomba'] = False
                    datos_juego['respuestas_eliminadas'] = []

                    datos_juego['indice'] += 1 
                    datos_juego['tiempo_restante'] = 20
                else:
                    activar_sonido(SONIDO_INCORRECTA, datos_juego['volumen_sfx'], datos_juego['bandera_mutear_sfx'])
                    datos_juego['contador_aciertos'] = 0
                    lista_respuestas[respuesta_click]['superficie'].fill(ROJO)

                    if datos_juego['bandera']['doble_intento'] == True:
                        datos_juego['bandera']['doble_intento'] = False
                    else:
                        datos_juego['bandera']['bomba'] = False
                        datos_juego['respuestas_eliminadas'] = []

                        datos_juego['indice'] += 1
                        datos_juego['tiempo_restante'] = 20

                mostrar_texto(lista_respuestas[respuesta_click]['superficie'], pregunta_actual[f"respuesta_{respuesta_click + 1}"], (10, 10), FUENTE_TEXTO, BLANCO)
                datos_juego['bandera_respuesta'] = True
                
                if datos_juego['indice'] == len(lista_preguntas):
                        datos_juego['indice'] = 0
                        mezclar_lista(lista_preguntas)
            elif comodin_click != None:
                aplicar_comodin(comodin_click, datos_juego, pregunta_actual)
    pantalla.blit(fondo_pantalla,(0,0))
    dibujar_elemento(pantalla, cuadrado_general)
    dibujar_elemento(pantalla, cuadrado_pregunta)
    dibujar_elemento(pantalla, cuadrado_superior)

    dibujar_elemento_lista(pantalla, lista_respuestas)
    dibujar_elemento_lista(pantalla, lista_comodines)
    
    for i in datos_juego['respuestas_eliminadas']:
            lista_respuestas[i]['superficie'].fill(GRIS_OSCURO)

    for i in range(4):
            mostrar_texto(lista_respuestas[i]['superficie'], pregunta_actual[f"respuesta_{i + 1}"], (10, 10), FUENTE_TEXTO, NEGRO)
    
    cuadrado_superior["superficie"].fill(AZUL_ULTRAMAR)
    mostrar_texto(cuadrado_pregunta['superficie'], pregunta_actual['pregunta'], (10, 30), FUENTE_PREGUNTA, NEGRO)
    mostrar_texto(cuadrado_superior['superficie'], f"VIDAS: {datos_juego['vidas']}",(10, 10), FUENTE_TEXTO, BLANCO)
    mostrar_texto(cuadrado_superior['superficie'], f" | PUNTUACION: {datos_juego['puntuacion']}",(80, 10),FUENTE_TEXTO, BLANCO)
    mostrar_texto(cuadrado_superior['superficie'], f" | Tiempo: {datos_juego['tiempo_restante']}", (255, 10), FUENTE_TEXTO, BLANCO)
    if retorno == "terminado":
        actualizar_cuadro_partida(cuadrado_general, cuadrado_pregunta, lista_respuestas)

    return retorno
