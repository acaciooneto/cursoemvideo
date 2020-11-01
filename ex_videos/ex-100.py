from random import randint
numeros = []
pedida = int(input('Quantos números você quer sortear? '))
def sorteia(x):
    for sorteado in range(0, pedida):
        numeros.append(randint(0, 10))
    print(f'Os {x} números sorteador foram: {numeros}')
def somapar(lista):
    soma = 0
    for elemento in numeros:
        if elemento % 2 == 0:
            soma += elemento
    print(f'A soma dos valores pares deu: {soma}.')
sorteia(pedida)
somapar(numeros)
