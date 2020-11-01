numeros = [] # ele faz as 3 matrizes dentro de uma só lista, com três 0 em cada uma
zero = []
um = []
dois = []
numeros.append(zero)
numeros.append(um)
numeros.append(dois)
for n in range(0, 3):
    zero.append(int(input(f'Digite o valor para [0, {n}]: ')))
for n in range(0, 3):
    um.append(int(input(f'Digite o valor para [1, {n}]: ')))
for n in range(0, 3):
    dois.append(int(input(f'Digite o vlaor para [2, {n}]: ')))
print(numeros)
print(f'[ {zero[0]} ] [ {zero[1]} ] [ {zero[2]} ]')
print(f'[ {um[0]} ] [ {um[1]} ] [ {um[2]} ]')
print(f'[ {dois[0]} ] [ {dois[1]} ] [ {dois[2]} ] ')
