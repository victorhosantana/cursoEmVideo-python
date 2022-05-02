#Cria uma Tupla com a classificação dos times do Campeonato Brasileiro Atual e realiza análises
times = ('São Paulo', 'Coritiba', 'Corinthinas', 'Atlético-MG', 'Ceará SC', 'Avaí', 'Cuiabá',
        'Bragantino', 'Juventude', 'Flamengo', 'Atlético-GO', 'Santos', 'Fluminense', 
        'Palmeiras', 'Fortaleza', 'América-MG', 'Botafogo', 'Internacional', 'Goiás', 
        'Atlético-PR')
print('~' * 20, '\nTIMES DO BRASILEIRÃO SÉRIE A\n', '~' * 20)
print(f"""Seguem as análises:
A) Os 5 primeiros colocados são: {times[:5]}
B) Os últimos 4 colocados são: {times[-4:]}
C) A ordem alfabética é: {sorted(times)}
D) Em qual posição está o Bragantino? {times.index('Bragantino') + 1}
""")
