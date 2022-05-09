#Cria uma função que faça uma sequência com intervalos  e dados a serem informados pelo usuário
from time import sleep

def contador(início, fim, passo):

    if passo < 0:
        intervalo = passo
        partida = max(início, fim)
        final = min(início, fim) - 1
    else:
        if passo == 0:
            intervalo = 1
            passo = 1
        if início > fim:
            intervalo = passo * -1
            partida = início
            final = fim - 1
        else:
            intervalo = passo
            partida = início
            final = fim + 1
    
    print('~' * 20)
    print(f'A contagem de {início} até {fim} com intervalo de {passo} em {passo} fica assim:')

    for elemento in range(partida, final, intervalo):
        sleep(0.5)
        print(elemento, end=' ')
    sleep(0.5)
    print('FIM!')
    sleep(0.5)


contador(1, 10, 1)
contador(10, 0, 2)

print('~' * 20)
print('Agora é sua vez!')
início = int(input('Qual será o início? '))
fim = int(input('Qual será o fim? '))
passo = int(input('Qual será o intervalo? '))
contador(início, fim, passo)
