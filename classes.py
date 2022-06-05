import pygame
from assets.dados.parametros import *
import random

class jogador(pygame.sprite.Sprite):
        def __init__(self, img, sound):
            pygame.sprite.Sprite.__init__(self)

            self.image = img
            self.mask = pygame.mask.from_surface(self.image)
            self.rect = self.image.get_rect()
            self.rect.centerx = WIDTH/2
            self.rect.bottom = HEIGHT - 40
            self.speedx = 0
            self.speedy = 0
            self.moedas = 0
            self.queijos = 0
            self.pontos = 0
            self.sound_caught = sound

        def update(self):
            self.rect.x += self.speedx
            self.rect.y += self.speedy

            if self.rect.right > WIDTH:
                self.rect.right = WIDTH
            if self.rect.left < 0:
                self.rect.left = 0
            if self.rect.top < 73:
                self.rect.top = 73
            if self.rect.bottom > HEIGHT:
                self.rect.bottom = HEIGHT

class inimigo(pygame.sprite.Sprite):
    def __init__(self, imgs, cat_sound, riso_sound):
        pygame.sprite.Sprite.__init__(self)
        self.images = imgs
        self.image = imgs[0]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH/2
        self.rect.bottom = 0 + 100
        self.speedx = 0
        self.speedy = 0
        self.cat_sound = cat_sound
        self.vovo_sound = riso_sound

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        i = 0
        if self.speedx < 0:
            i = 1
        elif self.speedx > 0:
            i = 0

        c = self.rect.center
        self.image = self.images[i]
        self.rect = self.image.get_rect()
        self.rect.center = c

        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top < 73:
            self.rect.top = 73
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

class coin(pygame.sprite.Sprite):
    def __init__(self,img, sound):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randint(COIN_WIDTH, WIDTH - COIN_WIDTH)
        self.rect.bottom = random.randint(COIN_HEIGHT+73, HEIGHT - COIN_HEIGHT)
        self.speedx = 0
        self.speedy = 0
        self.coin_sound = sound

class cheese(pygame.sprite.Sprite):
    def __init__(self,img):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randint(CHEESE_WIDTH, WIDTH - CHEESE_WIDTH)
        self.rect.bottom = random.randint(CHEESE_HEIGHT+73, HEIGHT - CHEESE_HEIGHT)
        self.speedx = 0
        self.speedy = 0

class movel(pygame.sprite.Sprite):
    def __init__(self, img, centerx, bottom):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = img
        # self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = centerx
        self.rect.bottom = bottom