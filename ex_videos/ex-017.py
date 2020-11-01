import math
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
hip = math.hypot(co, ca)
print('A hipotenusa desse triângulo foi é {:.2f}.'.format(hip))
