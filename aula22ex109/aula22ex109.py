#Aprimore o Desafio 108, adicionando um parâmetro para reduzir as chamadas de funções
from moeda import *

#Programa Principal
número = float(input('\nInforme o valor a ser calculado: R$'))

print(f'\nO valor informado foi {(número)}.')
print(f'O dobro de {moeda(número)} é {dobro(número, True)}.')
print(f'A metade de {moeda(número)} é {metade(número, True)}.')
print(f'Um adicional de 10% em {moeda(número)} é {aumentar(número, mostrar=True)}.')
print(f'Uma redução de 15% em {moeda(número)} é {diminuir(número, mostrar=True)}.\n')
