#Aprimore o Desafio 107, formatando os valores de moeda
import moeda

#Programa Principal
número = float(input('\nInforme o valor a ser calculado: R$'))

print(f'\nO valor informado foi {moeda.moeda(número)}.')
print(f'O dobro de {moeda.moeda(número)} é {moeda.moeda(moeda.dobro(número))}.')
print(f'A metade de {moeda.moeda(número)} é {moeda.moeda(moeda.metade(número))}.')
print(f'Um adicional de 10% em {moeda.moeda(número)} é {moeda.moeda(moeda.aumentar(número))}.')
print(f'Uma redução de 15% em {moeda.moeda(número)} é {moeda.moeda(moeda.diminuir(número))}.\n')
