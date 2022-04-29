#Cria um programa que demonstra a tabuada de um número digitado e pare quando este for negativo
print('\n - - - TABUADA - - - \nNúmeros negativos encerram o programa.\n')
while True:
    número = int(input('Quer ver a tabuada de qual número? '))
    print('=-' * 20)
    if número <0:
        break
    print(f'Tabuada do número {número}:')
    for c in range (1, 11):
        print(f'{número} x {c:2} = {número * c}')
    print('=-' * 20)
print('\n - - - FIM DO PROGRAMA - - -')
