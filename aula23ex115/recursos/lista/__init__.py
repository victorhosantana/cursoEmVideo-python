#LISTA do Sistema

#Importações necessárias
from time import sleep

#Função de Listagem das Pessoas cadastradas
def listar():
    """Esta função lista as pessoas registradas no arquivo e imprime no console de forma tabulada."""

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
        #Leitura e impressão das informações na tela
        if arquivo.read() == '':
            print('Ainda não existem pessoas cadastradas.')
            sleep(1)
            arquivo.close()
        else:
            with open('dados.txt', 'r') as arquivo:
                for linha in arquivo:
                    pessoa = linha.split(';')
                    pessoa[1] = pessoa[1].replace('\n','')
                    print(f'\033[36m{pessoa[0]:<32}{pessoa[1]:>3} anos\033[0m')
