numeros = []
while True:
    numeros.append(int(input('Digite um valor: ')))
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Você quer continua? [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'Foram digitados {len(numeros)} elementos.')
numeros.sort(reverse=True)
print(f'Decrescente: {numeros}')
if 5 in numeros:
    print('O número 5 foi inserido na lista.')
else:
    print('O número 5 NÃO foi inserido na lista.')
