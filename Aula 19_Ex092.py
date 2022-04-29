#Cria um dicionário que guarde dados de um usuário e complemente testando algumas condicionais
from datetime import date
trabalhador = dict()

trabalhador['Nome'] = str(input('Informe o nome do trabalhador: ')).strip()
trabalhador['Idade'] = date.today().year - int(input('Informe o ano de nascimento: '))
trabalhador['CTPS'] = int(input('Informe a CTPS (0 se não existir): '))
if trabalhador['CTPS'] != 0:
    trabalhador['Contratação'] = int(input('Informe o ano de contratação: '))
    trabalhador['Salário'] = float(input('Informe o salário: '))
    trabalhador['Aposentadoria'] = trabalhador['Contratação'] + 35 - date.today().year + trabalhador['Idade']

print(trabalhador)
print('\nAs informações deste trabalhador são:')
for k,v in trabalhador.items():
    print(f'{k} = {v}')
