#Módulo de Funções para o Desafio 109

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
