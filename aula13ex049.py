#Refazer o exercício 9 para demonstrar uma tabuada
import Dicio as dic

num = int(input('\nDigite um número para calcular a sua tabuada: '))

print('{}-={}'.format(dic.cores['azulpiscina'], dic.cores['limpa']) * 8)
for i in range (1, 11):
    print('{}{}{} x {}{:2}{} = {}{}{}'.format(dic.cores['amarelo'],num, dic.cores['limpa'], dic.cores['verde'], i, dic.cores['limpa'], dic.cores['vermelho'], num * i, dic.cores['limpa']))
print('{}-={}'.format(dic.cores['azulpiscina'], dic.cores['limpa']) * 8)
