soma = 0
contagem = 0
for num in range(1, 7):
    numero = int(input('Digite o {}º número: '.format(num)))
    if numero % 2 == 0:
        soma += numero
        contagem += 1
print('Você disse {} números PARES, e a soma deles deu {}.'.format(contagem, soma))
