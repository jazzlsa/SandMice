import pygame
from assets.dados.parametros import *
import random
from classes import *
from assets.dados.assets import load

def gamescreen(window):
    font = pygame.font.SysFont(None, 48)
    #Telas iniciais e finais
    dicionary_assets = load()
    
    # Carrega os sons do jogo
    pygame.mixer.music.load('assets/sons/intro-jogo.mp3')
    pygame.mixer.music.set_volume(0.5)
    cat_sound = pygame.mixer.Sound('assets/sons/gato-som.mp3')
    coin_sound = pygame.mixer.Sound('assets/sons/coin.mp3')
    cheese_sound = pygame.mixer.Sound('assets/sons/crunch_sound.mp3')
    caught_sound = pygame.mixer.Sound('assets/sons/rat-sound.mp3')
    risada_sound = pygame.mixer.Sound('assets/sons/vovo-rindo.mp3')
                        
    # ----- Inicia estruturas de dados

    def respawnamoedas(state, grupomoedas):
        if state == TROCA_ROUND:
            grupomoedas = ''
            grupomoedas = pygame.sprite.Group()
        while len(grupomoedas) < totalmoedas:
            moeda = coin(dicionary_assets['IMAGE_COIN'],coin_sound)
            grupomoedas.add(moeda)
        if state != INICIO and state != TROCA_ROUND:
            coin_sound.set_volume(0.1)
            moeda.coin_sound.play()
            
            
        return grupomoedas

    def respawnoqueijo(state, grupoqueijos):
        if state == TROCA_ROUND:
            grupoqueijos = pygame.sprite.Group()
        queijos = coin(dicionary_assets['IMAGE_CHEESE'],cheese_sound)
        grupoqueijos.add(queijos)
        if state != INICIO and state != TROCA_ROUND:
            queijos.coin_sound.play()
        return grupoqueijos

    def respawnogato(enemies_gato):
        while True:
            NovoInimigo = inimigo([dicionary_assets['IMAGE_CAT'], dicionary_assets['IMAGE_CAT']],cat_sound, '')
            NovoInimigo.rect.centerx = random.randint(CAT_WIDTH, WIDTH - CAT_WIDTH)
            NovoInimigo.rect.bottom = random.randint(CAT_HEIGHT, HEIGHT - CAT_HEIGHT)
            cat_sound.set_volume(0.3)
            NovoInimigo.cat_sound.play()
            manobra = pygame.sprite.Group()
            manobra.add(NovoInimigo)
            if not pygame.sprite.spritecollide(player, manobra, True):
                enemies_gato.add(NovoInimigo)
                break
            manobra = pygame.sprite.Group()  
        return enemies_gato

    game = True
    pygame.mixer.music.play(loops=-1) # Inicia música de introdução

    INICIO      = 0
    JOGANDO     = 1
    TROCA_ROUND = 2 
    FIM         = 3
    ALTERA_MOVIMENTO_GATO = 667
    ALTERA_MOVIMENTO_VOVO = 666

    estado = INICIO
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()
    FPS = 60
    vel_padrao_rato = 5
    vel_padrao_vovo = 2
    ultimotempo = [0]
    ultimotempogato = [0]
    tempo_respawn_gato = 5000 # A cada 5 segundos

    # Criando um grupo de sprites
    sprites = pygame.sprite.Group()
    enemies = pygame.sprite.Group()
    enemies_cat = pygame.sprite.Group()
    moedas = pygame.sprite.Group()
    queijos = pygame.sprite.Group()
    totalmoedas = 3
    # Criando o jogador
    player = jogador(dicionary_assets['IMAGE_MOUSE'],caught_sound)

    vovo = inimigo([dicionary_assets['IMAGE_GRANDMA_RIGHT'], dicionary_assets['IMAGE_GRANDMA_LEFT']],'', risada_sound)
    vovo.rect.x = random.randint(60, WIDTH-60)

    perto = True
    while(perto):
        x_enemy = random.randint(60, WIDTH-60)
        if((x_enemy > (player.rect.x + 200)) or (x_enemy < (player.rect.x - 200))):
            perto = False
    vovo.rect.x = x_enemy
    
    sprites.add(player)
    enemies.add(vovo)
    moedas = respawnamoedas(estado, moedas)
    
    Left = 0
    Right = 0
    Up = 0
    Down = 0
    A = 0
    D = 0
    W = 0
    S = 0
    numrounds = 1
    #Tela Inicial

    '''while estado == INICIO:
        tempo = pygame.time.get_ticks()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                estado = TROCA_ROUND
            if event.type == pygame.QUIT:
                estado = FIM
                game = False
        window.blit(dicionary_assets['START_IMAGE'], (0, 0))
        ultimotempo.append(tempo)
        ultimotempogato.append(tempo)
        pygame.display.update()'''


    musica_fundo = False
    colisao = False
    # ===== Loop principal =====
    while game:
        clock.tick(FPS)
        tempo = pygame.time.get_ticks()

        # ----- Trata eventos
        for event in pygame.event.get():

            if(musica_fundo == False):
                pygame.mixer.music.load('assets/sons/musica-jogo.mp3')
                pygame.mixer.music.set_volume(0.4)
                pygame.mixer.music.play(loops=-1)
                musica_fundo = True
                pygame.time.set_timer(ALTERA_MOVIMENTO_VOVO, 100)

            if estado == INICIO:
                numrounds = 1
                Left = 0
                Right = 0
                Up = 0
                Down = 0
                player.speedx = 0
                player.speedy = 0
                tempo = pygame.time.get_ticks()
                window.blit(dicionary_assets['START_IMAGE'], (0, 0))
                player.moedas = 0
                player.queijos = 0
                ultimotempo.append(tempo)
                ultimotempogato.append(tempo)
                pygame.display.update()
                while estado == INICIO:
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            estado = TROCA_ROUND
                        if event.type == pygame.QUIT:
                            estado = FIM
                            game = False

            # ----- Verifica consequências
            if estado == JOGANDO:
                if len(queijos) < 1:
                    queijo = coin(dicionary_assets['IMAGE_CHEESE'],cheese_sound)
                    queijos.add(queijo)

                if tempo-ultimotempogato[-1] > tempo_respawn_gato:
                    ultimotempogato.append(tempo)
                    enemies_cat = respawnogato(enemies_cat)
                    pygame.time.set_timer(ALTERA_MOVIMENTO_GATO, 500)

                if event.type == ALTERA_MOVIMENTO_GATO:
                    for gato in enemies_cat:
                        direita_esquerda = random.randint(0,2)
                        cima_baixo = random.randint(0,2)
                        if direita_esquerda == 1:
                            gato.speedx = vel_padrao_vovo
                        if direita_esquerda == 2:
                            gato.speedx = -vel_padrao_vovo
                        if direita_esquerda == 0:
                            gato.speedx = 0
                        if cima_baixo == 1:
                            gato.speedy = vel_padrao_vovo
                        if cima_baixo == 2:
                            gato.speedy = -vel_padrao_vovo
                        if cima_baixo == 0:
                            gato.speedy = 0

                if event.type == ALTERA_MOVIMENTO_VOVO:
                    pvovo_x = vovo.rect.x
                    pvovo_y = vovo.rect.y

                    pplayer_x = player.rect.x
                    pplayer_y = player.rect.y
            
                    if pvovo_x > pplayer_x:
                        vovo.speedx = -vel_padrao_vovo

                    if pvovo_x < pplayer_x:
                        vovo.speedx = vel_padrao_vovo
                    if pvovo_y > pplayer_y:
                        vovo.speedy = -vel_padrao_vovo
                    if pvovo_y < pplayer_y:
                        vovo.speedy = vel_padrao_vovo
                
            if event.type == pygame.QUIT:
                game = False

            if estado == TROCA_ROUND: # Adicionar aqui a mudança de personagem (if numrounds<=3) e tela de fim do jogo (numrounds<=0)
                Left = 0
                Right = 0
                Up = 0
                Down = 0
                player.speedx = 0
                player.speedy = 0
                if numrounds <= 0:
                    estado = FIM
                else:
                    texto_round = font.render('ROUND {0}'.format(7-numrounds), True, WHITE)
                    numrounds -= 1
                    window.fill(BLACK)
                    window.blit(texto_round, (WIDTH/2-70,HEIGHT/2-70))
                    pygame.display.update()
                    pygame.time.delay(2000)
                    tempo = pygame.time.get_ticks()
                    ultimotempo.append(tempo)
                    ultimotempogato.append(tempo)
                    
                    player.rect.centerx = WIDTH/2
                    player.rect.bottom = HEIGHT - 40
                    moedas = respawnamoedas(estado, moedas)

                    estado = JOGANDO

            if estado == FIM:
                if player.moedas >= 50 and player.queijos >= 30:
                    window.blit(dicionary_assets['IMAGE_VICTORY'], (0,0))
                    text_moedas = font.render(f'{player.moedas}', True, YELLOW)
                    text_queijos = font.render(f'{player.queijos}', True, YELLOW)
                    window.blit(text_queijos, (160, 340))
                    window.blit(text_moedas, (160, 420))
                    pygame.display.update()
                else:
                    window.blit(dicionary_assets['IMAGE_GAME_OVER'], (0,0))
                    text_moedas = font.render(f'{player.moedas}', True, YELLOW)
                    text_queijos = font.render(f'{player.queijos}', True, YELLOW)
                    window.blit(text_queijos, (160, 340))
                    window.blit(text_moedas, (160, 420))
                    pygame.display.update()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        estado = INICIO
                    if event.key == pygame.K_ESCAPE:
                        game = False

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
                    
        sprites.update()
        enemies.update()
        enemies_cat.update()
        pontuacao = font.render('Pontos: {0}'.format(player.moedas), True, BLACK)
        display_queijos = font.render('Queijos: {0}'.format(player.queijos), True, BLACK)
        texto_tempo = font.render('{0:.1f} s'.format((tempo - ultimotempo[-1])/1000), True, BLACK)

        if pygame.sprite.spritecollide(player, enemies, True, pygame.sprite.collide_mask):
            risada_sound.set_volume(3)
            vovo.vovo_sound.play()
            colisao = True


        if pygame.sprite.spritecollide(player, enemies_cat, True, pygame.sprite.collide_mask):
            player.sound_caught.play()
            colisao = True

        if colisao: #Se colisao com inimigo -> morte
            colisao = False
            musica_fundo = False
            estado = TROCA_ROUND

            enemies_cat = pygame.sprite.Group()
            enemies = pygame.sprite.Group()
            queijos = pygame.sprite.Group()

            vovo = inimigo([dicionary_assets['IMAGE_GRANDMA_RIGHT'], dicionary_assets['IMAGE_GRANDMA_LEFT']],'', risada_sound)

            perto = True
            while(perto):
                x_enemy = random.randint(60, WIDTH-60)
                if((x_enemy > (player.rect.x + 200)) or (x_enemy < (player.rect.x - 200))):
                    perto = False
            vovo.rect.x = x_enemy

            enemies.add(vovo)
            
            sprites.add(player)

            

        if pygame.sprite.spritecollide(player, moedas, True): #Se colisao com moeda -> ganha moeda e cria uma nova moeda
            player.moedas += 1
            moedas = respawnamoedas(estado, moedas)

        if pygame.sprite.spritecollide(player, queijos, True): #Se colisao com queijo -> ganha queijo e cria uma nova moeda
            player.queijos += 1
            queijos = respawnoqueijo(estado, queijos)

        # ----- Gera saídas
        if estado == JOGANDO:

            window.blit(dicionary_assets['IMAGE_BACKGROUND'],(0,0)) # Coloca o dicionary_assets['IMAGE_BACKGROUND']
            
            moedas.draw(window)
            queijos.draw(window)
            sprites.draw(window)
            enemies.draw(window)
            enemies_cat.draw(window)
            
            window.blit(pontuacao, (230, 630))
            window.blit(display_queijos, (450, 630))
            window.blit(texto_tempo, (10, 630))

        # ----- Atualiza estado do jogo
        pygame.display.update()  # Mostra o novo frame para o jogador