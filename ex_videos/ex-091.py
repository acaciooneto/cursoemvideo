from random import randint
from time import sleep
from operator import itemgetter
jogadas = {'Jogador 1': randint(1, 6),
'Jogador 2': randint(1,6),
'Jogador 3': randint(1,6),
'Jogador 4': randint(1,6)}
for chave, valor in jogadas.items():
    print(f'O {chave} tirou {valor}.')
    sleep(1)
ranking = []
ranking = sorted(jogadas.items(), key=itemgetter(1), reverse=True)
for indice, valor in enumerate(ranking):
    print(f'Em {indice+1}º lugar ficou o {valor[0]} que tirou {valor[1]}.')
