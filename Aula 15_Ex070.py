#Cria um loop para somar todas as compras em uma loja e retorna com uma análise dos preços
gasto = caro = barato = 0
mais_barato = ''
produto = 1
print('= ' *20)
print('\n{:^40}\n'.format('LOJA DO VICTOR'))
print('= ' *20)
print('\nInforme os produtos e os preços de sua compra.\n')
while True:
    print('~' * 10, '\n- Produto', produto)
    while True:
        nome = str(input('Nome do produto: ')).strip().title()
        if nome != '':
            break
    while True:
        preço_entrada = str(input('Preço do produto: R$')).strip().replace(' ','')
        preço_entrada = preço_entrada.replace(' ','')
        if preço_entrada.isnumeric():
            preço = float(preço_entrada)
            if preço > 0:
                break
    gasto += preço
    if preço > 1000:
        caro += 1
    if produto == 1:
        barato = preço
        mais_barato = nome
    elif preço < barato:
        barato = preço
        mais_barato = nome
    print('~' * 10)
    while True:
        escolha = str(input('Deseja inserir outro produto [S/N]? ')).strip().replace(' ','')
        if escolha in 'sSnN':
            break
    if escolha in 'nN':
        print(' - - - ')
        break
    produto += 1
print(' = ' * 5, 'FIM DAS COMPRAS', ' = ' *5)
print("""\nVocê comprou {} produtos e o total de suas compras deu R${:.2f}
Existem {} produtos com valor acima de R$1000.00
O produto mais barato é {} e custou {}.\n""".format(produto, gasto, caro, mais_barato, barato))
