numeros = []
while True:
    num = int(input('Digite um número: '))
    if num in numeros:
        print('O valor não foi adicionado porque já está na lista.')
    else:
        numeros.append(num)
        print('Valor adicionado corretamente.')
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Você deseja continuar? [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break
numeros.sort()
print(f'Você criou a lista: {numeros}')
