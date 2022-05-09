import emoji
from datetime import date
print('Teste de ano BISSEXTO. Digite "0" para usar o ano atual.')
ano = int(input('Informe o ano para saber se é bissexto: '))
'''if (ano % 4) == 0:
    if (ano % 100) == 0:
        if (ano % 400) != 0:
            print(emoji.emojize(f'O ano {ano} não é bissexto! :thumbsdown:', language='alias'))
        else:
            print(emoji.emojize(f'O ano {ano} é bissexto! :thumbsup:', language='alias'))
    else: print(emoji.emojize(f'O ano {ano} é bissexto! :thumbsup:', language='alias'))
else:
    print(emoji.emojize(f'O ano {ano} não é bissexto! :thumbsdown:', language='alias'))
'''
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(emoji.emojize(f'O ano {ano} é bissexto! :thumbsup:', language='alias'))
else:
    print(emoji.emojize(f'O ano {ano} não é bissexto! :thumbsdown:', language='alias'))
