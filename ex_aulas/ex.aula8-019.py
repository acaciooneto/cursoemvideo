import random
a1 = input('Digite o primero aluno: ')
a2 = input('Digite o segundo aluno: ')
a3 = input('Digite o terceiro aluno: ')
a4 = input('Digite o quarto aluno: ')
list = [a1, a2, a3, a4]
print('O aluno sorteado foi: {}'.format(random.choice(list)))
