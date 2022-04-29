#Cria um loop com entrada de informações sobre as pessoas e retorna uma análise com os dados
contador_pessoas = contador_homens = contador_mulheres = 0
while True:
    print('=-' * 20, '\nCADASTRO DE PESSOAS\n', '-=' * 20, '\n')
    while True:
        idade_entrada = str(input('Informe a idade: ')).strip().upper()
        idade_entrada = idade_entrada.replace(' ','')
        if idade_entrada.isnumeric():
            idade = int(idade_entrada)
            if idade >= 0:
                break
    while True:
        sexo = str(input('Informe o sexo [M/F]: ')).strip().upper()
        sexo = sexo.replace(' ','')
        if sexo != '' and sexo in 'mMfF':
            break
    if idade >= 18:
        contador_pessoas += 1
    if sexo in 'mM':
        contador_homens += 1
    else:
        if idade < 20:
            contador_mulheres += 1
    while True:
        escolha = str(input('Dseja continuar [S/N]? ')).strip().upper()
        escolha = escolha.replace(' ','')
        if escolha != '' and escolha in 'sSnN':
            break
    if escolha in 'nN':
        break
print(' ===== FIM DO PROGRAMA ===== ')
print(f""" - - - - - - - - - - - - - - -
Informações sobre os cadastros que você realizou:
Pessoas com mais de 18 anos: {contador_pessoas}
Total de homens: {contador_homens}
Mulheres menores de 20 anos: {contador_mulheres}
""")
