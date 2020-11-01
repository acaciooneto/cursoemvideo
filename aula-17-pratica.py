num = [2, 5, 9, 1]
print(num)
num[2] = 3
num.append(7)
print(num)
num.sort(reverse=True)
num.insert(2, 0)
print(num)
print(f'Essa lista tem {len(num)} elementos.')
'''num.pop()        já vi q funciona
num.pop(2)'''
num[2] = 2
print(num)
num.remove(2) # assim elimina o primeiro valor na sequencia da lista
if 4 in num:
    num.remove(4)
else:
    print('Não achei o número 4 pq a lista tá assim:')
print(num)

valores = []
valores.append(5)
valores.append(9)
valores.append(4)
print('Os valores são ', end='')
for valor in valores:
    print(f'{valor}...', end=' ')
print('\nEnumerados agora')
for c, v, in enumerate(valores):
    print(f'Na posição {c} eu encontrei o valor {v}')
'''for novo in range(0, 5):
    valores.append(int(input('Digita um valor: ')))
print(valores)
for a, b, in enumerate(valores):
    print(f'Achei o {b} na posição {a}.')'''

q = [2, 3, 4, 7]
w = q #não é só recebe, elas estão igualadas
print(f'Lista Q = {q}')
print(f'Lista W = {w}')
w[2] = 8 #por essa ligação, se eu mudar uma a outra muda tbm
#w.append(int(input('Digite um valor pra entrar na lista: ')))
print(f'\nLista Q = {q}')
print(f'Lista W = {w}')
t = [2, 3, 4, 7]
y = t[:] #isso cria uma cópia, não uma ligação
print(f'\nLista T = {t}')
print(f'Lista Y = {y}')
y[2] = 9 #agora funciona em uma só, pq é uma cópia
print(f'\nLista T = {t}')
print(f'Lista Y = {y}')
