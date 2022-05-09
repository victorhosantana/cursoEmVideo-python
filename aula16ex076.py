#Cria uma Tupla com uma listagem de nomes e preõs de produtos
produtos = tuple(['Guitarra', 750, 'Baixo', 900, 'Bateria', 3200, 'Alfaia', 470, 
                'Microfone', 220, 'Mesa de Som', 9760, 'Cabos', 48.5, 'Amplificadores', 2799])
print('=' * 40)
print('{:^40}'.format('LOJA DE INSTRUMENTOS'))
print('=' * 40)
print('Lista de instrumentos e preços:\n')
for referência, item in enumerate(produtos):
    if type(item) == str:
        print('{:.<30}'.format(item), f'R$ {produtos[referência + 1]:>7.2f}')
print('- ' * 21)
