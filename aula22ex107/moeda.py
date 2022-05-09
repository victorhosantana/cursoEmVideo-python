#Módulo de Funções para o Desafio 107

def aumentar(preço, taxa=10):
    return preço * (1 + taxa/100)

def diminuir(preço, taxa=15):
    return preço * (1 - taxa/100)

def dobro(preço):
    return preço * 2

def metade(preço):
    return preço / 2
