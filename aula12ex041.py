#Define a categoria de um aluno de natação
import Dicio as dic
from datetime import date
from time import sleep

ano = int(input('\nInforme o ano de seu nascimento: '))

idade = date.today().year - ano

print('\n{}PROCESSANDO...{}\n'.format(dic.cores['azulpiscina'], dic.cores['limpa']))
sleep(0.5)

print('A sua idade é: {}{}{} anos.\nDe acordo com a Confederação Nacional de Natação, a sua categoria é: '.format(dic.cores['roxo'], idade, dic.cores['limpa']), end='')

if idade <= 9:
    print('{}MIRIM{}'.format(dic.cores['verde'], dic.cores['limpa']))
elif idade <= 14:
    print('{}INFANTIL{}'.format(dic.cores['verde'], dic.cores['limpa']))
elif idade <= 19:
    print('{}JÚNIOR{}'.format(dic.cores['verde'], dic.cores['limpa']))
elif idade <= 25:
    print('{}SÊNIOR{}'.format(dic.cores['verde'], dic.cores['limpa']))
else:
    print('{}MASTER{}'.format(dic.cores['verde'], dic.cores['limpa']))
