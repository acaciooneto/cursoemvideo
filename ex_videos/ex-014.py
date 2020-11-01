c = float(input('Olá, digite aqui quantos graus celsius você quer que seja convertido: '))
print('Essa temperatura, em graus Fahrenheit, é de {:.1f} ºF.'.format((c * (9/5)) + 32 ))
print('Se você quiser saber em Kelvin, isso dá {:.1f} K'.format(c + 273.15))
