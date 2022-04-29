#Refazer o exercício 051 sobre o crescimento de uma PA
termo = int(input('\nInforme o termo da PA: '))
razão = int(input('Informe a razão da PA: '))
quantidade = int(input('Informe a quantidade de termos da PA: '))
soma = termo
contador = 1

if quantidade <= 0:
    print('Quantidade de termos inválida! Tente novamente.')
elif quantidade == 1:
    print(f'O primeiro e único termo da PA é: {termo}')
else:
    print('\nOs primeiros {} termos de uma PA de número {} e razão {} são:\n'.format(quantidade, termo, razão))
    print(f'{termo} → ', end='')
    while contador < quantidade:
        print(termo + razão, end='')
        termo += razão
        soma += termo
        contador += 1
        if contador != quantidade:
            print(' → ', end='')
print(f'\nO somatório dos termos da PA é {soma}.')
