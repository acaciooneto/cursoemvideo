numeros = (int(input('Digite um número: ')),
int(input('Digite outro número: ')),
int(input('Digite mais um número: ')),
int(input('Digite um último número: ')))
print(f'Os números digitados foram: {numeros}.')
print(f'O número 9 apareceu {numeros.count(9)} vezes.')
if 3 in numeros:
    print(f'O número 3 apareceu na {numeros.index(3)}ª posição.')
else:
    print('Você não digitou o número 3.')
print('Os números pares digitados foram: ', end='')
for elementos in numeros:
    if elementos % 2 == 0:
        print(elementos, end= ' ')
