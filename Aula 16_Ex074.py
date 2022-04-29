#Cria uma Tupla que receba cinco valores aleatórios e imprima o maior e o menor valor
from random import randint as rd
from matplotlib import pyplot as pd
gerados = (rd(0, 10), rd(0, 10), rd(0, 10), rd(0, 10), rd(0, 10))
print('Os números gerados foram:', end=' ')
for item in gerados:
    print(item, end=' ')
print()
print(f"""
O maior número gerado foi: {max(gerados)}
O menor número gerado foi: {min(gerados)}
""")
# pd.plot(gerados)
# pd.title('Tupla gerada')
# pd.show()
