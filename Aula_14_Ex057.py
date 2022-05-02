#Teste de entrada correta com repetições While
sexo = ' '
while sexo not in 'mMfF':
    sexo = str(input('Digite o sexo da pessoa (M/F): ')).strip()
if sexo in 'mM':
    print('Sexo Masculino registrado com sucesso!')
else:
    print('Sexo Feminino registrado com sucesso!')
