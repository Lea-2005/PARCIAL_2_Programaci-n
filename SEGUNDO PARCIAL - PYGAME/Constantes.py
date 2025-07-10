import pygame
pygame.init()

BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
AZUL_ULTRAMAR = (65, 102, 245)
NEGRO = (0, 0, 0)
GRIS = (155, 155, 155)
GRIS_OSCURO = (57, 61, 66)
DORADO = (255, 202, 17)
MORADO_OSCURO = (38, 2, 95)
 
CANTIDAD_VIDAS = 3
PUNTUACION_ACIERTO = 100
PUNTUACION_ERROR = 25
TIEMPO_JUEGO = 30

ANCHO = 500
ALTURA = 500 
VENTANA = ANCHO, ALTURA

FUENTE_TEXTO = pygame.font.SysFont("Arial Narrow", 25)
FUENTE_RESPUESTA = pygame.font.SysFont("Arial Narrow", 40)
FUENTE_PREGUNTA = pygame.font.SysFont("Arial Narrow", 35)
FUENTE_MENU = pygame.font.SysFont("Arial Narrow", 45)

SONIDO_CORRECTA = pygame.mixer.Sound("SEGUNDO PARCIAL - PYGAME\musica y sonidos\Respuesa correcta.mp3")
SONIDO_INCORRECTA = pygame.mixer.Sound("SEGUNDO PARCIAL - PYGAME\musica y sonidos\Event negative.mp3")

SONIDO_PERDER = pygame.mixer.Sound("SEGUNDO PARCIAL - PYGAME\musica y sonidos\Perder.mp3")
SONIDO_BOTON = pygame.mixer.Sound("SEGUNDO PARCIAL - PYGAME\musica y sonidos\Boton.mp3")
SONIDO_EXTRA = pygame.mixer.Sound("SEGUNDO PARCIAL - PYGAME\musica y sonidos\Sonido extra.mp3")
SONIDO_COMODIN = pygame.mixer.Sound("SEGUNDO PARCIAL - PYGAME\musica y sonidos\Comodin.mp3")
SONIDO_CLICK = pygame.mixer.Sound("SEGUNDO PARCIAL - PYGAME\musica y sonidos\click_sonido.mp3")

FPS = 60