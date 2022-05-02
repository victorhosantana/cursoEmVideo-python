#Soma todas as entradas pares
import Dicio as dic
soma = 0
cont = 0
for c in range(1, 7):
    digito = int(input('Digite o número {}/6 para a soma: '.format(c)))
    if digito % 2 == 0:
        soma += digito
        cont += 1
print('A soma dos {} números pares digitados foi {}{}{}!'.format(cont, dic.cores['negrito'], soma, dic.cores['limpa']))
