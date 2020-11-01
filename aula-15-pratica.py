cont = soma = 0
while cont <= 10:
    print(cont, '-> ', end='')
    cont += 1
print('Acabou')

while True:
    num = int(input('Digite um número: '))
    if num == 0:
        break
    soma += num
#print('A soma vale {}.'.format(soma))
print(f'A soma vale {soma}') #f'string, veio depois do python 3.6 e substitui o .format

nome = 'josé'
idade = 33
salário = 1300
print(f'O {nome} tem {idade} anos e ganha R${salário} por mês, o que dá cerca de R${salário/30:.2f} por dia.')
