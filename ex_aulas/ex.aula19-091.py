from random import randint
from time import sleep
from operator import itemgetter
dados = {'Jogador 1': randint(1,6),
'Jogador 2': randint(1,6),
'Jogador 3': randint(1,6),
'Jogador 4': randint(1,6)}
for key, values in dados.items():
    print(f'O {key} tirou {values}.')
    sleep(1)
print('-='*22)
print(f"{'-- O ranking dos jogadores ficou --':^44}")
ranking = []
ranking = sorted(dados.items(), key=itemgetter(1), reverse=True)
for indice, valor in enumerate(ranking):
    print(f'{f"Em {indice+1}º lugar ficou o {valor[0]} que tirou {valor[1]}.":^44}')
