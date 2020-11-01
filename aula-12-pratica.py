# ESTRUTURA CONDICIONAL ANINHADA
nome = str(input('Qual é seu nome: ')).strip().lower()
if nome == 'Gustavo':
    print('Fala Guanabara!')
elif nome == 'joão' or nome == 'josé' or nome == 'maria':
    print('Seu nome é bem popular por aqui.')
elif nome == 'acácio' or nome == 'acacio':
    print('Nossa, que nome lindo!')
elif nome in 'ana cláudia jéssica fernanda':
    print('Você tem um belo nome moça.')
elif nome == 'juliana':
    print('Desce uma caixa de cerveja que eu bebo!')
#else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}.'.format(nome.title()))
