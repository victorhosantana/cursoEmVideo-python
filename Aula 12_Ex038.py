import Dicio as dic
from time import sleep

num1 = int(input('\nInforme o primeiro número: '))
num2 = int(input('Informe o segundo número: '))

print('\n{}PROCESSANDO...{}'.format(dic.cores['azulpiscina'], dic.cores['limpa']))
sleep(0.75)

print()

if num1 == num2:
    print('Entre os números {}{}{} e {}{}{} não existe valor maior. Os valores são iguais.'.format(dic.cores['verde'], num1, dic.cores['limpa'], dic.cores['amarelo'], num2, dic.cores['limpa']))
elif num1 > num2:
    print('Entre os números {}{}{} e {}{}{}, o valor {}{}{} é o maior.'.format(dic.cores['verde'], num1, dic.cores['limpa'], dic.cores['amarelo'], num2, dic.cores['limpa'], dic.cores['verde'], num1, dic.cores['limpa']))
else:
    print('Entre os números {}{}{} e {}{}{}, o valor {}{}{} é o maior.'.format(dic.cores['verde'], num1, dic.cores['limpa'], dic.cores['amarelo'], num2, dic.cores['limpa'], dic.cores['amarelo'], num2, dic.cores['limpa']))

print()
