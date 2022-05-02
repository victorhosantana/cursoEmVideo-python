Ângulo = float(input('Digite o valor do ângulo: '))
from math import sin, cos, tan, radians
print('Para o ângulo de {}°, temos:\nSeno: {:.2f}\nCosseno: {:.2f}\nTangente: {:.2f}'.format(Ângulo, sin(radians(Ângulo)), cos(radians(Ângulo)), tan(radians(Ângulo))))
