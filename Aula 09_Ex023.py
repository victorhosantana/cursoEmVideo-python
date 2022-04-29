n = str(input('Digite um número inteiro entre 0 e 9999: '))
print('O número {} possui:\nUnidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}'.format(n, n[3], n[2], n[1], n[0]))
print(' ')
num = int(n)
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print("""A demonstração matemática fica:
Unidade: {}
Dezena: {}
Centena: {}
Milhar: {}""".format(u, d, c, m))
