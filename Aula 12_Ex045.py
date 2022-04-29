from random import choice
import Dicio as dic
from time import sleep

print('\n{}{}{}{}{}'.format(' ' * 22, dic.cores['negsub'], ' JOKENPÔ ', dic.cores['limpa'], ' ' * 22))
jogador = int(input("""

Escolha uma das opções para jogar contra o computador:

1 - Pedra
2 - Papel
3 - Tesoura

Qual é a sua jogada? """))

if jogador != 1 and jogador != 2 and jogador != 3:
    print('A opção {}{}{} não é válida. Tente novamente!'.format(dic.cores['negrito'], jogador, dic.cores['limpa']))
else:
    print('\n{}JO'.format(dic.cores['verde']))
    sleep(0.3)
    print('{}KEN'.format(dic.cores['amarelo']))
    sleep(0.4)
    print('{}PÔ{}\n'.format(dic.cores['vermelho'], dic.cores['limpa']))
    sleep(0.5)

    opções = ['Pedra', 'Papel', 'Tesoura']
    jogador = opções[jogador - 1]
    computador = choice(opções)

    print('-=' * 22)
    if jogador == computador:
        print('Empate! Ambos escolheram {}{}{}!'.format(dic.cores['negrito'], jogador, dic.cores['limpa']))
    else:
        if (jogador == 'Pedra' and computador == 'Tesoura') or (jogador == 'Papel' and computador == 'Pedra') or (jogador == 'Tesoura' and computador == 'Papel'):
            print('GANHOU! Você escolheu {}{}{} e o computador escolheu {}{}{}.'.format(dic.cores['negrito'], jogador, dic.cores['limpa'], dic.cores['negrito'], computador, dic.cores['limpa']))
        else:
            print('PERDEU, OTÁRIO! Você escolheu {}{}{} e o computador escolheu {}{}{}.'.format(dic.cores['negrito'], jogador, dic.cores['limpa'], dic.cores['negrito'], computador, dic.cores['limpa']))    
    print(('-=' * 22), '\n')
