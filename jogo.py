# ===== Inicialização =====
# ----- Importa e inicia pacotes
from re import L
import pygame
import random

pygame.init()

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255, 255, 0)

# ----- Gera tela principal
WIDTH, HEIGHT = 640, 640
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Teste')

# ----- Inicia assets
IMG_WIDTH = 50
IMG_HEIGHT = 50
ENEMY_WIDTH = 80
ENEMY_HEIGHT = 80
COIN_WIDTH = 30
COIN_HEIGHT = 30
TILE_WIDTH = 32
TILE_HEIGHT = 32

TILE_RESOLUTION = 32
TILES_HORIZONTAL, TILES_VERTICAL = WIDTH//TILE_RESOLUTION, HEIGHT//TILE_RESOLUTION

font = pygame.font.SysFont(None, 48)
IMGINICIAL = pygame.image.load('assets\SandMice.png').convert()
IMGFINAL = pygame.image.load('assets\SandMiceFinal.png').convert()
IMG = pygame.image.load('assets\mouse-face.png').convert_alpha()
IMG = pygame.transform.scale(IMG, (IMG_WIDTH, IMG_HEIGHT))
IMG2 = pygame.image.load('assets\grandma.png').convert_alpha()
IMG2 = pygame.transform.scale(IMG2, (ENEMY_WIDTH, ENEMY_HEIGHT))
IMG3 = pygame.image.load('assets\coin.png').convert_alpha()
IMG3 = pygame.transform.scale(IMG3, (COIN_WIDTH, COIN_HEIGHT))
TILE_parede = pygame.image.load('assets\parede.png').convert_alpha()
# TILE_parede = pygame.transform.scale(TILE_parede, (TILE_WIDTH, TILE_HEIGHT))
TILE_chao = pygame.image.load('assets\chao.png').convert_alpha()
# TILE_chao = pygame.transform.scale(TILE_chao, (TILE_WIDTH, TILE_HEIGHT))
# background = pygame.image.load('assets\planodefundo.png').convert()

def cria_mapa(tamanhox,tamanhoy):
    mapa = []
    for a in range(tamanhox):
        mapa.append([])
        for b in range(tamanhoy):
            mapa[a].append(random.randint(0,1))
    return mapa

rr = cria_mapa(TILES_HORIZONTAL,TILES_VERTICAL)
mapa1 = [[0 if bbbb<3 or bbbb>16 else 1 for aaaa in range(TILES_HORIZONTAL)] for bbbb in range(TILES_VERTICAL)]

# for a in mapa1:
#     print(a)
# print(mapa1)

def printa_mapa(mapa,chao,parede,tamanho):
    contx, conty = 0, 0
    for a in range(len(mapa)):
        for b in range(len(mapa)):
            if mapa[b][a] == 0:
                window.blit(parede,(contx,conty))
            else:
                window.blit(chao,(contx,conty))
            contx += tamanho
        conty += tamanho
        contx = 0

