#Aprimora o Desafio 093 com maios informações e mais entradas pela usuário
import Dicio as dic
jogadores = list()
jogador = dict()

dic.cabeçalho('ANÁLISE DE JOGADORES')

while True:
    print('-' * 40)
    jogador['Nome'] = str(input('Qual o nome do jogador a ser analisado? ')).strip().title()
    jogador['Partidas'] = int(input(f'Quantas partidas na carreira de {jogador["Nome"]}? '))
    jogador['Gols'] = list()
    for jogo in range(1, jogador['Partidas']+1):
        jogador['Gols'].append(int(input(f'Quantos gols {jogador["Nome"]} fez no jogo {jogo}? '))) 
    jogador['Total de Gols'] = sum(jogador['Gols'])

    jogadores.append(jogador.copy())
    jogador.clear()

    escolha = dic.deseja_continuar()
    if escolha == False:
        break

print('=-' * 30)
print('{:<7}{:<20}{:<20}{:<20}'.format('Cód.', 'Nome', 'Gols', 'Total de Gols'))
print('-' * 60)
for posição, elemento in enumerate(jogadores):
    print('[{:^4}]'.format(posição), end=' ')
    for chave, item in elemento.items():
        if chave == 'Total de Gols':
            print(f'{str(item):^20}', end='')
        elif chave != 'Partidas':
            print(f'{str(item):<20}', end='')
    print()
    
while True:
    print('-' * 60)
    while True:
        dados = str(input('Mostrar dados de qual jogador? ')).strip()
        if dados.isnumeric() and dados != None:
            dados = int(dados)
            break
    
    if dados == 999:
        break
    
    if dados not in range(0, len(jogadores)):
        print('Opção inválida! Tente novamente.')
    else:
        print(f'-- Levantamento do jogador {jogadores[dados]["Nome"]}')
        print(f'    => {jogadores[dados]["Partidas"]} partidas jogadas.')
        for jogo in range(1, jogadores[dados]['Partidas']+1):
            print(f'        => {jogadores[dados]["Gols"][jogo-1]} gols marcados no jogo {jogo}.')
        print(f'    => {jogadores[dados]["Total de Gols"]} gols durante a carreira.')

dic.rodapé()
