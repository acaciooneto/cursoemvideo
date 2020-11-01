maiores =  mulheres_menor = homens = 0
while True:
    continuar = ' '
    sexo = ' '
    idade = int(input('Digite a idade dessa pessoa: '))
    while sexo not in 'MF':
        sexo = str(input('Digite o sexo da pessoa [M/F]: ')).strip().upper()[0]
    if idade >= 18:
        maiores += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres_menor += 1
    while continuar not in 'SN':
        continuar = str(input('Você deseja continuar? [S/N]: ')).strip().upper()[0]
    if continuar == 'S':
        print('Vamos lá...')
    if continuar == 'N':
        break
print(f'{maiores} pessoas tem mais de 18 anos.')
print(f'{homens} homens foram cadastrados.')
print(f'{mulheres_menor} mulheres têm menos de 20 anos.')
