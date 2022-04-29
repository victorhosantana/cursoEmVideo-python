#Cria um loop de inserções numéricas na lista do usuário
import Dicio as dic
dic.cabeçalho('LOOP DE NÚMEROS')
usuário = []
while True:
    usuário.append(int(input('Digite um número para adicionar na lista: ')))
    escolha = dic.deseja_continuar()
    if escolha == False:
        break
print('A lista foi criada com sucesso!')
print(f'Foram digitados {len(usuário)} números.')
print('A lista de forma decrescente é:', end='')
usuário.sort(reverse=True)
for item in usuário:
    print(f' {item}', end='')
print('.')
if 5 in usuário:
    print('O número 5 foi digitado na lista e está nas posições', end=' ')
    for posição, item in enumerate(usuário):
        if item == 5:
            print(posição, end=' ')
    print('.')
else:
    print('O número 5 não foi encontrado na lista.')
dic.rodapé()
