from random import randint
computador = randint(1, 10)
#print(computador)
jogador = -1
tentativas = 0
while jogador != computador:
    jogador = int(input('Digite o valor que eu pensei: '))
    tentativas += 1
    if jogador != computador:
        print('Você errou, tente novamente.')
    if 1 < jogador > 10:
        print('Você tentou uma opção inválida, tente novamente.')
if tentativas == 1:
    print('Parabés, você acertou de primeira!')
else:
    print('Você acertou, e levou {} tentativas para descobrir.'.format(tentativas))
