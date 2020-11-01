numeros = []
for add in range(0, 5):
    num = int(input('Digite um número: '))
    if add == 0:# or num > numeros[-1] (para limpar o outro if)
        numeros.append(num)
        print('Foi adicionado ao final da lista.')
    for posição, elemento in enumerate(numeros):# ele fez while c/ pos=0+1 e len(lista)
        if num < elemento:
            numeros.insert(posição, num)
            print(f'Foi adicionado na posição {posição} da lista.')
            break
        if num > numeros[-1]:
            numeros.append(num)
            print('Foi adicionado ao final da lista.')
print(numeros)
