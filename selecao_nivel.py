import pygame
from pygame.locals import *
import ferramentas_menu as ferramentas
import nivel1
import nivel2
import nivel3

pygame.init() # inicia o pygame

#cores
vermelho = [255,0,0]
preto = [0, 0, 0]

tamanho = largura, altura = (700, 460) #tamanho da tela
pygame.display.set_caption('COBRINHA SHOW') # mensagem no topo da tela
tela = pygame.display.set_mode(tamanho)

imagen_fundo = 'menu.jpg' #imagem de fundo do menu de seleção de nível
imagem = pygame.image.load(imagen_fundo).convert()
clock = pygame.time.Clock()

def menu_nivel(): #menu de seleção de nível

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
        tela.blit(imagem, (0, 0))
        pygame.display.update()

        #opções de menu seleção de nível
        cursor2 = ferramentas.fer_menu(tela, ['Fácil', 'Médio', 'Difícil'], 30, 149, None, 40, 1.2, preto, vermelho)

        if cursor2 == 0: #se a opção escolhida for 0, executa o nível fácil do jogo
            nivel1.rodar1()

        elif cursor2 == 1: #se a opção escolhida for 2, executa o nível médio de jogo
            nivel2.rodar2()

        elif cursor2 == 2: #se a opção escolhida for 3, executa o nível difícil de jogo
            nivel3.rodar3()

        exit()
