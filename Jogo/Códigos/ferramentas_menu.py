import pygame
import sys


def fer_menu(tela, menu, x_pos=100, y_pos=100, fonte=None, tamanho=70, distancia=1.4, fgcor=(255, 255, 255), cor_cursor=(255, 0, 0), sair=True):

    # Desenha os pontos de menu
    pygame.font.init()
    if fonte == None: minha_fonte = pygame.font.Font(None, tamanho)

    else:
        minha_fonte = pygame.font.SysFont(fonte, tamanho)

    posicao_cursor = 0
    renderizar_caracteres = False

    for i in menu:

        if renderizar_caracteres == False:
            text = minha_fonte.render(str(posicao_cursor + 1) + ".  " + i, True, fgcor)
        else:
            text = minha_fonte.render(chr(char) + ".  " + i, True, fgcor)
            char += 1

        textrect = text.get_rect()
        textrect = textrect.move(x_pos, (tamanho // distancia * posicao_cursor) + y_pos)

        tela.blit(text, textrect)
        pygame.display.update(textrect)
        posicao_cursor += 1

        if posicao_cursor == 9:
            renderizar_caracteres = True
            char = 65

    # Desenha o ">"
    posicao_cursor = 0
    cursor = minha_fonte.render(">", True, cor_cursor)
    cursor_menu = cursor.get_rect()
    cursor_menu = cursor_menu.move(x_pos - (tamanho // distancia), (tamanho // distancia * posicao_cursor) + y_pos)

    #mostra o cursor
    #move o cursor
    selecao_cursor = True
    sair_menu = False
    clock = pygame.time.Clock()
    preencher = pygame.Surface.copy(tela)
    preencher_menu = preencher.get_rect()

    while True:

        clock.tick(30)

        if selecao_cursor == True:

            tela.blit(preencher, preencher_menu)
            pygame.display.update(cursor_menu)
            cursor_menu = cursor.get_rect()
            cursor_menu = cursor_menu.move(x_pos - (tamanho // distancia), (tamanho // distancia * posicao_cursor) + y_pos)
            tela.blit(cursor, cursor_menu)
            pygame.display.update(cursor_menu)
            selecao_cursor = False

        if sair_menu == True:
            break

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return -1

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE and sair == True:

                    if posicao_cursor == len(menu) - 1:
                        sair_menu = True

                    else:
                        posicao_cursor = len(menu) - 1
                        selecao_cursor = True

                elif event.key == pygame.K_UP:
                    selecao_cursor = True

                    if posicao_cursor == 0:
                        posicao_cursor = len(menu) - 1

                    else:
                        posicao_cursor -= 1

                elif event.key == pygame.K_DOWN:

                    selecao_cursor = True

                    if posicao_cursor == len(menu) - 1:
                        posicao_cursor = 0

                    else:
                        posicao_cursor += 1

                elif event.key == pygame.K_KP_ENTER or \
                                event.key == pygame.K_RETURN:
                    sair_menu = True

    return posicao_cursor


if __name__ == '__main__':
    sys.stderr.write("Ferramentas não foi iniciado")
    sys.exit()