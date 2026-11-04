import pygame

pygame.init()
pantalla = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Mi proyecto")
reloj = pygame.time.Clock()

corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    pantalla.fill((30, 30, 40))
    pygame.display.flip()
    reloj.tick(60)

pygame.quit()