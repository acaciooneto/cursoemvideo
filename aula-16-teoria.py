# VARIÁVEIS COMPOSTAS (TUPLAS)
# EXISTEM 3 VA. COMPOSTAS: TUPLAS, LISTAS E DICIONÁRIOS
lanche = ('hamburguer', 'suco', 'pizza', 'pudim')
print(lanche)
print(lanche[2])
print(lanche[0:2]) #ele não mostra a pizza pq é faiamento, então o ultimo valor é esquecido, p/ ver pizza = 3
print(lanche[1:])
print(lanche[-1])
print(len(lanche))
for comidas in lanche: #além do range, também dá pra usar o for em coleções!!
    print(f'{comidas} -> ',end= '')
print('Itadakimaaasu!')
# --- AS TUPLAS SÃO IMUTÁVEIS!! ---
# ^^^^ lembrar sempre disso ^^^^
