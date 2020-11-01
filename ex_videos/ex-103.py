def ficha(jogador, gols):
    return print(f'O jogador {jogador} fez {gols} gols no campeonato.')

nome = str(input('Informe o nome do jogador: ')).strip()
golos = str(input('Agora quantos gols ele fez: '))
if nome == '':
    nome = '<desconhecido>'
if golos.isnumeric():
    golos = int(golos)
else:
    golos = 0
ficha(nome, golos)
