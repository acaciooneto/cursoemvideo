#numero = input('Digite um número de 0 a 9999: ')
#uni = numero[-1]
#dez = numero[-2]
#cen = numero[-3]
#mil = numero[-4]
#print("""A unidade é: {}
#A dezena é: {}
#A centena é: {}
#A milhar é: {}""".format(uni, dez, cen, mil))

# ele não está funcionando para numeros com menos de 4 digitos :(

# MODELO MATEMÁTICO
num = int(input('Digite um número de 0 a 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print("""O que descobrimos foi que
A unidade é: {}
A dezena é: {}
A centena é: {}
A milhar é: {}""".format(u, d, c, m))
