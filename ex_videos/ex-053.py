frase = str(input('Digite uma frase: ')).split( )
frase_junta = ''.join(frase).lower()
#inverso = ''
#for letra in range(len(frase_junta) - 1, -1, -1): #lembrar de encaixar o tamanho da frase dentro a string de resposta
#    inverso += frase_junta[letra]
inverso = frase_junta[::-1]
if frase_junta == inverso:
    print('Aqui nós temos um palíndromo.')
else:
    print('Essa frase não é um palíndromo.')
