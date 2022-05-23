# ===== Inicialização =====
# ----- Importa e inicia pacotes
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

font = pygame.font.SysFont(None, 48)
IMGINICIAL = pygame.image.load('assets\SandMice.png').convert()
IMGFINAL = pygame.image.load('assets\SandMiceFinal.png').convert()
IMG = pygame.image.load('assets\mouse-face.png').convert_alpha()
IMG = pygame.transform.scale(IMG, (IMG_WIDTH, IMG_HEIGHT))
IMG2 = pygame.image.load('assets\grandma.png').convert_alpha()
IMG2 = pygame.transform.scale(IMG2, (ENEMY_WIDTH, ENEMY_HEIGHT))
IMG3 = pygame.image.load('assets\coin.png').convert_alpha()
IMG3 = pygame.transform.scale(IMG3, (COIN_WIDTH, COIN_HEIGHT))
background = pygame.image.load('assets\planodefundo.png').convert()
background = pygame.transform.scale(background, (WIDTH,HEIGHT))

# def message_new_round():
#     clock = pygame.time.Clock()
#     counter, text = 5, '5'.rjust(3)
#     pygame.time.set_timer(pygame.USEREVENT, 1000)
#     font = pygame.font.SysFont('Consolas', 15)
#     window.blit(font.render('A vovó te pegou. Você tem mais {0} vida(s)'.format(player.vida), True, YELLOW), (100, 100))
#     run = True
#     while run:
#         for e in pygame.event.get():
#             if e.type == pygame.USEREVENT: 
#                 counter -= 1
#                 text = str(counter).rjust(3) if counter > 0 else 'Vamos lá'
#             if e.type == pygame.QUIT: 
#                 run = False

#         window.blit(font.render(text, True, YELLOW), (150, 150))
#         pygame.display.flip()
#         clock.tick(5)
                    
# ----- Inicia estruturas de dados
class jogador(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH/2
        self.rect.bottom = HEIGHT - 100
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
        self.rect.bottom = 0 + 100
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
numrounds = 6
#Tela Inicial

INICIO = 0
JOGANDO = 1
TROCA_ROUND = 2
FIM = 3

estado = INICIO

while estado == INICIO:
    tempo = pygame.time.get_ticks()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            estado = TROCA_ROUND
        if event.type == pygame.QUIT:
            estado = FIM
            game = False
    window.blit(IMGINICIAL, (0, 0))
    ultimotempo.append(tempo)
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
        
        if estado == TROCA_ROUND: # Adicionar aqui a mudança de personagem (if numrounds<=3) e tela de fim do jogo (numrounds<=0)
            if numrounds <= 0:
                pygame.quit()
            texto_round = font.render('ROUND {0}'.format(7-numrounds), True, WHITE)
            numrounds -= 1
            window.fill(BLACK)
            window.blit(texto_round, (WIDTH/2-70,HEIGHT/2-70))
            pygame.display.update()
            pygame.time.delay(2000)
            tempo = pygame.time.get_ticks()
            ultimotempo.append(tempo)
            A = 0
            D = 0
            W = 0
            S = 0
            estado = JOGANDO
        
        if estado == JOGANDO:
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
    texto_tempo = font.render('{0:.1f} s'.format((tempo - ultimotempo[-1])/1000), True, YELLOW)

    if pygame.sprite.spritecollide(player, enemies, True): #Se colisao com inimigo -> morte
        # ATENÇÃO !!! SE O RATO MORRE EM CIMA DO SPAWN DA VOVO, O JOGO EXPLODE
        estado = TROCA_ROUND

        vovo = inimigo(IMG2)
        enemies.add(vovo)
        
        sprites.add(player)
        #message_new_round()

    if pygame.sprite.spritecollide(player, moedas, True): #Se colisao com moeda -> ganha ponto e cria uma nova moeda
        player.pontos += 50
        moeda = coin(IMG3)
        moedas.add(moeda)

    # ----- Gera saídas
    if estado == JOGANDO:

        window.blit(background,(0,0)) # Coloca o background

        sprites.draw(window)
        enemies.draw(window)
        moedas.draw(window)
        window.blit(pontuacao, (10, 10))
        window.blit(texto_tempo, (10, 600))

    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

pygame.quit()
quit()