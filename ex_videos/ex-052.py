numero = int(input('Digite um número: '))
divisivel = 0
for c in range(1, numero + 1):
    if numero % c == 0:
        print('\033[0;33m', end="")
        divisivel += 1
    else:
        print('\033[0;31m', end="")
    print('{} '.format(c), end='')        
print('\033[m\nO número {} foi divisível {} vezes, '.format(numero, divisivel), end='')
if divisivel == 2:
    print('por isso ele é um número primo.')
else:
    print('por isso não é um número primo.')
