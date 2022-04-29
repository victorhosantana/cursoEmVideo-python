from random import randint as aleatorio
import time
pc = aleatorio(0, 5)
print('-=-' * 20)
humano = int(input('Tenta acertar o número que o computador escolheu entre 0 e 5: '))
print('-=-' * 20)
print('PROCESSANDO...')
time.sleep(2)
if pc == humano:
    print('\nAcertou, Miserávi!')
else:
    print('\nA máquina ganhou de tu e achou fácil!')
print(f'\nA máquina escolheu {pc} e tu escolheu {humano}.')
