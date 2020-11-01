import random
print('Hoje é dia de apresentação, vamos saber a ordem.')
a1 = input('Diga um nome: ')
a2 = input('Diga outro nome: ')
a3 = input('Diga outro nome: ')
a4 = input('Diga outro nome: ')
lista = [a1, a2, a3, a4]
random.shuffle(lista)
print('A ordem de apresentação será:')
print(lista)
