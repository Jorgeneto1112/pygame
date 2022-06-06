
import pygame
import random

pygame.init()
pygame.mixer.init()


WIDTH = 800
HEIGHT = 800
janela = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Goiânia Run')


FPS = 30
altura= 100
largura= 80
paltura = 110
plargura = 70
score=0
fundo=pygame.image.load('imagens/grama.jpg').convert()
gasolina=pygame.image.load('imagens/gaso.png').convert_alpha()
gasolina = pygame.transform.scale(gasolina, (50,40))
def load_assets():
    assets = {}
    assets['chao'] = pygame.image.load('imagens/grama.jpg').convert_alpha()
    assets['chao'] = pygame.transform.scale(assets['chao'], (WIDTH,HEIGHT))
    assets['cachorro'] = pygame.image.load('imagens/cachorro.png').convert_alpha()
    assets['cachorro'] = pygame.transform.scale(assets['cachorro'], (largura, altura))
    assets['boi'] = pygame.image.load('imagens/boi.png').convert_alpha()
    assets['boi'] = pygame.transform.scale(assets['boi'], (largura, altura))
    assets['galinha'] = pygame.image.load('imagens/galinha.png').convert_alpha()
    assets['galinha'] = pygame.transform.scale(assets['galinha'], (largura, altura))
    assets['cavalo'] = pygame.image.load('imagens/cavalo.png').convert_alpha()
    assets['cavalo'] = pygame.transform.scale(assets['cavalo'], (largura,altura))
    assets['trator'] = pygame.image.load('imagens/trator.png').convert_alpha()
    assets['trator'] = pygame.transform.scale(assets['trator'], (plargura, paltura))
    morte_ani = []
    for i in range(5):

        filename = 'imagens/caveira{}.jpg'.format(i)
        img = pygame.image.load(filename).convert()
        img = pygame.transform.scale(img, (32, 32))
        morte_ani.append(img)
    assets["caveira"] = morte_ani
    assets["fonte"] = pygame.font.Font('PressStart2P.ttf', 28)

    pygame.mixer.music.load('audio/dudu.mp3')
    pygame.mixer.music.set_volume(0.4)
    assets['grito'] = pygame.mixer.Sound('audio/animal.mp3')
    return assets

class trator(pygame.sprite.Sprite):
    def __init__(self, groups, assets):

        pygame.sprite.Sprite.__init__(self)

        self.image = assets['trator']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0
        self.speedy = 0
        self.groups = groups
        self.assets = assets

    def update(self):

        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.top < 0:
            self.rect.top = 0
class chao1(pygame.sprite.Sprite):
    def __init__(self, assets):

        pygame.sprite.Sprite.__init__(self)

        self.image = assets['chao']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = -800
        self.speedx = 0
        self.speedy=4

    def update(self):

        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH:
            self.rect.x = 0
            self.rect.y = -770
            self.speedx = 0
            
            self.speedy = 4

class chao(pygame.sprite.Sprite):
    def __init__(self, assets):

        pygame.sprite.Sprite.__init__(self)

        self.image = assets['chao']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.speedx = 0
        self.speedy = 4

    def update(self):

        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH:
            self.rect.x = 0
            self.rect.y = -770
            self.speedx = 0
            
            self.speedy = 4



class cachorro(pygame.sprite.Sprite):
    def __init__(self, assets):

        pygame.sprite.Sprite.__init__(self)

        self.image = assets['cachorro']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH-largura)
        self.rect.y = random.randint(-100, -altura)
        self.speedx = 0
        self.speedy = random.randint(2, 9)

    def update(self):

        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH:
            self.rect.x = random.randint(0, WIDTH-largura)
            self.rect.y = random.randint(-100, -altura)
            self.speedx = 0
            self.speedy = random.randint(2, 9)

class boi(pygame.sprite.Sprite):
    def __init__(self, assets):

        pygame.sprite.Sprite.__init__(self)

        self.image = assets['boi']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH-largura)
        self.rect.y = random.randint(-100, -altura)
        self.speedx = 0
        self.speedy = random.randint(2, 9)

    def update(self):

        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH:
            self.rect.x = random.randint(0, WIDTH-largura)
            self.rect.y = random.randint(-100, -altura)
            self.speedx = 0
            self.speedy = random.randint(2, 9)

class galinha(pygame.sprite.Sprite):
    def __init__(self, assets):

        pygame.sprite.Sprite.__init__(self)

        self.image = assets['galinha']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH-largura)
        self.rect.y = random.randint(-100, -altura)
        self.speedx = 0
        self.speedy = random.randint(2, 9)

    def update(self):

        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH:
            self.rect.x = random.randint(0, WIDTH-largura)
            self.rect.y = random.randint(-100, -altura)
            self.speedx = 0
            self.speedy = random.randint(2, 9)

class cavalo(pygame.sprite.Sprite):
    def __init__(self, assets):

        pygame.sprite.Sprite.__init__(self)

        self.image = assets['cavalo']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH-largura)
        self.rect.y = random.randint(-100, -altura)
        self.speedx = 0
        self.speedy = random.randint(2, 9)

    def update(self):

        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH:
            self.rect.x = random.randint(0, WIDTH-largura)
            self.rect.y = random.randint(-100, -altura)
            self.speedx = 0
            self.speedy = random.randint(2, 9)



