from datetime import date
atual = date.today().year
maiores = []
for pessoas in range(0, 7):
    nascimento = int(input('Digite o ano de nascimento da pessoa: '))
    idade = atual - nascimento
    if idade >= 21:
        maiores.append(idade)
if len(maiores) == 0:
    print('Ninguém que você disse é de maior.')
elif len(maiores) == 1:
    print('Apenas 1 pessoa que você falou é de maior.')
else:
    print('{} pessoas que você falou são de maior.'.format(len(maiores)))
# ELE PRINTA QUANTOS SÃO DE MAIOR E QUANTOS DE MENOR
