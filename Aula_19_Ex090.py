#Cria um dicionário com entradas do usuário e calcula uma situação
aluno = dict()
aluno['Nome'] = str(input('\nInforme o nome do aluno: ')).strip()
aluno['Média'] = float(input(f'Informe a média de {aluno["Nome"]}: '))
aluno['Situação'] = 'Aprovado' if aluno['Média'] >= 7 else 'Reprovado'
print()

for k,v in aluno.items():
    print(f'{k} = {v}')
print()
