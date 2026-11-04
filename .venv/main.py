
import random
import pygame
# Inicialización y configuración de la ventana
pygame.init()
ANCHO, ALTO = 800, 500
PANTALLA = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("PONG - Proyecto Pygame")
RELOJ = pygame.time.Clock()
# Colores RGB
NEGRO = (15, 18, 28)
BLANCO = (240, 245, 255)
AZUL = (70, 170, 255)
VERDE = (90, 220, 160)
# Fuentes
FUENTE = pygame.font.Font(None, 48)
FUENTE_PEQUENA = pygame.font.Font(None, 28)
# Sprites: paletas y pelota
class Paleta(pygame.sprite.Sprite):
    def __init__(self, x, y, controles):
        super().__init__()
        self.image = pygame.Surface((14, 100))
        self.image.fill(AZUL)
        self.rect = self.image.get_rect(center=(x, y))
        self.controles = controles
        self.velocidad = 6
    def update(self, teclas):
        # Se lee el estado de las teclas cada fotograma
        if teclas[self.controles[0]]:
            self.rect.y -= self.velocidad
        if teclas[self.controles[1]]:
            self.rect.y += self.velocidad
        # Impide que la paleta salga de la ventana
        self.rect.top = max(0, self.rect.top)
        self.rect.bottom = min(ALTO, self.rect.bottom)
# Crea la clase que representa las pelotas e incicalizacion del sprite
class Pelota(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Crea una superficie transparente
        self.image = pygame.Surface((18, 18), pygame.SRCALPHA)
        pygame.draw.circle(self.image, BLANCO, (9, 9), 9) # Dibuja una pelota circular blanca.
        self.rect = self.image.get_rect(center=(ANCHO // 2, ALTO // 2)) # Coloca la pelota en el centro de la ventana.
        self.vx = random.choice((-5, 5))
        self.vy = random.choice((-4, 4))
# Función que devuelve la pelota a su posición inicial y colocacion de la pelota en el centro con las distintas velocidades
    def reiniciar(self):
        self.rect.center = (ANCHO // 2, ALTO // 2)
        self.vx = random.choice((-5, 5))
        self.vy = random.choice((-4, 4))      
# Va actualizando el movimiento de la pelota. Forma horizontal y vertical
    def update(self):
        self.rect.x += self.vx
        self.rect.y += self.vy
# Comprueba si la pelota toca el techo o el suelo.
        if self.rect.top <= 0 or self.rect.bottom >= ALTO:
# Invierte la dirección vertical para provocar el rebote.
            self.vy *= -1 
        # Rebote contra las paletas
        if pygame.sprite.collide_rect(self, jugador1) and self.vx < 0:
            self.vx *= -1
            self.vy += random.choice((-1, 0, 1))
        if pygame.sprite.collide_rect(self, jugador2) and self.vx > 0:
            self.vx *= -1
            self.vy += random.choice((-1, 0, 1))
        # Mantiene una velocidad vertical razonable
        self.vy = max(-7, min(7, self.vy))
# Grupos: permiten actualizar y dibujar varios sprites
jugador1 = Paleta(35, ALTO // 2, (pygame.K_w, pygame.K_s))
jugador2 = Paleta(ANCHO - 35, ALTO // 2,
                  (pygame.K_UP, pygame.K_DOWN))
pelota = Pelota()
todos = pygame.sprite.Group(jugador1, jugador2, pelota)
marcador1 = 0
marcador2 = 0
ejecutando = True
# Game loop de los eventos de actualización y  renderizado
while ejecutando:
    # Limita el juego a 60 fotogramas por segundo
    RELOJ.tick(60)
    # EVENTOS: cerrar ventana o pulsar ESC / R
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                ejecutando = False
            elif evento.key == pygame.K_r:
                marcador1 = marcador2 = 0
                pelota.reiniciar()
    # INPUT y ACTUALIZACIÓN
    teclas = pygame.key.get_pressed()
    jugador1.update(teclas)
    jugador2.update(teclas)
    pelota.update()
    # PUNTUACIÓN: la pelota salió por un lateral
    if pelota.rect.right < 0:
        marcador2 += 1
        pelota.reiniciar()
    elif pelota.rect.left > ANCHO:
        marcador1 += 1
        pelota.reiniciar()
    # RENDERIZADO: limpiar, dibujar y presentar
    PANTALLA.fill(NEGRO)
    pygame.draw.line(PANTALLA, (70, 75, 95),
                     (ANCHO // 2, 0), (ANCHO // 2, ALTO), 2)
    todos.draw(PANTALLA)
# Crea el texto del marcador con los puntos de ambos jugadores.
    texto = FUENTE.render(f"{marcador1}     {marcador2}", True, BLANCO)
# Coloca el marcador en la parte superior central.
    PANTALLA.blit(texto, texto.get_rect(center=(ANCHO // 2, 35)))
# Crea el texto que explica los controles del videojuego.
    ayuda = FUENTE_PEQUENA.render(
        "W/S: izquierda   Flechas: derecha   R: reiniciar   ESC: salir",
        True, VERDE)
    PANTALLA.blit(ayuda, (ANCHO // 2 - ayuda.get_width() // 2, ALTO - 30))
    # flip() presenta el buffer completo ya dibujado
    pygame.display.flip()
pygame.quit()