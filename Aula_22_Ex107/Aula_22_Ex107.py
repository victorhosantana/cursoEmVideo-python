#Com base num módulo, calcula novos valores para uma entrada dada pelo usuário
import moeda

#Programa Principal
número = float(input('\nInforme o valor a ser calculado: R$'))

print(f'\nO valor informado foi {número}.')
print(f'O dobro de {número} é {moeda.dobro(número):.1f}.')
print(f'A metade de {número} é {moeda.metade(número):.1f}.')
print(f'Um adicional de 10% em {número} é {moeda.aumentar(número):.2f}.')
print(f'Uma redução de 15% em {número} é {moeda.diminuir(número):.2f}.\n')
