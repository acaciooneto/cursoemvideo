from time import sleep

escolha = 0
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))

while escolha != 5:
    escolha = int(input('''\n[1] Somar
[2] Multiplicar
[3] Ver qual é maior
[4] Novos números
[5] Sair do programa
-- qual opção você vai querer? '''))

    if escolha == 1:
        print('{} + {} = {}'.format(n1, n2, n1 + n2))
    elif escolha == 2:
        print('{} x {} = {}'.format(n1, n2, n1 * n2))
    elif escolha == 3:
        if n1 > n2:
            print('O 1º: {} é maior que o 2º: {}'.format(n1, n2))
        elif n2 > n1:
            print('O 2º: {} é maior que o 1º: {}'.format(n2, n1))
        else:
            print('Os valores são iguais.')
    elif escolha == 4:
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
    elif escolha == 5:
        print('Escerrando...')
        sleep(1)
    else:
        print('Opção, inválida, tente novamente.')

print('Valeu malucão _\|/_')
