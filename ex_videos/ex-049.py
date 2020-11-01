numero = int(input('Digite um número: '))
for multiplicador in range(0, 11):
    print('{} x {} = {}'.format(numero, multiplicador, numero * multiplicador))
