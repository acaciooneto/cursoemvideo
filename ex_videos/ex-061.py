primeiro = int(input('Digite o primeiro termo da PA: '))
razão = int(input('Digite a razão dessa PA: '))
termo = primeiro - razão
contagem = 1
while contagem <= 10:
    termo += razão
    contagem += 1
    print('{} -> '.format(termo), end='')
print('Fim!')
