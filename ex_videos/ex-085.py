numeros = [[], []]
for pedida in range(1, 8):
    valor = int(input(f'Digite o {pedida}º valor: '))
    if valor % 2 == 0:
        numeros[0].append(valor)
    else:
        numeros[1].append(valor)
numeros[0].sort()
numeros[1].sort()
print(f'Os valores pares foram: {numeros[0]}')
print(f'Os valores ímpares foram: {numeros[1]}')
