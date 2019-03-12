import pygame
from pygame.locals import *
import ferramentas_menu as ferramentas
import menu

pygame.init() #inicia o pygame

#cores
vermelho = [255,0,0]
preto = [0, 0, 0]

tamanho = largura, altura = (700,460) #tamanho da tela
pygame.display.set_caption('COBRINHA SHOW') #mensagem no topo da tela
tela = pygame.display.set_mode(tamanho)

imagem_fundo = 'creditos.jpg' #imagem de fundo
imagem = pygame.image.load(imagem_fundo).convert()
clock = pygame.time.Clock()

def creditos_snake(): #função créditos

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
        tela.blit(imagem, (0, 0))
        pygame.display.update()

        #opçõe de volta ao menu principal
        cursor4 = ferramentas.fer_menu(tela, ['VOLTAR'], 30, 425, None, 30, 1.4, preto, vermelho)

        if cursor4 == 0: #se a opção escolhida for 0, volta ao menu principal
            menu.menu_principal()

        exit()
