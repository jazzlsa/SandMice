import pygame
from assets.dados.parametros import *

def load():
    asse = {}
    asse['IMGINICIAL'] = pygame.image.load('assets/imagens/SandMice.png').convert()
    asse['IMGAMEOVER'] = pygame.image.load('assets/imagens/gameover.png').convert()
    asse['IMGVIT'] = pygame.image.load('assets/imagens/vitoria.png')
    #Player 1 - Rato
    asse['IMG'] = pygame.image.load('assets/imagens/mouse-face.png').convert_alpha()
    asse['IMG'] = pygame.transform.scale(asse['IMG'], (IMG_WIDTH, IMG_HEIGHT))
    #Player 2 - Inimigo
    asse['GRANDMA_IMG'] = pygame.image.load('assets/imagens/grandma.png').convert_alpha()
    asse['GRANDMA_RIGTH'] = pygame.transform.scale(asse['GRANDMA_IMG'], (ENEMY_WIDTH, ENEMY_HEIGHT))
    asse['GRANDMA_LEFT'] = pygame.transform.flip(asse['GRANDMA_RIGTH'], True, False)
    #Moeda
    asse['IMG3'] = pygame.image.load('assets/imagens/coin.png').convert_alpha()
    asse['IMG3'] = pygame.transform.scale(asse['IMG3'], (COIN_WIDTH, COIN_HEIGHT))
    #Queijo
    asse['IMG4'] = pygame.image.load('assets/imagens/cheese.png').convert_alpha()
    asse['IMG4'] = pygame.transform.scale(asse['IMG4'], (COIN_WIDTH, COIN_HEIGHT))
    #Gato Inimigo
    asse['CAT_IMG'] = pygame.image.load('assets/imagens/cat.png').convert_alpha()
    asse['CAT_RIGTH'] = pygame.transform.scale(asse['CAT_IMG'], (CAT_WIDTH, CAT_HEIGHT))
    asse['CAT_LEFT'] = pygame.transform.flip(asse['CAT_RIGTH'], True, False)
    # background = pygame.image.load('assets/imagens/planodefundo.png').convert()
    asse['background'] = pygame.image.load('assets/imagens/fundo3.png').convert()
    asse['background'] = pygame.transform.scale(asse['background'], (WIDTH,HEIGHT))
    return asse