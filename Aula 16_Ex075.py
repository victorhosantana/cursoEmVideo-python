#Cria uma Tupla com quatro entradas do usuário e analisa os valores
virgula = 0
entradas = (int(input('Digite um número: ')), 
            int(input('Digite um número: ')), 
            int(input('Digite um número: ')), 
            int(input('Digite um número: ')))
print()
print(f'O número 9 apareceu {entradas.count(9)} vezes.' if 9 in entradas else 'O número 9 não apareceu entre os valores digitados.')
print(f'O número 3 apareceu, pela primeira vez, na {entradas.index(3) + 1}ª posição.' if 3 in entradas else 'O número 3 não apareceu entre os valores digitados.')
if (entradas[0] % 2) == 0 or (entradas[1] % 2) == 0 or (entradas[2] % 2) == 0 or (entradas[3] % 2) == 0:
    print('Os números pares digitados foram:', end=' ')
    for pares in entradas:
        if (pares % 2) == 0:
            if virgula == 1:
                print(',', end=' ')
            print(f'{pares}', end='')
            virgula = 1
    print()
else:
    print('Não houve números pares digitados.')
print(type(entradas), '\n')
