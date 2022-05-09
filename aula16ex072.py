#Criar uma Tupla para retornar o número digitado pelo usuário
import Dicio as dic
valores = tuple(['zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove',
                'dez', 'onxe', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete',
                'dezoito', 'dezenove', 'vinte'])
while True:
    while True:
        usuário = str(input('Digite um número entre 0 e 20 para ver no formato extenso: ')).strip().replace(' ','')
        if usuário.isnumeric() and int(usuário) >= 0 and int(usuário) <= 20:
            usuário = int(usuário)
            break
        else:
            print('Valor inválido! Tente novamente.')
    print(f'Você escolheu o número {valores[usuário]}.')
    print('-' * 20)
    escolha = dic.deseja_continuar()
    if escolha == False:
        break
    print('-' * 20)
