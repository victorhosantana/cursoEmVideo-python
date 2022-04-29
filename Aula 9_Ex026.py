frase = str(input('Digite uma frase qualquer: ')).strip().upper()
print("""
Na sua frase temos:
A letra "A" aparece {} vezes.
Ela aparece pela primeira vez na posição {}.
E pela última vez na posição {}.
""".format(frase.count('A'), frase.find('A'), frase.rfind('A')))
