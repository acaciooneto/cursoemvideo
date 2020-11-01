# an = a1 + (n - 1)*r
a1 = int(input('Digite o primeiro termo da PA: '))
razão = int(input('Digite a razão dessa PA: '))
an = a1 - razão
for numero in range(1, 11):
    an += razão
    print('{}º termo: {}.'.format(numero, an))
