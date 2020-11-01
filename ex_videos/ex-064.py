soma = contagem = 0
numero = int(input('Digite um número: '))
while numero != 999:
    soma += numero
    contagem += 1
    numero = int(input('Digite mais um número: '))
print('Você digitou {} números e a soma deles deu {}.'.format(contagem, soma))
