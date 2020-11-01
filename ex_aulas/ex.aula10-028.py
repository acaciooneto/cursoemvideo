# ele meteu um from random import randint(0, 5) q randomiza um número inteiro dentro do q eu selecionar
import random
lista = [0, 1, 2, 3, 4, 5]
pensou = random.choice(lista)
print('Eu pensei em um número aqui, será que você consegue descobrir?')
chute = int(input('Vamos lá! está entre 0 e 5, tente advinhar o número que eu pensei: '))
if chute == pensou:
    print('Carai cuzão, acertou, eu pensei no {}.'.format(pensou))
else:
    print('Eu sabia que você ia errar. Eu pensei no {}, não no {}.'.format(pensou, chute))
