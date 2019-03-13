import pygame
import sys
import time
import random
import fim_nivel3

pygame.init()# inicia o pygame

tela = pygame.display.set_mode((700, 460))# tamanho da tela
pygame.display.set_caption('COBRINHA SHOW')# mensagem do topo da tela

vermelho = [255, 0, 0]# cor da comida que almenta 1 ponto no placar
preto = [0, 0, 0]# cor da cobrinha,barreira,placar
verde = [115, 230, 0]# cor de fundo da tela
azul = [0, 128, 255]# cor da comida q faz a cobrinha perder na hora
amarelo = [255, 255, 0]# cor da comida q faz a cobrinha perder 3 pontos no placar

# posição e largura das bordas laterais
lateral1 = pygame.Rect(0, 20, 720, 4)
lateral2 = pygame.Rect(0, 456, 720, 4)
lateral3 = pygame.Rect(0, 22, 4, 720)
lateral4 = pygame.Rect(696, 20, 4, 720)

# posição e largura das barreiras laterais
obstaculo = pygame.Rect(45, 60, 5, 50)
obstaculo2 = pygame.Rect(664, 60, 5, 50)
obstaculo3 = pygame.Rect(45, 370, 5, 50)
obstaculo4 = pygame.Rect(664, 370, 5, 50)
obstaculo5 = pygame.Rect(45, 55, 50, 5)
obstaculo6 = pygame.Rect(619, 55, 50, 5)
obstaculo7 = pygame.Rect(45, 420, 50, 5)
obstaculo8 = pygame.Rect(619, 420, 50, 5)

#poição e largura das barreira do meio
obstaculo9 = pygame.Rect(115, 105, 200, 5)
obstaculo10 = pygame.Rect(350, 105, 250, 5)
obstaculo11 = pygame.Rect(115, 375, 200, 5)
obstaculo12 = pygame.Rect(350, 375, 250, 5)
obstaculo13 = pygame.Rect(115, 110, 5, 100)
obstaculo14 = pygame.Rect(115, 240, 5, 135)
obstaculo15 = pygame.Rect(600, 105, 5, 100)
obstaculo16 = pygame.Rect(600, 239, 5, 141)

relogio = pygame.time.Clock()# criação do relogio

pos_cobra = [100, 50]# posicao inical da cobrinha
tamanho = [[100, 50], [90, 50], [80, 50]]  # ,[70,50],[60,50],[50,50],[40,50],[30,50],[20,50]

global direcao
direcao = 'RIGHT'# direção inicial da cobrinha
global mudar_direcao
mudar_direcao = direcao# para poder controlar o movimento da cobrinha

# função que chama as laterais para aparecer na tela
def lateral():
    pygame.draw.rect(tela, preto, lateral1)
    pygame.draw.rect(tela, preto, lateral2)
    pygame.draw.rect(tela, preto, lateral3)
    pygame.draw.rect(tela, preto, lateral4)

