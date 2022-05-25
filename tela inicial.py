
import pygame

pygame.init()


WIDTH = 500
HEIGHT = 400
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Trator')

game = True

font = pygame.font.SysFont(None, 60)
text = font.render('Goiania Run', True, (255, 0, 0))
font2 = pygame.font.SysFont(None, 48)
text2 = font2.render('Pressione qualquer tecla', True, (255, 255, 255))
text3 = font2.render('para iniciar o jogo', True, (255, 255, 255))
image = pygame.image.load('assets/img/trator pro jogo.jpg').convert()
image_menor = pygame.transform.scale(image, (500, 400))

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    
    window.fill((0, 0, 0)) 
    window.blit(image_menor, (0, 0))
    window.blit(text, (120, 20))
    window.blit(text2, (40, 300))
    window.blit(text3, (100, 330))
    pygame.display.update()  

pygame.quit() 

