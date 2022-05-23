import pygame

pygame.init()
WIDTH = 500
HEIGHT = 400
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Hello World!')

game = True

image = pygame.image.load('grama.jpeg').convert()
image = pygame.transform.scale(image, (520, 500))

while game:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            game = False

    window.fill((0, 0, 0))  
    window.blit(image, (-10, 0))

    pygame.display.update() 

pygame.quit()