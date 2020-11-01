matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_pares = terceira_coluna = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite o valor para [{linha}, {coluna}]: '))
for linha in range (0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]',end='')
        if matriz[linha][coluna] % 2 == 0:
            soma_pares += matriz[linha][coluna]
        if coluna == 2:
            terceira_coluna += matriz[linha][coluna]
    print()    
print('=-'*20)
print(f'A soma dos números pares dessa matriz deu {soma_pares}.')
print(f'A soma dos elementos da terceira coluna da matriz deu {terceira_coluna}.')
print(f'o maior elemento da segunda linha foi {max(matriz[1])}')
