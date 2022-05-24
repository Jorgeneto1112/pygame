import pygame

pygame.init()
WIDTH = 700
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Hello World!')

game = True

grama = pygame.image.load('grama 2.webp').convert()
grama = pygame.transform.scale(grama, (WIDTH, HEIGHT))

while game:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            game = False

    window.fill((0, 0, 0))  
    window.blit(grama, (0, 0))
    
    pygame.display.update() 

pygame.quit()