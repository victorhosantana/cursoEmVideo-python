#Cria uma função que utilize um parâmetro para o fatorial e um parâmetro booleano para imprimir mais coisas
def fatorial(número=1, show=False):
    """ -> Calcula o fatorial de um inteiro passado como argumento.
        :param número: Valor inteiro a ser calculado.
        :param show: (Opcional) Demonstra o cálculo até chegar no resultado fatorial.
    """
    f = 1
    for item in range(número, 0, -1):
        f *= item
    print(f'{número}!', end='')
    if show and número != 1 and número != 0:
        print(' = ', end='')
        for item in range(número, 0, -1):
            print(item, end='')
            if item != 1:
                print(' x ', end='')
    print(f' = {f}')


#Programa Principal
help(fatorial)
""" fatorial(7, True)
fatorial(4, False)
fatorial(5)
 """
 