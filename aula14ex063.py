#Apresenta os n termos de uma sequência de Fibonacci
limite = int(input('\nInforme quantos termos deseja ver da Sequência de Fibonacci: '))
ta1 = ta2 = ta = 0
contador = 1
if limite <= 0:
    print(f'Não é possível mostrar {limite} elementos. Tente novamente.')
elif limite == 1:
    print(f"""Com {limite} elementos, a Sequência de Fibonacci fica da seguinte forma:
0""")
else:
    print('~' * 50)
    while contador <= limite:
        if contador == 2:
            ta = ta1 = 1
        else:
            ta = ta1 + ta2
            ta2 = ta1
            ta1 = ta
        print(ta, end='')
        contador += 1
        if contador <= limite:
            print(' → ', end='')
    print()    
    print('~' * 50)
print()
