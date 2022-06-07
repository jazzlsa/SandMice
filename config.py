import os
from os import path

IMAGES_PATH = path.join(path.dirname(__file__), 'assets', 'imagens')
SOUNDS_PATH = path.join(path.dirname(__file__), 'assets', 'sons')

# Cores
BLACK   = (0,0,0)
WHITE   = (255,255,255)
RED     = (255,0,0)
GREEN   = (0,255,0)
BLUE    = (0,0,255)
YELLOW  = (255, 255, 0)

# Estados do jogo
INICIO                  = 000
JOGANDO                 = 100
TROCA_ROUND             = 200 
FIM                     = 300
ALTERA_MOVIMENTO_GATO   = 501
ALTERA_MOVIMENTO_VOVO   = 502

# Configurações da tela
SCREEN_WIDTH    = 672 
SCREEN_HEIGHT   = 672
FPS             = 60
FONT_SIZE       = 48

# Configurações dos tamanhos dos objetos no jogo
IMG_SIZE    = 50
ENEMY_SIZE  = 80
COIN_SIZE   = 30
CHEESE_SIZE = 30
CAT_WIDTH   = 80
CAT_HEIGHT  = 60

# Configuração de onde mostrar o score no jogo
DISPLAY_COINS_X     = 230
DISPLAY_COINS_Y     = 630
DISPLAY_CHEESE_X    = 450
DISPLAY_CHEESE_Y    = 630
DISLAY_TIME_X       = 10
DISLAY_TIME_Y       = 630

# Configuração de onde mostrar o score da imagem final
FINAL_DISPLAY_COINS_X     = 160
FINAL_DISPLAY_COINS_Y     = 420
FINAL_DISPLAY_CHEESE_X    = 160
FINAL_DISPLAY_CHEESE_Y    = 340

# Configurações do som
BACKGROUND_VOLUME = 0.4
EFFECTS_VOLUME_CAT = 0.3
EFFECTS_VOLUME_COIN = 0.1
EFFECTS_VOLUME_GRANDMA = 1

# Configurações de jogabilidade
DELAY_SCREEN_ROUNDS = 1000
QUANTITY_ROUNDS = 1
QUANTITY_COINS_PER_ROUND = 3
QUANTITY_CHEESES_PER_ROUND = 1
SPEED_PLAYER = 5
SPEED_ENEMIES = 2
TIME_RESPAWN_CAT = 5000 #em ms
CHANGE_MOVIMENT_GRANDMA = 100 #em ms
CHANGE_MOVIMENT_CAT = 500 #em ms
QUANTITY_COINS_TO_WIN = 50
QUANTITY_CHEESE_TO_WIN = 30

#Quantidade de moedas e queijos para ganhar
VENCERMOEDAS = 60
VENCERQUEIJOS = 30