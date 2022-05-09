#Cria uma 'mini-sistema' colorido para o usuário utilizar o Interactive Help do Python
import Dicio as dic
import pydoc
pydoc.pager = pydoc.plainpager

def ajuda(msg):
    print('{}'.format(dic.cores['fundopreto']), end='')
    help(str(msg))
    print('{}'.format(dic.cores['limpa']))

# Programa Principal
while True:
    print('~' * 30)
    print('{}'.format(dic.cores['fundoverde']), end='')
    print(f'{"SISTEMA DE AJUDA DO PYTHON":^30}', end='')
    print('{}'.format(dic.cores['limpa']))
    print('~' * 30)
    escolha = str(input('Biblioteca ou Função: ')).strip()
    if escolha.upper() == 'FIM':
        break
    ajuda(escolha)

print('~' * 30)
print('{}'.format(dic.cores['fundovermelho']), end='')
print(f'{"Até logo":^30}', end='')
print('{}'.format(dic.cores['limpa']))
print('~' * 30)
