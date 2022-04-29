#Demonstra todos os números pares de um intervalo
for c in range(1, 51):
    if c % 2 == 0:
        if c != 50:
            print(c, end=', ')
        else:
            print(c)
