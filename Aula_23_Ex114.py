#Cria um programa que verifique se um site está acessível no momento
import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.google.com/')
except:
    print('\nO site \033[31mNÃO ESTÁ\033[0m acessível no momento.\n')
else:
    print('\nO site \033[32mESTÁ\033[0m acessível no momento.\n')
