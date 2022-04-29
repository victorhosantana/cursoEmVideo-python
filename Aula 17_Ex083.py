#Desenvolver um programa que avalie expressões matemáticas e informe se está correta
import Dicio as dic
dic.cabeçalho('AVALIADOR DE EXPRESSÕES')
print('Informe uma expressão matemática com parênteses () para o programa avaliar se é válida.')
frase = str(input('Sua expressão: ')).strip().replace(' ','')
pilha = list()
for item in frase:
    if item == '(':
        pilha.append(item)
    elif item == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(item)
if len(pilha) > 0:
    print('Sua expressão é {}inválida{}!'.format(dic.cores['vermelho'], dic.cores['limpa']))
else:
    print('Sua expressão é {}válida{}!'.format(dic.cores['verde'], dic.cores['limpa']))
dic.rodapé()
