from math import floor
viagem = float(input('Quantos Km vai ter essa viagem? '))
if viagem <= 200:
    preço = floor(viagem)*0.5
else:
    preço = floor(viagem)*0.45
print('\nPra uma viagem de {}Km, o preço vai ser R${:.2f}.\n'.format(viagem, preço))