class Explosao(pygame.sprite.Sprite):


    def __init__(self, center, assets):

        pygame.sprite.Sprite.__init__(self)


        self.morte_ani = assets['caveira']


        self.frame = 0  
        self.image = self.morte_ani[self.frame] 
        self.rect = self.image.get_rect()
        self.rect.center = center

        self.last_update = pygame.time.get_ticks()

        self.frame_ticks = 50

    def update(self):

        now = pygame.time.get_ticks()

        elapsed_ticks = now - self.last_update


        if elapsed_ticks > self.frame_ticks:

            self.last_update = now

            self.frame += 1


            if self.frame == len(self.morte_ani):

                self.kill()
            else:

                center = self.rect.center
                self.image = self.morte_ani[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center

def game_screen(window):
    clock = pygame.time.Clock()

    assets = load_assets()


    all_sprites = pygame.sprite.Group()
    all_cachorros = pygame.sprite.Group()
    all_cavalos = pygame.sprite.Group()
    all_galinhas = pygame.sprite.Group()
    all_bois = pygame.sprite.Group()
    groups = {}
    groups['all_sprites'] = all_sprites
    groups['all_cachorros'] = all_cachorros
    groups['all_cavalos'] = all_cavalos
    groups['all_galinhas'] = all_galinhas
    groups['boi'] = all_bois

   
    
    Chao=chao(assets)
    all_sprites.add(Chao)
    Chao1=chao1(assets)
    all_sprites.add(Chao1)
    player = trator(groups, assets)
    all_sprites.add(player)
   
    for i in range(2):
        cachorros = cachorro(assets)
        cavalos= cavalo(assets)
        galinhas=galinha(assets)
        bois=boi(assets)
        all_sprites.add(bois)
        all_sprites.add(cachorros)
        all_sprites.add(galinhas)
        all_sprites.add(cavalos)
        all_cachorros.add(cachorros)
        all_cavalos.add(cavalos)
        all_galinhas.add(galinhas)
        all_bois.add(bois)

    DONE = 0
    PLAYING = 1
    morrendo = 2
    state = PLAYING

    keys_down = {}
    score = 0
    lives = 30


    pygame.mixer.music.play(loops=-1)
    while state != DONE:
        clock.tick(FPS)

     
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                state = DONE
            
            if state == PLAYING:
                
                if event.type == pygame.KEYDOWN:
                   
                    keys_down[event.key] = True
                    if event.key == pygame.K_LEFT:
                        player.speedx -= 8
                    if event.key == pygame.K_RIGHT:
                        player.speedx += 8
                    if event.key == pygame.K_UP:
                        player.speedy -= 8
                    if event.key == pygame.K_DOWN:
                        player.speedy += 8
               
                if event.type == pygame.KEYUP:
                   
                    if event.key in keys_down and keys_down[event.key]:
                        if event.key == pygame.K_LEFT:
                            player.speedx += 8
                        if event.key == pygame.K_RIGHT:
                            player.speedx -= 8
                        if event.key == pygame.K_UP:
                            player.speedy += 8
                        if event.key == pygame.K_DOWN:
                            player.speedy -= 8
               
                        


        all_sprites.update()

        if state == PLAYING:
            score += 1

        
            

            hits = pygame.sprite.spritecollide(player, all_cachorros, True, pygame.sprite.collide_mask)
            hits1 = pygame.sprite.spritecollide(player, all_cavalos, True, pygame.sprite.collide_mask)
            hits2 = pygame.sprite.spritecollide(player, all_galinhas, True, pygame.sprite.collide_mask)
            hits3 = pygame.sprite.spritecollide(player, all_bois, True, pygame.sprite.collide_mask)
            if len(hits) > 0:

                assets['grito'].play()
                player.kill()
                lives -= 1
                morte = Explosao(player.rect.center, assets)
                all_sprites.add(morte)
                cachorros=cachorro(assets)
                all_sprites.add(cachorros)
                all_cachorros.add(cachorros)
                state = morrendo
                keys_down = {}
                morte_tick = pygame.time.get_ticks()
                morte_duration = morte.frame_ticks * len(morte.morte_ani) + 400
            if  len(hits1) > 0:

                assets['grito'].play()
                player.kill()
                lives -= 1
                morte = Explosao(player.rect.center, assets)
                all_sprites.add(morte)
                cavalos=cavalo(assets)
                all_sprites.add(cavalos)
                all_cavalos.add(cavalos)
                state = morrendo
                keys_down = {}
                morte_tick = pygame.time.get_ticks()
                morte_duration = morte.frame_ticks * len(morte.morte_ani) + 400
        elif state == morrendo:
            now = pygame.time.get_ticks()
            if now - morte_tick > morte_duration:
                if lives == 0:
                    state = DONE
                else:
                    state = PLAYING
                    player = trator(groups, assets)
                    all_sprites.add(player)


        janela.fill((0, 0, 0)) 
        janela.blit(fundo, (0, 0))

        all_sprites.draw(janela)


        text_surface = assets['fonte'].render("{:08d}".format(score), True, (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.midtop = (WIDTH / 2,  10)
        janela.blit(text_surface, text_rect)

  
        
        if lives==3:
            janela.blit(gasolina, (10, HEIGHT - 50)) 
            janela.blit(gasolina, (50, HEIGHT - 50))
            janela.blit(gasolina, (90, HEIGHT - 50))
        if lives==2:
            janela.blit(gasolina, (10, HEIGHT - 50))
            janela.blit(gasolina, (50, HEIGHT - 50))
        if lives==1:
            janela.blit(gasolina, (10, HEIGHT - 50))

            

        pygame.display.update() 

game_screen(janela)

pygame.quit()  