# função que chama as laterais e a do meio  para aparecer na tela
def barreira():
    pygame.draw.rect(tela, preto, obstaculo)
    pygame.draw.rect(tela, preto, obstaculo2)
    pygame.draw.rect(tela, preto, obstaculo3)
    pygame.draw.rect(tela, preto, obstaculo4)
    pygame.draw.rect(tela, preto, obstaculo5)
    pygame.draw.rect(tela, preto, obstaculo6)
    pygame.draw.rect(tela, preto, obstaculo7)
    pygame.draw.rect(tela, preto, obstaculo8)
    pygame.draw.rect(tela, preto, obstaculo9)
    pygame.draw.rect(tela, preto, obstaculo10)
    pygame.draw.rect(tela, preto, obstaculo11)
    pygame.draw.rect(tela, preto, obstaculo12)
    pygame.draw.rect(tela, preto, obstaculo13)
    pygame.draw.rect(tela, preto, obstaculo14)
    pygame.draw.rect(tela, preto, obstaculo15)
    pygame.draw.rect(tela, preto, obstaculo16)

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
    fim_nivel3.fim3() # chamando as oções de fim de jogo

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
def recebe_direcao(mudar_direcao, event):

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
    pygame.draw.rect(tela, amarelo, pygame.Rect(pos_comida_ruim2[0], pos_comida_ruim2[1], 10, 10))

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

    global pos_comida_ruim2
    pos_comida_ruim2 = [random.randrange(4, 69) * 10, random.randrange(2, 46) * 10]

    global gerar_comida_ruim2
    gerar_comida_ruim2 = True

    # laço onde o jogo roda
    while True:
        # laço que da a condição de fechar e usa a condição do pygame para verificar se foi clicado algum botão do teclado
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair()

            elif event.type == pygame.KEYDOWN:
                direcao = recebe_direcao(mudar_direcao, event)

        muda_direcao(mudar_direcao, direcao)

        posicao(direcao, pos_cobra)

        tamanho.insert(0, list(pos_cobra))

        # fazer que a cobrinha coma a comida
        if pos_cobra[0] == pos_comida[0] and pos_cobra[1] == pos_comida[1]:
            pontos += 1
            gerar_comida = False
        else:
            tamanho.pop()

        # gera novamente a comida em outro lugar da tela
        if gerar_comida == False:
            pos_comida = [random.randrange(4, 69) * 10, random.randrange(2, 46) * 10]
        gerar_comida = True

        tela.fill(verde)# colocando a cor de fundo

        # laço que define a cor e o tamanho da cobrinha
        for pos in tamanho:
            pygame.draw.rect(tela, preto, pygame.Rect(pos[0], pos[1], 10, 10))

        # fazer que a cobrinha coma a comida de cor azul e morra
        if pos_cobra[0] == pos_comida_ruim[0] and pos_cobra[1] == pos_comida_ruim[1]:
            gerar_comida_ruim = False
            fim_jogo()

        # fazer que a cobrinha coma a comida de cor amarela e diminuir 3 pontos no placar
        if pos_cobra[0] == pos_comida_ruim2[0] and pos_cobra[1] == pos_comida_ruim2[1]:
            gerar_comida_ruim2 = False
            pontos -= 3

        # gera novamente a comida amarela em outro lugar da tela
        if gerar_comida_ruim2 == False:
            pos_comida_ruim2 = [random.randrange(4, 69) * 10, random.randrange(2, 46) * 10]
        gerar_comida_ruim2 = True

        comida_na_tela()
        # condição se os pontos for menor que 0 fim de jogo
        if pontos < 0:
            fim_jogo()

        # condição para que a cobrinha morra casso passe da bordas laterais
        if pos_cobra[0] > 699 or pos_cobra[0] < 0:
            fim_jogo()

        if pos_cobra[1] > 450 or pos_cobra[1] < 19:
            fim_jogo()

        # condição para que a cobrinha morra casso bata nas barreiras
        if pos_cobra[0] == 40 and (pos_cobra[1] >= 60 and pos_cobra[1] <= 100):
            fim_jogo()

        if pos_cobra[0] == 660 and (pos_cobra[1] >= 60 and pos_cobra[1] <= 100):
            fim_jogo()

        # condição para que a cobrinha morra casso bata nas barreiras em forma de l
        if pos_cobra[0] == 40 and (pos_cobra[1] >= 365 and pos_cobra[1] <= 410):
            fim_jogo()

        if pos_cobra[0] == 660 and (pos_cobra[1] >= 365 and pos_cobra[1] <= 410):
            fim_jogo()
        if (pos_cobra[0] >= 50 and pos_cobra[0] <= 99) and pos_cobra[1] == 50:
            fim_jogo()

        if (pos_cobra[0] >= 619 and pos_cobra[0] <= 661) and pos_cobra[1] == 50:
            fim_jogo()

        if (pos_cobra[0] >= 50 and pos_cobra[0] <= 99) and pos_cobra[1] == 420:
            fim_jogo()

        if (pos_cobra[0] >= 619 and pos_cobra[0] <= 661) and pos_cobra[1] == 420:
            fim_jogo()

        # condição para que a cobrinha morra casso bata nas barreiras do meio
        if (pos_cobra[0] >= 110 and pos_cobra[0] <= 310) and pos_cobra[1] == 100:
            fim_jogo()

        if (pos_cobra[0] >= 350 and pos_cobra[0] <= 600) and pos_cobra[1] == 100:
            fim_jogo()

        if (pos_cobra[0] >= 110 and pos_cobra[0] <= 310) and pos_cobra[1] == 380:
            fim_jogo()

        if (pos_cobra[0] >= 350 and pos_cobra[0] <= 600) and pos_cobra[1] == 380:
            fim_jogo()

        if pos_cobra[0] == 110 and (pos_cobra[1] >= 100 and pos_cobra[1] <= 200):
            fim_jogo()

        if pos_cobra[0] == 110 and (pos_cobra[1] >= 235 and pos_cobra[1] <= 370):
            fim_jogo()

        if pos_cobra[0] == 600 and (pos_cobra[1] >= 100 and pos_cobra[1] <= 200):
            fim_jogo()

        if pos_cobra[0] == 600 and (pos_cobra[1] >= 230 and pos_cobra[1] <= 370):
            fim_jogo()

        # laço que faz a cobrinha morrer caso ela toque no proprio corpo
        for block in tamanho[1:]:
            if pos_cobra[0] == block[0] and pos_cobra[1] == block[1]:
                fim_jogo()

        placar()
        lateral()
        barreira()
        pygame.display.flip()
        relogio.tick(25)# velocidade que o jogo vai rodar


def rodar3():
    pos_cobra= [100,50]
    tamanho= [[100, 50], [90, 50], [80, 50]]
    jogo(pos_cobra, tamanho, mudar_direcao, direcao)