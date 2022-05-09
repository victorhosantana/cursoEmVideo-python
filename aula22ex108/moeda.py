#Módulo de Funções para o Desafio 108

def aumentar(preço=0, taxa=10):
    return preço * (1 + taxa/100)

def diminuir(preço=0, taxa=15):
    return preço * (1 - taxa/100)

def dobro(preço=0):
    return preço * 2

def metade(preço=0):
    return preço / 2

def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')
