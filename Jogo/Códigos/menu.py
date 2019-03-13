import pygame
from pygame.locals import *
import ferramentas_menu as ferramentas
import selecao_nivel
import ajuda
import creditos

pygame.init() #Inicia o pygame

#cores
vermelho = [255,0,0]
preto = [0, 0, 0]

tamanho = largura, altura = (700, 460) #tamanho da tela
pygame.display.set_caption('COBRINHA SHOW') #mensagem do topo da tela
tela = pygame.display.set_mode(tamanho)

imagem_fundo = 'menu.jpg' #imagem de fundo do menu
imagem = pygame.image.load(imagem_fundo).convert()
clock = pygame.time.Clock()

def menu_principal(): #função do menu principal

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
        tela.blit(imagem, (0, 0))
        pygame.display.update()

        #opcções do menu principal
        cursor = ferramentas.fer_menu(tela, ['Novo Jogo', 'Ajuda', 'Créditos', 'Sair'], 30, 149, None, 40, 1.4, preto, vermelho)

        if cursor == 0: #se a opção escolhida for 0, chama o menu onde é selecionado o nível de jogo
            selecao_nivel.menu_nivel()

        elif cursor == 1: #se a opção escolhida for 1, chama a ajuda do jogo
            ajuda.ajuda()

        elif cursor == 2: #se a opção escolhida for 2, chama os créditos do jogo
            creditos.creditos_snake()

        elif cursor == 3: #se a opção escolhida for 3, finaliza o jogo
            pygame.quit()

        exit()

