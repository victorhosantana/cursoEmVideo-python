m = float(input('Informe o valor em metros: '))
print('O valor informado foi de {} metros.\nIsto equivale a {:.0f} centimetros e a {:.0f} milimetros.\nAdicionalmente, isto equivale a {}km, {}hm, {}dam e {}dm.'.format(m, m*100, m*1000, m/1000, m/100, m/10, m*10))
