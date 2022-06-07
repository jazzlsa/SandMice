import pygame
from assets.dados.parametros import *

# Define as imagens e áudios do jogo
def load():
    dicionary_assets = {}
    # Imagem de inicialização
    dicionary_assets['START_IMAGE'] = pygame.image.load('assets/imagens/SandMice.png').convert()
    # Imagem caso o jogador perca
    dicionary_assets['IMAGE_GAME_OVER'] = pygame.image.load('assets/imagens/gameover.png').convert()
    # Imagem caso o jogador ganhe
    dicionary_assets['IMAGE_VICTORY'] = pygame.image.load('assets/imagens/vitoria.png')
    # Imagem do jogador
    dicionary_assets['IMAGE_MOUSE'] = pygame.image.load('assets/imagens/mouse-face.png').convert_alpha()
    dicionary_assets['IMAGE_MOUSE'] = pygame.transform.scale(dicionary_assets['IMAGE_MOUSE'], (IMG_SIZE, IMG_SIZE))
    # Imagens da vovó
    dicionary_assets['IMAGE_GRANDMA_RIGHT'] = pygame.image.load('assets/imagens/grandma.png').convert_alpha()
    dicionary_assets['IMAGE_GRANDMA_RIGHT'] = pygame.transform.scale(dicionary_assets['IMAGE_GRANDMA_RIGHT'], (ENEMY_SIZE, ENEMY_SIZE))
    dicionary_assets['IMAGE_GRANDMA_LEFT'] = pygame.transform.flip(dicionary_assets['IMAGE_GRANDMA_RIGHT'], True, False)
    # Imagem da moeda
    dicionary_assets['IMAGE_COIN'] = pygame.image.load('assets/imagens/coin.png').convert_alpha()
    dicionary_assets['IMAGE_COIN'] = pygame.transform.scale(dicionary_assets['IMAGE_COIN'], (COIN_SIZE, COIN_SIZE))
    # Imagem do queijo
    dicionary_assets['IMAGE_CHEESE'] = pygame.image.load('assets/imagens/cheese.png').convert_alpha()
    dicionary_assets['IMAGE_CHEESE'] = pygame.transform.scale(dicionary_assets['IMAGE_CHEESE'], (COIN_SIZE, COIN_SIZE))
    # Imagem do gato
    dicionary_assets['IMAGE_CAT'] = pygame.image.load('assets/imagens/cat.png').convert_alpha()
    dicionary_assets['IMAGE_CAT'] = pygame.transform.scale(dicionary_assets['IMAGE_CAT'], (CAT_WIDTH, CAT_HEIGHT))
    # Imagem do fundo
    dicionary_assets['IMAGE_BACKGROUND'] = pygame.image.load('assets/imagens/fundo3.png').convert()
    dicionary_assets['IMAGE_BACKGROUND'] = pygame.transform.scale(dicionary_assets['IMAGE_BACKGROUND'], (SCREEN_WIDTH,SCREEN_HEIGHT))
    
    return dicionary_assets

# Define as imagens e nome da tela
def loadScreen():
    screen_assets = {}
    screen_assets['ICON_SCREEN'] = pygame.image.load('assets/imagens/mouse-face.png')
    screen_assets['ICON_SCREEN'] = pygame.transform.scale(screen_assets['ICON_SCREEN'], (SCREEN_WIDTH,SCREEN_HEIGHT))
    screen_assets['NAME'] = 'SandMice'
    
    return screen_assets