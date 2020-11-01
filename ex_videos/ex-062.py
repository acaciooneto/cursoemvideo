primeiro_termo = int(input('Digite o primeiro termo dessa PA: '))
razão = int(input('Digite a razão dessa PA: '))
an = primeiro_termo - razão
contador = 0
mais_termos = 1
total_termos = 10
while mais_termos != 0:
    while contador < total_termos:
        contador += 1
        an += razão
        print('{} -> '.format(an), end= '')
    mais_termos = int(input('\nQuantos termos a mais você quer ver? '))
    total_termos += mais_termos
print('O último foi o {}º, que foi {}.'.format(total_termos, an))
