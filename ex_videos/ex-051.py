# an = a1 + (n - 1) * razão
primeiro = int(input('Digite o primeiro termoda PA: '))
razão = int(input('Digite a razão dessa PA: '))
décimo = primeiro + (10 - 1) * razão
for numero in range(primeiro, décimo + razão, razão):
    print('{}'.format(numero), end=' - ')
print('Acabou.')
