import pygame
from assets.dados.config import *
import random

class jogador(pygame.sprite.Sprite):
        def __init__(self, img, sound):
            pygame.sprite.Sprite.__init__(self)

            self.image = img
            self.mask = pygame.mask.from_surface(self.image)
            self.rect = self.image.get_rect()
            self.rect.centerx = SCREEN_WIDTH/2
            self.rect.bottom = SCREEN_HEIGHT - 40
            self.speedx = 0
            self.speedy = 0
            self.moedas = 0
            self.queijos = 0
            self.sound = sound

        def update(self):
            self.rect.x += self.speedx
            self.rect.y += self.speedy

            if self.rect.right > SCREEN_WIDTH:
                self.rect.right = SCREEN_WIDTH
            if self.rect.left < 0:
                self.rect.left = 0
            if self.rect.top < 73:
                self.rect.top = 73
            if self.rect.bottom > 615:
                self.rect.bottom =615

class inimigo(pygame.sprite.Sprite):
    def __init__(self, imgs, sound):
        pygame.sprite.Sprite.__init__(self)
        self.images = imgs
        self.image = imgs[0]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH/2
        self.rect.bottom = 0 + 100
        self.speedx = 0
        self.speedy = 0
        self.sound = sound

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

        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top < 73:
            self.rect.top = 73
        if self.rect.bottom > 615:
            self.rect.bottom = 615

class coin(pygame.sprite.Sprite):
    def __init__(self,img, sound):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randint(COIN_SIZE, SCREEN_WIDTH - COIN_SIZE)
        self.rect.bottom = random.randint(COIN_SIZE+73, 615 - COIN_SIZE)
        self.speedx = 0
        self.speedy = 0
        self.sound = sound