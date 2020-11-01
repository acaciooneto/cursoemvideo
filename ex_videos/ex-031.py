dist = int(input("Diga-nos quantos km's tem essa viagem que você quer fazer: "))
preço = dist * 0.50 if dist <= 200 else dist * 0.45
print('O valor de sua passagem será {} R$.'.format(preço))
