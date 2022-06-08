# Importa pacotes e arquivos
import pygame
from config import *
from gsc import *
from assets import loadScreen

# Instancia a classe pygame
pygame.init()
pygame.mixer.init()

# Carrega dados da tela
screen_assets = loadScreen()

# Configura o ícone da tela
pygame_icon = screen_assets['ICON_SCREEN']
pygame.display.set_icon(pygame_icon)

# Configura o nome da tela
pygame.display.set_caption(screen_assets['NAME'])

# Configura o tamanho da tela
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Gera a tela
gamescreen(window)

# Sai do jogo
pygame.quit()
quit()