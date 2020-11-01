def ficha(jogador, gols):
    if gols == '' or gols.isalpha():
        gols = 0
    if jogador == '':
        jogador = '<desconhecido>'
    print(f'O jogador {jogador} fez {gols} gol(s) no campeonato.')

nome = str(input('Digite o nome do jogador: ')).title().strip()
goles = str(input('Quantos gols ele fez: '))
ficha(nome, goles)
