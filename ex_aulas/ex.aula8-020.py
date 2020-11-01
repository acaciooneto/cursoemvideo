from random import shuffle
a1 = input('Digite o nome do alunx: ')
a2 = input('Digite o nome do alunx: ')
a3 = input('Digite o nome do alunx: ')
a4 = input('Digite o nome do alunx: ')
list = [a1, a2, a3, a4]
shuffle(list)
print('A ordem de apresentação será: {}'.format(list))
