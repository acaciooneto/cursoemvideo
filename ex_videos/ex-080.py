numeros = []
for add in range(0, 5):
    num = int(input('Digite um número: '))
    if add == 0 or num > numeros[-1]:
        numeros.append(num)
        print(f'O número {num} foi adicionado ao final da lista.')
    for posição, valor in enumerate(numeros):
        if num < valor:
            numeros.insert(posição, num)
            print(f'O número {num} foi adicionado na posição {posição} da lista.')
            break
print(f'então a lista ficou desse jeito: {numeros}')
