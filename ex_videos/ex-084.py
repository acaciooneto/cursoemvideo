pessoas = []
dado = []
maior = menor = 0
while True:
    continuar = ' '
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maior = menor = dado[1]
    else:
        if dado[1] > maior:
            maior = dado[1]
        if dado[1] < menor:
            menor = dado[1]
    pessoas.append(dado[:])
    dado.clear()
    while continuar not in 'SN':
        continuar = str(input('Você deseja inserir mais alguém? [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'Você inseriu os dados de {len(pessoas)} pessoas.')
print(f'O maior peso foi de {maior}Kg, e quem o tem é ',end='')
for elemento in pessoas:
    if elemento[1] == maior:
        print(f'[{elemento[0].title()}] ',end='')
print(f'\nO menor peso foi de {menor}Kg, e quem o tem é ',end='')
for elemento in pessoas:
    if elemento[1] == menor:
        print(f'[{elemento[0].title()}] ',end='')
