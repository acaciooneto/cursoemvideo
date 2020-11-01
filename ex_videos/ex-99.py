def maior(*num):
    maior = 0
    print('=~'*24)
    print('Você informou os valores: ',end='')
    for indice, valor in enumerate(num):
        if indice == 0 or valor > maior:
            maior = valor
        print(f'{valor} ',end='')
    print(f'\nAo todo são {len(num)} valores, e o maior deles foi {maior}')

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
maior(-2, -7, -10, -1)
