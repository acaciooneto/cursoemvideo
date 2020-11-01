num = int(input('Digite um número: '))
#multiplicador = -1 (mania feia do carai)
print('A tabuada de {} é:'.format(num))
for tabuada in range(0, 11):
    multiplicador = tabuada # não precisa disso, só botar 'tabuada' embaixo
    resultado = num * multiplicador # nem isso também, podia * dentro do format
    print('{} x {} = {}'.format(num, multiplicador, resultado ))
