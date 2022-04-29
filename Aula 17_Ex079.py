#Cria um loop de inserção de valores pelo usuário
import Dicio as dic
dic.cabeçalho('CRIAÇÃO DE LISTA NUMÉRICA')
usuário = list()
while True:
    valor = int(input('Digite um valor numérico: '))
    if valor in usuário:
        print(f'O número {valor} já foi adicionado anteriormente!')
    else:
        print(f'O número {valor} foi adicionado com sucesso!')
        usuário.append(valor)
    escolha = dic.deseja_continuar()
    if escolha == False:
        break
print(' - ' * 10)
usuário.sort()
print(f'A lista digitada foi:', end=' ')
for item in usuário:
    print(item, end=' ')
dic.rodapé()
