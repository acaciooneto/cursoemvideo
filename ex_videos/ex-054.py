from datetime import date
atual = date.today().year
maiores = 0
menores = 0
for pessoas in range(1, 8):
    nascimento = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(pessoas)))
    idade = atual - nascimento
    if idade < 21:
        menores += 1
    else:
        maiores += 1
print('{} pessoas são de menor e {} pessoas são de maior.'.format(menores, maiores))
