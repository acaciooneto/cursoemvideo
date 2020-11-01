for c in range(1, 10):
    print(c, end= ' ')
print('fim')

a = 1
while a < 10:
    print(a, end= ' ')
    a += 1
print('end')

'''n = 1
while n != 0:
    n = int(input('Digite um valor: '))
print('cabô')

r = 'S'
while r == 'S':
    n = int(input('Digite o valor: '))
    r = str(input('Quer continuar? [S/N]: ')).upper()
print('é isso pessoal')'''

o = 1
par = impar = 0
while o != 0:
    o = int(input('Digite um valor: '))
    if o % 2 == 0:
        par += 1
    else:
        impar += 1

print('terminou e vc digitou {} pares e {} ímpares.'.format(par, impar))