# ----- Inicia estruturas de dados
class jogador(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH/2
        self.rect.bottom = HEIGHT - 100
        self.vida = 5
        self.speedx = 0
        self.speedy = 0
        self.pontos = 0

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

class inimigo(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH/2
        self.rect.bottom = HEIGHT - 300
        self.speedx = 0
        self.speedy = 0

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

class coin(pygame.sprite.Sprite):
    def __init__(self,img):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randint(COIN_WIDTH, WIDTH - COIN_WIDTH)
        self.rect.bottom = random.randint(COIN_HEIGHT, HEIGHT - COIN_HEIGHT)
        self.speedx = 0
        self.speedy = 0

game = True
# Variável para o ajuste de velocidade
clock = pygame.time.Clock()
FPS = 60
vel_padrao_rato = 5
vel_padrao_vovo = 3
ultimotempo = [0]

# Criando um grupo de sprites
sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
moedas = pygame.sprite.Group()
# Criando o jogador
player = jogador(IMG)
vovo = inimigo(IMG2)
for i in range(5):
    moeda = coin(IMG3)
    moedas.add(moeda)
sprites.add(player)
enemies.add(vovo)
moedas.add(moeda)

Left = 0
Right = 0
Up = 0
Down = 0
A = 0
D = 0
W = 0
S = 0
#Tela Inicial
inicio = False
while inicio == False:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            inicio = True
        if event.type == pygame.QUIT:
            inicio = True
            game = False
    window.fill((0, 0, 0))
    window.blit(IMGINICIAL, (0, 0))
    pygame.display.update()

# ===== Loop principal =====
while game:
    clock.tick(FPS)
    tempo = pygame.time.get_ticks()
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and Left == 0:
                player.speedx -= vel_padrao_rato
                Left += 1
            if event.key == pygame.K_RIGHT and Right == 0:
                player.speedx += vel_padrao_rato
                Right += 1
            if event.key == pygame.K_UP and Up == 0:
                player.speedy -= vel_padrao_rato
                Up += 1
            if event.key == pygame.K_DOWN and Down == 0:
                player.speedy += vel_padrao_rato
                Down += 1
            if event.key == pygame.K_a and A == 0:
                vovo.speedx -= vel_padrao_vovo
                A += 1
            if event.key == pygame.K_d and D == 0:
                vovo.speedx += vel_padrao_vovo
                D += 1
            if event.key == pygame.K_w and W == 0:
                vovo.speedy -= vel_padrao_vovo
                W += 1
            if event.key == pygame.K_s and S == 0:
                vovo.speedy += vel_padrao_vovo
                S += 1
        # Verifica se soltou alguma tecla.
        if event.type == pygame.KEYUP:
            # Dependendo da tecla, altera a velocidade.
            if event.key == pygame.K_LEFT and Left == 1:
                player.speedx += vel_padrao_rato
                Left -= 1
            if event.key == pygame.K_RIGHT and Right == 1:
                player.speedx -= vel_padrao_rato
                Right -= 1
            if event.key == pygame.K_UP and Up == 1:
                player.speedy += vel_padrao_rato
                Up -= 1
            if event.key == pygame.K_DOWN and Down == 1:
                player.speedy -= vel_padrao_rato
                Down -= 1
            if event.key == pygame.K_a and A == 1:
                vovo.speedx += vel_padrao_vovo
                A -= 1
            if event.key == pygame.K_d and D == 1:
                vovo.speedx -= vel_padrao_vovo
                D -= 1
            if event.key == pygame.K_w and W == 1:
                vovo.speedy += vel_padrao_vovo
                W -= 1
            if event.key == pygame.K_s and S == 1:
                vovo.speedy -= vel_padrao_vovo
                S -= 1
    
    sprites.update()
    enemies.update()
    pontuacao = font.render('Pontos: {0}'.format(player.pontos), True, YELLOW)
    vidas_rato = font.render('Vidas: {0}'.format(player.vida), True, YELLOW)
    texto_tempo = font.render('{0:.1f} s'.format((tempo - ultimotempo[-1])/1000), True, YELLOW)

    if pygame.sprite.spritecollide(player, enemies, True): #Se colisao com inimigo -> morte
        player.vida -= 1
        ultimotempo.append(tempo)
        A = 0
        D = 0
        W = 0
        S = 0
        vovo = inimigo(IMG2)
        enemies.add(vovo)
    
    if pygame.sprite.spritecollide(player, moedas, True): #Se colisao com moeda -> ganha ponto e cria uma nova moeda
        player.pontos += 50
        moeda = coin(IMG3)
        moedas.add(moeda)
    
    if player.vida <= 0:
        game = False

    # ----- Gera saídas
    window.fill(WHITE)  # Preenche com a cor branca
    # window.blit(background,(0,0)) # Coloca o background
    printa_mapa(mapa1,TILE_chao,TILE_parede,TILE_RESOLUTION)
    sprites.draw(window)
    enemies.draw(window)
    moedas.draw(window)
    window.blit(pontuacao, (10, 10))
    window.blit(vidas_rato, (10, 50))
    window.blit(texto_tempo, (10, 600))

    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

#if game==False: # ----- Caso o jogo termine, ele fica esperando que o usuário digite a letra Q para sair.
#    window.blit(IMGFINAL, (0, 0))
#    pygame.display.update()
#    while(True):
#        for event in pygame.event.get():
#            if event.type==pygame.KEYDOWN:
#                if event.key==pygame.K_q:
#                    pygame.quit()
#                    quit()

pygame.quit()
quit()