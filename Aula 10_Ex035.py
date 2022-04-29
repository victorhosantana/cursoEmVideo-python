reta1 = float(input('Qual a medida da primeira reta, em centímetros? '))
reta2 = float(input('Qual a medida da segunda reta, em centímetros? '))
reta3 = float(input('Qual a medida da terceira reta, em centímetros? '))
'''if (reta1 + reta2) > reta3:
    if (reta1 + reta3) > reta2:
        if (reta2 + reta3) > reta1:
            print('Beleza! As retas de medida {:.2f}cm, {:.2f}cm e {:.2f}cm podem formar um triângulo!'.format(reta1, reta2, reta3))
        else:
            print('Não rolou! As restas de medida {:.2f}cm, {:.2f}cm e {:.2f}cm não podem formar um triângulo!'.format(reta1, reta2, reta3))
    else:
        print('Não rolou! As restas de medida {:.2f}cm, {:.2f}cm e {:.2f}cm não podem formar um triângulo!'.format(reta1, reta2, reta3))
else:
    print('Não rolou! As restas de medida {:.2f}cm, {:.2f}cm e {:.2f}cm não podem formar um triângulo!'.format(reta1, reta2, reta3))
'''
if reta1 + reta2 > reta3 and reta1 + reta3 > reta2 and reta2 + reta3 > reta1:
    print('Beleza! As retas de medida {:.2f}cm, {:.2f}cm e {:.2f}cm podem formar um triângulo!'.format(reta1, reta2, reta3))
else:
    print('Não rolou! As retas de medida {:.2f}cm, {:.2f}cm e {:.2f}cm não podem formar um triângulo!'.format(reta1, reta2, reta3))
