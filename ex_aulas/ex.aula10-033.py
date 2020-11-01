n1 = int(input('Digite um número: '))
n2 = int(input('Diga outro número: '))
n3 = int(input('Mais outro número: '))
if n1 > n2 > n3:
    print('{} é o maior, e {} é o menor.'.format(n1, n3))
elif n1 > n3 > n2:
    print('{} é o maior, e {} é o menor.'.format(n1, n2))
elif n2 > n1 > n3:
    print('{} é o maior, e {} é o menor.'.format(n2, n3))
elif n2 > n3 > n1:
    print('{} é o maior, e {} é o menor.'.format(n2, n1))
elif n3 > n2 > n1:
    print('{} é o maior, e {} é o menor.'.format(n3, n1))
elif n3 > n1 > n2:
    print('{} é o maior, e {} é o menor.'.format(n3, n2))
