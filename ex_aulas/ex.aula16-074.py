from random import randint
aleatórios = (randint(0, 10), randint(0, 10), 
randint(0, 10), randint(0, 10), randint(0, 10))
print('Os valores sorteados foram: ',end='')
for valores in aleatórios:
    print(f'{valores}',end=' ')
ordenados = sorted(aleatórios)
print(f'\nO menor valor foi {ordenados[0]}') #{min(aleatórios)}
print(f'O maior valor foi {ordenados[4]}') #{mas(aleatórios)}
