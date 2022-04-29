#Cálculo do fatorial de um número dado como entrada

#Entradas do programa
from math import factorial
cont = num = int(input('\nInforme o número inteiro para calcular o seu fatorial: '))
total = total2 = 1

#Método While
print('\n - - - Método While - - - ')
if num == 0 or num == 1:
    print(f'\n{num}! = 1')
else:
    print(f'{num}! = ', end='')
    while cont >= 1:
        print(f'{cont}', end='')
        print(' x ' if cont > 1 else ' = ', end='')
        total *= cont
        cont -= 1
    print(f'= {total}')

#Método For
print('\n - - - Método For - - - ')
if num == 0 or num == 1:
    print(f'\n{num}! = 1')
else:
    for c in range(num, 0, -1):
        if c == num:
            print(f'{num}! = {num} x ', end='')
        else:
            if c == 1:
                print(f'{c} ', end='')
            else:
                print(f'{c} x ', end='')
        total2 *= c
    print(f'= {total2}\n')

#Método Function()
print(' - - - Método Function() - - - ')
print(f'O fatorial de {num}! = {factorial(num)}\n')
