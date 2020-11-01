teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:]) #com os : ele copia, mas não faz a ligação
teste[0] = 'Maria' #se eu mudar a primeira estrutura, a segunda tb é modificada
teste[1] = 22
galera.append(teste) #aí dando append de novo, vai duplicar a modificação
print(galera)
minaa = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(minaa)
print(minaa[0])
print(minaa[2][0])
print(minaa[2][1])
print('Pegando itens separadamente')
for numero, pessoa in enumerate(minaa):
    print(f'{numero+1}ª pessoa: {pessoa[0]}')

everyone = []
dado = []
maiores = menores = 0
for pessoa in range(1, 4):
    dado.append(str(input('Digite o nome: ')))
    dado.append(int(input('Digite a idade: ')))
    everyone.append(dado[:]) #se esquecer os : ele vai igualar, ai o clear em dados limparia o everyone tb
    dado.clear()
print(everyone)
for pessoa in everyone:
    if pessoa[1] >= 21:
        print(f'{pessoa[0]} é maior de idade.')
        maiores += 1
    else:
        print(f'{pessoa[0]} é menor de idade.')
        menores += 1
print(f'Temos {maiores} maiores, e {menores} menores de idade.')
