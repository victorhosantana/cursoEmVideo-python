#Calcula o valor da Hipotenusa de um triângulo
from math import hypot
c1 = float(input('Qual o comprimento do Cateto Oposto? '))
c2 = float(input('Qual o comprimento do Cateto Adjascente? '))
print('A medida da Hipotenusa é {:.2f}.'.format(hypot(c1, c2)))
