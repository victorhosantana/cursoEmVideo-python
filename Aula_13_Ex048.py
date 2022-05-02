#Somar todos os números ímpares e divisíveis por 3
soma = 0
cont = 0
for c in range (1, 501):
    if c % 2 == 1:
        if c % 3 == 0:
            cont += 1
            soma += c
print(f'A soma dos {cont} valores encontrados deu {soma}!')
