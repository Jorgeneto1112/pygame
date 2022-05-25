import pygame

pygame.init()
WIDTH = 600
HEIGHT = 600
tamanhotx = 120
tamanhoty = 110
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Hello World!')
game = True
grama = pygame.image.load('grama 2.webp').convert()
grama = pygame.transform.scale(grama, (WIDTH, HEIGHT))
trator = pygame.image.load('trator_cima.png').convert_alpha()
trator = pygame.transform.scale(trator, (tamanhotx, tamanhoty))

while game:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            game = False
    window.fill((0, 0, 0))  
    window.blit(grama, (0, 0))
    window.blit(trator, ((WIDTH/2)-(tamanhotx/2), HEIGHT-tamanhoty))
    
    pygame.display.update() 

pygame.quit()