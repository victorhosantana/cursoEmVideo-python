#Cria um loop para digitação de números inteiros, contabilizando a quantidade e a soma deles
quantidade = soma = num = 0
print("""
Qual o número que você deseja adicionar ao cálculo? (999 finaliza o programa)""")
while num != 999:
    num = int(input('Seu número: '))
    if num != 999:
        quantidade += 1
        soma += num
print(f""" 
- - - Programa Finalizado - - - 

A quantidade de números digitados foi {quantidade} e a soma deles deu {soma}!
""")
