#Crie uma Tupla e analize as vogais de todas as palavras
import Dicio as dic
palavras = tuple(['patrono', 'estupefaça', 'wingardium leviosa', 'avada kedavra', 'lumus', 
                    'alohomora', 'crucius', 'accio', 'imperius', 'reparo'])
for mágicas in palavras:
    mágicas = mágicas.lower()
    if 'a' in mágicas or 'e' in mágicas or 'i' in mágicas or 'o' in mágicas or 'u' in mágicas:
        print('\nA palavra {}{}{} possui as vogais:'.format(dic.cores['azulpiscina'], mágicas.title(), dic.cores['limpa']), end=' ')
        print('{}'.format(dic.cores['negrito']), end='')
        for vogais in mágicas:
            if vogais in 'aeiou':
                print(vogais, end=' ')
        print('{}'.format(dic.cores['limpa']), end='')
    else:
        print(f'A palavra {mágicas.title()} não possui vogais.')
print('\n')
