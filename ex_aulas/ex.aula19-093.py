aproveitamento = {}
gols = []
aproveitamento['nome'] = str(input('Digite o nome do jogador: ')).title()
aproveitamento['partidas'] = int(input('Quantas partidas ele jogou: '))
for matches in range(0, aproveitamento['partidas']):
    gols.append(int(input(f'Digite quantos gols ele fez na {matches+1}ª partida: ')))
aproveitamento['gols'] = gols
aproveitamento['score'] = sum(gols)
print(aproveitamento)
print('-='*20)
for chaves, valores in aproveitamento.items():
    print(f'{chaves.title():<10} -- {valores} ')
for partida in range(0, aproveitamento['partidas']):
    print(f'Na {partida+1}ª partida ele fez {gols[partida]} gols. ')
print(f'Encerrando o campeonato com {aproveitamento["score"]} ',end='') 
print(f'gols feitos, um aproveitamento de {sum(gols)/aproveitamento["partidas"]:.1f} gols por partida.')
