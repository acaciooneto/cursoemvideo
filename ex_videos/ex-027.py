# MINHA RESOLUÇÃO
#nome = str(input('Digite seu nome completo: ')).strip().title()
#name = nome.split()
#print('Olá {}, vi aqui que o seu último nome é {}.'.format(name[0], name[-1]))

# RESOLUÇÃO DELE
n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome)-1]))
# ele usa o lenght com -1, pq o len não conta 0, então o -1 vai dar o ultimo elemento da lista
