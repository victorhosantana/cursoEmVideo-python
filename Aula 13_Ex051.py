#Demonstra uma Progressão Aritmética
termo = int(input('Informe o termo da PA: '))
razão = int(input('Informe a razão da PA: '))

print('\nOs primeiros 10 termos do número {} e razão {} são:'.format(termo, razão))

print('\nModo prático:')
seguinte = termo
for c in range(1, 11):
    print(f'{seguinte} ', end='→ ')
    seguinte += razão
print('ACABOU!')

print('\nModo matemático:')
décimo = termo + (10 - 1) * razão
for c in range(termo, décimo +1, razão):
    print(f'{c} ', end='→ ')
print('ACABOU!')
