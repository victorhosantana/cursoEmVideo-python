#Bibliotecas utilizadas
import emoji

#Dicionário de cores para o terminal
cores = {
    'limpa' : '\033[0m',
    'branco' : '\033[0;30m',
    'vermelho' : '\033[0;31m',
    'verde' : '\033[0;32m',
    'amarelo' : '\033[0;33m',
    'azulclaro' : '\033[0;34m',
    'roxo' : '\033[0;35m',
    'azulpiscina' : '\033[0;36m',
    'preto' : '\033[0;37m',
    'negrito' : '\033[1m',
    'sublinhado' : '\033[4m',
    'negsub' : '\033[1;4m',
    'fundopreto' : '\033[40m',
    'fundovermelho' : '\033[41m',
    'fundoverde' : '\033[42m',
    'fundoamarelo' : '\033[43m',
    'fundoazulclaro' : '\033[44m',
    'fundoroxo' : '\033[45m',
    'fundoazulpiscina' : '\033[46m',
    'fundobranco' : '\033[47m'
}

#Função para perguntar se o usuário quer continuar com o programa
def deseja_continuar():
    while True:
        print(' - ' * 8)
        escolha = str(input('Quer continuar [S/N]? ')).strip().replace(' ','')
        if escolha in 'sSnN' and escolha != '':
            print(' - ' * 8)
            break
        else:
            print('Opção inválida! Tente novamente.')
            print(' - ' * 8)
    if escolha in 'nN':
        continuar = False
    else:
        continuar = True
    return continuar

#Função para perguntar o sexo
def pergunta_sexo():
    while True:
        sexo = str(input('Informe o sexo: ')).strip().upper().replace(' ','')
        if sexo not in 'MF':
            print('Opção inválida! Tente novamente.')
        else:
            break
    return sexo

#Função para imprimir um cabeçalho no início dos programas
def cabeçalho(texto):
    print()
    print('=-' * 20)
    print(f'{texto:^40}')
    print('=-' * 20)
    print()

#Função para imprimir um rodapé no final dos programas
def rodapé():
    print()
    print('~' * 40)
    print('{:^40}'.format('FIM DO PROGRAMA'))
    print('~' * 40)
    print()
