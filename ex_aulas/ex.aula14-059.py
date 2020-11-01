escolha = 0
while not escolha == 5:    
    n1 = int(input('Digite o primeiro valor: '))
    n2 = int(input('Digite o segundo valor: '))
    escolha = 0
    while escolha < 4: #O 4 ELE FEZ UM IF E BOTOU PRA LER AS VARIÁVEIS DE NOVO LÁ DENTRO :/
        escolha = int(input("""--- Agora escolha o comando que vou fazer ---
[1] Somar
[2] Multiplicar
[3] Ver qual é o maior
[4] Digitar novos números
[5] Sair do programa
Qual sua escolha? """))#ELE FEZ O COMANDO REPETIR OS MESMOS NÚMEROS, NÃO FICAR PEDINDO NOVOS SEMPRE    
        if escolha == 1:
            print('{} + {} = {}'.format(n1, n2, n1 + n2))
        if escolha == 2:
            print('{} x {} = {}'.format(n1, n2, n1 * n2))
        if escolha == 3:
            if n1 > n2:
                print('O 1º valor: {} é maior que o 2º: {}.'.format(n1, n2))
            elif n2 > n1:
                print('O 2º valor: {} é maior que o 1º: {}.'.format(n2, n1))
            else:
                print('Os valores são iguais.')
        if 1 < escolha > 5:
            print('Você digitou uma opção inválida, tente novamente.')           
print('Encerrando o programa\nTenha um bom dia.')
