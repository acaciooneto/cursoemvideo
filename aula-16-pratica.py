lanche = 'Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita' #da pra ser sem () tbm, a partirdo python 3.5
'''print(lanche)
print(lanche[1])
print(lanche[3])
print(lanche[-4])
print(lanche[1:3])
print(lanche[2:])
print(lanche[:2])
print(lanche[-3:])
print(lanche[-2::-1])'''
#for posição, comidas in enumerate(lanche): #serve pra ter o número sem usar o range
#    print(f'Eu vou comer {comidas} na posição {posição}')
#for contagem in range(0, len(lanche)):
#   print(f'Eu vou comer {lanche[contagem]} na posição {contagem}') #os dois jeitos respondem iguais
print('comi pra caralho')
print(sorted(lanche)) #põe a tupla em ordem, criando uma lista 
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b #concatenou, não somou (se for b + a o resultado vai ser diferente)
print(c)
print(sorted(c))
print(c.count(5)) #quantas vezes aparece esse elemento
print(c.index(8)) #mostra em qual posição está o número 8

pessoa = ('Acácio', 23, 'M', 84, 1.92)
print(pessoa) #tuplas pegam números e strings
#del(pessoa) assim apaga toda a tupla, não se pode deletar 1 iten, só ela toda.
print(pessoa[0::2])
