print('Então quer dizer que você vai viajar?')
dist = int(input("Que legal! diga-nos quantos km's é essa sua viagem: "))
'''if dist <= 200:
    print('Sua passagem irá custar {:.2f} R$.'.format(dist*0.50))
else:
    print('Sua passagem irá custar {:.2f} R$.'.format(dist*0.45))''' #as 3 aspas transforma em coment
# ELE FAZ COM EM CONDIÇÃO SIMPLES COM OPERADOR TERNÁRIO
preço = dist * 0.50 if dist <= 200 else dist * 0.45
print('Sua passagem irá custar {:.2f} R$.\nFaça uma boa viagem!'.format(preço))
