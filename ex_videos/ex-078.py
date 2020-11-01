conjunto = []
for numeros in range(0, 5):
    conjunto.append(int(input('Digite um número: ')))
maior = max(conjunto)
menor = min(conjunto)
print(f'O maior número adicionado foi {maior} nas posições ', end='')
for indice, valor in enumerate(conjunto):
    if valor == maior:
        print(f'{indice} - ',end='')
print(f'\nO menor número adicionado foi {menor} nas posições ', end='')
for indice, valor in enumerate(conjunto):
    if valor == menor:
        print(f'{indice} - ', end='')
