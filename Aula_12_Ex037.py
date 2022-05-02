from time import time
import Dicio as dic
from time import sleep

n = int(input('\nDigite um número para ser convertido: '))

escolha = int(input("""
Escolha para qual formato deseja converter o número {}:
{}1) Binário
{}2) Octal
{}3) Hexadecimal{}
""".format(n, dic.cores['vermelho'], dic.cores['verde'], dic.cores['amarelo'], dic.cores['limpa'])))

print('\n{}PROCESSANDO...{}'.format(dic.cores['azulpiscina'], dic.cores['limpa']))
sleep(1)

print()

if escolha == 1:
    print('O número {} é igual a {} em Binário.'.format(n, bin(n)[2:]))
elif escolha == 2:
    print('O número {} é igual a {} em Octal.'.format(n, oct(n)[2:]))
elif escolha == 3:
    print('O número {} é igual a {} em Hexadecimal.'.format(n, hex(n)[2:]))
else:
    print('A opção {} não é uma opção válida.'.format(escolha))

print()
