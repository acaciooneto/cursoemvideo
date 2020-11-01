import math
a = float(input('Digite um ângulo: '))
ang = math.radians(a) #LEMBRAR DE CONVERTER O ANGULO PARA RADIANS
print('O seno desse ângulo é {:.2f}, seu cosseno é {:.2f} e sua tangente é {:.2f}.'.format(math.sin(ang), math.cos(ang), math.tan(ang)))
