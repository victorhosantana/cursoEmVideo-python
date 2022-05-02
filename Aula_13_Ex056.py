#Identificar e mostrar características específicas de um grupo de pessoas

media = 0
velho = ''
mulheres = 0
compv = 0
print()
for c in range(1, 5):
    print(f' ---- {c}ª PESSOA ---- ')
    nome = str(input('Qual é o nome? ')).strip()
    idade = int(input('Qual é a idade? '))
    sexo = str(input('Qual é o sexo (M/F)? ')).strip()
    
    media += idade
    if sexo in 'Mm':
        if idade > compv:
            velho = nome
            compv = idade
    else:
        if idade < 20:
            mulheres += 1
print("""\nAlgumas informações sobre o grupo informado:
A média de idade é de {:.1f} anos.
O homem mais velho é o {}.
Existem {} mulheres com menos de 20 anos.
""".format(media / 4, velho, mulheres))
