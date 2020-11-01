numeros = []
pares = []
impares = []
numeros.append(pares)
numeros.append(impares)
for num in range(0, 7):
    entrada = int(input('Digite um valor: '))
    if entrada % 2 == 0:
        pares.append(entrada)
    else:
        impares.append(entrada)
print(numeros)
pares.sort()
impares.sort()
print(f'Os valores pares digitados foram: {pares}')
print(f'Os valores ímpares digitados foram: {impares}')
