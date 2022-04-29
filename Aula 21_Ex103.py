#Cria uma função que 'valida' algumas informações de entrada
def ficha(nome='<desconhecido>', gols=0):
    
    if nome == '':
        nome = '<desconhecido>'

    if gols.__class__ == str:
        if gols.isnumeric():
            gols = int(gols)
        else:
            gols = 0
    
    print(f'O jogador {nome} fez {gols} gols durante esta temporada.')


#Programa Principal
jogador = str(input('Qual o nome do jogador? ')).strip().capitalize().replace(' ','')
gol = input('Quantos gols ele marcou? ')
ficha(jogador, gol)
