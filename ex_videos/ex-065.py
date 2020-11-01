maior = menor = soma = contagem = 0
resposta = 'S'
while resposta == 'S':
    numero = int(input('Digite um número: '))
    contagem+= 1
    soma += numero
    if contagem == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    resposta = str(input('Você deseja continuar? [S/N]: ')).upper().strip()[0]
print('O maior número digitado foi {}, e o menor foi {}.'.format(maior, menor))
print('Você digitou {} números, e a média deles foi {}.'.format(contagem, soma/contagem))
