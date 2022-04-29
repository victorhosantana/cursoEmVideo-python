#Cria uma Lista com 5 entradas do usuário e realiza uma análise dos valores
import Dicio as dic
dic.cabeçalho('LISTA DE VALORES')
valores = list()
for posição in range(0, 5):
    valores.append(int(input(f'Digite o número da posição {posição+1}: ')))
print('\nA lista digitada foi: ', end='')
for item in valores:
    print(item, end=' ')
maior = max(valores)
menor = min(valores)
print(f'\nO maior valor foi o {maior}, nas posições ', end='')
for posição, item in enumerate(valores):
    if item == maior:
        print(f'{posição+1}', end=' ')
print(f'\nO menor valor foi o {menor}, nas posições ', end='')
for item in valores:
    if item == menor:
        print(f'{valores.index(item)+1}', end=' ')
dic.rodapé()
