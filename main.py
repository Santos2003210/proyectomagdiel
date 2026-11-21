import pygame
import random
import sys

#INICIALIZAR PYGAME Y EL SONIDO

pygame.init()
pygame.mixer.init()

# Música de fondo estilo piano
pygame.mixer.music.load("media/piano_10_segundos.wav")
pygame.mixer.music.set_volume(0.6)
pygame.mixer.music.play(-1)

#CONFIGURACION DE LA PANTALLA

ANCHO = 600
ALTO = 400

ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Adivina el numero")

reloj = pygame.time.Clock()

#CARGAR LAS IMAGENES DE FONDO

try:

    imagenes = [
        pygame.transform.scale(
            pygame.image.load("Media/imagenuno.jpg").convert(),
            (ANCHO, ALTO)
        ),

        pygame.transform.scale(
            pygame.image.load("Media/imagendos.jpg").convert(),
            (ANCHO, ALTO)
        ),

        pygame.transform.scale(
            pygame.image.load("Media/imagentres.jpg").convert(),
            (ANCHO, ALTO)
        )
    ]

    print("¡Imagenes cargadas correctamente!")

except (pygame.error, FileNotFoundError) as e:

    imagenes = []
    print(f"Error al cargar las imagenes: {e}")

# CONFIGURACION DE LAS TRANSICIONES
indice_imagen = 0

# Tiempo que permanece cada imagen
tiempo_cambio = 2000

# Duracion del efecto de transicion
duracion_transicion = 800

tiempo_ultimo_cambio = pygame.time.get_ticks()

# Variables para controlar el desvanecimiento
transicion_activa = False
tiempo_inicio_transicion = 0
siguiente_imagen = 0


#CONFIGURACION DE LAS FUENTES

fuente = pygame.font.SysFont(None, 35)
fuente_pequena = pygame.font.SysFont(None, 28)

#VARIABLES DEL JUEGO
numero = random.randint(1, 20)

respuesta = ""
mensaje = "Adivina un numero del 1 al 20"

intentos = 0
max_intentos = 5

terminado = False
ejecutando = True

#BUCLE PRINCIPAL DEL JUEGO

while ejecutando:

    tiempo_actual = pygame.time.get_ticks()

    # TRANSICION AUTOMATICA DE IMAGENES

    if imagenes:

        # Comprobar si ya es momento de cambiar
        if not transicion_activa:

            if tiempo_actual - tiempo_ultimo_cambio >= tiempo_cambio:

                siguiente_imagen = (
                    (indice_imagen + 1) % len(imagenes)
                )

                transicion_activa = True
                tiempo_inicio_transicion = tiempo_actual

        # Mostrar imagen actual
        ventana.blit(imagenes[indice_imagen], (0, 0))

        # Aplicar efecto Fade
        if transicion_activa:

            tiempo_transcurrido = (
                tiempo_actual - tiempo_inicio_transicion
            )

            progreso = min(
                tiempo_transcurrido / duracion_transicion,
                1
            )

            # Crear transparencia de la imagen nueva
            imagen_nueva = imagenes[siguiente_imagen].copy()

            imagen_nueva.set_alpha(int(255 * progreso))

            # Dibujar imagen nueva encima de la anterior
            ventana.blit(imagen_nueva, (0, 0))

            # Finalizar la transicion
            if progreso >= 1:

                indice_imagen = siguiente_imagen

                transicion_activa = False

                tiempo_ultimo_cambio = tiempo_actual

    else:

        # Fondo blanco si no se cargaron las imagenes
        ventana.fill((255, 255, 255))

    
    #DETECTAR LOS EVENTOS DEL TECLADO

    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:

            ejecutando = False

        if evento.type == pygame.KEYDOWN:

            # Salir del juego
            if evento.key == pygame.K_ESCAPE:

                ejecutando = False

            # Volver a jugar con R
            elif evento.key == pygame.K_r and terminado:

                numero = random.randint(1, 20)

                respuesta = ""
                intentos = 0
                terminado = False

                mensaje = "Adivina un numero del 1 al 20"

            # Rendirse con S
            elif evento.key == pygame.K_s and not terminado:

                mensaje = f"Te rendiste. El numero era {numero}"

                terminado = True
                respuesta = ""

            elif not terminado:

                # Comprobar respuesta con ENTER
                if evento.key == pygame.K_RETURN:

                    if respuesta.isdigit():

                        intento = int(respuesta)

                        # Validar rango
                        if intento < 1 or intento > 20:

                            mensaje = "Escribe un numero del 1 al 20"

                        else:

                            intentos += 1

                            # Comprobar el numero
                            if intento > numero:

                                mensaje = "El numero es menor"

                            elif intento < numero:

                                mensaje = "El numero es mayor"

                            else:

                                mensaje = "Felicidades! Acertaste"

                                terminado = True

                            # Comprobar intentos disponibles
                            if intentos >= max_intentos and not terminado:

                                mensaje = f"Perdiste! Era el {numero}"

                                terminado = True

                        respuesta = ""

                # Borrar numero
                elif evento.key == pygame.K_BACKSPACE:

                    respuesta = respuesta[:-1]

                # Escribir numeros
                elif evento.unicode.isdigit() and len(respuesta) < 2:

                    respuesta += evento.unicode

    # 9. MOSTRAR LOS MENSAJES DEL JUEGO

    texto = fuente.render(
        mensaje,
        True,
        (0, 0, 0)
    )

    ventana.blit(texto, (30, 90))

    # Mostrar respuesta
    texto = fuente.render(
        "Tu numero: " + respuesta,
        True,
        (0, 0, 255)
    )

    ventana.blit(texto, (30, 150))

    # Contador de intentos
    texto = fuente_pequena.render(
        f"Intentos: {intentos} de {max_intentos}",
        True,
        (200, 0, 0)
    )

    ventana.blit(texto, (30, 205))

    # Indicaciones del juego
    if not terminado:

        texto = fuente_pequena.render(
            "ENTER: Adivinar | S: Rendirse",
            True,
            (0, 100, 0)
        )

        ventana.blit(texto, (30, 260))

    else:

        texto = fuente_pequena.render(
            "R: Jugar otra vez | ESC: Salir",
            True,
            (0, 0, 150)
        )

        ventana.blit(texto, (30, 260))

    # Instruccion para salir
    texto = fuente_pequena.render(
        "ESC: Salir del juego",
        True,
        (100, 100, 100)
    )

    ventana.blit(texto, (30, 320))

    # 10. ACTUALIZAR LA PANTALLA

    pygame.display.flip()

    # Limitar el juego a 60 FPS
    reloj.tick(60)

pygame.quit()
sys.exit()