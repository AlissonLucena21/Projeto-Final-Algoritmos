import pygame
import sys
import time
import random
import fim_nivel1

pygame.init()# inicia o pygame

tela = pygame.display.set_mode((720, 460))# tamanho da tela
pygame.display.set_caption('COBRINHA SHOW')# mensagem do topo da tela

vermelho = [255, 0, 0]# cor da comida que almenta 1 ponto no placar
preto = [0, 0, 0]# cor da cobrinha,barreira,placar
verde = [115, 230, 0]# cor de fundo da tela
azul = [0, 128, 255]# cor da comida q faz a cobrinha perder na hora

# posição e largura das bordas laterais
lateral1 = pygame.Rect(0, 20, 720, 4)
lateral2 = pygame.Rect(0, 456, 720, 4)
lateral3 = pygame.Rect(0, 22, 4, 720)
lateral4 = pygame.Rect(696, 20,4, 720)

relogio = pygame.time.Clock()# criação do relogio
global pos_cobra
pos_cobra = [100, 50]# posicao inical da cobrinha
global tamanho
tamanho = [[100, 50], [90, 50], [80, 50]]  # ,[70,50],[60,50],[50,50],[40,50],[30,50],[20,50]

global direcao
direcao = 'RIGHT' # direção inicial da cobrinha
global mudar_direcao
mudar_direcao = direcao # para poder controlar o movimento da cobrinha

# função que chama as laterais para aparecer na tela
def lateral():
    pygame.draw.rect(tela, preto, lateral1)
    pygame.draw.rect(tela, preto, lateral2)
    pygame.draw.rect(tela, preto, lateral3)
    pygame.draw.rect(tela, preto, lateral4)

# função utilizada para fim de jogo
def fim_jogo():

    fonte_gameover = pygame.font.SysFont('System Negrito', 90) # fonte e tamanho da mensagem final
    mensagem_final = fonte_gameover.render('Fim de Jogo!', True, vermelho)# mensagem final e cor
    posisao_mensagem = mensagem_final.get_rect()
    posisao_mensagem.midtop = (360, 190)# posição da mensagem
    tela.blit(mensagem_final, posisao_mensagem)
    placar(0) # chamando o placar para aperecer na mensagem final
    pygame.display.flip()
    time.sleep(2) # tempo que a mensagem vai ficar na tela
    fim_nivel1.fim1() # chamando as oções de fim de jogo

# função do placar
def placar(choice=1):

    fonte_placar = pygame.font.SysFont('coopeer preto', 20) # fonte e tamanho
    mensagem_final = fonte_placar.render('PONTUAÇÃO: {0}'.format(pontos), True, preto) # mensagem final e cor do placar
    posicao_mensagem = mensagem_final.get_rect()

    if choice == 1:
        posicao_mensagem.midtop = (55, 5) # posição do placar durante o jogo
    else:
        posicao_mensagem.midtop = (360, 150) # posição do placar na fução fim_jogo()


    tela.blit(mensagem_final, posicao_mensagem)

# função sair
def sair():

    pygame.quit()
    sys.exit()

# função onde ativa as setas do teclado e coloca a posição em mudar_direção
def recebe_direcao(mudar_direcao,event):

    if event.key == pygame.K_RIGHT:
        mudar_direcao = 'RIGHT'

    if event.key == pygame.K_LEFT:
        mudar_direcao = 'LEFT'

    if event.key == pygame.K_UP:
        mudar_direcao = 'UP'

    if event.key == pygame.K_DOWN:
        mudar_direcao = 'DOWN'

    if event.key == pygame.K_ESCAPE:
        pygame.event.post(pygame.event.Event(pygame.QUIT))

    return mudar_direcao

#função que faz a cobra mudar a direção
def muda_direcao(mudar_direcao, direcao):

    if mudar_direcao == 'RIGHT' and not direcao == 'LEFT':
        direcao = 'RIGHT'

    if mudar_direcao == 'LEFT' and not direcao == 'RIGHT':
        direcao = 'LEFT'

    if mudar_direcao == 'UP' and not direcao == 'DOWN':
        direcao = 'UP'

    if mudar_direcao == 'DOWN' and not direcao == 'UP':
        direcao = 'DOWN'
    return direcao

# posição que faz a cobrinha andar
def posicao(direcao, pos_cobra):

    if direcao == 'RIGHT':
        pos_cobra[0] += 10

    if direcao == 'LEFT':
        pos_cobra[0] -= 10

    if direcao == 'UP':
        pos_cobra[1] -= 10

    if direcao == 'DOWN':
        pos_cobra[1] += 10

#funcao que chama a comida na tela
def comida_na_tela():
    #define a cor posição e tamanho da comida
    pygame.draw.rect(tela, vermelho, pygame.Rect(pos_comida[0], pos_comida[1], 10, 10))
    pygame.draw.rect(tela, azul, pygame.Rect(pos_comida_ruim[0], pos_comida_ruim[1], 10, 10))

# função que chama o jogo
def jogo(pos_cobra, tamanho, mudar_direcao, direcao):

    global pontos
    pontos = 0 #contador do placar

    # coloca as comidas Aleatoriamente na tela e gera
    global pos_comida
    pos_comida = [random.randrange(4, 69) * 10, random.randrange(2, 46) * 10]

    global gerar_comida
    gerar_comida = True

    global pos_comida_ruim
    pos_comida_ruim = [random.randrange(4, 69) * 10, random.randrange(2, 46) * 10]

    global gerar_comida_ruim
    gerar_comida_ruim = True

    #laço onde o jogo roda
    while True:
        # laço que da a condição de fechar e usa a condição do pygame para verificar se foi clicado algum botão do teclado
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sair()

            elif event.type == pygame.KEYDOWN:
                direcao = recebe_direcao(mudar_direcao,event)

        muda_direcao(mudar_direcao, direcao)

        posicao(direcao, pos_cobra)

        tamanho.insert(0, list(pos_cobra))

        # fazer que a cobrinha coma a comida
        if pos_cobra[0] == pos_comida[0] and pos_cobra[1] == pos_comida[1]:
            pontos += 1
            gerar_comida = False
        else:
            tamanho.pop()

        #gera novamente a comida em outro lugar da tela
        if gerar_comida == False:
            pos_comida = [random.randrange(4, 69) * 10, random.randrange(2, 46) * 10]
        gerar_comida = True

        tela.fill(verde) # colocando a cor de fundo

        #laço que define a cor e o tamanho da cobrinha
        for pos in tamanho:
            pygame.draw.rect(tela, preto, pygame.Rect(pos[0], pos[1], 10, 10))

        # fazer que a cobrinha coma a comida de cor azul e morra
        if pos_cobra[0] == pos_comida_ruim[0] and pos_cobra[1] == pos_comida_ruim[1]:
            gerar_comida_ruim = False
            fim_jogo()

        comida_na_tela()

        # condição para que a cobrinha morra casso passe da bordas laterais
        if pos_cobra[0] > 699 or pos_cobra[0] < 0:
            fim_jogo()


        if pos_cobra[1] > 450 or pos_cobra[1] < 19:
            fim_jogo()

        # laço que faz a cobrinha morrer caso ela toque no proprio corpo
        for block in tamanho[1:]:

            if pos_cobra[0] == block[0] and pos_cobra[1] == block[1]:
                fim_jogo()


        placar()
        lateral()


        pygame.display.flip()
        relogio.tick(10) #velocidade que o jogo vai rodar



def rodar1():
    pos_cobra= [100,50]
    tamanho= [[100, 50], [90, 50], [80, 50]]
    jogo(pos_cobra, tamanho, mudar_direcao, direcao)

