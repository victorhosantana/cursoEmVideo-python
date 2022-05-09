#Cria uma função que analize o maior valor passado como parâmetro
from time import sleep

def maior(*números):
    if len(números) == 0:
        print('=-' * 40)
        sleep(1)
        print('Não foi informado nenhum número.')
    else:
        print('=-' * 40)
        sleep(1)
        print(f'Foram informados {len(números)} números. Estes números são:')
        sleep(2)
        for item in números:
            sleep(0.5)
            print(item, end=' ')
        print()
        sleep(1)
        print(f'O maior valor foi o {max(números)}.')


#Testes de argumentos para a função
maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior(0)
maior()
