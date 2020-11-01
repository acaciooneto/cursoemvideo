n1 = float(input('digite aqui a primeira nota: '))
n2 = float(input('agora a segunda: '))
n3 = float(input('a terceira nota: '))
n4 = float(input('e a quarta: '))
m = (n1+n2+n3+n4)/4
print('a média entre {}, {}, {} e {} foi {:.1f}.'.format(n1, n2, n3, n4, m))
if m >= 7:
    print('parabéns, você passou!')
#    elif m <= 3:
 #       print('você foi reprovado :(')
  #      else
   #     print('você ficou de recuperação :/')
