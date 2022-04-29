#Repetição do jogo do desafio 029, com repetição e contagem de tentativas até o acerto
from random import randint
pc = randint(0,10)
acertou = False
tentativas = 0
print("""
 - - - - - - - - - - JOGO DA ADIVINHAÇÃO - - - - - - - - - - 
 
 Tente acertar o número, entre 0 e 10, ao qual o computador pensou.
 """)
while not acertou:
    jogador = int(input('Tente acertar: '))
    if jogador < pc:
        print('Um pouco mais que isso...\n')
    elif jogador > pc:
        print('Um pouco menos que isso...\n')
    else:
        acertou = True
    tentativas += 1
print(f'\nPARABÉNS! Você venceu e precisou de {tentativas} tentativas para acertar.\n')
