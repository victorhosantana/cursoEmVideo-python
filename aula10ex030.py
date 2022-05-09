número = int(input('Digite um número e eu vou adivinhar se ele é par ou ímpar: '))
"""
if (número % 2) != 0:
    print(f'O número {número} é ímpar!')
else:
    print(f'O número {número} é par!')
"""
print(f'O número {número} é ímpar!' if (número % 2) != 0 else f"O número {número} é par!")
