import random
a1 = input('Diga o primeiro nome: ')
a2 = input('Diga o segundo nome: ')
a3 = input('Diga o terceiro nome: ')
a4 = input('Diga o quarto nome: ')
a5 = input('Diga o quinto nome: ')
list = [a1, a2, a3, a4, a5]
sort = random.choice(list)
print('{} foi escolhidx para apagar o quadro.'.format(sort))
