import math
an = float(input('Digite um ângulo qualquer: '))
ang = math.radians(an)
seno = math.sin(ang)
coss = math.cos(ang)
tang = math.tan(ang)
print('O seno de {}° é {:.2f}, o cosseno vale {:.2f} e sua tangente vale {:.2f}.'.format(an, seno, coss, tang))
