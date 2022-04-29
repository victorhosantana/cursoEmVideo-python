from html.entities import name2codepoint


n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))
print(f'\nOs números digitados foram: {n1}, {n2} e {n3}')
if n1 > n2:
    maior = n1
    menor = n2
else:
    maior = n2
    menor = n1
if n3 > maior:
    print(f'O maior número é o {n3} e o menor é o {menor}.\n')
else:
    if n3 < menor:
        print(f'O maior número é o {maior} e o menor é o {n3}.\n')
    else:
        print(f'O maior número é o {maior} e o menor é o {menor}.\n')
