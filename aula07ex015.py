km = float(input('Quantos km tu rodou com o carro? Km'))
dias = int(input('Quantos dias tu passou com o carro? '))
Custo = (km * 0.15) + (dias * 60)
print('Pra tu, deixo o preço todo por R${:.2f}'.format(Custo))
