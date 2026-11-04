
import pygame
import random

pygame.init()

# Crear la ventana del juego.

ventana = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Adivina el numero")

#Creacion de las fuentes del texto  de tipo de tamaño y letra que se esta utilizando.
fuente = pygame.font.SysFont(None, 35)
fuente_pequena = pygame.font.SysFont(None, 28)

# Inicializacion de las avariables y su creacion y la creacion del menasje mostradon junto con hasta el limite del numero random de nuestra adivinanza
numero = random.randint(1, 20)
respuesta = ""
mensaje = "Adivina un numero del 1 al 20"

intentos = 0
max_intentos = 5
terminado = False
ejecutando = True

# bucle del codigo con las condicones for y if 
while ejecutando:
    
            # Detectar los eventos
    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            ejecutando = False

            # Detecta las teclas presionadas
        if evento.type == pygame.KEYDOWN:

            # Salir del juego
            if evento.key == pygame.K_ESCAPE:
                ejecutando = False

            # Volver a jugar con la tecla R
            elif evento.key == pygame.K_r and terminado:
                numero = random.randint(1, 20)
                respuesta = ""
                intentos = 0
                terminado = False
                mensaje = "Adivina un numero del 1 al 20"

            # Rendirse con la tecla S
            elif evento.key == pygame.K_s and not terminado:
                mensaje = f"Te rendiste. El numero era {numero}"
                terminado = True
                respuesta = ""

            elif not terminado:
                
            # Se encarga de leer y comprobar el numero
                if evento.key == pygame.K_RETURN:

                    if respuesta.isdigit():

                        intento = int(respuesta)
                        
            # Validar el rango de los numeros randoms con la condicional  If 
                        if intento < 1 or intento > 20:
                            mensaje = "Escribe un numero del 1 al 20"

                        else:
                            intentos += 1

            # Mensaje del resultado obtenido del numero comprobando las respuesta del usuario

                            if intento > numero:
                                mensaje = "El numero es menor"

                            elif intento < numero:
                                mensaje = "El numero es mayor"

                            else:
                                mensaje = "Felicidades! Acertaste"
                                terminado = True

                            # Comprobar si se agotaron los intentos
                            if intentos >= max_intentos and not terminado:
                                mensaje = f"Perdiste! Era el {numero}"
                                terminado = True

                        respuesta = ""

                elif evento.key == pygame.K_BACKSPACE:
                    respuesta = respuesta[:-1]

                elif evento.unicode.isdigit() and len(respuesta) < 2:
                    respuesta += evento.unicode

    # Dibujar la  ventana y los mmensajes principales 
    ventana.fill((255, 255, 255))

    texto = fuente.render(mensaje, True, (0, 0, 0))
    ventana.blit(texto, (30, 90))

    texto = fuente.render(
        "Tu numero: " + respuesta, True, (0, 0, 255)
    )
    ventana.blit(texto, (30, 150))
    
    # Contador de intentos
    texto = fuente_pequena.render(
        f"Intentos: {intentos} de {max_intentos}",
        True, (200, 0, 0)
    )
    ventana.blit(texto, (30, 205))

    # Las indicacinoes segun el estado del jugador si se quiere rendir
    if not terminado:
        texto = fuente_pequena.render(
            "ENTER: Adivinar | S: Rendirse",
            True, (0, 100, 0)
        )
        ventana.blit(texto, (30, 260))
        
    # Muestra la instruccion de salir oh jugar otra vez
    else:
        texto = fuente_pequena.render(
            "R: Jugar otra vez | ESC: Salir",
            True, (0, 0, 150)
        )
        ventana.blit(texto, (30, 260))

    # Salir del juego comple
    texto = fuente_pequena.render(
        "ESC: Salir del juego",
        True, (100, 100, 100)
    )
    ventana.blit(texto, (30, 320))

    pygame.display.flip()

pygame.quit()
