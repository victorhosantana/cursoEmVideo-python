#Cálculo de média do aluno
import Dicio as dic
import emoji

nota1 = float(input('\nQual foi a sua primeira nota? '))
nota2 = float(input('Qual foi a sua segunda nota? '))

media = (nota1 + nota2)/2

if media < 5:
    print(emoji.emojize('\nSua média foi de {}{:.1f}{}. Reprovado! :sob:'.format(dic.cores['vermelho'], media, dic.cores['limpa']), language='alias'))
elif media >= 5 and media < 7:
    print(emoji.emojize('\nSua média foi de {}{:.1f}{}. Ficou em recuperação. :scream:'.format(dic.cores['amarelo'], media, dic.cores['limpa']), language='alias'))
else:
    print(emoji.emojize('\nSua média foi de {}{:.1f}{}. Aprovado! :smile:'.format(dic.cores['verde'], media, dic.cores['limpa']), language='alias'))
