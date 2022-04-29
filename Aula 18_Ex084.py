#Cria um loop de inserção de valores numa lista e analisa os dados contidos
import Dicio as dic
dic.cabeçalho('LISTAS DE PESSOAS')
entrada = []
pessoas = []
maior = menor = 0
while True:
    entrada.append(str(input('Digite o nome da pessoa: ')))
    entrada.append(float(input('Digite o peso da pessoa: Kg')))
    pessoas.append(entrada[:])

    if len(pessoas) == 1:
        maior = menor = entrada[1]
    elif entrada[1] > maior:
        maior = entrada[1]
    if entrada[1] < menor:
        menor = entrada[1]

    entrada.clear()

    escolha = dic.deseja_continuar()
    if escolha == False:
        break

print(f'Foram registradas {len(pessoas)} pessoas.')
print(f'O maior peso foi {maior}Kg para', end=' ')
for pessoa in pessoas:
    for posição, item in enumerate(pessoa):
        if item == maior:
            print(f'{pessoa[posição - 1]}', end=' ')
print(f'\nO menor peso foi {menor}Kg para', end=' ')
for pessoa in pessoas:
    for posição, item in enumerate(pessoa):
        if item == menor:
            print(f'{pessoa[posição - 1]}', end=' ')

dic.rodapé()
