principal = []
pares = []
impares = []
while True:
    continuar = ' '
    principal.append(int(input('Digite um número: ')))
    while continuar not in 'SN':
        continuar = str(input('Você deseja continuar? [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break
for elemento in principal:
    if elemento % 2 == 0:
        pares.append(elemento)
    else:
        impares.append(elemento)
print(f'A lista principal é: {principal}')
print(f'A lista de pares é: {pares}')
print(f'A lista de ímpares é: {impares}')
