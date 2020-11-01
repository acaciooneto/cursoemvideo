import random
a1 = 'cara'
a2 = 'coroa'
list = [a1, a2]
choice = input('Vamos ao nosso jogo de cara ou coroa, o que você escolhe? ')
jogo = random.choice(list)
if choice == a1:
    print('Você escolheu cara e o resultado foi {}.'.format(jogo))
elif choice == a2:
    print('Você escolheu coroa e o resultado foi {}.'.format(jogo))
else:
    print('Você escolheu uma opção inválida.')
if jogo == choice:
    print('Parabéns, você ganhou.')
elif jogo != choice:
    print('Lamento, você perdeu.')
else:
    print('Escolha direito na próxima vez.')
    
# {}'.format(random.randint(a, b))
