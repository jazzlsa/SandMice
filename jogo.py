# ===== Inicialização =====
# ----- Importa e inicia pacotes
from asyncio.windows_events import NULL
from ssl import create_default_context
import pygame
from assets.dados.parametros import *
from gsc import *

pygame.init()
pygame.mixer.init() 

#muda o ícone do jogo 
pygame_icon = pygame.image.load('assets/imagens/mouse-face.png')
pygame.display.set_icon(pygame_icon)

# ----- Gera tela principal
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('SandMice')

#inicia o jogo
gamescreen(window)

pygame.quit()
quit()