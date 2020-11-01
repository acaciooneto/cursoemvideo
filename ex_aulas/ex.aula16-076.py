lista = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.90, 
'Estojo', 25, 'Transferidor', 4.20, 'Compasso', 9.99, 
'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90, 
'Pren-Pren', 9.99)
print('-='*21)
print('{:^42}'.format('LISTAGEM DE PREÇOS'))
print('-='*21)
for contador in range(0, 20, 2):
    print(f'{lista[contador]:.<30} R${lista[contador+1]:>8.2f}')
print('-='*21)
