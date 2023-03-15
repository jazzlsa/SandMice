# Importa pacotes e arquivos
import pygame
from config import *
import random
from sprites import *
from assets import *

def gamescreen(window):
    # Carrega arquivos do jogo
    dicionary_images = load_images()
    dicionary_sounds = load_sounds()
    dicionary_fonts = load_fonts()
    
    # Instancia a fonte padrão do jogo
    font = dicionary_fonts['FONT_GAME']
    
    # Função de criação de itens (moedas ou queijos)
    def respawnItem(status, item_group, type_item):
        item = {}
        if status == TROCA_ROUND:
            item_group = pygame.sprite.Group()
        if(type_item == 'moeda'):
            item['max_quantity'] = QUANTITY_COINS_PER_ROUND
            item['image'] = dicionary_images['IMAGE_COIN']
            item['sound'] = dicionary_sounds['SOUND_COIN']
        if(type_item == 'queijo'):
            item['max_quantity'] = QUANTITY_CHEESES_PER_ROUND
            item['image'] = dicionary_images['IMAGE_CHEESE']
            item['sound'] = dicionary_sounds['SOUND_CHEESE']
        while len(item_group) < item['max_quantity']:
            new_item = coin([item['image']],item['sound'])
            item_group.add(new_item)
        if status != INICIO and status != TROCA_ROUND:
            if(MUTE!=True):
                new_item.sound.play()
        return item_group

    # Função de criação de novo inimigo (gato)
    def respawnCat(enemy_cat):
        while True:
            new_enemy = inimigo([dicionary_images['IMAGE_CAT'], dicionary_images['IMAGE_CAT']],dicionary_sounds['SOUND_CAT'])
            new_enemy.rect.centerx = random.randint(CAT_WIDTH, SCREEN_WIDTH - CAT_WIDTH)
            new_enemy.rect.bottom = random.randint(CAT_HEIGHT, SCREEN_HEIGHT - CAT_HEIGHT)
            if(MUTE!=True):
                new_enemy.sound.play()
            manobra = pygame.sprite.Group()
            manobra.add(new_enemy)
            if not pygame.sprite.spritecollide(player, manobra, True):
                enemy_cat.add(new_enemy)
                break
            manobra = pygame.sprite.Group()
        return enemy_cat

    # Atualiza e desenha os scores na tela
    def changeScreenScore(quantity_coins, quantity_cheese, time):
        display_coins = font.render('Moedas: {0}'.format(quantity_coins), True, BLACK)
        display_cheese = font.render('Queijos: {0}'.format(quantity_cheese), True, BLACK)
        display_time = font.render('{0:.1f} s'.format((time[0] - time[1] - time[2])/1000), True, BLACK)
        window.blit(display_coins, (DISPLAY_COINS_X, DISPLAY_COINS_Y))
        window.blit(display_cheese, (DISPLAY_CHEESE_X, DISPLAY_CHEESE_Y))
        window.blit(display_time, (DISLAY_TIME_X, DISLAY_TIME_Y))
        if(PAUSE):
            printScreenPaused()                
        pygame.display.update()

    def printScreenPaused():
        display_pause = font.render('JOGO PAUSADO',True, RED)
        display_instructions = font.render('Aperte P para continuar',True, RED)
        window.blit(display_pause, ((SCREEN_WIDTH/2)-130, SCREEN_HEIGHT/2))
        window.blit(display_instructions, ((SCREEN_WIDTH/2)-190, (SCREEN_HEIGHT/2)+100))

    # Desenha os Sprites na tela
    def drawSpritesOnScreen():
        window.blit(dicionary_images['IMAGE_BACKGROUND'],(0,0))
        moedas_group.draw(window)
        queijos_group.draw(window)
        player_group.draw(window)
        enemies_cat_group.draw(window)
        enemies_group.draw(window) 

    # Desenha a tela de round
    def drawSpriteRoundScreen():
        texto_round = font.render('ROUND {0}'.format(round), True, WHITE)
        window.fill(BLACK)
        window.blit(texto_round, (SCREEN_WIDTH/2-70,SCREEN_HEIGHT/2-70))
        pygame.display.update()
        pygame.time.delay(DELAY_SCREEN_ROUNDS)

    def drawFinalScreen():
        # Mostra a quantidade de moedas e queijos e atualiza a tela
        text_moedas = font.render(f'{player.moedas}', True, YELLOW)
        text_queijos = font.render(f'{player.queijos}', True, YELLOW)
        window.blit(text_queijos, (FINAL_DISPLAY_CHEESE_X, FINAL_DISPLAY_CHEESE_Y))
        window.blit(text_moedas, (FINAL_DISPLAY_COINS_X, FINAL_DISPLAY_COINS_Y))
        pygame.display.update()


    # Toca música de fundo
    def playMusicLoop(music, volume):
        pygame.mixer.music.load(music)
        if(MUTE != True):
            pygame.mixer.music.set_volume(volume)
        pygame.mixer.music.play(loops=-1)

    # Variável que mantém o jogo em looping
    EXECUTAR = True
    # Variável que define se está mudo ou não
    MUTE = False
    # Variável que define se está pausado ou não
    PAUSE = False
    # Instanciando array de tempo pausado
    tempo_pausado = {}
    tempo_pausado['total'] = 0
    tempo_pausado['inicial'] = 0
    # Estado inicial do jogo
    estado = INICIO
    # Instanciando arrays de tempo
    last_time = [0]
    last_time_cat = [0]
    # Instanciando timer
    clock = pygame.time.Clock()

    # Criando o jogador
    player = jogador([dicionary_images['IMAGE_MOUSE']],dicionary_sounds['SOUND_MOUSE'])
    # Criando vovó em um local do eixo X aleatório
    vovo = inimigo([dicionary_images['IMAGE_GRANDMA_RIGHT'], dicionary_images['IMAGE_GRANDMA_LEFT']],dicionary_sounds['SOUND_GRANDMA'])
    vovo.rect.x = random.randint(60, SCREEN_WIDTH-60)

    # Criando grupos de sprites
    player_group = pygame.sprite.Group()
    enemies_group = pygame.sprite.Group()
    enemies_cat_group = pygame.sprite.Group()
    moedas_group = pygame.sprite.Group()
    queijos_group = pygame.sprite.Group()
    
    # Adicionando os sprites dentro dos grupos
    player_group.add(player)
    enemies_group.add(vovo)
    moedas_group = respawnItem(estado, moedas_group, 'moeda')
    queijos_group = respawnItem(estado, queijos_group, 'queijo')
    
    # Definindo variáveis para inicialização
    Left,Right,Up,Down = 0,0,0,0
    round = 1
    colisao = False

    # O jogo está sendo jogado
    while EXECUTAR:
        # Fica calculando o tempo e os FPS do jogo
        clock.tick(FPS)
        if(PAUSE == False):
            tempo = pygame.time.get_ticks()

        # Trata os estados do jogo
        for event in pygame.event.get():

            if estado == INICIO:
                #Tocando a música de introdução
                playMusicLoop(dicionary_sounds['SOUND_BACKGROUND_INTRO'], BACKGROUND_VOLUME)
                
                # Definindo variáveis para inicialização
                Left,Right,Up,Down,player.speedx,player.speedy,player.moedas,player.queijos = 0,0,0,0,0,0,0,0
                round = 1

                tempo = pygame.time.get_ticks()
                text_vencerqueijos = dicionary_fonts['FONT_PEQUENA'].render(f'{QUANTITY_CHEESE_TO_WIN}', True, YELLOW)
                text_vencermoedas = dicionary_fonts['FONT_PEQUENA'].render(f'{QUANTITY_COINS_TO_WIN}', True, YELLOW)
                window.blit(dicionary_images['START_IMAGE'], (0, 0))
                window.blit(text_vencermoedas, (416, 482))
                window.blit(text_vencerqueijos, (40, 511))
                last_time.append(tempo)
                last_time_cat.append(tempo)
                pygame.display.update()
                while estado == INICIO:
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            estado = TROCA_ROUND
                        if event.type == pygame.QUIT:
                            estado = FIM
                            EXECUTAR = False
            
            # Caso o jogo esteja sendo jogado
            if estado == JOGANDO:

                # Dá respawn no gato
                if tempo-last_time_cat[-1] > TIME_RESPAWN_CAT and PAUSE == False:
                    last_time_cat.append(tempo)
                    enemies_cat_group = respawnCat(enemies_cat_group)
                    pygame.time.set_timer(ALTERA_MOVIMENTO_GATO, CHANGE_MOVIMENT_CAT)

                # Altera o movimento aleatório do gato
                if event.type == ALTERA_MOVIMENTO_GATO and PAUSE == False:
                    for gato in enemies_cat_group:
                        direita_esquerda = random.randint(0,2)
                        cima_baixo = random.randint(0,2)
                        if direita_esquerda == 1:
                            gato.speedx = SPEED_ENEMIES
                        if direita_esquerda == 2:
                            gato.speedx = -SPEED_ENEMIES
                        if direita_esquerda == 0:
                            gato.speedx = 0
                        if cima_baixo == 1:
                            gato.speedy = SPEED_ENEMIES
                        if cima_baixo == 2:
                            gato.speedy = -SPEED_ENEMIES
                        if cima_baixo == 0:
                            gato.speedy = 0
                
                # Altera o movimento da vovó para seguir o jogador
                if event.type == ALTERA_MOVIMENTO_VOVO and PAUSE == False:
                    pvovo_x = vovo.rect.x
                    pvovo_y = vovo.rect.y
                    pplayer_x = player.rect.x
                    pplayer_y = player.rect.y
            
                    if pvovo_x > pplayer_x:
                        vovo.speedx = -SPEED_ENEMIES
                    if pvovo_x < pplayer_x:
                        vovo.speedx = SPEED_ENEMIES
                    if pvovo_y > pplayer_y:
                        vovo.speedy = -SPEED_ENEMIES
                    if pvovo_y < pplayer_y:
                        vovo.speedy = SPEED_ENEMIES
                
                # Altera o movimento do jogador de acordo com a tecla pressionada ou solta
                if event.type == pygame.KEYDOWN and PAUSE == False:
                    if event.key == pygame.K_LEFT and Left == 0:
                        player.speedx -= SPEED_PLAYER
                        Left += 1
                    if event.key == pygame.K_RIGHT and Right == 0:
                        player.speedx += SPEED_PLAYER
                        Right += 1
                    if event.key == pygame.K_UP and Up == 0:
                        player.speedy -= SPEED_PLAYER
                        Up += 1
                    if event.key == pygame.K_DOWN and Down == 0:
                        player.speedy += SPEED_PLAYER
                        Down += 1

                # Verifica se soltou alguma tecla.
                if event.type == pygame.KEYUP and PAUSE == False:
                    if event.key == pygame.K_LEFT and Left == 1:
                        player.speedx += SPEED_PLAYER
                        Left -= 1
                    if event.key == pygame.K_RIGHT and Right == 1:
                        player.speedx -= SPEED_PLAYER
                        Right -= 1
                    if event.key == pygame.K_UP and Up == 1:
                        player.speedy += SPEED_PLAYER
                        Up -= 1
                    if event.key == pygame.K_DOWN and Down == 1:
                        player.speedy -= SPEED_PLAYER
                        Down -= 1

                # Verifica se está ou não mutado, tirando ou voltando o som
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_m:
                        if(MUTE):
                            pygame.mixer.music.set_volume(BACKGROUND_VOLUME)
                            MUTE = False
                        else:    
                            pygame.mixer.music.set_volume(0)
                            MUTE = True

                # Verifica se está pausado o jogo, pausando ou não
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        if(PAUSE):
                            PAUSE = False
                            tempo_pausado['total'] += pygame.time.get_ticks() - tempo_pausado['inicial']
                        else:
                            PAUSE = True
                            Left,Right,Up,Down = 0,0,0,0
                            vovo.speedx,vovo.speedy,player.speedy,player.speedx = 0,0,0,0
                            for gato in enemies_cat_group:
                                gato.speedx,gato.speedy = 0,0
                            tempo_pausado['inicial'] = pygame.time.get_ticks()

            # Caso o jogador tenha perdido o round mostra o próximo
            if estado == TROCA_ROUND:
                # Tocando música de fundo
                playMusicLoop(dicionary_sounds['SOUND_BACKGROUND'], BACKGROUND_VOLUME)
                pygame.time.set_timer(ALTERA_MOVIMENTO_VOVO, CHANGE_MOVIMENT_GRANDMA)
                
                # Definindo variáveis para inicialização do round
                Left,Right,Up,Down,player.speedx,player.speedy = 0,0,0,0,0,0

                if round <= QUANTITY_ROUNDS:
                    drawSpriteRoundScreen()
                    round += 1
                    tempo = pygame.time.get_ticks()
                    last_time.append(tempo)
                    last_time_cat.append(tempo)
                    tempo_pausado['inicial'],tempo_pausado['total'] = 0,0
                    
                    # Volta o jogador na posição inicial
                    player.rect.centerx = SCREEN_WIDTH/2
                    player.rect.bottom = SCREEN_HEIGHT - 40

                    #Cria moedas e queijos para o próximo round
                    moedas_group = respawnItem(estado, moedas_group, 'moeda')
                    queijos_group = respawnItem(estado, queijos_group, 'queijo')

                    estado = JOGANDO
                else:
                    estado = FIM
                    
            # Mostra a imagem do final do jogo
            if estado == FIM and round >= QUANTITY_ROUNDS:
                # Caso o jogador vença
                if player.moedas >= QUANTITY_COINS_TO_WIN and player.queijos >= QUANTITY_CHEESE_TO_WIN:
                    window.blit(dicionary_images['IMAGE_VICTORY'], (0,0))
                # Caso o jogador perca
                else:
                    window.blit(dicionary_images['IMAGE_GAME_OVER'], (0,0))

                # Desenha a imagem final
                drawFinalScreen()

                # Verifica se a tacla de espaço ou ESC foram apertadas
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        estado = INICIO
                    if event.key == pygame.K_ESCAPE:
                        EXECUTAR = False
                
            # Caso o evento de fechamento do pygame seja acionado
            if event.type == pygame.QUIT:
                EXECUTAR = False

        # Caso o jogador colida com a vovó
        if pygame.sprite.spritecollide(player, enemies_group, True, pygame.sprite.collide_mask):
            if(MUTE!=True):
                vovo.sound.play()
            colisao = True

        # Caso o jogador colida com o gato
        if pygame.sprite.spritecollide(player, enemies_cat_group, True, pygame.sprite.collide_mask):
            if(MUTE!=True):
                player.sound.play()
            colisao = True

        # Caso colisão com a vovó ou o gato seja verdadeira
        if colisao:
            colisao = False
            
            # Reinicia música de fundo
            playMusicLoop(dicionary_sounds['SOUND_BACKGROUND'], BACKGROUND_VOLUME)
            
            # Muda o estado para trocar o round
            estado = TROCA_ROUND

            # Reinicia todos os grupos de sprites
            enemies_cat_group = pygame.sprite.Group()
            enemies_group = pygame.sprite.Group()
            queijos_group = pygame.sprite.Group()

            # Reinicia o local da vovó e reinicia a velocidade para 0
            vovo = inimigo([dicionary_images['IMAGE_GRANDMA_RIGHT'], dicionary_images['IMAGE_GRANDMA_LEFT']],dicionary_sounds['SOUND_GRANDMA'])
            vovo.rect.x = random.randint(60, SCREEN_WIDTH-60)
            vovo.speedx,vovo.speedy = 0, 0

            # Instancia a vovó e o jogador no grupo dos sprites
            enemies_group.add(vovo)
            player_group.add(player)
            
        # Jogador pegou uma moeda
        if pygame.sprite.spritecollide(player, moedas_group, True):
            player.moedas += 1
            moedas_group = respawnItem(estado, moedas_group, 'moeda')

        # Jogador pegou um queijo
        if pygame.sprite.spritecollide(player, queijos_group, True):
            player.queijos += 1
            queijos_group = respawnItem(estado, queijos_group, 'queijo')

        # Atualiza o frame o jogo esteja executando
        # Este estado está aqui porque ele indifere dos eventos do jogo
        if estado == JOGANDO:
            drawSpritesOnScreen()
            changeScreenScore(player.moedas, player.queijos, [tempo,last_time[-1],tempo_pausado['total']])
        
        # Atualiza grupos de sprites no jogo
        player_group.update()
        enemies_group.update()
        enemies_cat_group.update()
