# Importa pacotes e arquivos
import pygame
from assets.dados.config import *
import random
from sprites import *
from assets.dados.assets import load

def gamescreen(window):
    # Carrega arquivos do jogo
    dicionary_assets = load()
    
    # Instancia a fonte padrão do jogo
    font = dicionary_assets['FONT_GAME']
    
    # Função de criação de itens (moedas ou queijos)
    def respawnItem(status, item_group, type_item):
        item = {}
        if status == TROCA_ROUND:
            item_group = pygame.sprite.Group()
        if(type_item == 'moeda'):
            item['max_quantity'] = QUANTITY_COINS_PER_ROUND
            item['image'] = dicionary_assets['IMAGE_COIN']
            item['sound'] = dicionary_assets['SOUND_COIN']
        if(type_item == 'queijo'):
            item['max_quantity'] = QUANTITY_CHEESES_PER_ROUND
            item['image'] = dicionary_assets['IMAGE_CHEESE']
            item['sound'] = dicionary_assets['SOUND_CHEESE']
        while len(item_group) < item['max_quantity']:
            new_item = coin(item['image'],item['sound'])
            item_group.add(new_item)
        if status != INICIO and status != TROCA_ROUND:
            new_item.sound.play()
        return item_group

    # Função de criação de novo inimigo (gato)
    def respawnCat(enemies_gato):
        while True:
            new_enemy = inimigo([dicionary_assets['IMAGE_CAT'], dicionary_assets['IMAGE_CAT']],dicionary_assets['SOUND_CAT'])
            new_enemy.rect.centerx = random.randint(CAT_WIDTH, SCREEN_WIDTH - CAT_WIDTH)
            new_enemy.rect.bottom = random.randint(CAT_HEIGHT, SCREEN_HEIGHT - CAT_HEIGHT)
            new_enemy.sound.play()
            manobra = pygame.sprite.Group()
            manobra.add(new_enemy)
            if not pygame.sprite.spritecollide(player, manobra, True):
                enemies_gato.add(new_enemy)
                break
            manobra = pygame.sprite.Group()
        return enemies_gato

    # Toca música de fundo
    def playMusicLoop(music, volume):
        pygame.mixer.music.load(music)
        pygame.mixer.music.set_volume(volume)
        pygame.mixer.music.play(loops=-1)

    # Variável que mantém o jogo em looping
    game = True
    # Estado inicial do jogo
    estado = INICIO
    # Instanciando arrays de tempo
    last_time = [0]
    last_time_cat = [0]
    # Instanciando timer
    clock = pygame.time.Clock()

    # Criando o jogador
    player = jogador(dicionary_assets['IMAGE_MOUSE'],dicionary_assets['SOUND_MOUSE'])
    # Criando vovó em um local do eixo X aleatório
    vovo = inimigo([dicionary_assets['IMAGE_GRANDMA_RIGHT'], dicionary_assets['IMAGE_GRANDMA_LEFT']],dicionary_assets['SOUND_GRANDMA'])
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
    
    Left = 0
    Right = 0
    Up = 0
    Down = 0
    round = 1
    #Tela Inicial

    colisao = False
    # ===== Loop principal =====
    while game:
        clock.tick(FPS)
        tempo = pygame.time.get_ticks()

        # ----- Trata eventos
        for event in pygame.event.get():

            if estado == INICIO:
                playMusicLoop(dicionary_assets['SOUND_BACKGROUND_INTRO'], BACKGROUND_VOLUME)

                round = 1
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
                last_time.append(tempo)
                last_time_cat.append(tempo)
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

                if tempo-last_time_cat[-1] > TIME_RESPAWN_CAT:
                    last_time_cat.append(tempo)
                    enemies_cat_group = respawnCat(enemies_cat_group)
                    pygame.time.set_timer(ALTERA_MOVIMENTO_GATO, CHANGE_MOVIMENT_CAT)

                if event.type == ALTERA_MOVIMENTO_GATO:
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

                if event.type == ALTERA_MOVIMENTO_VOVO:
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
                
            if event.type == pygame.QUIT:
                game = False

            if estado == TROCA_ROUND:
                pygame.mixer.music.load(dicionary_assets['SOUND_BACKGROUND'])
                pygame.mixer.music.play(loops=-1)
                pygame.time.set_timer(ALTERA_MOVIMENTO_VOVO, CHANGE_MOVIMENT_GRANDMA)
                Left = 0
                Right = 0
                Up = 0
                Down = 0
                player.speedx = 0
                player.speedy = 0
                if round > QUANTITY_ROUNDS:
                    estado = FIM
                else:
                    texto_round = font.render('ROUND {0}'.format(round), True, WHITE)
                    round += 1
                    window.fill(BLACK)
                    window.blit(texto_round, (SCREEN_WIDTH/2-70,SCREEN_HEIGHT/2-70))
                    pygame.display.update()
                    pygame.time.delay(2000)
                    tempo = pygame.time.get_ticks()
                    last_time.append(tempo)
                    last_time_cat.append(tempo)
                    
                    player.rect.centerx = SCREEN_WIDTH/2
                    player.rect.bottom = SCREEN_HEIGHT - 40
                    moedas_group = respawnItem(estado, moedas_group, 'moeda')
                    queijos_group = respawnItem(estado, queijos_group, 'queijo')

                    estado = JOGANDO
                    

            if estado == FIM:
                if player.moedas >= QUANTITY_COINS_TO_WIN and player.queijos >= QUANTITY_CHEESE_TO_WIN:
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
                if event.type == pygame.KEYUP:
                    # Dependendo da tecla, altera a velocidade.
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
                    
        player_group.update()
        enemies_group.update()
        enemies_cat_group.update()
        pontuacao = font.render('Pontos: {0}'.format(player.moedas), True, BLACK)
        display_queijos = font.render('Queijos: {0}'.format(player.queijos), True, BLACK)
        texto_tempo = font.render('{0:.1f} s'.format((tempo - last_time[-1])/1000), True, BLACK)

        if pygame.sprite.spritecollide(player, enemies_group, True, pygame.sprite.collide_mask):
            vovo.sound.play()
            colisao = True

        if pygame.sprite.spritecollide(player, enemies_cat_group, True, pygame.sprite.collide_mask):
            player.sound.play()
            colisao = True

        if colisao: #Se colisao com inimigo -> morte
            colisao = False
            playMusicLoop(dicionary_assets['SOUND_BACKGROUND'], BACKGROUND_VOLUME)
            estado = TROCA_ROUND

            enemies_cat_group = pygame.sprite.Group()
            enemies_group = pygame.sprite.Group()
            queijos_group = pygame.sprite.Group()

            vovo = inimigo([dicionary_assets['IMAGE_GRANDMA_RIGHT'], dicionary_assets['IMAGE_GRANDMA_LEFT']],dicionary_assets['SOUND_GRANDMA'])
            vovo.rect.x = random.randint(60, SCREEN_WIDTH-60)
            vovo.speedx = 0
            vovo.speedy = 0

            enemies_group.add(vovo)
            player_group.add(player)

            

        if pygame.sprite.spritecollide(player, moedas_group, True): #Se colisao com moeda -> ganha moeda e cria uma nova moeda
            player.moedas += 1
            moedas_group = respawnItem(estado, moedas_group, 'moeda')

        if pygame.sprite.spritecollide(player, queijos_group, True): #Se colisao com queijo -> ganha queijo e cria uma nova moeda
            player.queijos += 1
            queijos_group = respawnItem(estado, queijos_group, 'queijo')

        # ----- Gera saídas
        if estado == JOGANDO:

            window.blit(dicionary_assets['IMAGE_BACKGROUND'],(0,0)) # Coloca o dicionary_assets['IMAGE_BACKGROUND']
            
            moedas_group.draw(window)
            queijos_group.draw(window)
            player_group.draw(window)
            enemies_group.draw(window)
            enemies_cat_group.draw(window)
            
            window.blit(pontuacao, (230, 630))
            window.blit(display_queijos, (450, 630))
            window.blit(texto_tempo, (10, 630))

        # ----- Atualiza estado do jogo
        pygame.display.update()  # Mostra o novo frame para o jogador