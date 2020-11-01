from datetime import date
ano = int(input('Diga-nos o ano que você quer saber, -1 se quiser saber o ano atual: '))
if ano == -1:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('{} foi um ano bissexto.'.format(ano))
else:
    print('{} não foi um ano bissexto.'.format(ano))
