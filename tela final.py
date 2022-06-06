
import pygame

pygame.init()
pygame.mixer.init()

WIDTH = 500
HEIGHT = 400
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Trator')

game = True

font = pygame.font.SysFont(None, 60)
text = font.render('Ja era uai', True, (255, 0, 0))
font2 = pygame.font.SysFont(None, 48)
text2 = font2.render('Pressione qualquer tecla', True, (255, 255, 255))
text3 = font2.render('para jogar novamente', True, (255, 255, 255))
image = pygame.image.load('pygame/imagens/trator capotado.webp').convert()
image_menor = pygame.transform.scale(image, (500, 400))

pygame.mixer.music.load('pygame/audio/musica final.mp3')
pygame.mixer.music.set_volume(50)
pygame.mixer.music.play(loops=-1)

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    
    window.fill((0, 0, 0)) 
    window.blit(image_menor, (0, 0))
    window.blit(text, (140, 10))
    window.blit(text2, (40, 320))
    window.blit(text3, (70, 350))
    pygame.display.update()  

pygame.quit() 

