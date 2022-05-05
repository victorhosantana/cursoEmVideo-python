#Cria um Programa que realiza um Tratamento de Exceções da entrada do usuário

def leiaInt():
    while True:
        try:
            inteiro = int(input('Digite um número INTEIRO: '))
        except:
            print('\033[31mERRO! A entrada passada não é um número Inteiro válido.\033[0m')
        else:
            return inteiro

def leiaFloat():
    while True:
        try:
            real = float(input('Digite um número REAL: '))
        except:
            print('\033[31mERRO! A entrada passada não é um número Real válido.\033[0m')
        else:
            return real


#Programa Principal
print(f'Os números digitados foram:\nInteiro: {leiaInt()}\nReal: {leiaFloat()}')
