import pygame

pygame.init()
WIDTH = 550
HEIGHT = 650
tamanhotx = 100
tamanhoty = 110
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Hello World!')
game = True
grama = pygame.image.load('pygame/imagens/grama.webp').convert()
grama = pygame.transform.scale(grama, (WIDTH, HEIGHT))
trator = pygame.image.load('pygame/imagens/trator_cima.png').convert_alpha()
trator = pygame.transform.scale(trator, (tamanhotx, tamanhoty))
pedra = pygame.image.load('pygame/imagens/boi.png').convert_alpha()
pedra = pygame.transform.scale(pedra, (130, 100))

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