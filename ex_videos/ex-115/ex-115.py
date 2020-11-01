from lib.interface import *
from lib.arquivo import *


arq = 'cursoemvideo.txt'

if not arquivoexiste(arq):
    criararquivo(arq)

#cabeçalho('SISTEMA ARQUIVO v1.0')
while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if resposta == 1: # Listar conteúdo do arquivo
        lerarquivo(arq)
    elif resposta == 2:
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: ')).title()
        idade = leiaint('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho('Saindo do sistema... Valeu!')
        break
    else:
        print(f'{cor(1)}ERRO! Digite uma opção válida!{cor(0)}')
