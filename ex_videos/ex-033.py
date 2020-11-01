a = int(input('Digite um valor: '))
b = int(input('Digite outro valor: '))
c = int(input('Mais outro valor: '))

menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print('O menor número foi {}.'.format(menor))
print('O maior número foi {}.'.format(maior))
