import pygame
import random

pygame.init()
pygame.mixer.init()


WIDTH = 900
HEIGHT = 700
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
    assets['chao'] = pygame.image.load('imagens/terra1.png').convert_alpha()
    assets['chao'] = pygame.transform.scale(assets['chao'], (WIDTH,2000))
    assets['cachorro'] = pygame.image.load('imagens/cachorro.png').convert_alpha()
    assets['cachorro'] = pygame.transform.scale(assets['cachorro'], (largura, altura))
    assets['boi'] = pygame.image.load('imagens/boi.png').convert_alpha()
    assets['boi'] = pygame.transform.scale(assets['boi'], (largura, altura))
    assets['galinha'] = pygame.image.load('imagens/galinha.png').convert_alpha()
    assets['galinha'] = pygame.transform.scale(assets['galinha'], (largura, altura))
    assets['diesel'] = pygame.image.load('imagens/diesel.png').convert_alpha()
    assets['diesel'] = pygame.transform.scale(assets['diesel'], (largura, altura))
    assets['cavalo'] = pygame.image.load('imagens/cavalo.png').convert_alpha()
    assets['cavalo'] = pygame.transform.scale(assets['cavalo'], (largura,altura))
    assets['trator'] = pygame.image.load('imagens/trator.png').convert_alpha()
    assets['trator'] = pygame.transform.scale(assets['trator'], (plargura, paltura))
    explosion_anim = []
    for i in range(7):

        filename = 'imagens/caveira{}.jpg'.format(i)
        img = pygame.image.load(filename).convert()
        img = pygame.transform.scale(img, (32, 32))
        explosion_anim.append(img)
    assets["caveira"] = explosion_anim
    assets["fonte"] = pygame.font.Font('PressStart2P.ttf', 28)

    pygame.mixer.music.load('audio/dudu.mp3')
    pygame.mixer.music.set_volume(0.4)
    assets['grito'] = pygame.mixer.Sound('audio/grito.mp3')
    return assets

class trator(pygame.sprite.Sprite):
    def _init_(self, groups, assets):

        pygame.sprite.Sprite._init_(self)

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
            
            
            
class chao(pygame.sprite.Sprite):
    def _init_(self, assets):

        pygame.sprite.Sprite._init_(self)

        self.image = assets['chao']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = -1200
        self.speedx = 0
        self.speedy = 4.0

    def update(self):
        self.speedy+=0.005
        self.rect.y+=self.speedy
       
        
        

        if self.rect.top > 0:
            self.rect.x = 0
            self.rect.y = -1200
            

class diesel(pygame.sprite.Sprite):
    def _init_(self, assets):

        pygame.sprite.Sprite._init_(self)

        self.image = assets['diesel']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0,1000)
        self.rect.y = 0
        self.speedx = 0
        self.speedy = 4
        

    def update(self):
        if self.speedy > 15:
            self.speedy=15
        else:
            self.speedy+=0.005
            
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        

        if self.rect.top > HEIGHT:
            self.kill()

class cachorro(pygame.sprite.Sprite):
    def _init_(self, assets):

        pygame.sprite.Sprite._init_(self)
        
        self.image = assets['cachorro']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH-largura)
        self.rect.y = -100
        self.speedx = 0
        self.speedy = 4 


    def update(self):
        if self.speedy >15:
            self.speedy=15
        else:
            self.speedy+=0.005
      
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        

        if self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH:
            self.rect.x = random.randint(0, WIDTH-largura)
            self.rect.y = -100
            

class boi(pygame.sprite.Sprite):
    def _init_(self, assets):

        pygame.sprite.Sprite._init_(self)

        self.image = assets['boi']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH-largura)
        self.rect.y = -200
        self.speedx = 0
        self.speedy = 4

    def update(self):
        if self.speedy > 15:
            self.speedy=15
        else:
            self.speedy+=0.005
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH:
            self.rect.x = random.randint(0, WIDTH-largura)
            self.rect.y = -200
            

