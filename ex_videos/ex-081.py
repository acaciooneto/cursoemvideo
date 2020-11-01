valores = []
while True:
    valores.append(int(input('Digite um número: ')))
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Você deseja continuar? [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'A lista está com {len(valores)} elementos.')
valores.sort(reverse=True)
print(f'Em ordem decrescente: {valores}')
if 5 in valores:
    print(f'O número 5 foi encontrado na posição {valores.index(5)} da lista.')
else:
    print('O número 5 não foi encontrado na lista.')
