velor = float(input('Qual foi a velocidade que tu passou? '))
if velor > 80:
    print('Levou multa, otário!\nTu passou a {}Km/h e vai ter que desembolsar {} pratas.'.format(velor, (velor-80)//1*7))
else:
    print(f'Muito suspeito... andando a {velor}Km/h, certinho e dentro da lei...')
