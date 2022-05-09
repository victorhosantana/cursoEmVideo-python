nome = str(input('Digite o seu nome completo: '))
nome = nome.title().strip()
div = nome.split()
print("""
Primeiro nome: {}
Último nome: {}""".format(div[0], div[(len(div)-1)]))
