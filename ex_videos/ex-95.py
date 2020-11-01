artilheiros = []
while True:
    continuar = ' '
    jogador = {}
    gols = []
    jogador["nome"] = str(input('Informe o nome do jogador: ')).title()
    jogador["partidas"] = int(input('Quantas partidas ele jogou? '))
    for jogo in range(0, jogador['partidas']):
        gols.append(int(input(f'Quantos gols ele fes na {jogo+1}ª partida? ')))
    jogador["gols"] = gols
    jogador["total de gols"] = sum(gols)
    jogador['mediapj'] = sum(gols)/jogador['partidas']
    print('-='*40)
    artilheiros.append(jogador)
    while continuar not in 'SN':
        continuar = str(input('Deseja adicionar mais algum jogador? [S/N]: ')).upper()[0]
    if continuar == 'N':
        break
print(f"{'Cod.'} {'Nome':<15} {'Gols':<30} {'Total de Gols':<15} {'Partidas'}")
for indice, player in enumerate(artilheiros):
    print(f"{indice:>4} {player['nome']:<15} {str(player['gols']):<35} {player['total de gols']:<15} {player['partidas']}")
print('-='*40)
while True:
    dado = int(input(f'Digite o código do artilheiro para ver análise detalhada [666 encerra]: '))
    if dado == 666:
        break
    if dado < 0 or dado > len(artilheiros)-1:
        print('Não temos jogador com esse código, tente de novo.')
    else:
        print(f'-- Levantamento da temporada de {artilheiros[dado]["nome"]} --')
        for indice, golos in enumerate(artilheiros[dado]['gols']):
            print(f"No {indice+1}º jogo ele fez {golos} gols.")
        print(f"- {artilheiros[dado]['nome']} teve uma média de {artilheiros[dado]['mediapj']:.1f} gols por partida -")
print('-='*40)
print(f'Programa encerrado.')
