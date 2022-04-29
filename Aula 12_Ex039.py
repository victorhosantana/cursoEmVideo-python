import Dicio as dic
from time import sleep
from datetime import date

sexo = int(input("""
Digite a opção referente ao seu sexo:

{}[ 1 ] Masculino
{}[ 2 ] Feminino
{}[ 3 ] {}Xx{}tr{}xs{}

Sua opção: """.format(dic.cores['azulclaro'], dic.cores['vermelho'], dic.cores['limpa'], dic.cores['verde'], dic.cores['roxo'], dic.cores['amarelo'], dic.cores['limpa'])))

if sexo != 1 and sexo != 2 and sexo != 3:
    print('A opção informada não é válida. Tente novamente!')
else:
    if sexo == 3:
        print('Vxcx nxx prxcxsx sx xlxstxr!')
    elif sexo == 2:
        print('Que sorte a sua! Mulheres não são obrigadas a se alistar no Brasil.')
    else:
        ano = int(input('\nInforme o ano de seu nascimento: '))
        idade = date.today().year - ano

        print('\n{}PROCESSANDO...{}\n'.format(dic.cores['azulpiscina'], dic.cores['limpa']))
        sleep(0.7)

        if idade == 18:
            print('Você tem {}{}{} anos e está na hora de se alistar!\n'.format(dic.cores['verde'], idade, dic.cores['limpa']))
        elif idade > 18:
            print('Você tem {}{}{} anos e já passou do tempo de alistamento em {}{}{} anos!'.format(dic.cores['amarelo'], idade, dic.cores['limpa'], dic.cores['vermelho'], idade - 18, dic.cores['limpa']))
            print('Seu ano de alistamento foi em {}{}{}\n'.format(dic.cores['sublinhado'], date.today().year - (idade - 18), dic.cores['limpa']))
        else:
            print('Você tem {}{}{} anos e ainda vai precisar se alistar em {}{}{} anos!'.format(dic.cores['amarelo'], idade, dic.cores['limpa'], dic.cores['verde'], 18 - idade, dic.cores['limpa']))
            print('Seu ano de alistamento será em {}{}{}\n'.format(dic.cores['sublinhado'], date.today().year + (18 - idade), dic.cores['limpa']))
