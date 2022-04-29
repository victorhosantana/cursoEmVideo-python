#Cria um loop enquanto o usuário quiser digitar valores
quantidade = soma = num = media = maior = menor = 0
continuar = 'S'
while continuar in 'sS':
    num = int(input('\nDigite o número: '))
    quantidade += 1
    soma += num
    if quantidade == 1:
        maior = menor = num
    maior = max(maior, num)
    menor = min(menor, num)
    continuar = ''
    while continuar != 'S' and continuar != 'N':
        continuar = str(input('Deseja continuar (S/N)? ')).strip().upper()
        continuar = continuar.replace(' ','')
        if continuar != 'S' and continuar != 'N':
            print('\nOpção inválida! Tente novamente.   ')
media = soma / quantidade
print(f"""
 - - - PROGRAMA FINALIZADO - - - 
 
Você digitou {quantidade} números.
Média: {media:.1f}
Maior: {maior}
Menor: {menor}
""")
