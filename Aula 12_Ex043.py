#Cálculo de IMC
import Dicio as dic

peso = float(input('\nQual é o seu peso? '))
altura = float(input('Qual é a sua altura? '))

imc = peso / altura ** 2

print('\nO seu IMC é de {}{:.1f}{} e você está'.format(dic.cores['negrito'], imc, dic.cores['limpa']), end=' ')

if imc < 18.5:
    print('{}abaixo do Peso.'.format(dic.cores['negsub']))
elif imc < 25:
    print('{}no peso ideal.'.format(dic.cores['negsub']))
elif 25 <= imc < 30: #O PYTHON ACEITA ESTA FORMA DE COMPARAÇÃO
    print('{}sobrepeso.'.format(dic.cores['negsub']))
elif imc < 40:
    print('{}com obesidade.'.format(dic.cores['negsub']))
else:
    print('{}com obesidade mórbida.'.format(dic.cores['negsub']))
