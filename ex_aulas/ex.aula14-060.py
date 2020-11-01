'''from math import factorial
num = int(input('Digite um valor: '))
print('{}! = {}'.format(num, factorial(num)))'''

fatorial = int(input('Digite um número: '))
multiplicador = fatorial - 1
resultado = 0
contagem = 0
while multiplicador != 0:
    contagem += 1
    if contagem == 1:
        resultado = fatorial * multiplicador
        multiplicador = multiplicador - 1
    else:
        resultado = resultado * multiplicador
        multiplicador = multiplicador - 1
print('{}! = {}.'.format(fatorial, resultado))

'''fatorial = int(input('Digite um número: '))
for numero in range(fatorial, 1, -1):
    if numero == fatorial:
        numero = numero - 1
        resultado = fatorial * numero
        print('{} x {} = {}'.format(fatorial, numero, resultado))
    else:
        numero = numero - 1
        print('{} x {} = '.format(resultado, numero),end='')
        resultado = resultado * numero
        print('{}'.format(resultado))
print('{}! = {}'.format(fatorial, resultado))'''
