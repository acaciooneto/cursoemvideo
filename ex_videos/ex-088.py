from random import randint, sample
from time import sleep

for n in range(int(input('Quantos jogos você vai querer? '))): #nos coments do yt
    print(f'{n+1}º jogo: {sorted(sample(range(1, 61),6))}')
    sleep(.5)

mega = [] #minha solução
jogos = int(input('Quantos jogos você vai querer? '))
for game in range(1, jogos+1):
    while not len(mega) == 6:
        jogada = randint(1, 60)
        if jogada not in mega:
            mega.append(jogada)
    mega.sort()
    print(f'{game}º jogo: {mega}')
    sleep(0.5)
    mega.clear()
