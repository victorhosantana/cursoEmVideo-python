real = float(input('Digite um número: '))
from math import trunc
print('O número {:.3f} tem a parte inteira {}'.format(real, trunc(real)))

'''Outra forma de executar esse problema é utilizando o próprio Int
print('O número {} tem parte inteira de {}'.format(real, int(real))'''
