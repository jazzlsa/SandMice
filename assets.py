import pygame
from config import *

# Carrega as imagens
def load_images():
    dicionary_images = {}

    # Imagem de inicialização
    dicionary_images['START_IMAGE'] = pygame.image.load(os.path.join(IMAGES_PATH, 'screen-initial.png')).convert()
    # Imagem caso o jogador perca
    dicionary_images['IMAGE_GAME_OVER'] = pygame.image.load(os.path.join(IMAGES_PATH, 'screen-failed.png')).convert()
    # Imagem caso o jogador ganhe
    dicionary_images['IMAGE_VICTORY'] = pygame.image.load(os.path.join(IMAGES_PATH, 'screen-victory.png')).convert()
    # Imagem do jogador
    dicionary_images['IMAGE_MOUSE'] = pygame.image.load(os.path.join(IMAGES_PATH, 'icon-player.png')).convert_alpha()
    dicionary_images['IMAGE_MOUSE'] = pygame.transform.scale(dicionary_images['IMAGE_MOUSE'], (IMG_SIZE, IMG_SIZE))
    # Imagens da vovó
    dicionary_images['IMAGE_GRANDMA_RIGHT'] = pygame.image.load(os.path.join(IMAGES_PATH, 'icon-grandma.png')).convert_alpha()
    dicionary_images['IMAGE_GRANDMA_RIGHT'] = pygame.transform.scale(dicionary_images['IMAGE_GRANDMA_RIGHT'], (ENEMY_SIZE, ENEMY_SIZE))
    dicionary_images['IMAGE_GRANDMA_LEFT'] = pygame.transform.flip(dicionary_images['IMAGE_GRANDMA_RIGHT'], True, False)
    # Imagem da moeda
    dicionary_images['IMAGE_COIN'] = pygame.image.load(os.path.join(IMAGES_PATH, 'icon-coin.png')).convert_alpha()
    dicionary_images['IMAGE_COIN'] = pygame.transform.scale(dicionary_images['IMAGE_COIN'], (COIN_SIZE, COIN_SIZE))
    # Imagem do queijo
    dicionary_images['IMAGE_CHEESE'] = pygame.image.load(os.path.join(IMAGES_PATH, 'icon-cheese.png')).convert_alpha()
    dicionary_images['IMAGE_CHEESE'] = pygame.transform.scale(dicionary_images['IMAGE_CHEESE'], (COIN_SIZE, COIN_SIZE))
    # Imagem do gato
    dicionary_images['IMAGE_CAT'] = pygame.image.load(os.path.join(IMAGES_PATH, 'icon-cat.png')).convert_alpha()
    dicionary_images['IMAGE_CAT'] = pygame.transform.scale(dicionary_images['IMAGE_CAT'], (CAT_WIDTH, CAT_HEIGHT))
    # Imagem do fundo
    dicionary_images['IMAGE_BACKGROUND'] = pygame.image.load(os.path.join(IMAGES_PATH, 'background.png')).convert()
    dicionary_images['IMAGE_BACKGROUND'] = pygame.transform.scale(dicionary_images['IMAGE_BACKGROUND'], (SCREEN_WIDTH,SCREEN_HEIGHT))
    
    return dicionary_images

#Carrega os sons
def load_sounds():
    dicionary_sounds = {}
    # Música de fundo da introdução
    dicionary_sounds['SOUND_BACKGROUND_INTRO'] = os.path.join(SOUNDS_PATH, 'background_intro_music.mp3')
    # Música de fundo do jogo
    dicionary_sounds['SOUND_BACKGROUND'] = os.path.join(SOUNDS_PATH, 'background_music.mp3')
    # Som do gato
    dicionary_sounds['SOUND_CAT'] = pygame.mixer.Sound(os.path.join(SOUNDS_PATH, 'sound_cat.mp3'))
    # Som da moeda
    dicionary_sounds['SOUND_COIN'] = pygame.mixer.Sound(os.path.join(SOUNDS_PATH, 'sound_coin.mp3'))
    # Som do queijo
    dicionary_sounds['SOUND_CHEESE'] = pygame.mixer.Sound(os.path.join(SOUNDS_PATH, 'sound_cheese.mp3'))
    # Som do jogador
    dicionary_sounds['SOUND_MOUSE'] = pygame.mixer.Sound(os.path.join(SOUNDS_PATH, 'sound_player.mp3'))
    # Som da vovó
    dicionary_sounds['SOUND_GRANDMA'] = pygame.mixer.Sound(os.path.join(SOUNDS_PATH, 'sound_grandma.mp3'))

    # Configurando o volume da moeda
    dicionary_sounds['SOUND_COIN'].set_volume(EFFECTS_VOLUME_COIN)
    # Configurando o volume da gato
    dicionary_sounds['SOUND_CAT'].set_volume(EFFECTS_VOLUME_CAT)
    # Configurando o volume da vovó
    dicionary_sounds['SOUND_GRANDMA'].set_volume(EFFECTS_VOLUME_GRANDMA)
    
    return dicionary_sounds

#Carrega as fontes de texto
def load_fonts():
    dicionary_fonts = {}
    
    # Fonte do Jogo
    dicionary_fonts['FONT_GAME'] = pygame.font.SysFont(None, FONT_SIZE)
    dicionary_fonts['FONT_PEQUENA'] = pygame.font.SysFont(None, 24)
    
    return dicionary_fonts

# Define as imagens e nome da tela
def loadScreen():
    screen_assets = {}
    screen_assets['ICON_SCREEN'] = pygame.image.load(os.path.join(IMAGES_PATH, 'icon-player.png'))
    screen_assets['ICON_SCREEN'] = pygame.transform.scale(screen_assets['ICON_SCREEN'], (SCREEN_WIDTH,SCREEN_HEIGHT))
    screen_assets['NAME'] = 'SandMice'
    
    return screen_assets