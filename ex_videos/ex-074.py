from random import randint
aleatórios = (randint(0, 10), randint(0, 10), 
randint(0, 10), randint(0, 10), randint(0, 10))
print('Os números sorteados foram: ', end='')
for elementos in aleatórios:
    print(elementos, end=' ')
print(f'\nO maior valor foi {max(aleatórios)} e o menor foi {min(aleatórios)}.')
