import pygame
from pygame.locals import *
import Ferramentas_menu2 as ferramentas2
import menu

pygame.init() #inicia o pygame

#cores
vermelho = [255,0,0]
preto = [0, 0, 0]

tamanho = largura, altura = (700, 460) #tamanho da tela
pygame.display.set_caption('COBRINHA SHOW') # mensagem no topo da tela
tela = pygame.display.set_mode(tamanho)

imagem_fundo = 'ajuda.jpg' #imagem de fundo
imagem = pygame.image.load(imagem_fundo).convert()
clock = pygame.time.Clock()

def ajuda(): #função de ajuda do jogo

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
        tela.blit(imagem, (0, 0))
        pygame.display.update()

        #opçõe de volta ao menu principal
        cursor3 = ferramentas2.fer_menu2(tela, ['VOLTAR'], 30, 425, None, 30, 1.4, preto, vermelho)

        if cursor3 == 0: #se a opção escolhida for 0, volta ao menu principal
            menu.menu_principal()

        exit()


