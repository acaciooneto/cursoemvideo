import math
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
h = math.sqrt( co**2 + ca**2 )
print('A hipotenusa desse triângulo retângulo é {:.2f}.'.format(h))
