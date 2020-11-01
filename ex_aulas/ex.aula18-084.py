pessoas = []
dado = []
menor = maior = contagem = 0
while True:
    continuar = ' '    
    dado.append(str(input('Digite o nome: ')))
    dado.append(float(input('Digite o peso: ')))
    print(dado)
    pessoas.append(dado[:])    
    if contagem == 0: # if len(pessoas) == 0: maior = menor = dado[1]
        menor = maior = dado[1]
    else:
        if dado[1] > maior:
            maior = dado[1]
        if dado[1] < menor:
            menor = dado[1]
    dado.clear()
    contagem += 1
    while continuar not in 'SN':
        continuar = str(input('Você desseja continuar? [S/N]: ')).upper().strip()[0]
    if continuar == 'N':
        break
print(f'{len(pessoas)} pessoas compõem a lista.')
print(f'O maior peso foi de {maior}Kg, carregado por ', end='')
for pessoa in pessoas:
    for peso in pessoa: # não precisava desse
        if peso == maior: # aqui botava pessoa[1] == maior q ele identificava o peso
            print(f'{pessoa[0].title()} / ', end='')
print(f'\nO menor peso foi de {menor}Kg, carregado por ', end='')
for pessoa in pessoas:
    for peso in pessoa:
        if peso == menor:
            print(f'{pessoa[0].title()} / ', end='')
