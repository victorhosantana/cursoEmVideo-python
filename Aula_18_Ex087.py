#Replica o Desafio 086 e realiza análises com os dados da matriz
import Dicio as dic
dic.cabeçalho('IMPRESSÃO DE UMA MATRIZ')

matriz = [[], [], []]
pares = terceira_coluna = segunda_linha = 0

for linha in range(0, 3):
    for coluna in range(0, 3):
        número = int(input(f'Digite o número na posição [{linha}:{coluna}] da matriz: '))
        matriz[linha].append(número)

        if número % 2 == 0: #Localiza os pares
            pares += número
        if coluna == 2: #Localiza os elementos da terceira coluna
            terceira_coluna += número
        if linha == 1: #Localiza os elementos da segunda linha
            segunda_linha = max(matriz[linha])

print('=-' * 10)

for linha in matriz:
    for coluna in linha:
        print(f'[{coluna:^5}]', end=' ')
    print()

print('=-' * 10)

print(f'A soma de todos os números pares é {pares}.')
print(f'A soma de todos os números da terceira coluna é {terceira_coluna}.')
print(f'O maior número da segunda linha é {segunda_linha}.')

dic.rodapé()
