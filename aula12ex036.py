#Aprova Empréstimo Bancário
import datetime as tempo

cores = {
    'limpa' : '\033[0m',
    'branco' : '\033[0;30m',
    'vermelho' : '\033[0;31m',
    'verde' : '\033[0;32m',
    'amarelo' : '\033[0;33m',
    'azulclaro' : '\033[0;34m',
    'roxo' : '\033[0;35m',
    'azulpiscina' : '\033[0;36m',
    'preto' : '\033[0;37m'
}

casa = float(input('{}Qual o valor da casa?{} '.format(cores['vermelho'], cores['limpa'])))
salario = float(input('Qual o valor do salário? '))
anos = int(input('Em quantos anos pretende pagar a casa? '))

prestação = casa / (anos * 12)

print(f'De acordo com o seu salário, podemos realizar um empréstimo até o valor de R${salario * 0.3} na prestação.')

if prestação > (salario * 0.3):
    print(f'A prestação ficou em R${prestação:.2f} e o seu empréstimo foi negado.')
else:
    print(f'A prestação ficou em R${prestação:.2f} e o seu empréstimo foi aceito.')
