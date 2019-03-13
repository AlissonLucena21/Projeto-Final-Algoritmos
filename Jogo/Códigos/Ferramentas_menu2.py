import pygame
import sys


def fer_menu2(tela, menu, x_pos=100, y_pos=100, fonte=None, tamanho=70, distancia=1.4, fgcor=(255, 255, 255), cor_cursor=(255, 0, 0), sair=True):

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

                if event.key == pygame.K_1:

                    posicao_cursor = 0
                    selecao_cursor = True
                    sair_menu = True

                elif event.key == pygame.K_2 and len(menu) >= 2:
                    posicao_cursor = 1
                    selecao_cursor = True
                    sair_menu = True

                elif event.key == pygame.K_3 and len(menu) >= 3:
                    posicao_cursor = 2
                    selecao_cursor = True
                    sair_menu = True

                elif event.key == pygame.K_4 and len(menu) >= 4:
                    posicao_cursor = 3
                    selecao_cursor = True
                    sair_menu = True

                elif event.key == pygame.K_5 and len(menu) >= 5:
                    posicao_cursor = 4
                    selecao_cursor = True
                    sair_menu = True

                elif event.key == pygame.K_6 and len(menu) >= 6:
                    posicao_cursor = 5
                    selecao_cursor = True
                    sair_menu = True

                elif event.key == pygame.K_7 and len(menu) >= 7:
                    posicao_cursor = 6
                    selecao_cursor = True
                    sair_menu = True

                elif event.key == pygame.K_8 and len(menu) >= 8:
                    posicao_cursor = 7
                    selecao_cursor = True
                    sair_menu = True

                elif event.key == pygame.K_9 and len(menu) >= 9:
                    posicao_cursor = 8
                    selecao_cursor = True
                    sair_menu = True

                elif event.key == pygame.K_a and len(menu) >= 10:
                    posicao_cursor = 9
                    selecao_cursor = True
                    sair_menu = True

                elif event.key == pygame.K_b and len(menu) >= 11:
                    posicao_cursor = 10
                    selecao_cursor = True
                    sair_menu = True

                elif event.key == pygame.K_c and len(menu) >= 12:
                    posicao_cursor = 11
                    selecao_cursor = True
                    sair_menu = True

                elif event.key == pygame.K_d and len(menu) >= 13:
                    posicao_cursor = 12
                    selecao_cursor = True
                    sair_menu = True

                elif event.key == pygame.K_e and len(menu) >= 14:
                    posicao_cursor = 13
                    selecao_cursor = True
                    sair_menu = True

                elif event.key == pygame.K_f and len(menu) >= 15:
                    posicao_cursor = 14
                    selecao_cursor = True
                    sair_menu = True

                elif event.key == pygame.K_g and len(menu) >= 16:
                    posicao_cursor = 15
                    selecao_cursor = True
                    sair_menu = True

                elif event.key == pygame.K_h and len(menu) >= 17:
                    posicao_cursor = 16
                    selecao_cursor = True
                    sair_menu = True

                elif event.key == pygame.K_i and len(menu) >= 18:
                    posicao_cursor = 17
                    selecao_cursor = True
                    sair_menu = True

                elif event.key == pygame.K_j and len(menu) >= 19:
                    posicao_cursor = 18
                    selecao_cursor = True
                    sair_menu = True

                elif event.key == pygame.K_k and len(menu) >= 20:
                    posicao_cursor = 19
                    selecao_cursor = True
                    sair_menu = True

                elif event.key == pygame.K_l and len(menu) >= 21:
                    posicao_cursor = 20
                    selecao_cursor = True
                    sair_menu = True

                elif event.key == pygame.K_m and len(menu) >= 22:
                    posicao_cursor = 21
                    selecao_cursor = True
                    sair_menu = True

                elif event.key == pygame.K_n and len(menu) >= 23:
                    posicao_cursor = 22
                    selecao_cursor = True
                    sair_menu = True

                elif event.key == pygame.K_o and len(menu) >= 24:
                    posicao_cursor = 23
                    selecao_cursor = True
                    sair_menu = True

                elif event.key == pygame.K_p and len(menu) >= 25:
                    posicao_cursor = 24
                    selecao_cursor = True
                    sair_menu = True

                elif event.key == pygame.K_q and len(menu) >= 26:
                    posicao_cursor = 25
                    selecao_cursor = True
                    sair_menu = True

                elif event.key == pygame.K_r and len(menu) >= 27:
                    posicao_cursor = 26
                    selecao_cursor = True
                    sair_menu = True

                elif event.key == pygame.K_s and len(menu) >= 28:
                    posicao_cursor = 27
                    selecao_cursor = True
                    sair_menu = True

                elif event.key == pygame.K_t and len(menu) >= 29:
                    posicao_cursor = 28
                    selecao_cursor = True
                    sair_menu = True

                elif event.key == pygame.K_u and len(menu) >= 30:
                    posicao_cursor = 29
                    selecao_cursor = True
                    sair_menu = True

                elif event.key == pygame.K_v and len(menu) >= 31:
                    posicao_cursor = 30
                    selecao_cursor = True
                    sair_menu = True

                elif event.key == pygame.K_w and len(menu) >= 32:
                    posicao_cursor = 31
                    selecao_cursor = True
                    sair_menu = True

                elif event.key == pygame.K_x and len(menu) >= 33:
                    posicao_cursor = 32
                    selecao_cursor = True
                    sair_menu = True

                elif event.key == pygame.K_y and len(menu) >= 34:
                    posicao_cursor = 33
                    selecao_cursor = True
                    sair_menu = True

                elif event.key == pygame.K_z and len(menu) >= 35:
                    posicao_cursor = 34
                    selecao_cursor = True
                    sair_menu = True

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