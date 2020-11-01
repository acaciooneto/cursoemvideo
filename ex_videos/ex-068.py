from random import randint
print('Olá Humano, vamos jogar um jogo?!')
contagem = 0
while True:
    npc = randint(1, 10)
    player = int(input('Pense na sua jogada: '))
    while player < 0 or player > 10:
        player = int(input('Você tem um limite de dedos, cumpra-o: '))
    escolha = str(input('Você vai querer Par ou Ímpar? {P/I]: ')).strip().upper()[0]
    while escolha not in 'PI':
        escolha = str(input('Você só pode escolher entre Par ou Ímpar, jogue direito por favor: ')).strip().upper()[0]
    resultado = npc + player
    print('-='*23)
    print(f'Eu joguei {npc} e você jogou {player}, o que dá -> {resultado} <-')
    print('-='*23)
    if resultado % 2 == 0:
        if escolha == 'P':
            print('Você ganhou, vamos outra...')
        else:
            break
    else:
        if escolha == 'I':
            print('Você ganhou, vamos outra...')
        else:
            break
    contagem += 1
print('VOCÊ PERDEU! HAHAHA')    
print(f'E ganhou {contagem} vezes antes disso.')
