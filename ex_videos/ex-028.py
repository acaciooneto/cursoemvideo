from random import randint
from time import sleep
computador = randint(0, 5) #faz o computador "pensar"
print('-=-'*20)
print('Vou pensar em um número entre 0 e 5, tente advinhar...')
print('-=-'*20)
jogador = int(input('Diz aí qual número você acha que eu pensei: '))
print('Processando.......')
sleep(2)

if jogador == computador:
    print('Caramba! como você acertou?? eu realmente pensei {}.'.format(computador))
else:
    print('HAHA! eu sabia que você ia errar, eu pensei {} e não {}.'.format(computador, jogador))
