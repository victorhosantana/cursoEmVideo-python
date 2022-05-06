#LISTA do Sistema

#Importações necessárias
from time import sleep

#Função de Listagem das Pessoas cadastradas
def listar():

    #Cabeçalho da Listagem
    print('-' * 40)
    print('PESSOAS CADASTRADAS'.center(40))
    print('-' * 40)
    sleep(1)

    #Abertura e Tratamento do arquivo com a Base de Dados
    try:
        arquivo = open('dados.txt', 'r')
    except:
        print('Ainda não existem pessoas cadastradas.')
        sleep(1)
    else:
        #Leitura das informações presentes na Base de Dados
        pessoas = arquivo.read().split(';')

        #Impressão das informações na tela
        for posição, elemento in enumerate(pessoas):
            if posição < (len(pessoas) - 1):
                if posição == 0 or posição % 2 == 0:
                    print(f'\033[36m{elemento:<32}', end='')
                else:
                    print(f'{elemento:>3}', 'anos\033[0m')
        arquivo.close()
