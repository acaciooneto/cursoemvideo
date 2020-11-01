numero = int(input('Digite um número inteiro: '))
lista = [] # foi desnecessária
if numero == 1:
    print('Esse NÃO é um número primo.')
else:
    for espaço in range(2, numero):
        lista.append(espaço)
        if numero % espaço == 0:
            print('Esse NÃO é um número primo.')
            exit()
    print('Esse É um número primo!')
#print(lista)
#print(espaço)
'''if espaço % numero != 0:
    print('carai')'''

'''lista = [0]
a = lista[0]
for num in range(2, numero):
    lista.append(num)
    b = lista[0+1]
    print(b)
    #if 

print(lista)
print(b)'''
'''for divisor in range(2, numero):
    quociente = numero / divisor
    resto = numero % divisor
    if numero / 1 == numero and numero / numero == 1:
        primo = True
    else:
        primo = False
print('{} é um numero primo? {}'.format(numero, primo))'''
