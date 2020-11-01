vp = float(input('Digite o valor do produto que irá ser descontado: '))
d = int(input('Diga agora porcento ele irá ser descontado:  '))
vd = (vp * (100 - d))/100
print('Já que o produto custa {:.2f} R$, e o desconto foi de {} %, na promoção ele sairá por {:.2f} R$'.format(vp, d, vd))
