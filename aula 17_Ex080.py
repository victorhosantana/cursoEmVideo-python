#Cria um loop que adiciona entradas numéricas do usuário, ordenando-as em tempo real, sem sort()
import Dicio as dic
dic.cabeçalho('LISTA ORDENADA EM TEMPO REAL')
usuário = list()
for índice in range(0, 5):
    número = int(input('Digite um número para adicionar na lista: '))
    if len(usuário) == 0:
        print(f'O número {número} foi inserido na lista.')
        usuário.append(número)
    elif número in usuário:
        print(f'O número {número} foi adicionado na posição {usuário.index(número)}.')
        usuário.insert(usuário.index(número), número)
    else:
        controle = 0
        while controle < len(usuário):
            if número < usuário[controle]:
                print(f'O número {número} foi adicionado na posição {controle}.')
                usuário.insert(controle, número)
                break
            elif controle == len(usuário) - 1:
                print(f'O número {número} foi adicionado no final da lista.')
                usuário.append(número)
                break
            controle += 1
print('\nA lista foi finalizada com a seguinte ordem:', end=' ')
for item in usuário:
    print(item, end=' ')
dic.rodapé()
