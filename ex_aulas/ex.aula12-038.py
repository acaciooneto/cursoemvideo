n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))
if n1 > n2:
    print('O primeiro valor ({}) É maior que o segundo ({})'.format(n1, n2))
elif n2 > n1:
    print('O segundo valor ({}) É maior que o primeiro ({})'.format(n2, n1))
elif n1 == n2:
    print('Os valores digitados são iguais.')
