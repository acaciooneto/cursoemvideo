# VARIÁVEIS COMPOSTAS (LISTAS)
lanche = ['hamburguer', 'suco', 'pizza', 'picole']
print(lanche)
lanche.append('cookie') # p/ adicionar no final
print(lanche)
lanche.insert(0,'cachorro quente') # p/ adicionar na posição tal
lanche.insert(3,'sushi')
print(lanche)
del lanche[3] # p/ deletar elemento tal na lista
lanche.pop(0) # sem o 0 elimina o último elemento, se declarar elimina o tal
lanche.remove('pizza') #esse remove pelo índice, não pela classificação da lista
if 'pizza' in lanche: #pra evitar o bug da linguagem, elimina só se tiver
    lanche.remove('pizza')
print(lanche)
sequência = list(range(4, 11))
print(sequência)
print(len(sequência))
sequência.sort(reverse=True)
print(sequência)
valores = [8, 2, 5, 4, 9, 3, 0]
print(valores)
print(sorted(valores))
print(valores.sort()) # ele não pega pq ta no print, pra pegar tem q ser como tá embaixo
valores.sort(reverse=True)
print(valores)
