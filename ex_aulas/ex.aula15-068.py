from random import randint
from time import sleep
contagem = 0
print('Olá Humano! Vamos jogar par ou ímpar.')
while True:
    npc = randint(0, 10)
    player = int(input('Prepare sua mão: '))
    escolha = str(input('Você vai querer Par ou Ímpar? [P/I]: ')).strip().upper()[0]
    if escolha not in 'PI' or player < 0 or player > 10:
        print('Opção inválida, xau.') #ele bota um while no P/I, melhor pq repete e não encerra
        exit()
    print('Arraaaastá!')
    soma = npc + player
    sleep(1)
    print(f'Eu joguei {npc} e você jogou {player}, o que dá {soma}.')
    print('-='*20)
    if escolha == 'P':
        if soma % 2 == 0:
            print('Deu par, você ganhou! vamos outra...')
        else:                    
            break
    else:
        if soma % 2 != 0:
            print('Deu ímpar, você ganhou! vamos outra...')
        else:                  
            break
    print('-='*20)
    contagem += 1
print('VOCÊ PERDEU! HAHAHA')
print(f'Fim de jogo! Você ganhou {contagem} vezes.')
