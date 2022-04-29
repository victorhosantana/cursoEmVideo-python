#Cria uma função que analisa dados de entrada, independente da quantidade de entradas, e retorna um dicionário
def notas(*entradaNotas, sit=False):
    """---> Esta função recebe uma quantidade de notas como entrada e realiza uma análise detalhada.
    :param *entradaNotas: Descompacta todas as notas passados como parâmetro.
    :param sit: (Opcional) Verifica a situação da média entre as notas informadas.
    """
    from statistics import mean

    dicio = {
        'Notas' : entradaNotas,
        'Quantidade' : len(entradaNotas),
        'Maior' : max(entradaNotas),
        'Menor' : min(entradaNotas),
        'Média' : mean(entradaNotas)
    }
    
    if dicio['Média'] < 3:
        situação = 'HORRÍVEL'
    elif 3 <= dicio['Média'] < 5:
        situação = 'RUIM'
    elif 5 <= dicio['Média'] < 7:
        situação = 'OK'
    elif 7 <= dicio['Média'] < 9:
        situação = 'BOA'
    elif 9 <= dicio['Média']:
        situação = 'EXCELENTE'
    
    if sit:
        dicio['Situação'] = situação

    return dicio

#Programa Principal
resultado = notas(7, 9, 3, 8, sit=True)
print(resultado)
# help(notas)
