#Funções para o Desafio 111

#Ajustes de formatação de moeda
def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')

#Cálculo de Aumento
def aumentar(preço=0, taxa=10, mostrar=False):
    if mostrar == False:
        return preço * (1 + taxa/100)
    else: 
        return moeda(preço * (1 + taxa/100))

#Cálculo de Redução
def diminuir(preço=0, taxa=15, mostrar=False):
    if mostrar == False:
        return preço * (1 - taxa/100)
    else:
        return moeda(preço * (1 - taxa/100))

#Cálculo do Dobro
def dobro(preço=0, mostrar=False):
    if mostrar == False:
        return preço * 2
    else:
        return moeda(preço * 2)

#Cálculo da Metade
def metade(preço=0, mostrar=False):
    if mostrar == False:
        return preço / 2
    else:
        return moeda(preço / 2)

#Impressão do Resumo dos Cálculos
def resumo(preço=0, aumento=0, redução=0):
    
    print('-' * 32)
    print('CÁLCULOS DO PREÇO'.center(32))
    print('-' * 32)
    print(f'Preço analisado:\t{moeda(preço)}')
    print(f'Dobro do Preço:\t\t{dobro(preço, mostrar=True)}')
    print(f'Metade do Preço:\t{metade(preço, mostrar=True)}')
    print(f'Aumento de {aumento}%:\t\t{aumentar(preço, aumento, mostrar=True)}')
    print(f'Redução de {redução}%:\t\t{diminuir(preço, redução, mostrar=True)}')
    print('-' * 32)