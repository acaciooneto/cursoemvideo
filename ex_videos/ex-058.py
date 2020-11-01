from random import randint
computador = randint(1, 20)
acertou = False
tentativas = 0
while acertou is not True:
    jogador = int(input('Digite o número que estou pensando: '))
    tentativas += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais...')
        else:
            print('Menos...')
print('Você acertou com {} tentativas.'.format(tentativas))
