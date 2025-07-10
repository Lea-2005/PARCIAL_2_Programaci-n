import pygame
from Constantes import *
from Funciones import *
pygame.init()
 
fondo_pantalla = pygame.transform.scale(pygame.image.load(r"SEGUNDO PARCIAL - PYGAME\texturas\fondo_perder.png"), VENTANA)
boton_texturas = [r"SEGUNDO PARCIAL - PYGAME\texturas\guardar.png", r"SEGUNDO PARCIAL - PYGAME\texturas\no_guardar.png"]
lista_boton = crear_botones_confirmacion(boton_texturas, 108, 44, 98, 422)
puntaje_rectangulo = crear_elemento_juego_textura(r"SEGUNDO PARCIAL - PYGAME\texturas\barra_puntaje.png", 300, 50, 100, 142)
rectangulo_nombre = crear_elemento_juego_textura(r"SEGUNDO PARCIAL - PYGAME\texturas\barra_para_nombre.png", 368, 44, 68, 252)

FUENTE_PUNTOS = pygame.font.SysFont("Arial Narrow", 60)
FUENTE_INFORMACION = pygame.font.SysFont("Arial Narrow", 40)

def mostrar_pantalla_nombre(pantalla: pygame.Surface, datos_juego: dict, cola_eventos: list[pygame.event.Event], lista_ranking: list) -> str:
    pantalla.blit(fondo_pantalla, (0,0))
    retorno = "terminado"

    if datos_juego['bandera_nombre_error'] == True:
        activar_sonido(SONIDO_EXTRA, datos_juego['volumen_sfx'], datos_juego['bandera_mutear_sfx'])
        pygame.time.delay(2000)
        datos_juego['bandera_nombre_error'] = False
        
    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            mostrar_texto(pantalla, "Antes de salir: ¡Guarde su nombre!", (65, 310), FUENTE_TEXTO, DORADO)
            datos_juego['bandera_nombre_error'] = True
        elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            confirmacion_click = detectar_click(lista_boton, evento.pos)

            if confirmacion_click != None:
                activar_sonido(SONIDO_BOTON, datos_juego['volumen_sfx'], datos_juego['bandera_mutear_sfx'])
                if confirmacion_click == 0:
                    if mostrar_mensaje_error(pantalla, datos_juego) == False:
                        guardar_ranking(datos_juego, lista_ranking)
                        generar_json("partidas.json", lista_ranking)
                        retorno = "reiniciar"
                    else:
                        datos_juego['bandera_nombre_error'] = True
                else:
                    retorno = "reiniciar"
        elif evento.type == pygame.KEYDOWN:
            bloc_mayus = pygame.key.get_mods() & pygame.KMOD_CAPS
            letra_presionada = pygame.key.name(evento.key)
        
            if letra_presionada == "backspace" and len(datos_juego['nombre']) >= 1:
                datos_juego["nombre"] = datos_juego["nombre"][:-1]
                actualizar_frame_cuadrado(rectangulo_nombre, r"SEGUNDO PARCIAL - PYGAME\texturas\barra_para_nombre.png")
                
            elif letra_presionada == "space":
                datos_juego['nombre'] += " "
            elif len(letra_presionada) == 1 and len(datos_juego['nombre']) <= 15:
                if bloc_mayus != 0:
                    datos_juego['nombre'] += letra_presionada.upper()
                else:
                    datos_juego['nombre'] += letra_presionada

            elif letra_presionada == "return":
                if mostrar_mensaje_error(pantalla, datos_juego) == False:
                    guardar_ranking(datos_juego, lista_ranking)
                    generar_json("partidas.json", lista_ranking)
                    retorno = "reiniciar"
                else:
                    datos_juego['bandera_nombre_error'] = True
    dibujar_elemento_lista(pantalla, lista_boton)
    dibujar_elemento(pantalla, puntaje_rectangulo)
    mostrar_texto(pantalla, "TOTAL DE PUNTOS:", (110, 110), FUENTE_INFORMACION, MORADO_OSCURO)
    mostrar_texto(pantalla, "ESCRIBA SU NOMBRE:", (100, 220), FUENTE_INFORMACION, MORADO_OSCURO)
    mostrar_texto(pantalla, "¿Quieres guardar en el ranking?", (100, 330), FUENTE_TEXTO, DORADO)
    mostrar_texto(puntaje_rectangulo['superficie'], f"{datos_juego['puntuacion']}", (50, 10), FUENTE_PUNTOS, NEGRO)
    mostrar_texto(rectangulo_nombre['superficie'], f"{datos_juego['nombre']}", (30, 15), FUENTE_TEXTO, BLANCO)
    dibujar_elemento(pantalla, rectangulo_nombre)

    if retorno != "terminado":
        actualizar_frame_cuadrado(puntaje_rectangulo, r"SEGUNDO PARCIAL - PYGAME\texturas\barra_puntaje.png")
        actualizar_frame_cuadrado(rectangulo_nombre, r"SEGUNDO PARCIAL - PYGAME\texturas\barra_para_nombre.png")
        datos_juego['bandera_nombre_error'] = False

    return retorno