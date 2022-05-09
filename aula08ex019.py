import random
a1 = str(input('Qual o nome do aluno 1? '))
a2 = str(input('Qual o nome do aluno 2? '))
a3 = str(input('Qual o nome do aluno 3? '))
a4 = str(input('Qual o nome do aluno 4? '))
rnd = random.choice([a1, a2, a3, a4])
print('O aluno sorteado foi {}!'.format(rnd))
