c = ('\033[m',      #0 sem cores
'\033[0;31m',       #1 vermelho
'\033[0;32m',       #2 verde
'\033[0;33m',       #3 amarelo
'\033[0;34m',       #4 azul
'\033[0;35m')       #5 roxo

def ajuda(entrada):
    titulo(f'Acessando o manual do comando \'{entrada}\' ', 3)
    print(c[1], end='')
    help(entrada)
    print(c[0], end='')

def titulo(msg, cor=0):
    tamanho = len(msg) + 4
    print(c[cor],end='')
    print('~'*tamanho)
    print(f'  {msg}')
    print('~'*tamanho)
    print(c[0],end='')

while True:
    titulo('Sistema de ajuda PyHELP', 2)
    comando = ''
    comando = str(input(f'{c[3]}Função ou biblioteca: ')).lower()
    if comando == 'fim':
        titulo('Encerrando...', 1)
        break
    ajuda(comando)
