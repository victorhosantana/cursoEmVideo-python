#Refazer o Desafio 064, utilizando o comando Break
quantidade = soma = 0
print("""
Qual o número que você deseja adicionar ao cálculo? (999 finaliza o programa)""")
while True:
    num = int(input('Seu número: '))
    if num == 999:
        break
    quantidade += 1
    soma += num
print(f""" 
- - - Programa Finalizado - - - 

A quantidade de números digitados foi {quantidade} e a soma deles deu {soma}!
""")
