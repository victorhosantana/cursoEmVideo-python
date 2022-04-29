import Dicio as dic

print('\n{}{:=^40}{}'.format(dic.cores['verde'], ' LOJA DO VICTOR ', dic.cores['limpa']))

preço = float(input('\nQual é o preço do produto? R$'))
cond = int(input("""
Qual será a condição de pagamento? Digite uma das opções válidas

1 - Dinheiro/Cheque
2 - 1x Cartão
3 - 2x no Cartão
4 - 3x ou mais no Cartão

Qual é sua opção: """))

if cond != 1 and cond != 2 and cond != 3 and cond != 4:
    print(f'\nA opção {cond} para a condição de pagamento não é válida. Tente novamente!')
else:
    print('\nO valor de {}R${:.2f}{} será pago'.format(dic.cores['negrito'], preço, dic.cores['limpa']), end=' ')
    if cond == 1:
        print('à vista, com {}dinheiro ou cheque{}, e terá 10% de desconto.'.format(dic.cores['negrito'], dic.cores['limpa']))
        novopreço = preço * 0.9
    elif cond == 2:
        print('à vista, no {}cartão{}, e terá 5% de desconto.'.format(dic.cores['negrito'], dic.cores['limpa']))
        novopreço = preço * 0.95
    elif cond == 3:
        print('parcelado, em {}2x no cartão{}, e não terá desconto.'.format(dic.cores['negrito'], dic.cores['limpa']))
        novopreço = preço
        print(f'Para o pagamento em 2x, cada parcela será de {novopreço/2:.2f}')
    else:
        print('parcelado, em {}3x ou mais vezes no cartão{}, e terá 20% de juros.'.format(dic.cores['negrito'], dic.cores['limpa']))
        qtdparc = int(input('Quantas parcelas? '))
        novopreço = preço * 1.2
        print(f'Para o pagamento em {qtdparc}x, cada parcela será de {novopreço/qtdparc:.2f}')
    print('O valor total da compra será de {}R${:.2f}'.format(dic.cores['sublinhado'], novopreço))
