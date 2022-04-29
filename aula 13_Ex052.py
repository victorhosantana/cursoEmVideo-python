#Identificar números primos
import emoji
import Dicio as dic

num = int(input('\nInforme um número para verificar se é um número primo: '))

confere = 0

for cont in range (1, num +1):
    if num % cont == 0:
        confere += 1
        print('{}'.format(dic.cores['amarelo']), end='')
    else:
        print('{}'.format(dic.cores['azulclaro']), end='')
    if cont != num:
        print(cont, end=' ')
    else:
        print(cont, '{}'.format(dic.cores['limpa']))
print(f'\nQuantidade de divisores: {confere}')
if confere > 2:
    print(emoji.emojize('O número {}{}{} {}NÃO{} é um número primo! :thumbsdown:\n'.format(dic.cores['vermelho'], num, dic.cores['limpa'], dic.cores['negrito'], dic.cores['limpa']), language='alias'))
else: 
    print(emoji.emojize('O número {}{}{} {}É{} um número primo! :thumbsup:\n'.format(dic.cores['verde'], num, dic.cores['limpa'], dic.cores['negrito'], dic.cores['limpa']), language='alias'))
