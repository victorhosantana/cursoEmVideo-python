#Cria duas funções. Uma irá sortaear números e a outra soma os pares
from time import sleep
from random import randint

def sorteio():
    print('=-' * 20)
    print('Sorteando números...')
    sleep(1)
    lista = [randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10)]
    print('Os números sorteados foram:')
    for item in lista:
        sleep(0.5)
        print(item, end=' ')
    print()
    sleep(1)
    return lista

def somaPar(números):
    print('=-' * 20)
    print('Calculando os números pares...')
    sleep(1)
    pares = 0
    for item in números:
        if item % 2 == 0:
            pares += item
    if pares > 0:
        print(f'A soma dos números pares deu {pares}.')
    else:
        print('Não houve nenhum número par.')


#Programa Principal
num = sorteio()
somaPar(num)
