salario = float(input('Qual é teu salário, meu patrão? '))
if salario > 1250:
    aumento = salario * 1.1
    perc = "10%"
else:
    aumento = salario * 1.15
    perc = "15%"
print(f'Boa! Aumento de {perc}. Teu salário vai pra {aumento:.2f} reais.')
