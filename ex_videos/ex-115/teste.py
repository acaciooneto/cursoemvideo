from lib.arquivo import *
from lib.interface import *
if not arquivoexiste('cotacao.txt'):
    criararquivo('cotacao.txt')
arq = 'cotacao.txt'
while True:
    cabeçalho('COTAÇÃO ATUAL DAS DROGAS')
    resposta = menu(['Ver a tabela', 'Adicionar algum iten', 'Encerrar compra'])
    if resposta == 1:
        lerarquivo(arq)
    elif resposta == 2:
        nome = str(input('Lombra nova: ')).title()
        ida = int(input('Tempo de lombra: '))
        cadastrar(arq, nome, ida)
    elif resposta == 3:
        cabeçalho(f'{cor(2)}Saindo {cor(3)}da loja... {cor(1)}boa lombra!{cor(0)}')
        break
    else:
        print('Opção inválida!')
