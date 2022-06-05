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