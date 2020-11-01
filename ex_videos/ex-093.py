jogador = {}
gols = []
jogador["nome"] = str(input('Informe o nome do jogador: ')).title()
jogador["partidas"] = int(input('Quantas partidas ele jogou? '))
for jogo in range(0, jogador['partidas']):
    gols.append(int(input(f'Quantos gols ele fes na {jogo+1}ª partida? ')))
jogador["gols"] = gols
jogador["total de gols"] = sum(gols)
print('-='*20)
for chave, valor in jogador.items():
    print(f'{chave.title():<15} -- {valor} ')
print('-='*20)
for indice, valor in enumerate(gols):
    print(f'Na {indice+1}ª partida ele fez {valor} gols.')
print('-='*20)
print(f'No fim do campeonato {jogador["nome"]} fez {sum(gols)} gols,',end=' ')
print(f'tendo um aproveitamento de {sum(gols)/jogador["partidas"]:.1f} gols por partida.')
