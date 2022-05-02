#Contagem regressiva para o estouro de fogos de artifício
import Dicio as dic
import emoji
from time import sleep

print('\n', '-=' * 10, 'CONTAGEM REGRESSIVA', '=-' * 10, '\n')
for c in range (10, -1, -1):
    if c == 5:
        print('{}'.format(dic.cores['amarelo']), end='')
    if c == 3:
        print('{}'.format(dic.cores['vermelho']), end='')
    print(c)
    sleep(0.5)
print(emoji.emojize('\n{}{}PARABÉNS!!!{} :sparkles:'.format(dic.cores['limpa'], dic.cores['negrito'], dic.cores['limpa']),language='alias'))
