#CADASTRO de Pessoas no sistema

#Importações necessárias
from time import sleep

#Função de cadastrar novo usuário
def cadastrar():
    """Esta função realiza o cadastro de um novo usuário, adicionando um Nome e Idade ao arquivo dados.txt
    """

    #Loop principal do Cadastro
    while True:

        #Cabeçalho do Cadastro
        print('-' * 40)
        print('NOVO CADASTRO'.center(40))
        print('-' * 40)
        sleep(1)

        #Tratamento de erros na entrada do usuário
        nome = str(input('Nome: ')).strip().title()
        while True:
            try:
                idade = int(input('Idade: '))
            except:
                print('\033[31mERRO! A idade precisa ser um número inteiro válido.\033[0m')
                sleep(1)
            else:
                break
        
        #Inserção de dados na Base de Dados
        try:
            arquivo = open('dados.txt', 'a')
        except:
            arquivo = open('dados.txt', 'w')
        else:
            arquivo.write(nome)
            arquivo.write(';')
            arquivo.write(str(idade))
            arquivo.write(';')
        arquivo.close()
        print(f'O registro de {nome} foi realizado com sucesso!')
        sleep(1)
        break
