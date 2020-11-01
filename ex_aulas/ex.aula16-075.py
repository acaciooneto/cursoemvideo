n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
n4 = int(input('Digite um úlimo número: '))
numeros = (n1, n2, n3, n4) # ele criou 4 int(input) dentro da tupla, então ela pergunta e armazena em si
print(f'Você digitou os valores {numeros}')
print(f'O número 9 foi digitado {numeros.count(9)} vezes.')
if numeros.count(3) == 0:
    print('Você não digitou o número 3.')
else:
    print(f'O número 3 apareceu primeiro na {numeros.index(3)+1}ª posição.')
print('Os números pares foram: ',end='')
for contador in range(0, 4): #podia ter feito contador in numeros
    if numeros[contador] % 2 == 0:
        print(f'{numeros[contador]} ',end='')
