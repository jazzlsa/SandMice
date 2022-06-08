import pygame
from config import *

# Define as imagens e áudios do jogo
def load():
    dicionary_assets = {}

    # Imagem de inicialização
    dicionary_assets['START_IMAGE'] = pygame.image.load(os.path.join(IMAGES_PATH, 'screen-initial.png')).convert()
    # Imagem caso o jogador perca
    dicionary_assets['IMAGE_GAME_OVER'] = pygame.image.load(os.path.join(IMAGES_PATH, 'screen-failed.png')).convert()
    # Imagem caso o jogador ganhe
    dicionary_assets['IMAGE_VICTORY'] = pygame.image.load(os.path.join(IMAGES_PATH, 'screen-victory.png')).convert()
    # Imagem do jogador
    dicionary_assets['IMAGE_MOUSE'] = pygame.image.load(os.path.join(IMAGES_PATH, 'icon-player.png')).convert_alpha()
    dicionary_assets['IMAGE_MOUSE'] = pygame.transform.scale(dicionary_assets['IMAGE_MOUSE'], (IMG_SIZE, IMG_SIZE))
    # Imagens da vovó
    dicionary_assets['IMAGE_GRANDMA_RIGHT'] = pygame.image.load(os.path.join(IMAGES_PATH, 'icon-grandma.png')).convert_alpha()
    dicionary_assets['IMAGE_GRANDMA_RIGHT'] = pygame.transform.scale(dicionary_assets['IMAGE_GRANDMA_RIGHT'], (ENEMY_SIZE, ENEMY_SIZE))
    dicionary_assets['IMAGE_GRANDMA_LEFT'] = pygame.transform.flip(dicionary_assets['IMAGE_GRANDMA_RIGHT'], True, False)
    # Imagem da moeda
    dicionary_assets['IMAGE_COIN'] = pygame.image.load(os.path.join(IMAGES_PATH, 'icon-coin.png')).convert_alpha()
    dicionary_assets['IMAGE_COIN'] = pygame.transform.scale(dicionary_assets['IMAGE_COIN'], (COIN_SIZE, COIN_SIZE))
    # Imagem do queijo
    dicionary_assets['IMAGE_CHEESE'] = pygame.image.load(os.path.join(IMAGES_PATH, 'icon-cheese.png')).convert_alpha()
    dicionary_assets['IMAGE_CHEESE'] = pygame.transform.scale(dicionary_assets['IMAGE_CHEESE'], (COIN_SIZE, COIN_SIZE))
    # Imagem do gato
    dicionary_assets['IMAGE_CAT'] = pygame.image.load(os.path.join(IMAGES_PATH, 'icon-cat.png')).convert_alpha()
    dicionary_assets['IMAGE_CAT'] = pygame.transform.scale(dicionary_assets['IMAGE_CAT'], (CAT_WIDTH, CAT_HEIGHT))
    # Imagem do fundo
    dicionary_assets['IMAGE_BACKGROUND'] = pygame.image.load(os.path.join(IMAGES_PATH, 'background.png')).convert()
    dicionary_assets['IMAGE_BACKGROUND'] = pygame.transform.scale(dicionary_assets['IMAGE_BACKGROUND'], (SCREEN_WIDTH,SCREEN_HEIGHT))
    
    # Música de fundo da introdução
    dicionary_assets['SOUND_BACKGROUND_INTRO'] = os.path.join(SOUNDS_PATH, 'background_intro_music.mp3')
    # Música de fundo do jogo
    dicionary_assets['SOUND_BACKGROUND'] = os.path.join(SOUNDS_PATH, 'background_music.mp3')
    # Som do gato
    dicionary_assets['SOUND_CAT'] = pygame.mixer.Sound(os.path.join(SOUNDS_PATH, 'sound_cat.mp3'))
    # Som da moeda
    dicionary_assets['SOUND_COIN'] = pygame.mixer.Sound(os.path.join(SOUNDS_PATH, 'sound_coin.mp3'))
    # Som do queijo
    dicionary_assets['SOUND_CHEESE'] = pygame.mixer.Sound(os.path.join(SOUNDS_PATH, 'sound_cheese.mp3'))
    # Som do jogador
    dicionary_assets['SOUND_MOUSE'] = pygame.mixer.Sound(os.path.join(SOUNDS_PATH, 'sound_player.mp3'))
    # Som da vovó
    dicionary_assets['SOUND_GRANDMA'] = pygame.mixer.Sound(os.path.join(SOUNDS_PATH, 'sound_grandma.mp3'))

    # Configurando o volume da moeda
    dicionary_assets['SOUND_COIN'].set_volume(EFFECTS_VOLUME_COIN)
    # Configurando o volume da gato
    dicionary_assets['SOUND_CAT'].set_volume(EFFECTS_VOLUME_CAT)
    # Configurando o volume da vovó
    dicionary_assets['SOUND_GRANDMA'].set_volume(EFFECTS_VOLUME_GRANDMA)

    # Fonte do Jogo
    dicionary_assets['FONT_GAME'] = pygame.font.SysFont(None, FONT_SIZE)
    dicionary_assets['FONT_PEQUENA'] = pygame.font.SysFont(None, 24)
    
    return dicionary_assets

# Define as imagens e nome da tela
def loadScreen():
    screen_assets = {}
    screen_assets['ICON_SCREEN'] = pygame.image.load(os.path.join(IMAGES_PATH, 'icon-player.png'))
    screen_assets['ICON_SCREEN'] = pygame.transform.scale(screen_assets['ICON_SCREEN'], (SCREEN_WIDTH,SCREEN_HEIGHT))
    screen_assets['NAME'] = 'SandMice'
    
    return screen_assets