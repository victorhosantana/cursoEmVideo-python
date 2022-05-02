#Recebe uma entrada de usuários e adiciona em uma lista. Depois separa uma lista par e outra ímpar.
import Dicio as dic
dic.cabeçalho('LISTAS PARES E ÍMPARES')
principal = []
pares = []
ímpares = []
while True:
    principal.append(int(input('Digite um número para adicionar na lista principal: ')))
    escolha = dic.deseja_continuar()
    if escolha == False:
        break
principal.sort()
for item in principal:
    if (item % 2) == 0:
        pares.append(item)
    else:
        ímpares.append(item)
print('\nA lista principal possui os números:', end=' ')
for índice_principal in principal:
    print(f' {índice_principal}', end='')
print('\nA lista par possui os números:', end=' ')
for índice_pares in pares:
    print(f' {índice_pares}', end='')
print('\nA lista ímpar possui os números:', end=' ')
for índice_ímpares in ímpares:
    print(f' {índice_ímpares}', end='')
dic.rodapé()
