#Aprimorar o exercício 061 sobre o crescimento de uma PA para deixar em loop
itens = termo = int(input('\nInforme o termo da PA: '))
razão = int(input('Informe a razão da PA: '))
escolha = True
soma = total = 0
contador = 1

while escolha:
    print('=-' * 30)
    quantidade = int(input('Informe a quantidade de termos que você quer exibir: '))
    if quantidade < 0:
        print('Quantidade de termos inválida! Tente novamente.')
    elif quantidade > 0:
        contador = 1
        while contador <= quantidade:
            print(itens, end='')
            soma += itens
            itens += razão
            contador += 1
            total += 1
            if contador <= quantidade:
                print(' → ', end='')
        print()
    else:
        escolha = False
print(f'\nO somatório dos {total} termos da PA é {soma}.')

""" while quantidade != 0:
    print('=-' * 30)
    quantidade = int(input('Informe a quantidade de termos que você quer exibir: '))
    contador = 1
    soma = 0
    itens = termo
    if quantidade < 0:
        print('Quantidade de termos inválida! Tente novamente.')
    elif quantidade > 0:
        if quantidade == 1:
            print(f'O primeiro e único termo da PA é: {termo}')
        else:
            while contador <= quantidade:
                print(itens, end='')
                soma += itens
                itens += razão
                contador += 1
                if contador <= quantidade:
                    print(' → ', end='')
            print(f'\nO somatório dos termos da PA é {soma}.')
print()
 """