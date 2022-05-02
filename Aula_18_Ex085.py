#Cria uma lista que possua uma lista de números pares e outra de números ímpares
import Dicio as dic
dic.cabeçalho('LISTAS PARES E ÍMPARES')

números = [[], []]

for entrada in range (1, 8):
    valor_digitado = int(input(f'Digite o {entrada}° valor: '))
    if valor_digitado % 2 == 0:
        números[0].append(valor_digitado)
    else:
        números[1].append(valor_digitado)

números[0].sort()
números[1].sort()

print(f'Os números pares digitados foram: {números[0]}')
print(f'Os números ímpares digitados foram: {números[1]}')
dic.rodapé()
