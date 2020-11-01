numeros = []
while True:
    continuar = ' '
    num = int(input('Digite um número: '))
    if num in numeros:
        print('Esse número não foi adicionado porque já está na lista.')
    else:
        numeros.append(num)
        print('Número adicionado com sucesso.')
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break
print(numeros)
numeros.sort()
print(numeros)
