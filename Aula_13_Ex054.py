#Conta a quantidade de pessoas maiores de 21 anos
from datetime import date
maior = 0
total = int(input('\nQuantas pessoas você deseja comparar? '))
print()
for c in range(1, total + 1):
    ano = int(input(f'Qual é o ano de nascimento da pessoa {c}/{total}? '))
    if (date.today().year - ano) >= 21:
        maior += 1
print()
if maior == 0:
    print(f'Existem {total} pessoas menores do que 21 anos.')
elif maior ==1:
    print(f'Existe {maior} pessoa maior do que 21 anos e {total - maior} menores de idade.')
elif total == 0:
    print(f'Existem {maior} pessoas maiores do que 21 anos.')
elif total ==1:
    print(f'Existe {total} pessoa menor do que 21 anos e {maior - total} maiores de idade.')
else:
    print(f'Existem {maior} pessoas maiores do que 21 anos e {total - maior} menores de idade.')
print()