class galinha(pygame.sprite.Sprite):
    def _init_(self, assets,speedy):

        pygame.sprite.Sprite._init_(self)

        self.image = assets['galinha']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH-largura)
        self.rect.y = 0
        self.speedx = 0
        self.speedy = speedy

    def update(self):
        if self.speedy > 15:
            self.speedy=15
        else:
            self.speedy+=0.005
            galinha.velocidade=self.speedy
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH:
            self.rect.x = random.randint(0, WIDTH-largura)
            self.rect.y = 0

class cavalo(pygame.sprite.Sprite):
    def _init_(self, assets):

        pygame.sprite.Sprite._init_(self)

        self.image = assets['cavalo']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH-largura)
        self.rect.y = -300
        self.speedx = 0
        self.speedy = 4

    def update(self):
        if self.speedy > 15:
            self.speedy=15
        else:
            self.speedy+=0.005
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH:
            self.rect.x = random.randint(0, WIDTH-largura)
            self.rect.y = -300



class Explosao(pygame.sprite.Sprite):


    def _init_(self, center, assets):

        pygame.sprite.Sprite._init_(self)


        self.explosion_anim = assets['caveira']


        self.frame = 0  
        self.image = self.explosion_anim[self.frame] 
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


            if self.frame == len(self.explosion_anim):

                self.kill()
            else:

                center = self.rect.center
                self.image = self.explosion_anim[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center
 
                


def game_screen(janela):
    clock = pygame.time.Clock()

    assets = load_assets()


    all_sprites = pygame.sprite.Group()
    all_cachorros = pygame.sprite.Group()
    all_cavalos = pygame.sprite.Group()
    all_galinhas = pygame.sprite.Group()
    all_bois = pygame.sprite.Group()
    all_diesels = pygame.sprite.Group()
    groups = {}
    groups['all_sprites'] = all_sprites
    groups['all_cachorros'] = all_cachorros
    groups['all_cavalos'] = all_cavalos
    groups['all_galinhas'] = all_galinhas
    groups['boi'] = all_bois
    groups['all_diesels'] = all_diesels


    
    Chao=chao(assets)
    all_sprites.add(Chao)



    player = trator(groups, assets)
    all_sprites.add(player)
    
    
    

    for i in range(2):
        cachorros = cachorro(assets)
        cavalos= cavalo(assets)
        galinhas=galinha(assets,4)
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
    EXPLODING = 2
    state = PLAYING

    keys_down = {}
    score = 0
    lives = 4
    game= True
    while game==True:
        
        pygame.mixer.init()

        game = True

        font = pygame.font.SysFont(None, 60)
        text = font.render('Goiania Run', True, (255, 0, 0))
        font2 = pygame.font.SysFont(None, 48)
        text2 = font2.render('Pressione qualquer tecla', True, (255, 255, 255))
        text3 = font2.render('para iniciar o jogo', True, (255, 255, 255))
        image = pygame.image.load('imagens/telai.jpg').convert()
        image_menor = pygame.transform.scale(image, (1000, 800))

        pygame.mixer.music.load('audio/musica sertanejo.mp3')
        pygame.mixer.music.set_volume(0.4)
        pygame.mixer.music.play(loops=-1)

        while game:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game = False
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    game= False
                    
            
            janela.fill((0, 0, 0)) 
            janela.blit(image_menor, (0, 0))
            janela.blit(text, (120, 20))
            janela.blit(text2, (40, 300))
            janela.blit(text3, (100, 330))
            pygame.display.update()  

            
        
    pygame.mixer.music.load('audio/dudu.mp3')
    pygame.mixer.music.set_volume(0.4)    
    pygame.display.update() 

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

            if score == 1000 and lives<5:
                diesels=diesel(assets)
                all_diesels.add(diesels)
                all_sprites.add(diesels)
            if score == 2000 and lives<5:
                diesels=diesel(assets)
                all_diesels.add(diesels)
                all_sprites.add(diesels)
            if score == 3000 and lives<5:
                diesels=diesel(assets)
                all_diesels.add(diesels)
                all_sprites.add(diesels)    
            if score == 4000 and lives<5:
                diesels=diesel(assets)
                all_diesels.add(diesels)
                all_sprites.add(diesels)
            if score == 5000 and lives<5:
                diesels=diesel(assets)
                all_diesels.add(diesels)
                all_sprites.add(diesels)
            

            hits = pygame.sprite.spritecollide(player, all_cachorros, True, pygame.sprite.collide_mask)
            hits1 = pygame.sprite.spritecollide(player, all_cavalos, True, pygame.sprite.collide_mask)
            hits2 = pygame.sprite.spritecollide(player, all_galinhas, True, pygame.sprite.collide_mask)
            hits3 = pygame.sprite.spritecollide(player, all_bois, True, pygame.sprite.collide_mask)
            hits4 = pygame.sprite.spritecollide(player, all_diesels, True, pygame.sprite.collide_mask)
            if len(hits) > 0:

                assets['grito'].play()
                player.kill()
                lives -= 1
                explosao = Explosao(player.rect.center, assets)
                all_sprites.add(explosao)
                cachorros=cachorro(assets)
                all_sprites.add(cachorros)
                all_cachorros.add(cachorros)
                state = EXPLODING
                keys_down = {}
                explosion_tick = pygame.time.get_ticks()
                explosion_duration = explosao.frame_ticks * len(explosao.explosion_anim) + 400
            if  len(hits1) > 0:

                assets['grito'].play()
                player.kill()
                lives -= 1
                explosao = Explosao(player.rect.center, assets)
                all_sprites.add(explosao)
                cavalos=cavalo(assets)
                all_sprites.add(cavalos)
                all_cavalos.add(cavalos)
                state = EXPLODING
                keys_down = {}
                explosion_tick = pygame.time.get_ticks()
                explosion_duration = explosao.frame_ticks * len(explosao.explosion_anim) + 400
            if  len(hits2) > 0:

                assets['grito'].play()
                player.kill()
                lives -= 1
                explosao = Explosao(player.rect.center, assets)
                all_sprites.add(explosao)
                galinhas=galinha(assets,galinha.velocidade)
                all_sprites.add(galinhas)
                all_galinhas.add(galinhas)
                state = EXPLODING
                keys_down = {}
                explosion_tick = pygame.time.get_ticks()
                explosion_duration = explosao.frame_ticks * len(explosao.explosion_anim) + 400
            if  len(hits3) > 0:

                assets['grito'].play()
                player.kill()
                lives -= 1
                explosao = Explosao(player.rect.center, assets)
                all_sprites.add(explosao)
                bois=boi(assets)
                all_sprites.add(bois)
                all_bois.add(bois)
                state = EXPLODING
                keys_down = {}
                explosion_tick = pygame.time.get_ticks()
                explosion_duration = explosao.frame_ticks * len(explosao.explosion_anim) + 400
            if  len(hits4) > 0:
                lives+=1
            
        elif state == EXPLODING:
            now = pygame.time.get_ticks()
            if now - explosion_tick > explosion_duration:
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
        if lives==5:
            janela.blit(gasolina, (10, HEIGHT - 50)) 
            janela.blit(gasolina, (50, HEIGHT - 50))
            janela.blit(gasolina, (90, HEIGHT - 50))
            janela.blit(gasolina, (130, HEIGHT - 50))
            janela.blit(gasolina, (170, HEIGHT - 50))
        if lives==4:
            janela.blit(gasolina, (10, HEIGHT - 50)) 
            janela.blit(gasolina, (50, HEIGHT - 50))
            janela.blit(gasolina, (90, HEIGHT - 50))
            janela.blit(gasolina, (130, HEIGHT - 50))
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