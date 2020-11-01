maiores = homens = mulheres_menor = 0
while True:
    sexo = ' '
    continuar = ' '
    idade = int(input('Digite a idade da pessoa: '))
    while sexo not in 'MF':
        sexo = str(input('Digite o sexo dessa pessoa [M/F]: ')).strip().upper()[0]
    if idade >= 18:
        maiores += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres_menor += 1
    while continuar not in 'SN':
        continuar = str(input('Você deseja continuar? [S/N]: ')).strip().upper()[0]
    if continuar == 'S':
        print('Ok, vamor lá...')
    else:
        break
print(f'O número de pessoas maior de idade foi {maiores}.')
print(f'O número de homens foi {homens}.')
print(f'o número de mulheres com menos de 20 anos foi {mulheres_menor}.')
