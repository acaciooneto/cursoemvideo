def pyhelp():
    while True:
        inicio = len('SISTEMA DE AJUDA PYHELP')+4
        print('~'*inicio)
        print('  SISTEMA DE AJUDA PYHELP')
        print('~'*inicio)
        comando = input('Função ou Biblioteca: ')
        if comando == 'fim':
            endi = len('  Até Logo!  ')
            print('~'*endi)
            print('  Até Logo!')
            print('~'*endi)
            break
        tamanho_meio = len(f"  Acessando o manual do comando '{comando}'  ")
        print('~'*tamanho_meio)
        print(f"  Acessando o manual do comando '{comando}'  ")
        print('~'*tamanho_meio)
        help(comando)

pyhelp()
