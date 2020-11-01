from random import randint
from time import sleep
opçoes = ['Pedra', 'Papel', 'Tesoura']
computador = randint(0, 2)
npc = opçoes[computador]
print(npc)
jogador = int(input('''Essas são as opções:
1 = Pedra
2 = Papel
3 = Tesoura
Qual será a sua jogada? '''))
if jogador not in (0, 1, 2):
    print('Opção inválida, jogue direito!')
    exit()
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
print('-='*10)
print('{: ^20}'.format('Eu joguei {}'.format(npc)))
print('{: ^20}'.format('Você jogou {}'.format(opçoes[jogador])))
if jogador == computador:
    print('{: ^20}'.format('Deu EMPATE :/'))
if computador == 0:
    if jogador == 1:
        print('{: ^20}'.format('Você VENCEU.'))
    elif jogador == 2:
        print('{: ^20}'.format('Eu VENCI!'))
elif computador == 1:
    if jogador == 0:
        print('{: ^20}'.format('Eu VENCI!'))
    elif jogador == 2:
        print('{: ^20}'.format('Você VENCEU.'))
elif computador == 2:
    if jogador == 0:
        print('{: ^20}'.format('Você VENCEU.'))
    elif jogador == 1:
        print('{: ^20}'.format('Eu VENCI!'))
print('-='*10)
