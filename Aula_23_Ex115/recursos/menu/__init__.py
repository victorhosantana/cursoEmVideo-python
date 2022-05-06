#MENU do Sistema

#Importações necessárias
from time import sleep
from recursos import lista, cadastro

#Comandos disponíveis no sistema
comandos = {    1:lista.listar,
                2:cadastro.cadastrar
}

#Função do Menu do Sistema
def menu():
    """Mostra o MENU com as opções de interatividade do Sistema
    """

    #Loop do Programa Principal
    while True:
        
        #Impressão do Menu
        print('-' * 40)
        print('MENU PRINCIPAL'.center(40))
        print('-' * 40)
        sleep(0.5)

        índice = 1
        opçõesDoMenu = ['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema']
        
        for item in opçõesDoMenu:
            print(f'\033[33m[ {índice} ]\033[0m - \033[34m{item}\033[0m')
            índice += 1
        sleep(0.5)
        print('-' * 40)

        #Entrada do Usuário com tratamento de erro para INT
        try:
            opção = int(input('\033[32mSua opção: \033[0m'))
        except:
            print('\033[31mERRO! Digite um número inteiro válido.\033[0m')
            sleep(0.5)
        else:

            #Comando realizado com a entrada
            if opção in comandos:
                comandos[opção]()
            elif opção == 3:
                print('-' * 40) 
                print('\033[35mFinalizando o sistema...\033[0m\n')
                sleep(0.5)
                break
            else:
                print('\033[31mERRO! Digite uma opção válida!\033[0m')
                sleep(0.5)
