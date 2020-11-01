maior = 0
menor = 10000 # gambiarra, bota = 0 e no for abre um if se for o 1º pra igualar as duas variaveis com o peso
for pessoa in range(1, 6):
    peso = float(input('Digite o peso da {}ª pessoa: '.format(pessoa)))
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print('O maior foi {}, e o menor foi {}.'.format(maior, menor))
