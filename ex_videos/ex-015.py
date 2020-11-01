d = int(input('Diga quantos dias você ficou com o carro: '))
km = float(input('Diga quantos quilometros você rodou com o carro: '))
valor = (d * 60) + (km * 0.15)
print('Você terá que pagar {:.2f} R$ pelo aluguel do carro. Obrigado, volte sempre.'.format(valor))
