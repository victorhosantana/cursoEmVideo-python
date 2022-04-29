#Identifica os Palíndromos para cada frase digitada
frase = str(input('Digite a frase para verificar se é palíndromo.\nSua frase: ')).strip().lower()
frase2 = frase
p = 'não é um Palíndromo'
frase = frase.replace(' ','')
if frase == frase[::-1]:
    p = 'é um Palíndromo'
print('\nA sua frase {}!'.format(p))

print('\nOutra solução no código:')
inverso = ''
frase2 = frase2.strip().upper().split()
frase2 = ''.join(frase2)
for letra in range(len(frase2) - 1, -1, -1):
    inverso += frase2[letra]
print(f'As frases {frase2} e {inverso} ', end='')
if frase2 == inverso:
    print('formam um palíndromo!\n')
else:
    print('não formam um palíndromo!\n')
