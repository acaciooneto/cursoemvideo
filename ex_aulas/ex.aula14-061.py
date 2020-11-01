primeiro_termo = int(input('Digite o primeiro termo da PA: '))
razão = int(input('Digite a razão dessa PA: '))
termo = 0
an = primeiro_termo - razão
while termo != 10:
    termo += 1
    an += razão
    print('{}º termo = {}'.format(termo, an))
