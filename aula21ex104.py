#Cria uma função que 'valide' uma entrada até que seja um valor inteiro
import Dicio as dic

def leiaInt(pergunta):
    
    while True:
        número = str(input(f'{pergunta}: ')).strip().replace(' ','')
        if número.isnumeric():
            número = int(número)
            return número
        else:
            print('{}ERRO! A entrada digitada não é um número.{}'.format(dic.cores['vermelho'], dic.cores['limpa']))


#Programa Principal
n = leiaInt('Digite um n')
print('{}O número digitado foi {}.{}'.format(dic.cores['verde'], n, dic.cores['limpa']))
