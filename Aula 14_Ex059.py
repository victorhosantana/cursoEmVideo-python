#Criação de um Menu com repetição While
print("""
- - - Calculadora simples - - - 
""")
escolha = 0
while escolha != 5:
    if escolha == 4 or escolha == 0:
        print('Informar os números.\n')
        valor1 = float(input('Primeiro valor: '))
        valor2 = float(input('Segundo valor: '))
        if valor1 < valor2:
            maior = valor2
        else:
            maior = valor1
    print()
    print('=-' * 33)
    print(f'Os valores atuais são {valor1:.2f} e {valor2:.2f}. O que você deseja saber agora? ')
    print('-=' * 33)
    escolha = int(input("""
[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Digitar Novos Números
[ 5 ] Sair do Programa

Sua opção: """))
    if escolha != 1 and escolha != 2 and escolha != 3 and escolha != 4 and escolha != 5:
        print('\nOperação não existe. Tente novamente.\n')
    if escolha == 1:
        print(f'\nA soma de {valor1:.2f} e {valor2:.2f} é {valor1 + valor2:.2f}.\n')
    if escolha == 2:
        print(f'\nA multiplicação de {valor1:.2f} e {valor2:.2f} é {valor1 * valor2:.2f}.\n')
    if escolha == 3:
        print(f'\nEntre {valor1:.2f} e {valor2:.2f}, o MAIOR valor é o {maior:.2f}.\n')
print('\n - - - FIM DO PROGRAMA - - - \n')
