frase = str(input('Digite uma frase: ')).split(' ')
carai = ''.join(frase).lower()
print('a frase: {}'.format(frase))
print(carai)
lista = []
b = 0 #é bom melhorar isso aqui
for letra in range(0, len(carai)):
    lista.append(carai[b-1])
    b = b - 1
print('lista {}'.format(lista))
print(''.join(lista))
porra = ''.join(lista)
if carai == porra:
    print('A frase é a miséra de um palíndromo!')
else:
    print('É só uma frase normal.')
# ELE FAZ SEM FOR, USANDO FATIAMENTO: lista = carai[::-1] ele vai do início até o fim, só q o -1 é de trás pra frente
