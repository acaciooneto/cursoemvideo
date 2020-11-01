import random
print('Olá terráqueo, vamor jogar um jogo?')
player = str(input('É uma partida de jokenpô!\nEscolha sua jogada: ')).strip().title()
lista = ['Pedra', 'Papel', 'Tesoura']
npc = random.choice(lista)
if player in lista:
    if player == npc:
        print('Nós dois jogamos {}, então deu EMPATE.'.format(npc))
    elif player == 'Pedra' and npc == 'Tesoura':
        print('{} quebra a {}, então VOCÊ GANHOU essa.'.format(player, npc))
    elif player == 'Tesoura' and npc == 'Pedra':
        print('{} é quebrada pela {}, então EU GANHEI essa.'.format(player, npc))
    elif player == 'Papel' and npc == 'Pedra':
        print('{} cobre a {}, então VOCÊ GANHOU essa.'.format(player, npc))
    elif player == 'Pedra' and npc == 'Papel':
        print('{} e coberta pelo {}, então EU GANHEI essa.'.format(player, npc))
    elif player == 'Tesoura' and npc == 'Papel':
        print('{} corta {}, então VOCÊ GANHOU essa.'.format(player, npc))
    elif player == 'Papel' and npc == 'Tesoura':
        print('{} é cortado pela {}, então EU GANHEI essa.'.format(player, npc))
else:
    print('{} não é uma opção, jogue direito.'.format(player))
    