primeiro_termo = int(input('Digite o primeiro termo da PA: '))
razão = int(input('Digite a razão dessa PA: '))
mais_termos = -1
termo = 0
an = primeiro_termo - razão
while mais_termos != 0:
    while termo < 10:
        novo_termo = 0
        termo += 1
        an += razão
        print('{}º termo: {}'.format(termo, an))
    mais_termos = int(input('Você quer acrescestar mais termos? '))
    novo_termo = mais_termos
    while novo_termo != 0:
        termo += 1
        novo_termo = novo_termo - 1
        an += razão
        print('{}º termo: {}'.format(termo, an))
print('O {}º e último termo dessa PA foi {}.'.format(termo, an))
