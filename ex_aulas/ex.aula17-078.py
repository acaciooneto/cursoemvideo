numeros = []
contagem = 0
for entrada in range(0, 5):
    numeros.append(int(input(f'Digite o número da posição {contagem}: ')))
    contagem += 1
maior = max(numeros)
menor = min(numeros)
print(numeros)
print(f'O maior valor inserido foi {maior}, nas posições {numeros.index(maior)}', end='')
if numeros.count(maior) > 1: #gambiarra grande
    menor_index = numeros.index(maior) # era for com enumerate
    for repetições in range(1, numeros.count(maior)): # for indice, valor in enumerate(numeros)
        maior_index = numeros.index(maior, menor_index+1) #if valor == maior:
        print(f' / {maior_index}', end='')                  #print(indice)
        menor_index = maior_index
print(f'\nO menor valor inserifo foi {menor}, na posição {numeros.index(menor)}', end='')
if numeros.count(menor) > 1:
    index_menor = numeros.index(menor)
    for repetitions in range(1, numeros.count(menor)):
        index_maior = numeros.index(menor, index_menor+1)
        print(f' / {index_maior}', end='')
        index_menor = index_maior
