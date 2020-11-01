num = quantos = soma = 0 # reduz a linha legal
#quantos = 0
#soma = 0
while num != 999:
    num = int(input('Digite um número inteiro [999 p/ parar]: '))
    quantos += 1
    soma += num
    if num == 999: #gambiarra, pra evitar bota 'num' fora do while e outro dentro,
        soma = soma - 999 #  aí quando ele ler o 999, ele quita antes de acrescentar valores nas variáveis
        quantos = quantos - 1
print('{} números foram digitados e a soma deles dá {}.'.format(quantos, soma))
