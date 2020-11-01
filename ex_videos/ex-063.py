print('Vamos conhecer a sequência de Fibonacci?')
termos = int(input('Quantos termos você quer ver? '))
contagem = 2
t1 = 0
t2 = 1
print('{} -> {} -> '.format(t1, t2), end='')
while contagem != termos:
    contagem += 1
    t3 = t1 + t2
    print('{} -> '.format(t3), end='')
    t1 = t2
    t2 = t3
print('Fim!')
