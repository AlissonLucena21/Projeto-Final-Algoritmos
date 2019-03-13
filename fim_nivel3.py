import pygame
from pygame.locals import *
import ferramentas_menu as ferramentas
import menu
import nivel3

pygame.init() #inicia o pygame

#cores
vermelho = [255,0,0]
preto = [0, 0, 0]

tamanho = largura, altura = (700, 460) #tamanho da tela
pygame.display.set_caption('COBRINHA SHOW') # mensagem no topo da tela
tela = pygame.display.set_mode(tamanho)

imagem_fundo = 'fim.jpg' #imagem de fundo
imagem = pygame.image.load(imagem_fundo).convert()
clock = pygame.time.Clock()

def fim3(): #função para as opções de fim de jogo

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
        tela.blit(imagem, (0, 0))
        pygame.display.update()

        #opçõe de fim de jogo
        cursor3 = ferramentas.fer_menu(tela, ['Jogar Novamente', 'Voltar', 'Sair'], 30, 149, None, 40, 1.2, preto, vermelho)

        if cursor3 == 0: #se a opção escolhida for 0, reinicia o nível 3
            nivel3.rodar3()

        elif cursor3 == 1 : #se a opção escolhida for 1, volta ao menu principal
            menu.menu_principal()

        elif cursor3 == 2: #se a opção escolhida for 2, sai do jogo
            pygame.quit()

        exit()


