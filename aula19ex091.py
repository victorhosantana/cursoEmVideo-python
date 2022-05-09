#Cria um dicionário que guarde valores aleatórios e ordene de forma decrescente
from random import randint
from time import sleep
import operator

jogadores ={'Jogador1' : randint(1, 6),
            'Jogador2' : randint(1, 6),
            'Jogador3' : randint(1, 6),
            'Jogador4' : randint(1, 6)}

print('=-' * 20)
print('Os valores sorteados foram:')
for k, v in jogadores.items():
    sleep(0.5)
    print(f'{k} tirou {v} no dado.')
print('=-' * 20)
print('  == RANKING GERAL ==  ')

ordenado = list()
ordenado = sorted(jogadores.items(), key=operator.itemgetter(1), reverse=True)

for posição, elemento in enumerate(ordenado):
    sleep(0.5)
    print(f'{posição+1}° lugar ficou com o {elemento[0]} que tirou {elemento[1]}.')

print()
