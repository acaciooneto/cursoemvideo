from random import randint
numeros = []
pedida = int(input('Digite o valor de números sorteados: '))
def sorteia(x):
    for vezes in range(0, x):
        vezes += 1
        numeros.append(randint(0, 10))
    print(f'Os {x} números sorteados foram: {numeros}')
def somapar(lista):
    pares = 0
    for elemento in lista:
        if elemento % 2 == 0:
            pares += elemento
    print(f'A soma dos valores pares foi: {pares}')
sorteia(pedida)
somapar(numeros)
