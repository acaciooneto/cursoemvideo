vp = float(input('Digite o valor do produto vendido: '))
vcd = (vp * 90)/100
vap = (vp * 108)/100
#fp = int(input("digite 1 se o pagamento for feito a vista, ou 2 se for a prazo: "))
#if fp == 1 
#    print('Como o pagamento é a vista, com o desconto de 10% ele vai sair por {} R$.'.format(vcd))
#     else:
#    print('Como vai ser feito a prazo, o novo valor, com acréscimo de 8% fica em {} R$.')
print('Se o pagamento for a vista, temos um desconto de 10%, ficando o valor de {:.2f} R$.'.format(vcd))
print('Mas se o pagamento for a prazo, terá o acréscimo de 8%, ficando o valor de {:.2f} R$.'.format(vap))
