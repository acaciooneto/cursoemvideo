zero = []
um = []
dois = []
pares = []
terceira = []
for n in range(0, 3):
    valor = int(input(f'Digite o valor para [0, {n}]: '))
    zero.append(valor)
    if n == 2:
        terceira.append(valor)
    if valor % 2 == 0:
        pares.append(valor)
for n in range(0, 3):
    valor = int(input(f'Digite o valor para [1, {n}]: '))
    um.append(valor)
    if n == 2:
        terceira.append(valor)
    if valor % 2 == 0:
        pares.append(valor)
for n in range(0, 3):
    valor = int(input(f'Digite o valor para [2, {n}]: '))
    dois.append(valor)
    if n == 2:
        terceira.append(valor)
    if valor % 2 == 0:
        pares.append(valor)
print(f'[ {zero[0]} ] [ {zero[1]} ] [ {zero[2]} ]')
print(f'[ {um[0]} ] [ {um[1]} ] [ {um[2]} ]')
print(f'[ {dois[0]} ] [ {dois[1]} ] [ {dois[2]} ]')
print(f'A soma de todos os valores pares foi {sum(pares)}')
print(f'A soma dos valores da terceira coluna foi {sum(terceira)}')
print(f'O maior valor da segunda linha foi {max(um)}')
