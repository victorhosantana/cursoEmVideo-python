#Cria um Dicionário que armazene informações sobre um jogador de futebol
jogador = dict()

jogador['Nome'] = str(input('Qual o nome do jogador a ser analisado? ')).strip()
jogador['Partidas'] = int(input(f'Quantas partidas na carreira de {jogador["Nome"]}? '))
jogador['Gols'] = list()
for jogo in range(1, jogador['Partidas']+1):
    jogador['Gols'].append(int(input(f'Quantos gols {jogador["Nome"]} fez no jogo {jogo}? '))) 
#jogador['Gols'] = gols.copy() -> É possível fazer por uma lista e adicionar ao Dicionário
jogador['Total de Gols'] = sum(jogador['Gols'])

print('=-' * 20)
print(f'Seguem as informações de {jogador["Nome"]}:')
print(f'    => {jogador["Partidas"]} partidas jogadas.')
for jogo in range(1, jogador['Partidas']+1):
    print(f'        => {jogador["Gols"][jogo-1]} gols marcados no jogo {jogo}.')
print(f'    => {jogador["Total de Gols"]} gols durante a carreira.')
print('=-' * 20)
print(jogador)
print('=-' * 20)
