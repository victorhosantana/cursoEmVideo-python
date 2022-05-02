#Cria uma função para o cálculo de uma área
def área(a, b):
    área = a * b
    print(f'A área de um terreno com {a:.2f}m x {b:.2f}m é de {área:.2f}m².\n')


print('\nControle de Terrenos')
print('-' * 30)

largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))

área(largura, comprimento)
