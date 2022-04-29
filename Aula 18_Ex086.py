#Cria uma Lista com as entradas do usuário e imprima uma matriz tabulada
import Dicio as dic
dic.cabeçalho('IMPRESSÃO DE UMA MATRIZ')

matriz = [[], [], []]

for linha in range(0, 3):
    for coluna in range(0, 3):
        número = int(input(f'Digite o número na posição [{linha}:{coluna}] da matriz: '))
        matriz[linha].append(número)

for linha in matriz:
    for coluna in linha:
        print('[{:^5}]'.format(coluna), end=' ')
    print()

dic.rodapé()
