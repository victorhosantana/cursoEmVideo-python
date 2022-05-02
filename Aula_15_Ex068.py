#Cria um jogo de PAR ou IMPAR contra o computador
from random import randint
from time import sleep
print('\n', '=-' * 10, ' JOGO DO PAR OU ÍMPAR ', '-=' * 10, '\nJogue contra o computador e tente ganhar o máximo de vezes.\n')
vitórias = 0
while True:
    print('~' * 30)
    jogador = int(input('Escolha o seu número: '))
    escolha = str(input('Você quer PAR ou ÍMPAR [P/I]? ')).strip().upper()
    escolha = escolha.replace(' ','')
    if escolha == '' or escolha not in 'pPiI':
        print('\nOpção inválida! Escolha novamente.')
    else:
        if escolha in 'pP':
            opção_jogador = 'PAR'
            opção_computador = 'ÍMPAR'
        else:
            opção_jogador = 'ÍMPAR'
            opção_computador = 'PAR'
        computador = randint(0, 10)
        if ((jogador + computador) % 2 == 0):
            resultado = 'PAR'
        else:
            resultado = 'ÍMPAR'
        print('- - - \nANALISANDO...')
        print('- - - ')
        sleep(2)
        print('Você escolheu {} e jogou {}.\nO computador ficou com o {} e jogou {}.\nO resultado deu {} e foi {}.'.format(opção_jogador, jogador, opção_computador, computador, jogador + computador, resultado))
        print('- - - ')
        if opção_jogador == resultado:
            print('\n - VOCÊ VENCEU! - \nTente vencer outra vez.\n')
            vitórias += 1
        else:
            print('\n - VOCÊ PERDEU! - \nTenha mais sorte na próxima.\n')
            break
print(f'\n - - - FIM DO JOGO - - - \nVocê obteve {vitórias} vitórias.\n')
