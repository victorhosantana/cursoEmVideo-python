a = float(input('Qual é a altura da parede? '))
l = float(input('Qual é a largura da parede? '))
print('Com uma tinta que pinta 2m² por litro, você vai precisar de {1:.2f} litros para pintar o total de {0:.2f}m² de área da parede.'.format(a*l, (a*l)/2))
