from random import randint
from time import sleep
mega = []
jogos = int(input('Quantos jogos você quer fazer? '))
for games in range(0, jogos):
    while not len(mega) == 6:
        jogada = randint(1, 60)
        if jogada not in mega:
            mega.append(jogada)
    mega.sort()
    print(f'Jogo {games+1}: {mega}')
    sleep(0.5)
    mega.clear()
print(f'{"-="*5} BOA SORTE FIO {"-="*5}')
