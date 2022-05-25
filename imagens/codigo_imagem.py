import pygame

pygame.init()
WIDTH = 600
HEIGHT = 600
tamanhotx = 120
tamanhoty = 110
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Hello World!')
game = True
grama = pygame.image.load('grama.webp').convert()
grama = pygame.transform.scale(grama, (WIDTH, HEIGHT))
trator = pygame.image.load('trator_cima.png').convert_alpha()
trator = pygame.transform.scale(trator, (tamanhotx, tamanhoty))
pedra = pygame.image.load('pedra.png').convert_alpha()
pedra = pygame.transform.scale(pedra, (130, 90))

while game:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            game = False
    window.fill((0, 0, 0))  
    window.blit(grama, (0, 0))
    window.blit(trator, ((WIDTH/2)-(tamanhotx/2), HEIGHT-tamanhoty))
    window.blit(pedra, (0, 0))
    
    pygame.display.update() 

pygame.quit()