#Cria um Dicionário que receba informações de pessoas como entrada e analize os dados
import Dicio as dic
pessoas = list()
pessoa = dict()

while True:
    pessoa['Nome'] = str(input('Digite o nome da pessoa: ')).strip()
    pessoa['Sexo'] = dic.pergunta_sexo()
    pessoa['Idade'] = int(input('Informe a idade da pessoa: '))

    pessoas.append(pessoa.copy())
    pessoa.clear()

    escolha = dic.deseja_continuar()
    if escolha == False:
        break

média = 0
mulheres = list()
acima_média = list()

for elemento in pessoas:
    média += elemento['Idade']

média = média / len(pessoas)

for elemento in pessoas:
    if elemento['Sexo'] == 'F':
        mulheres.append(elemento['Nome'])
    if elemento['Idade'] > média:
        acima_média.append(elemento['Nome'])

print('=-' * 20)
print(f'Foram cadastradas {len(pessoas)} pessoas.')
print(f'A média de idade do grupo é {média:.1f} anos')
print('As mulheres cadastradas foram:', mulheres if len(mulheres) > 1 else 'Nenhuma mulher foi cadastrada')
print('As pessoas com idade acima da média são:', acima_média)
print('=-' * 20)
