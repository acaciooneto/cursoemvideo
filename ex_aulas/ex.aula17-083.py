carai = []
equação = str(input('Digite a equação: '))
for letra in equação:
    carai.append(letra)
#print(carai)
aberto = carai.count('(')
fechado = carai.count(')')
#somado = aberto + fechado
if aberto == fechado: #somado % 2 == 0: erro de lógica, pq 4'(' e 2')' funfava, só q errado.
    print('A equação é válida.')
else:
    print('A equação está errada.')
