#Cria um Caixa Eletrônico para informar as cédulas de uma retirada, priorizando as de maior valor
total_cédulas = 0
cédula = 50
print('=' * 30, '\n{:^30}\n'.format('VICTORBANK'), '=' * 30)
while True:
    quantia_entrada = str(input('Qual o valor que deseja retirar? R$')).strip().replace(' ','')
    if quantia_entrada.isnumeric():
        quantia = int(quantia_entrada)
        break
print('~' * 30)
print('Você receberá:')
while True:
    if quantia >= cédula:
        total_cédulas += 1
        quantia -= cédula
    else:
        if total_cédulas > 0:
            print(f'{total_cédulas} cédulas de R${cédula}')            
        if cédula == 50:
            cédula = 20
        elif cédula == 20:
            cédula = 10
        elif cédula == 10:
            cédula = 1
        elif cédula == 1:
            break
        total_cédulas = 0
print('')
