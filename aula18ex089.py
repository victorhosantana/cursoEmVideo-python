from statistics import mean
import Dicio as dic
dic.cabeçalho('TESTE DO PROGRAMA')

alunos = []

while True:
    
    alunos.append([])
    alunos[-1].append(str(input('Digite o nome do aluno: ')).strip().title())

    alunos[-1].append([])
    alunos[-1][1].append(float(input('Digite a primeira nota deste aluno: ')))
    alunos[-1][1].append(float(input('Digite a segunda nota deste aluno: ')))

    escolha = dic.deseja_continuar()
    if escolha == False:
        break

print('=-' * 20)
print('{:^40}'. format('BOLETIM ESCOLAR'))
print('=-' * 20)
print(' No.   NOME                       MÉDIA')
print('--' * 20)
for posição, elementos in enumerate(alunos):
    print(f'[ {posição} ] {elementos[0]}', end=' ')
    print('.' * (27 - len(elementos[0])), end=' ')
    print('{:.1f}'.format(mean(elementos[1])))
print('--' * 20)

while True:
    nota = int(input('Deseja ver as notas de qual aluno? (999 interrompe o programa) '))
    if nota == 999:
        break
    elif nota not in range(len(alunos)):
        print('Opção inválida! Tente novamente.')
    else:
        print(f'As notas de {alunos[nota][0]} são {alunos[nota][1][0]} e {alunos[nota][1][1]}')
    print('--' * 20)

dic.rodapé()
