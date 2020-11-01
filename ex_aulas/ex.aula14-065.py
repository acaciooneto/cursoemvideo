soma = maior = menor = contagem = 0
#maior = 0
#menor = 0
#contagem = 0
continuar = 'S'
while continuar == 'S':
    contagem += 1
    num = int(input('Digite um número inteiro: '))
    if contagem == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
    soma += num
    continuar = str(input('Você quer continuar? [S/N]: ')).upper().strip()[0]#pega só a 1ª letra
print('O maior foi {}, e o menor foi {}.'.format(maior, menor))
print('Já a média dos {} números deu {}.'.format(contagem, soma/contagem))
