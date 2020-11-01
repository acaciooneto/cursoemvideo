jogadores = []
contagem = 0
while True: 
    continuar = ' '
    contagem += 1
    aproveitamento = {}
    gols = []
    aproveitamento['nome'] = str(input(f'Digite o nome do {contagem}º jogador: ')).title()
    aproveitamento['partidas'] = int(input(f'Quantas partidas {aproveitamento["nome"]} jogou? '))
    for partida in range(0, aproveitamento['partidas']):
        gols.append(int(input(f'Diga quantos gol ele marcou na {partida+1}ª partida: ')))
    aproveitamento['gols'] = gols
    aproveitamento['total'] = sum(gols)
    aproveitamento['mediapp'] = sum(gols)/aproveitamento['partidas']
    while continuar not in 'SN':
        continuar = str(input('Você deseja adicionar mais alguém? [S/N]: ')).strip().upper()[0]
    jogadores.append(aproveitamento)
    print('-='*31)
    if continuar == 'N':
        break
print(f'Cod. {"Nome":<20} {"Gols":<30} {"Total":>5} ')
for indice, jogador in enumerate(jogadores):
    print(f"{indice:>4} {jogador['nome']:<20} {str(jogador['gols']):<30} {jogador['total']:<5} ")
while True:
    dados = int(input('Digite o código do jogador para análise detalhada [666 p/ parar]: '))
    if dados == 666:
        break
    if dados < 0 or dados > len(jogadores)-1:
        print('Código inválido, tente de novo.')
    else:
        print(f'-- Levantamento do jogador {jogadores[dados]["nome"]} --')
        print('- Assim foi a temporada para ele -')
        for num, jogo in enumerate(jogadores[dados]['gols']): 
            print(f'No {num+1}º jogo ele fez {jogo} gols.')
        print(f'- Ele teve uma média de {jogadores[dados]["mediapp"]:.1f} gols por partida -')
print('Programa encerrado.')
