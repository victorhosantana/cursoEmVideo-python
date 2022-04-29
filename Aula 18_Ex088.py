#Cria um programa que sorteie jogos da Megasena
from random import randint
import Dicio as dic
from time import sleep
dic.cabeçalho('SORTEIO DE JOGOS DA MEGASENA')

números = []
jogos = []
quantidade = int(input('Quantos jogos você quer sortear? '))
print('~' * 40)

for sorteios in range(0, quantidade):

    while len(números) < 6:
        escolhido = randint(1, 60)
        if escolhido not in números:
            números.append(escolhido)

    números.sort()
    jogos.append(números.copy())
    números.clear()

print('Os jogos sorteados foram:\n')
for número_sorteio, jogo in enumerate(jogos):
    sleep(0.5)
    print(f'Jogo {número_sorteio + 1}: {jogo}')

dic.rodapé()
