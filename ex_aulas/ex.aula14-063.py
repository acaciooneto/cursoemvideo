print('Quer ver a sequência de fibonacci?')
limite = int(input('Digite um número limite: '))
vezes = 2
#sequencia = 0
primeiro = 0
segundo = 1
print('{} -> {} ->'.format(primeiro, segundo), end= ' ')
while vezes < limite:
    vezes += 1
    sequencia = primeiro + segundo
    primeiro = segundo
    segundo = sequencia
    print('{} ->'.format(sequencia), end=' ')
print('Fim!')
