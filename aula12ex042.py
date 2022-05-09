#Refazer o Desafio 35, informando novas possibilidades
import Dicio as dic
from time import sleep

reta1 = float(input('\nQual é a medida da primeira reta? '))
reta2 = float(input('Qual é a medida da segunda reta? '))
reta3 = float(input('Qual é a medida da terceira reta? '))

print('\n{}PROCESSANDO...{}\n'.format(dic.cores['azulpiscina'], dic.cores['limpa']))
sleep(0.4)

if reta1 + reta2 > reta3 and reta1 + reta3 > reta2 and reta2 + reta3 > reta1:
    print('As retas de medida {:.1f}cm, {:.1f}cm e {:.1f}cm podem formar um triângulo'.format(reta1, reta2, reta3), end=' ')
    if reta1 != reta2 != reta3 != reta1: #É POSSÍVEL TESTAR ARGUMENTOS DE FORMA ANINHADA
        print('{}Escaleno!{}'.format(dic.cores['negrito'], dic.cores['limpa']))
    elif reta1 == reta2 == reta3: #É POSSÍVEL TESTAR ARGUMENTOS DE FORMA ANINHADA
        print('{}Equilátero!{}'.format(dic.cores['negrito'], dic.cores['limpa']))
    else:
        print('{}Isósceles!{}'.format(dic.cores['negrito'], dic.cores['limpa']))
else:
    print('As retas de {}cm, {}cm e {}cm não podem formar um triângulo!'.format(reta1, reta2, reta3))
