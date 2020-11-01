def cor(num): 
    c = ('\033[m',      #0 sem cores
'\033[0;31m',       #1 vermelho
'\033[0;32m',       #2 verde
'\033[0;33m',       #3 amarelo
'\033[0;34m',       #4 ciano
'\033[0;35m',       #5 roxo
'\033[0;36m')       #6 azul escuro
    return c[num]
def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except KeyboardInterrupt:
            print('\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        except:
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
        else:
            return n

def linha(tamanho=50):
    print('-' * tamanho)


def cabeçalho(txt):
    linha()
    print(txt.center(50))
    linha()


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    for indice, elemento in enumerate(lista):
        print(f'{cor(3)}{indice+1} - {cor(6)}{elemento}{cor(0)}')
    linha()
    opção = leiaint(f'{cor(2)}Sua opção: {cor(0)}')
    return opção
