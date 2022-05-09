#Cria uma função que avalie a opção de voto com base numa entrada
from time import sleep

def voto(ano=1900):
    from datetime import date #Importação de função em Escopo Local
    idade = date.today().year - ano
    if idade < 16:
        return f'Com {idade} anos, seu voto é NEGADO.'
    elif 16 <= idade < 18 or idade >= 65:
        return f'COm {idade} anos, seu voto é OPCIONAL.'
    else:
        return f'Com {idade} anos, seu voto é OBRIGATÓRIO.'


#Programa Principal
ano = int(input('Digite o ano de seu nascimento: '))
print('ANALISANDO...')
print('-' * 30)
sleep(1)
print(voto(ano))
