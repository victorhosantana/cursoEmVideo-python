#Informa o maior e o menor peso de uma quantidade de pessoas
print()
for c in range(1, 6):
    kg = float(input(f'Digite o peso da pessoa {c}/5: '))
    if c == 1:
        maior = menor = kg
    else:
        if kg > maior:
            maior = kg
        if kg < menor:
            menor = kg
print(f'\nO maior peso informado foi {maior:.1f}Kg e o menor foi {menor:.1f}Kg!\n')
